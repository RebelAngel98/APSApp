from flask import Flask, render_template, request, jsonify
import pandas as pd


app = Flask(__name__, static_folder="static")

"""Do not mess with the static_folder. It contains the JavaScript, text-styles, dark-styles, and logo. 

Below is the app.route. This is going to point the app where to go. You won't ever mess with this, it's to stay as index.html as
it points to the HTML template.  """
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_answer', methods=['GET','POST']) 
def send_answers():
    if request.method == "POST":
        PostData = request.get_json()
        user_project_number = PostData["project_number"]
        user_answer = PostData["user_answer"]
    
    
    df = pd.read_excel("data/PMO Testing Comments.xlsx") 
    """Above is where you'll be changing the .xlsx to match up with the current Operational Metrics inside of the "data/..." MAKE 
     SURE TO PUT THE OPERATIONAL METRICS IN THE DATA FOLDER"""


    """Confirming that the Project Number the user inserted is in the excel sheet, otherwise, the status 'Error: Project Number not found'
     will returned"""    
    print(user_project_number)

    if user_project_number not in df['Project Number'].values:
        return jsonify({'status': 'Error: Project Number not found'})
    

    # If the project number exists, add the answer to the DataFrame
    df.loc[df['Project Number'] == user_project_number, "PMO Comments"] = user_answer

    print(df)

    """df.to_excel needs to be updated the same way as above with "data/... .xlsx". It'll be the Operational Metrics datasheet"""
    df.to_excel("data/PMO Testing Comments.xlsx", index=False)

    return jsonify({'status': 'Comment Submitted Successfully'})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_project_number = request.form.get('project_number')
    user_answer = request.form.get('user_answer')

    # Read the Excel file into a DataFrame
    df = pd.read_excel()

    # Search for a matching row labeled as 'Project Number' and 'PMO Comments'
    match = df[(df['Project Number'] == user_project_number) & (df['PMO Comments'] == user_answer)]

    # if there is no matching 'Project Number' or 'PMO Comments' the code will return with 'No match found' 
    if not match.empty:
        return jsonify({'status': 'Match found'})
    else:
        return jsonify({'status': 'No match found'})
    

if __name__ == '__main__':
    app.run(debug=True)

