from pkg_resources import require
import streamlit as st
import pandas as pd
import mysql.connector
from datetime import datetime
import random
from bokeh.models.widgets import Div

def main():
    st.title("Covid 19 Prediction")
    menu = ["Home","Covid Prediction" , "Results" , "About" ]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice =="Home":
        
        st.subheader("What is Corona Virus ? \n Coronaviruses (CoV) are a large family of viruses that cause illness ranging from the common cold to more severe diseases. A novel coronavirus (nCoV) is a new strain that has not been previously identified in humans")
       
        st.image('./images/covid.jpg')
        st.subheader('What Causes Covid 19 ? \n COVID-19 is caused by infection with the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) virus strain' )
        st.image('./images/lungs.jpg')

        st.subheader('What are variants of COVID-19 ? \n Alpha, beta, gamma, and delta variants of the SARS-CoV-2 coronavirus are classified as variants of concern. A variant of high consequence is a variant for which current vaccines do not offer protection. As of now, there are no SARS-CoV-2 variants of high consequence')
        st.image('./images/variants.png')
        st.subheader('Comparing COVID-19 cases from around the world')
        st.image('./images/Graph.png')
        
        st.subheader('Where was COVID-19 first discovered  ? \n The first known infections from SARS-CoV-2 were discovered in Wuhan, China. The original source of viral transmission to humans remains unclear, as does whether the virus became pathogenic before or after the spillover event. ')
        st.image('./images/wuhan.jpg')

        st.subheader('How COVID-19 was transferring one to other ? \n')
        st.video('./videos/animation.mp4')



    if choice =="Covid Prediction":
        st.subheader("Covid Prediction Using pre Condition")
        st.image('./images/covid 19.jpg')
        form = st.form(key='form')
        username = form.text_input("Username" )
        gender = form.selectbox("Gender",["Male","Female"])
        age = form.text_input("age")
        date = form.date_input('Date')
        form.subheader("Select the Applicable Comborbidities")
        intubed= form.checkbox('Intubed')
        pneumonia= form.checkbox('Pneumonia')
        pregnancy= form.checkbox('Pregnancy')
        copd= form.checkbox('COPD')
        asthama= form.checkbox('Asthama')
        inmsupr= form.checkbox('Inmsupr')
        hypertension= form.checkbox('Hypertension')
        cardiovascular= form.checkbox('Cardiovascular')
        obesity= form.checkbox('Obesity')
        renal_chronic= form.checkbox('Renal chronic')
        tobacco= form.checkbox('Tobacco')
        contact_other_covid= form.checkbox('contacted other covid Patients')
        submit_button=form.form_submit_button("Submit")

        if submit_button:
            st.success("Hello {} your details Submitted Succesfully :smile: ".format(username))
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Awez@0987",
            port= "3306",
            database="database2"
            )

            mycursor = mydb.cursor()
            id = random.randint(10000, 99999)
            sql1 = "INSERT INTO covid (id, name, age, date, intubed, pneumonia, gender, pregnancy, copd, asthama, inmsupr, hypertension, cardiovascular, obesity, renal_chronic, tobacco, contact_other_covid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (id, username , age , date , intubed , pneumonia , gender , pregnancy , copd , asthama , inmsupr , hypertension, cardiovascular , obesity , renal_chronic , tobacco , contact_other_covid )
            mycursor.execute(sql1, val)
            mydb.commit()



    if choice =="About":
        st.subheader("About")
        js = "window.open('http://127.0.0.1:5500/machine.html')"  # New tab or window
        js = "window.location.href = 'http://127.0.0.1:5500/machine.html'"  # Current tab
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

    if choice =="Results":
        st.image('./images/result.jpg')
        st.subheader("Get your Report Here !!")
        form2 = st.form(key='form2')
        ID = form2.text_input("ID" )
        submit_button=form2.form_submit_button("Submit")
        
        if submit_button:
            st.success("Hello  your Result is Retriving From database..Please Wait !! :smile: ")
        

  

if __name__ == '__main__':
	main()