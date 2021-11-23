import twilio
import random
from twilio.rest import Client 
from os import times
import mysql.connector
from datetime import datetime
with open('id.txt','r') as file: id = file.read()
account_sid = 'ACcfdb2af6df861a91e8e2d2b5ed9105f2' 
auth_token = 'e1fd82d5d880314fffddf6ce27079bfc' 
client= Client(account_sid, auth_token) 
message = client.messages.create( 
body='Thank you for using covid predictor your id is : ' + str(id), 
from_='+18646614447', 
to = '+916303731463' 
)

print(message.sid) 


