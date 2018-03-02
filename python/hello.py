from flask import Flask
import json
import os
import mysql.connector

#import time
#import csv
#import math
#import random

app = Flask(__name__)
port = int(os.getenv("PORT"))
data = json.loads(os.getenv("VCAP_SERVICES"))

@app.route('/')
def hello_world():
	try:
		cnx = mysql.connector.connect(user=data['mysql'][0]['credentials']['username'], password=data['mysql'][0]['credentials']['password'],host=data['mysql'][0]['credentials']['host'],port=json.dumps(data['mysql'][0]['credentials']['port']),ssl_ca='/etc/ssl/certs/',ssl_verify_cert=True)
		cursor = cnx.cursor(buffered=True)
		cursor.execute("USE SurveyResults")
		cursor.execute("SELECT * FROM SurveyResults")
		return str(cursor.execute(query))
	except mysql.connector.Error as err:
		return str(err)
	else:
		cursor.close()
  		cnx.close()

if __name__ == '__main__':
	app.run(host= '0.0.0.0',port=port)
