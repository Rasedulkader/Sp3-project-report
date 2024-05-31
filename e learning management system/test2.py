import mysql.connector
import webbrowser

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object
cursor = db.cursor()

# Execute a SQL query to select all records from the
# users table
cursor.execute("SELECT * FROM users")

# Fetch all the rows
rows = cursor.fetchall()

# Close the cursor and the connection
cursor.close()
db.close()

# Open the login.html file in a web browser
url = "login.html"
webbrowser.open(url)