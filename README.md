# BAN6420_PROJ
# BAN6420: Programming in R & Python
# Final Project: Flask Healthcare Application
# Student Name: Taiwo Babalola
# Learner ID: 162894

This README file provides details about Flask application with instructions for setting up, running, and analyzing data through visualizations. It also includes details about how the app works, where to find the output, and how to interpret the visualizations.

---

# User Data Flask Application

This Flask application allows users to register /submit, update their profile with personal information (name, email, age, gender),income and expenses, and export data to CSV. 

It also generates various visualizations of the data, such as the distribution of total income, expense breakdowns, and correlations between income and expenses. 
The application connects to a MongoDB database  on atlas cloud to store user data securely.

---

## Features
- User registration, login, and profile updates.
- Users can input personal information (name, age, gender, income) and categorize expenses (e.g., food, transportation, healthcare, etc.).
- CSV export of user data.
- Various data visualizations using `pandas`, `matplotlib`, and `seaborn` for deeper analysis of income, expenses, and demographics.

---

## Prerequisites

Before running the application, make sure you have the following:

- **Python 3.x** installed.
- **MongoDB** instance (either local or MongoDB Atlas).
- Install the required Python dependencies using the provided `requirements.txt`.

---

## Setup and Installation

### 1. Clone the Repository

clone the repository:
 - git clone https://github.com/AmazingTaiwo/BAN6420_PROJ.git
 - cd your-repository-name

### 2. Install Dependencies
Install required libraries:
 - pip install -r requirements.txt

Make sure the `requirements.txt` file includes:

 - Flask==2.x.x
 - pymongo==3.x.x
 - pandas==1.x.x
 - seaborn==0.x.x
 - matplotlib==3.x.x

### 3. MongoDB Setup

The app requires a MongoDB connection. A connetion was established to MongoDB Atlas account on cloud via: mongodb+srv://dbuser:<db_password>@cluster0.sjal2.mongodb.net/
   - Create a MongoDB database and collection.
   - the password for the MongoDB URI in `flaskapp.py` with your actual MongoDB URI.
      - uri = "mongodb+srv://dbuser:<password>@cluster0.sjal2.mongodb.net/?retryWrites=true&w=majority"


### 4. Run the Application
To run the Flask development server, we have hosted the flaskapp (index.html, flaskapp.py) on EC2 instance on AWS (ec2-13-49-68-37.eu-north-1.compute.amazonaws.com).

 - We have already started the flask app with below on AWS
  - python flaskapp.py
 - navigate to the flask app on browser browser via: "http://13.49.68.37:5000/" to access the data collection form
 - Register few candidate by providing the candidate name, email, age, gender, Total income and expense category (Foor, Transportation, Utilities, Entertainment, School fees, Shopping, Healtcare, Other) and submit
   

## Using the Application

1. **Homepage:**  
   Navigate to the homepage (index.html) hosted via `http://13.49.68.37:5000/`.

2. **User Registration & Login:**  
   Users can log in with their email address. If they don't have an account, they are prompted to register.

3. **Profile Update:**  
   Once logged in, users can update their profile with information like name, age, gender, total income, and expense categories.

4. **Export CSV**  
   Once data is entered, users can export their data in CSV format by clicking the export button at the bottom of the page.
   Upon the click of the export to "CSV", it triggeres an export and saved as `user_data.csv` and will be available for download on your PC.

5. **Visuallization**
    - Copy the downloaded 'user_data.csv to the same location where you cloned the repository for this project
    - Open user_data_visualization.ipynb on python IDE of your choice or run with CMD.
    - The execution of this user_data_visualization.ipynb file produce below visualizations and save each visual in .png format in your working directory. 
   

   ## Visualizations
      The app also includes the following visualizations based on the user data:

      1. **Total Income Distribution:**  
        A histogram that shows the distribution of total income across users.
   
           ![Total Income Distribution](total_income_distribution.png)

     2. **Total Expenses by Category:**  
        A bar chart showing the total amount spent in different expense categories (food, transportation, healthcare, etc.).

           ![Expense by Category](expense_by_category.png)

     3. **Income vs. Expenses:**  
        A scatter plot comparing total income against total expenses to reveal any trends.

           ![Income vs Expenses](income_vs_expenses.png)

     4. **Expense Correlation Heatmap:**  
        A heatmap showing the correlation between different expense categories.

          ![Expense Correlation Heatmap](expense_correlation_heatmap.png)

     5. **Gender Distribution:**  
        A count plot that shows the gender distribution of users.

          ![Gender Distribution](gender_distribution.png)

          ### How to View the Visualizations:

          Once the data is exported, the visualizations will be saved in the directory where the Flask app is hosted. To access the visualizations:

- Look for the files named `total_income_distribution.png`, `expense_by_category.png`, `income_vs_expenses.png`, `expense_correlation_heatmap.png`, and `gender_distribution.png` in the project directory.
- These can be viewed in any image viewer.

5. ## Application Structure

```
/your-flask-app
│
├── app.py               # Main Flask application file
├── templates/           # HTML templates for rendering views
│   ├── index.html
│   ├── login.html
│   └── update_profile.html
├── static/              # Static files (CSS, JS)
├── extracted/           # Folder where CSV files are saved
├── user_data.csv        # Sample data file
├── total_income_distribution.png  # Visualization of total income
├── expense_by_category.png        # Visualization of expenses by category
├── income_vs_expenses.png         # Visualization of income vs expenses
├── expense_correlation_heatmap.png # Visualization of expense correlations
├── gender_distribution.png        # Visualization of gender distribution
└── requirements.txt     # List of Python dependencies
└── README.md            # Documentation file (this file)


### Notes:

- The data analysis and visualizations are generated from the CSV file that is exported from the Flask app hosted on EC2 instance on AWS.

