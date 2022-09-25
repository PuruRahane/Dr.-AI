# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 14:15:21 2022

@author: purur
"""

import requests
import pickle
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Dr. AI", page_icon=":trollface:", layout="wide")

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
Cancer_model = pickle.load(open('cancer_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction AI',
                           ['Home',
                            'Diabetes Prediction',
                            'Heart Predictiion',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           icons = ['house-door','activity', 'heart', 'person','body-text'],
                           default_index = 0)

if (selected == 'Home'):

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_AI = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_j1oeaifz.json")

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style.css")

    with st.container():
        st.subheader("Hi, I am Dr. AI :wave:")
        st.title("A Virtual Disease Predictor.")
        st.write("I am a Virtual assistant to help you find the proper outcomes & to guide you to the best solution.")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                """
                With the help of Machine Learning algorithms, I developed some models that will predict if you have some disease or not by taking the medical information from your test reports.
                Some of my work is as follows:
                - Studied over 1500+ reports.
                - More than 70% accuracy rate.
                - Easy to use and can access from anywhere.
                
                Thank You.
                """)
        with right_column:
            st_lottie(lottie_AI, height=300, key="AI")

    with st.container():
        st.write("---")
        st.header("Feedback.")
        st.write("##")
        contact_form = """
        <form action="https://formsubmit.co/pururahane90@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <textarea name="message" placeholder="Your message here" required></textarea>
             <button type="submit">Send</button>
        </form>
         """
         
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction AI')
    
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style1.css")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number Of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Level')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age')
    diabetes_dignosis = ''
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (diabetes_prediction[0] == 1):
            diabetes_dignosis = 'The person is Diabetic'
        else:
            diabetes_dignosis = 'The person does not have Diabetes'
    st.success(diabetes_dignosis)
    st.write("[Find best hospital for your Diabetes treatment >](https://www.medifee.com/list/best-hospitals-diabetes)")
    
if (selected == 'Heart Predictiion'):
    st.title('Heart Disease Predictiion AI')
    
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style1.css")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral In mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST Depression Induced By Exercise')
    with col2:
        slope = st.text_input('Slope Of The Peak Exercise ST')
    with col3:
        ca = st.text_input('Major Vessels Colored By Flourosopy')
    with col1:
        thal = st.text_input('thal 0 = Normal 1 = Fixed Defect 2 = Reversable Defect')
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person has Heart Disease'
        else:
          heart_diagnosis = 'The person does not have any Heart Disease'
    st.success(heart_diagnosis)
    st.write("[Find best hospital for your Heart care >](https://www.medifee.com/list/best-cardiology-hospitals-in-mumbai)")
    
if (selected == 'Parkinsons Prediction'):
    st.title('Parkinsons Disease Prediction AI')
    
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style1.css")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    with col1:
        fo = st.text_input('MDVP: Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP: Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP: RAP')
    with col2:
        PPQ = st.text_input('MDVP: PPQ')
    with col3:
        DDP = st.text_input('Jitter: DDP')
    with col4:
        Shimmer = st.text_input('MDVP: Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer: APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer: APQ5')
    with col3:
        APQ = st.text_input('MDVP: APQ')
    with col4:
        DDA = st.text_input('Shimmer: DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('Spread1')
    with col5:
        spread2 = st.text_input('Spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')
    parkinsons_diagnosis = ''    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
    st.success(parkinsons_diagnosis)
    st.write("[Find best hospital for your Parkinsons disease treatment >](https://www.justdial.com/Mumbai/Parkinson-Disease-Doctors/nct-10937609)")
    
if (selected == 'Breast Cancer Prediction'):
    st.title('Breast Cancer Prediction AI')
    col1, col2, col3, col4, col5 = st.columns(5)
    
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style1.css")
    
    with col1:
        radius_mean = st.text_input('Radius Mean')
    with col2:
        texture_mean = st.text_input('Texture Mean')
    with col3:
        perimeter_mean = st.text_input('Perimeter Mean')
    with col4:
        area_mean = st.text_input('Area Mean')
    with col5:
        smoothness_mean = st.text_input('Smoothness Mean')
    with col1:
        compactness_mean = st.text_input('Compactness Mean')
    with col2:
        concavity_mean = st.text_input('Concavity Mean')
    with col3:
        concave_points_mean = st.text_input('Concave Points Mean')
    with col4:
        symmetry_mean = st.text_input('Symmetry Mean')
    with col5:
        fractal_dimension_mean = st.text_input('Fractal Dimension Mean')
    with col1:
        radius_se = st.text_input('Radius SE')
    with col2:
       texture_se = st.text_input('Texture SE')
    with col3:
        perimeter_se = st.text_input('Perimeter SE')
    with col4:
        area_se = st.text_input('Area SE')
    with col5:
        smoothness_se = st.text_input('Smoothness SE')
    with col1:
        compactness_se = st.text_input('Compactness SE')
    with col2:
        concavity_se = st.text_input('Concavity SE')
    with col3:
        concave_points_se = st.text_input('Concave Points SE')
    with col4:
        symmetry_se = st.text_input('Symmetry SE')
    with col5:
        fractal_dimension_se = st.text_input('Fractal Dimension SE')
    with col1:
        radius_worst = st.text_input('Radius Worst')
    with col2:
        texture_worst = st.text_input('Texture Worst')
    with col3:
        perimeter_worst = st.text_input('Perimeter Worst')
    with col4:
        area_worst = st.text_input('Area Worst')
    with col5:
        smoothness_worst = st.text_input('Smoothness Worst')
    with col1:
        compactness_worst = st.text_input('Compactness Worst')
    with col2:
        concavity_worst = st.text_input('Concavity Worst')
    with col3:
        concave_points_worst = st.text_input('Concave Points Worst')
    with col4:
        symmetry_worst = st.text_input('Symmetry Worst')
    with col5:
        fractal_dimension_worst = st.text_input('Fractal Dimension Worst')
    cancer_diagnosis = ''    
    if st.button("Test Result"):
        Cancer_prediction = Cancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst,concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])
        if (parkinsons_prediction[0] == 1):
          cancer_diagnosis = "'The breast cancer in Malignant'"
        else:
          cancer_diagnosis = "The breast cancer in Benign"
    st.success(cancer_diagnosis)
    st.write("[Find best hospital for your Cancer treatment >](https://www.medifee.com/list/best-oncology-hospitals-in-mumbai)")