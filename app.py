from flask import Flask, render_template, request, jsonify
import pandas as pd


app = Flask(__name__, static_folder="static")


# df=pd.read_excel(r'data/PMO Testing Comments.xlsx', sheet_name='Sheet1') #this is the dataframe to which the PMO Excel file goes to, and the sheet name of which it's under. 


# the index.html is what connects the whole code together. It's the main part of code, besides Python.
@app.route('/')
def index():
    return render_template('index.html')

# this is sending the answers from the user_input_form in the index.html to store somewhere safely.
@app.route('/send_answer', methods=['GET','POST']) 
# NEED TO MAYBE ADD 'GET' TO THIS METHOD! SEE NOTES.PY
def send_answers():
    if request.method == "POST":
        # user_project_number = request.form.get('project_number')
        # user_answer = request.form.get('user_answer')

        PostData = request.get_json()
        user_project_number = PostData["project_number"]
        user_answer = PostData["user_answer"]

    # this is reading the excel file to make sure the project number matches up to one of them in the file.
    df = pd.read_excel("data/PMO Testing Comments.xlsx")

    # if the project number doesn't exist in the file, the error will pop up. It's important to keep the excel file updated
    # print(df['Project Number'].values)
    print(user_project_number)

    if user_project_number not in df['Project Number'].values:
        return jsonify({'status': 'Error: Project Number not found'})
    

    # If the project number exists, add the answer to the DataFrame
    # df = df.append({'Project Number': user_project_number, 'PMO Comments': user_answer}, ignore_index=True)
    df.loc[df['Project Number'] == user_project_number, "PMO Comments"] = user_answer

    print(df)

    # Save the updated DataFrame to the Excel file
    df.to_excel("data/PMO Testing Comments.xlsx", index=False)

    return jsonify({'status': 'Comment Submitted Successfully'})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_project_number = request.form.get('project_number')
    user_answer = request.form.get('user_answer')

    # Read the Excel file into a DataFrame
    df = pd.read_excel()

    # Search for a matching row
    match = df[(df['Project Number'] == user_project_number) & (df['PMO Comments'] == user_answer)]

    if not match.empty:
        return jsonify({'status': 'Match found'})
    else:
        return jsonify({'status': 'No match found'})
    

if __name__ == '__main__':
    app.run(debug=True)

