# Employee and Department Information Chatbot

This project is a Flask-based chatbot that interacts with an SQLite database to provide information about employees and departments. It can answer queries like:

- Show me all employees in the [department] department.
- Who is the manager of the [department] department?
- List all employees hired after [date].
- What is the total salary expense for the [department] department?

## How it Works

The chatbot uses Flask to handle user queries, processes them, and fetches data from the SQLite database. The chatbot responds based on pre-defined queries about employees, departments, and related details.

## Steps to Run Locally
1. Open the Chatbot folder in the visual studio code and execute the following command in the terminal
   - <b> python app.py </b>
3. Copy this URL http://127.0.0.1:5000 from the terminal.
4. Paste it on the web browser

Limitations
1. Currently only supports hardcoded queries.
2. No error handling for invalid inputs.
3. Lack of NLP support for natural language queries.
