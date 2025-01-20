from flask import Flask, render_template, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
#client = MongoClient('mongodb://localhost:27017/')
#client = MongoClient('mongodb+srv://cluster0.sjal2.mongodb.net/')

#client = MongoClient(os.environ.get('mongodb+srv://cluster0.sjal2.mongodb.net/'))

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://dbuser:Password1@cluster0.sjal2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#db = client['user_data']
db = client['dbuser']
#collection = db['expenses']
collection = db['cluster0']
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_data = {
        'age': request.form['age'],
        'gender': request.form['gender'],
        'income': request.form['income'],
        'utilities': request.form['utilities'],
        'entertainment': request.form['entertainment'],
        'school_fees': request.form['school_fees'],
        'shopping': request.form['shopping'],
        'healthcare': request.form['healthcare']
    }
    
    # Save data in MongoDB
    collection.insert_one(user_data)
    return 'Data submitted successfully!'

if __name__ == "__main__":
    app.run(debug=True)
