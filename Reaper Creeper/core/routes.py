from flask import request, render_template
from . import app, db                         # Get from __init__
# import tensorflow as tf
# import keras
# from keras.models import Sequential
# from keras.layers import Dense
from .models import Table                    # Get db models
from .MessageHandler import MessageHandler   # Get simple message processor
# import numpy as np

# Python imports


msgHandler = MessageHandler()


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('index.html',
                                title=':::Health Genie:::')

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


@app.route('/diabetes-analysis', methods=['GET', 'POST'])
def diabetesAnalysis():
    if request.method == 'POST':
        num_preg = request.values['num_preg'].strip()
        glucoseLevel = request.values['glucoseLevel'].strip()
        bloodPressure = request.values['bloodPressure'].strip()
        skinThickness = request.values['skinThickness'].strip()
        insulin = request.values['insulin'].strip()
        bmi = request.values['bmi'].strip()
        diabetesePedigree = request.values['diabetesePedigree'].strip()
        age = request.values['age'].strip()

        # Minimum = np.array([0.00,0.00,0.00,0.00,0.00,0.00,0.08,21.00])

        return render_template('results.html',
                                disease='Diabetes',
                                percentage="13%")


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


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        return render_template('about.html',
                                title=':::Health Genie - About:::')

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
        return render_template('results.html',
                                disease='Heart Disease',
                                percentage="56%")
        
    return render_template('error.html',
                            title='Error!',
                            message='Must use GET request type...')
