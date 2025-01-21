# BAN6420_PROJ
# Final Project: Flask Healthcare Application
# BAN6420: Programming in R & Python
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

If you haven't already, clone the repository:

```bash
git clone https://github.com/your-repository-name.git
cd your-repository-name
```

### 2. Install Dependencies

Install required libraries:

```bash
pip install -r requirements.txt
```

Make sure the `requirements.txt` file includes:

```txt
Flask==2.x.x
pymongo==3.x.x
pandas==1.x.x
seaborn==0.x.x
matplotlib==3.x.x
```

### 3. MongoDB Setup

The app requires a MongoDB connection. You'll need a MongoDB Atlas account or a local MongoDB setup.

- Create a MongoDB database and collection.
- Replace the MongoDB URI in `app.py` with your actual MongoDB URI.

Example:

```python
uri = "mongodb+srv://<username>:<password>@cluster0.sjal2.mongodb.net/?retryWrites=true&w=majority"
```

### 4. Run the Application

To run the Flask development server locally:

```bash
python app.py
```

The app will be accessible at `http://127.0.0.1:5000/`.

### 5. Running in Production (optional)

For production environments, it is recommended to use **Gunicorn** and **Nginx**.

1. Install Gunicorn:

```bash
pip install gunicorn
```

2. Run the application with Gunicorn:

```bash
gunicorn -w 4 app:app
```

3. Set up Nginx as a reverse proxy (example provided in the previous instructions).

---

## Using the Application

1. **Homepage:**  
   Access the homepage at `http://127.0.0.1:5000/` or your public IP if deployed.

2. **User Registration & Login:**  
   Users can log in with their email address. If they don't have an account, they are prompted to register.

3. **Profile Update:**  
   Once logged in, users can update their profile with information like name, age, gender, total income, and expense categories.

4. **Export CSV:**  
   Once data is entered, users can export their data in CSV format by clicking the export button. The file will be saved as `user_data.csv` and will be available for download.

---

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

---

## Application Structure

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
```

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit the changes (`git commit -am 'Add new feature'`).
5. Push to your branch (`git push origin feature-branch`).
6. Open a Pull Request.

### Notes:

- The data analysis and visualizations are generated from the CSV file that is exported from the Flask app.

