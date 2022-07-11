import streamlit as st
import pickle
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title = None,
    options = ["Home","Predict","About"], 
    icons = ["house","speedometer","person"], 
    menu_icon = "menu-button", 
    orientation = "horizontal",
)

if selected == "Home":
    with st.container():
        st.title('Medical Insurance Predictor!')
        st.subheader('By Anirudh :wave:')
    with st.container():
        st.title('Predict your insurance cost :information_source:')
        st.write('The insurance predicor is not super accurate by you can get the basic idea of how much it will cost you. Insurance cost are extremely expensive these days and the differ from person to person so this app helps to curate the insurance cost for you.')
        st.subheader('Disclaimer :heavy_exclamation_mark:')
        st.write('The predicted cost may be more or less compared with the true cost. Remember that this is just for a idea.')
        st.subheader('This is a sample Dataset:')
        df = pd.read_csv("medical_insurance.csv")
        st.write(df)


if selected == "Predict":
    st.title('Predict your insurance cost')
    st.subheader('Enter the details')
    model = pickle.load(open('linearregression.sav','rb'))
    
    def mip(input_data):
        na = np.asarray(input_data)
        d = na.reshape(1,-1)
        
        prediction = model.predict(d)
        return prediction


    def main():

        age = st.text_input('Age')
        sex_1 = st.selectbox('Sex',('Male','Female'))
        bmi = st.text_input('BMI')
        children = st.text_input('Children')
        smoker_1 = st.selectbox('Smoker',('Yes','No'))
        region_1 = st.selectbox('Region',('Southeast','Southwest','Northwest','Northeast'))
        #sex
        if sex_1 == 'Male':
           sex = 1
        else:
           sex = 0    
        #smoker
        if smoker_1 == 'Yes':
           smoker = 1
        else:
           smoker = 0  
        #region
        if region_1 == 'Southeast':
           region = 0
        elif region_1 == 'Southwest':
           region = 1   
        elif region_1 == 'Northwest':
           region = 2
        else:
           region = 3  

        Medical_Insurance = ''
        if st.button('Get cost'):
            Medical_Insurance  = mip([int(age), sex, int(bmi), int(children), smoker, region])  
        st.success(Medical_Insurance)

    if __name__ == '__main__':
        main()

if selected == "About":
    #st.title('About')
    st.title('Hi, Anirudh here :smiley:')
    st.subheader('Hope this app was useful to you :innocent:')
    st.write('I am a student as of now who is passionate about Data Science and this is a insurance prdictor which uses linear regression to predict the cost of the insurance but the model accuracy is low ie 0.7454474167181153 so it is not exact but it is enough to get a idea. see the sample dataset to know how to fill in details.')
    st.write('[More projects in GITHUB >](https://github.com/4nirudh5)')
