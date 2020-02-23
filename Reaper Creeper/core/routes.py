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
        education = request.values['education'].strip()
        isSmoker = request.values['isSmoker'].strip()
        num_cigs = request.values['num_cigs'].strip()
        isOnBloodpressureMeds = request.values['isOnBloodpressureMeds'].strip()
        hasPrevalentstroke = request.values['hasPrevalentstroke'].strip()
        hasHighbloodpressure = request.values['hasHighbloodpressure'].strip()
        hasDiabetes = request.values['hasDiabetes'].strip()
        weight = request.values['weight'].strip()
        height = request.values[ 'height'].strip()
        return "Age: " + age + " Gender: " +  gender + " Education: " + education \
            + " isSmoker " + isSmoker + " num_cigs " + num_cigs + " isOnBloodpressureMeds " + isOnBloodpressureMeds \
            + " hasPrevalentstroke " + hasPrevalentstroke + " hasHighbloodpressure " + hasHighbloodpressure \
            + " hasDiabetes " + hasDiabetes + " weight " + weight + " height " + height

    return render_template('error.html',
                            title='Error!',
                            message='Must use GET request type...')
