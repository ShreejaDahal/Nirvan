"""This is the main flask server that connects to the Mongodb database and
 updates it as per the user input. It also renders various html pages."""
#import os
import pickle
from pathlib import Path
import numpy as np
from flask import Flask, request, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import requests
from flask_mail import Mail, Message

# Creating the flask application
app = Flask(__name__)


def mail_config():
    """Configures the main server, port, username, password, tls use and ssl use

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    None

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021

    """
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    


def get_database():
    """Connects to the mongodb database named seniorproject

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    database class object
         class object contains all the collection of documents

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """

    load_dotenv()
    env_path = Path('.')/'.env'
    load_dotenv(dotenv_path=env_path)
    conn_string = os.environ.get('conn_string')
    # Creating a connection using MongoClient
    client = MongoClient(conn_string)
    print(type(client['seniorproject']))
    return client['seniorproject']
   
   
@app.route('/')
def home():
    """Routes to the main page of the website

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    main html page
         the welcome page with navigation bar and tests to choose from

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """
    return render_template('main_index.html')


@app.route('/depression_page.html')
def depression():
    """Routes to the depression test page

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    depression test page
        screens user for depression

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021

    """
    return render_template('depression_page.html')


@app.route('/contact.html')
def contact():
    """Routes to the contacts page

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    contacts page
        allows user to contact the team members with questions

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """
    return render_template('contact.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    """Processes information from the contacts page and
        sends email to the Nirvan team

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    renders contact page
        lets the user how their message has been received

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """

    # calls the mail_config function
    mail_config()
    mail = Mail(app)

    # gets form information from the user
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    message = request.form.get("message")

    # forms the email header and sets the sender and recipient
    msg_nirvaan = Message('Shreeja, a new user has contacted us!', sender='user.nirvan@gmail.com',recipients=['contact.us.nirvan@gmail.com'])
    # forms the message body
    msg_nirvaan.body = "First Name: " + first_name + " " +  "Last Name: " + last_name + " " + " Email: " + email + " " +  "Message: " + message
    # sends the message to the recipient
    mail.send(msg_nirvaan)
    return render_template('contact.html', result='Congratulations!\n'
                           ' Your message has been sent! A team member\n'
                           ' will get back to you shortly!')


@app.route('/bipolar.html')
def bipolar():
    """Routes to the bipolar test page

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    bipolar test page
        screens user for bipolar

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021

    """
    return render_template('bipolar.html')


@app.route('/pmdd.html')
def pmdd():
    """Routes to the PMDD test page

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    bipolar test page
        screens user for PMDD

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """
    return render_template('pmdd.html')


@app.route('/bio.html')
def bio():
    """Routes to the bio page

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    bio  page
        information on the author

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021

    """
    return render_template('bio.html')


@app.route('/anxiety.html')
def anxiety():
    """Routes to the anxiety test page

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    anxiety test page
        screens user for anxiety

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """
    return render_template('anxiety.html')


@app.route('/main_index.html')
def main_index():
    """Routes to the main welcome page

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    main html page
         the welcome page with navigation bar and tests to choose from

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """
    return render_template('main_index.html')


@app.route('/lgbtq_and_bully.html')
def bully():
    """Routes to the lqbtqi+ and bully resources  page

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    lqbtqi+ and bully resources  page
        contains articles, groups, and awareness videos on lgbtqi+ and bullying

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """
    return render_template('lgbtq_and_bully.html')


@app.route('/mental_health_resources.html')
def mental_health_resources():
    """Routes to the mental health resources  page

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    mental health resources  page
        contains information on different health care providers in Nepal

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """
    return render_template('mental_health_resources.html')


@app.route('/support.html')
def support():
    """Routes to the support page

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    lqbtqi+ and bully resources  page
        contains articles, support groups, and videos on mental health

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """
    return render_template('support.html')


@app.route('/predict_anxiety', methods=['GET', 'POST'])
def predict_anxiety():
    """loads machine learning model to predict anxiety

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    anxiety test page with a success and result message
        result could either be minimal, mild, moderate, or severe anxiety

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """

    # loads model_anxiety pickle from the models folder
    model = pickle.load(open('models/model_anxiety.pkl', 'rb'))
    # converts the form values into float
    features = [float(i) for i in request.form.values()]
    array_features = [np.array(features)]
    # model predicts the output based on the features
    prediction = model.predict(array_features)
    output = prediction
    # minimal anxiety
    if output == 0:
        return render_template('anxiety.html', success='Your answers\n'
                               ' have been processed! Click on Result\n',
                               result='You are most likely to have a\n'
                               ' minimal anxiety.')
    # mild anxiety
    elif output == 1:
        return render_template('anxiety.html', success='Your answers\n'
                               ' have been processed! Click on Result \n',
                               result='You are most likely to have a\n'
                               ' mild anxiety.')
    # moderate anxiety
    elif output == 2:
        return render_template('anxiety.html', success='Your answers\n'
                               ' have been processed! Click on Result \n',
                               result='You are most likely to have a\n'
                               ' moderate anxiety.')
    # severe anxiety
    else:
        return render_template('anxiety.html', success='Your answers\n'
                               ' have been processed! Click on Result \n',
                               result='You are most likely to have a\n'
                               ' severe anxiety.')


@app.route('/predict_depression', methods=['GET', 'POST'])
def predict_depression():
    """loads machine learning model to predict depression

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    depression test page with a success and result message
        result could either be minimal, mild, moderate, or severe depression

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021

    """

    # loads model_depression pickle from the models folder
    model = pickle.load(open('models/model_depression.pkl', 'rb'))
    # converts the form values into float
    features = [float(i) for i in request.form.values()]
    array_features = [np.array(features)]
    # model predicts the output based on the features
    prediction = model.predict(array_features)
    output = prediction
    # minimal depression
    if output == 0:
        return render_template('depression_page.html', success='Your answers\n'
                               ' have been processed! Click on Result.',
                               result='You are most likely to have a\n'
                               ' minimal depression.')
    # minimal depression
    elif output == 1:
        return render_template('depression_page.html', success='Your answers\n'
                               ' have been processed! Click on Result.',
                               result='You are most likely to have a\n'
                               ' mild depression.')
    # minimal depression
    elif output == 2:
        return render_template('depression_page.html', success='Your answers\n'
                               ' have been processed! Click on Result.',
                               result='You are most likely to have a\n'
                               ' moderate depression.')
    # severe depression
    else:
        return render_template('depression_page.html', success='Your answers\n'
                               ' have been processed! Click on Result.',
                               result='You are most likely to have a\n'
                               ' severe depression.')


@app.route('/predict_bipolar', methods=['GET', 'POST'])
def predict_bipolar():
    """loads machine learning model to predict bipolar

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    bipolar test page with a success and result message
        result could either be likely bipolar or not likely bipolar

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021

    """
    # loads model_bipolar pickle from the models folder
    model = pickle.load(open('models/model_bipolar.pkl', 'rb'))
    # converts the form values into float
    features = [float(i) for i in request.form.values()]
    array_features = [np.array(features)]
    # model predicts the output based on the features
    prediction = model.predict(array_features)
    output = prediction
    # no bipolar
    if output == 0:
        return render_template('bipolar.html', success='Your answers\n'
                               ' have been processed! Click on Result.',
                               result='You are most likely to not have \n'
                               ' bipolar')
    # bipolar
    elif output == 1:
        return render_template('bipolar.html', success='Your answers\n'
                               ' have been processed! Click on Result.',
                               result='You are most likely to have \n'
                               ' bipolar')


@app.route('/predict_pmdd', methods=['GET', 'POST'])
def predict_pmdd():
    """loads machine learning model to predict pmdd

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    pmdd test page with a success and result message
        result could either be likely pmdd or not likely pmdd

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """
    # loads model_pmdd pickle from the models folder
    model = pickle.load(open('models/model_pmdd.pkl', 'rb'))
    # converts the form values into float
    features = [float(i) for i in request.form.values()]
    array_features = [np.array(features)]
    # model predicts the output based on the features
    prediction = model.predict(array_features)
    output = prediction
    # no pmdd
    if output == 0:
        return render_template('pmdd.html', success='Your answers\n'
                               ' have been processed! Click on Result.',
                               result='You are most likely to not have \n'
                               ' PMDD')
    # pmdd
    elif output == 1:
        return render_template('pmdd.html', success='Your answers\n'
                               ' have been processed! Click on Result.',
                               result='You are most likely to have \n'
                               ' bipolar')


@app.route('/domestic.html',  methods=['GET', 'POST'])
def domestic():
    """Connects to the mongodb database named seniorproject
      ,inserts the health care provider's info in the database, and renders the
      data

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    domestic contacts page
        adds rescue team's contact information

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """
    # connect to the database
    dbname = get_database()
    # get contact_list collection from database
    collection_name = dbname["contact_list"]
    # get information from the form
    features = list(request.form.values())
    count = 0
    # get name, district, contact_name, position, contact_number, and email
    # of the rescue person
    while count < len(features):
        name = features[count]
        count += 1
        district = features[count]
        count += 1
        contact_name = features[count]
        count += 1
        position = features[count]
        count += 1
        contact_number = features[count]
        count += 1
        email = features[count]
        count += 1
        post_detail = {
                "Name": name,
                "District": district,
                "Contact Name": contact_name,
                "Position": position,
                "Contact Number": contact_number,
                "Email": email,
        }
        # insert the contact info in the database collection
        collection_name.insert_one(post_detail)
    subjects = ["Name", "District", "Contact Name", "Position",
                "Contact Number", "Email"]
    data = ()
    # create a tuple of all the documents in the database collection
    for data_entry in collection_name.find():
        entry = ((data_entry["Name"], data_entry["District"],
                  data_entry["Contact Name"], data_entry["Position"],
                  data_entry["Contact Number"], data_entry["Email"]),)
        data += entry
    return render_template('domestic.html', Subjects=subjects, Data=data)


@app.route('/connect.html',  methods=['GET', 'POST'])
def connect():
    """Connects to the mongodb database named seniorproject
      ,inserts user posts in the database, and renders the
      data

    PARAMETERS
    -----------
    None

    RETURNS
    -----------
    find support page
        contains anonymous posts from users

    AUTHOR
    -----------
    Shreeja Dahal

    DATE
    -----------
    10:18 AM 09/29/2021
    """
    # Get the database
    dbname = get_database()
    # get user_posts collection from database
    collection_name = dbname["user_posts"]
    features = list(request.form.values())
    count = 0
    # get subject, description, category, date from the post
    while count < len(features):
        subject = features[count]
        count += 1
        category = features[count]
        count += 1
        date = features[count]
        count += 1
        description = features[count]
        count += 1
        post_detail = {
                "Subject": subject,
                "Description": description,
                "Category": category,
                "Date": date
        }
        # insert the post in the database collection
        collection_name.insert_one(post_detail)
    subjects = ["Subjects", "Description", "Category", "Date"]
    data = ()
    # create a tuple of all the documents in the database collection
    for data_entry in collection_name.find():
        entry = ((data_entry["Subject"], data_entry["Description"],
                  data_entry["Category"], data_entry["Date"]),)
        data += entry
    return render_template("connect.html", Subjects=subjects, Data=data)


if __name__ == '__main__':
    app.run()
