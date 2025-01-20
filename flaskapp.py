import os
from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
from pymongo import MongoClient, errors
import pandas as pd
import csv

app = Flask(__name__)

# MongoDB connection URI
uri = "mongodb+srv://dbuser:Password1@cluster0.sjal2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Access the database and collection
db = client['dbuser']
collection = db['cluster0']

# Create a unique index on email to enforce uniqueness
collection.create_index([('email', 1)], unique=True)

@app.route('/')
def home():
    return render_template('index.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        # Check if the email exists in the database
        user = collection.find_one({'email': email})
        if user:
            # Redirect to update profile page if user exists
            return redirect(url_for('update_profile', email=email))
        else:
            return jsonify({"message": "Email not found. Please register."}), 400
    return render_template('login.html')

# Route to update user profile based on unique email
@app.route('/update_profile/<email>', methods=['GET', 'POST'])
def update_profile(email):
    # Fetch the user data based on the email
    user = collection.find_one({'email': email})

    if request.method == 'POST':
        updated_data = {
            'name': request.form.get('name', user['name']),
            'age': request.form.get('age', user['age']),
            'gender': request.form.get('gender', user['gender']),
            'total_income': request.form.get('total_income', user['total_income']),
            'expenses': {}
        }

        # Update expenses based on form data
        expense_categories = ['food', 'transportation', 'utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare', 'other']
        for category in expense_categories:
            updated_data['expenses'][category] = float(request.form.get(f'{category}_amount', 0))

        # Update the user's data in the database
        collection.update_one({'email': email}, {'$set': updated_data})
        return jsonify({"message": "Profile updated successfully!"})

    return render_template('update_profile.html', user=user)

@app.route('/submit', methods=['POST'])
def submit():
    user_data = {
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'age': request.form.get('age'),
        'gender': request.form.get('gender'),
        'total_income': request.form.get('total_income'),
        'expenses': {}  # Initialize expenses
    }

    expense_categories = ['food', 'transportation', 'utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare', 'other']
    for category in expense_categories:
        expense_value = request.form.get(f'{category}_amount', 0)
        user_data['expenses'][category] = float(expense_value)

    try:
        collection.insert_one(user_data)
        return jsonify({"message": "Data submitted successfully!"})
    except errors.DuplicateKeyError:
        try:
            result = collection.update_one({'email': user_data['email']}, {'$set': user_data})
            if result.modified_count > 0:
                return jsonify({"message": "Profile updated successfully!"})
            else:
                return jsonify({"message": "No changes detected."})
        except Exception as e:
            print(f"Error updating data: {e}")
            return jsonify({"message": "Error occurred while updating data."}), 500
    except Exception as e:
        print(f"Error inserting data: {e}")
        return jsonify({"message": "Error occurred while saving data."}), 500

@app.route('/export_csv', methods=['GET'])
def export_csv():
    # Fetch data from MongoDB
    cursor = collection.find({})

    # Prepare list to hold user data
    user_data = []
    for doc in cursor:
        user_data.append({
            'name': doc.get('name'),
            'age': doc.get('age'),
            'email': doc.get('email'),
            'gender': doc.get('gender'),
            'total_income': doc.get('total_income'),
            'food': doc.get('expenses', {}).get('food', 0),
            'transportation': doc.get('expenses', {}).get('transportation', 0),
            'utilities': doc.get('expenses', {}).get('utilities', 0),
            'entertainment': doc.get('expenses', {}).get('entertainment', 0),
            'school_fees': doc.get('expenses', {}).get('school_fees', 0),
            'shopping': doc.get('expenses', {}).get('shopping', 0),
            'healthcare': doc.get('expenses', {}).get('healthcare', 0),
            'other': doc.get('expenses', {}).get('other', 0)
        })

    # Define the folder to save the CSV file
    extracted_folder = os.path.join(os.getcwd(), 'extracted')
    if not os.path.exists(extracted_folder):
        os.makedirs(extracted_folder)

    # Define the file path for saving the CSV
    csv_file_path = os.path.join(extracted_folder, 'user_data.csv')
    
# Define the file path to save the CSV in the home directory
    home_directory_csv_path = os.path.join(os.getcwd(), 'user_data.csv')

# Write the user data to CSV
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=user_data[0].keys())
        writer.writeheader()  # Write the header
        writer.writerows(user_data)  # Write the user data rows

# Also write the user data to CSV in the home directory
    with open(home_directory_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=user_data[0].keys())
        writer.writeheader()  # Write the header
        writer.writerows(user_data) 

    # Serve the file for download
    return send_from_directory(extracted_folder, 'user_data.csv', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
