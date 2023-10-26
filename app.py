from flask import Flask, render_template, request, jsonify, radiofield
import pandas as pd
import os
from openpyxl import Workbook

#DO NOT TOUCH! This is bringing the 'static' folder into the app. You can completely crash the app if you change it
app = Flask(__name__, static_folder='static')
#this will read the excel file, finding the locations where the project number and pmo comments are located.
#keep in mind that when you need to change the file, put it into the 'data' folder


df=pd.read_excel(r'PMO Testing Comments.xlsx', sheet_name='Sheet 1') #this is the dataframe to which the PMO Excel file goes to, and the sheet name of which it's under. 


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
    df =pd.read_excel()

    # if the project number doesn't exist in the file, the error will pop up. It's important to keep the excel file updated
    if user_project_number not in df['Project Number'].values:
        return jsonify({'status': 'Error: Project Number not found'})

    # If the project number exists, add the answer to the DataFrame
    df = df.append({'Project Number': user_project_number, 'PMO Comments': user_answer}, ignore_index=True)

    # Save the updated DataFrame to the Excel file
    df.to_excel('data/PMO Testing Comments.xlsx', index=False)

    return jsonify({'status': 'Comment Submitted Successfully'})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_project_number = request.form.get('project_number')
    user_answer = request.form.get('user_answer')

    # Read the Excel file into a DataFrame
    df = read_excel()

    # Search for a matching row
    match = df[(df['Project Number'] == user_project_number) & (df['PMO Comments'] == user_answer)]

    if not match.empty:
        return jsonify({'status': 'Match found'})
    else:
        return jsonify({'status': 'No match found'})
    
    
if __name__ == '__main__':
    app.run(debug=True)

