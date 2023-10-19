from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

#DO NOT TOUCH! This is bringing the 'static' folder into the app. You can completely crash the app if you change it
app = Flask(__name__, static_folder='static')

#this will read the excel file, finding the locations where the project number and pmo comments are located.
#keep in mind that when you need to change the file, put it into the 'data' folder
def read_excel_file():
    excel_file_path = os.path.abspath('data/PMO Testing Comments.xlsx') #also change the name here to line up with what the file is called i.e. "July Operational Metrics"
    return pd.read_excel(excel_file_path)

# the index.html is what connects the whole code together. It's the main part of code, besides Python.
@app.route('/')
def index():
    return render_template('index.html')

# this is sending the answers from the user_input_form in the index.html to store somewhere safely.
@app.route('/send_answer', methods=['POST'])
def send_answers():
    user_project_number = request.form.get('project_number')
    user_answer = request.form.get('user_answer')

    # this is reading the excel file to make sure the project number matches up to one of them in the file.
    df = read_excel_file()

    # if the project number doesn't exist in the file, the error will pop up. It's important to keep the excel file updated
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
