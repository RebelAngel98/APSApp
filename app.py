from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__, static_folder='static')

# Function to read the Excel file and return a DataFrame
def read_excel_file():
    excel_file_path = os.path.abspath('data/PMO Testing Comments.xlsx')
    return pd.read_excel(excel_file_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_answer', methods=['POST'])
def send_answers():
    user_project_number = request.form.get('project_number')
    user_answer = request.form.get('user_answer')

    # Read the Excel file into a DataFrame
    df = read_excel_file()

    # Check if the entered project number exists in the DataFrame
    if user_project_number not in df['Project Number'].values:
        return jsonify({'status': 'Error: Project number not found'})

    # If the project number exists, add the answer to the DataFrame
    df = df.append({'Project Number': user_project_number, 'PMO Comments': user_answer}, ignore_index=True)

    # Save the updated DataFrame to the Excel file
    df.to_excel('data/PMO Testing Comments.xlsx', index=False)

    return jsonify({'status': 'Answer submitted successfully'})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_project_number = request.form.get('project_number')
    user_comments = request.form.get('user_comments')

    # Read the Excel file into a DataFrame
    df = read_excel_file()

    # Search for a matching row
    match = df[(df['Project Number'] == user_project_number) & (df['PMO Comments'] == user_comments)]

    if not match.empty:
        return jsonify({'status': 'Match found'})
    else:
        return jsonify({'status': 'No match found'})

if __name__ == '__main__':
    app.run(debug=True)
