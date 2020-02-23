from flask import request, render_template
from . import app, db                         # Get from __init__

from .models import Table                    # Get db models
from .MessageHandler import MessageHandler   # Get simple message processor


# Python imports


msgHandler = MessageHandler()


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('index.html',
                                title=':::Reaper Creeper:::')

    return render_template('error.html',
                            title='Error!',
                            message='Must use GET request type...')


@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes():
    if request.method == 'GET':
        return render_template('diabetes.html',
                                title=':::Diabetes:::')

    return render_template('error.html',
                            title='Error!',
                            message='Must use GET request type...')


@app.route('/heart-disease', methods=['GET', 'POST'])
def heartDisease():
    if request.method == 'GET':
        return render_template('heart-disease.html',
                                title=':::Heart Disease:::')

    return render_template('error.html',
                            title='Error!',
                            message='Must use GET request type...')


@app.route('/heart-disease-analysis', methods=['GET', 'POST'])
def heartDiseaseAnalysis():
    if request.method == 'POST':
        age    = request.values['age'].strip()
        gender = request.values['gender'].strip()
        return "Age: " + age + " Gender: " +  gender

    return render_template('error.html',
                            title='Error!',
                            message='Must use GET request type...')
