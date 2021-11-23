from pkg_resources import require
import streamlit as st
import pandas as pd
import os
import mysql.connector
from datetime import datetime
import random
from bokeh.models.widgets import Div
import time
import webbrowser

from streamlit.elements.arrow import Data


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
        mobile = form.text_input("mobile")
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
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Awez@0987",
            port= "3306",
            database="database2"
            )

            mycursor = mydb.cursor()
            id = random.randint(10000, 99999)
            sql1 = "INSERT INTO covid (id, name, age, date, mobile , intubed, pneumonia, gender, pregnancy, copd, asthama, inmsupr, hypertension, cardiovascular, obesity, renal_chronic, tobacco, contact_other_covid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (id, username , age , date ,mobile , intubed , pneumonia , gender , pregnancy , copd , asthama , inmsupr , hypertension, cardiovascular , obesity , renal_chronic , tobacco , contact_other_covid )
            mycursor.execute(sql1, val)
            mydb.commit()
            f = open( 'id.txt', 'w' )
            f.write(str(id))
            f.close()
            
            sql2="truncate table database2.currentuser3"
            mycursor.execute(sql2)
            mydb.commit()

            sql3="INSERT INTO database2.currentuser3 (id, name, date) VALUES (%s, %s, %s );"
            val3=(id,username,date)
            mycursor.execute(sql3, val3)
            mydb.commit()

            st.warning('ID Sent to your mobile number')
            st.success("Hello {} your details Submitted Succesfully :smile: , Your id is  {} ".format(username, id))
            os.system('python notification.py')
            



    if choice =="About":
        st.subheader("About")
        st.subheader("Platform : Streamlit  " )
        st.subheader("Communication : Twilio 2.0")
        st.subheader("Database: Mysql")
        st.subheader("version : 1.0")
        url = 'http://127.0.0.1:5500/about.html'
        if st.button('Meet the Creators'):
            webbrowser.open_new_tab(url)

    if choice =="Results":
        st.image('./images/result.jpg')
        st.subheader("Get your Report Here !!")
        form2 = st.form(key='form2')
        ID = form2.text_input("ID" )
        submit_button=form2.form_submit_button("Submit")
        
        if submit_button:
           
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Awez@0987",
            port= "3306",
            database="database2"
            )
            sql_select_Query = """select * from covid where id = %s"""
            st.write(ID)
            val=(ID)
            cursor = mydb.cursor()
            cursor.execute(sql_select_Query, (ID,)) 
            records = cursor.fetchall()
            
             
            if(cursor.rowcount!=0):
                st.success("Hello {} your Result is Retriving From database..Please Wait !! :smile: " .format(records[0][1]))
                time.sleep(2)
                for row in records:
                    st.write("Id : ", row[0], )
                    st.write("Name : ", row[1])
                    st.write("Age  : ", row[2])
                    st.write("Gender  : ", row[3])
                    st.write("Mobile  : ", row[5])
                    st.write("Date of Symptoms Started  : ", row[4])
                    
                    st.write("Covid Result  : ")
                    if(row[18]=='1'):
                        st.write("Likely to get Covid Positive")
                    if(row[18]=='0'):
                        st.write("Likely to get Covid Negative")
                    if(row[18]==None):
                        st.write("Awaiting for result")
                    
            
            else:
                st.success("Please Enter the valid ID !! \U0001F62C ")




        

  

if __name__ == '__main__':
	main()

