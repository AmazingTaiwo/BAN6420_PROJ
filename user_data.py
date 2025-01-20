import csv
import pandas as pd
from pymongo import MongoClient

# Define User class
class User:
    def __init__(self, age, gender, income, utilities, entertainment, school_fees, shopping, healthcare):
        self.age = age
        self.gender = gender
        self.income = income
        self.utilities = utilities
        self.entertainment = entertainment
        self.school_fees = school_fees
        self.shopping = shopping
        self.healthcare = healthcare

# Connect to MongoDB
#client = MongoClient('mongodb://localhost:27017/')
#db = client['user_data']
#collection = db['expenses']

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

# Fetch data from MongoDB
users = []
for data in collection.find():
    user = User(
        age=data['age'],
        gender=data['gender'],
        income=data['income'],
        utilities=data['utilities'],
        entertainment=data['entertainment'],
        school_fees=data['school_fees'],
        shopping=data['shopping'],
        healthcare=data['healthcare']
    )
    users.append(user)

# Save data to CSV
with open('user_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Age', 'Gender', 'Income', 'Utilities', 'Entertainment', 'School Fees', 'Shopping', 'Healthcare'])
    for user in users:
        writer.writerow([user.age, user.gender, user.income, user.utilities, user.entertainment, user.school_fees, user.shopping, user.healthcare])

# Read into DataFrame
df = pd.read_csv('user_data.csv')
