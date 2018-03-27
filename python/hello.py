from flask import Flask, make_response
import json
import os
import mysql.connector
from mysql.connector.constants import ClientFlag
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from math import pi
from random import randint
import random
import StringIO
from wordcloud import WordCloud

app = Flask(__name__)
port = int(os.getenv("PORT"))
db_creds = json.loads(os.getenv("VCAP_SERVICES"))['mysql'][0]['credentials']

@app.route('/')
def hello_world():

	analysisdf = pd.DataFrame(result, columns = ["EM1","TEAM",'AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP','TA1','TA2','TA3','TB1','TB2','TB3'])
        TA1 = ' '.join([w.replace(' ', '_') for w in analysisdf["TA1"].tolist()])
        TA2 = ' '.join([w.replace(' ', '_') for w in analysisdf["TA2"].tolist()])
        TA3 = ' '.join([w.replace(' ', '_') for w in analysisdf["TA3"].tolist()])
        TB1 = ' '.join([w.replace(' ', '_') for w in analysisdf["TB1"].tolist()])
        TB2 = ' '.join([w.replace(' ', '_') for w in analysisdf["TB2"].tolist()])
        TB3 = ' '.join([w.replace(' ', '_') for w in analysisdf["TB3"].tolist()])
        workskills = TA1 + ' ' + TA2 + ' ' + TA3
        otherskills = TB1 + ' ' + TB2 + ' ' + TB3

	return workskills
	#return "All Done"

@app.route('/workskills.png')
def workskills():
	try:
		cnx = mysql.connector.connect(host=db_creds['host'],port=db_creds['port'],user=db_creds['username'],password=db_creds['password'],database=db_creds['name'],client_flags=[ClientFlag.SSL])
		cursor = cnx.cursor(buffered=True)
		cursor.execute("SELECT * FROM SurveyResults")
		result = cursor.fetchall()
	except mysql.connector.Error as err:
		return str(err)
	else:
		cursor.close()
		cnx.close()

        analysisdf = pd.DataFrame(result, columns = ["EM1","TEAM",'AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP','TA1','TA2','TA3','TB1','TB2','TB3'])
        TA1 = ' '.join([w.replace(' ', '_') for w in analysisdf["TA1"].tolist()])
        TA2 = ' '.join([w.replace(' ', '_') for w in analysisdf["TA2"].tolist()])
        TA3 = ' '.join([w.replace(' ', '_') for w in analysisdf["TA3"].tolist()])
        TB1 = ' '.join([w.replace(' ', '_') for w in analysisdf["TB1"].tolist()])
        TB2 = ' '.join([w.replace(' ', '_') for w in analysisdf["TB2"].tolist()])
        TB3 = ' '.join([w.replace(' ', '_') for w in analysisdf["TB3"].tolist()])
        workskills = TA1 + ' ' + TA2 + ' ' + TA3
   
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	wordcloud = WordCloud(background_color="white", width=1000, height=1000, relative_scaling=.9, prefer_horizontal=.7).generate(workskills)
	axis.imshow(wordcloud, interpolation='bilinear')
	axis.set_title("Work Skills", size=20, y=1.02, fontweight='bold')
	axis.set_axis_off()

	canvas = FigureCanvas(fig)
	output = StringIO.StringIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	
	return response

@app.route('/otherskills.png')
def otherskills():
	try:
		cnx = mysql.connector.connect(host=db_creds['host'],port=db_creds['port'],user=db_creds['username'],password=db_creds['password'],database=db_creds['name'],client_flags=[ClientFlag.SSL])
		cursor = cnx.cursor(buffered=True)
		cursor.execute("SELECT * FROM SurveyResults")
		result = cursor.fetchall()
	except mysql.connector.Error as err:
		return str(err)
	else:
		cursor.close()
		cnx.close()

        analysisdf = pd.DataFrame(result, columns = ["EM1","TEAM",'AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP','TA1','TA2','TA3','TB1','TB2','TB3'])
        TA1 = ' '.join([w.replace(' ', '_') for w in analysisdf["TA1"].tolist()])
        TA2 = ' '.join([w.replace(' ', '_') for w in analysisdf["TA2"].tolist()])
        TA3 = ' '.join([w.replace(' ', '_') for w in analysisdf["TA3"].tolist()])
        TB1 = ' '.join([w.replace(' ', '_') for w in analysisdf["TB1"].tolist()])
        TB2 = ' '.join([w.replace(' ', '_') for w in analysisdf["TB2"].tolist()])
        TB3 = ' '.join([w.replace(' ', '_') for w in analysisdf["TB3"].tolist()])
        otherskills = TB1 + ' ' + TB2 + ' ' + TB3
    
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	wordcloud = WordCloud(background_color="white", width=1000, height=1000, relative_scaling=.9, prefer_horizontal=.7).generate(otherskills)
	axis.imshow(wordcloud, interpolation='bilinear')
	axis.set_title("Other Skills", size=20, y=1.02, fontweight='bold')
	axis.set_axis_off()

	canvas = FigureCanvas(fig)
	output = StringIO.StringIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	
	return response


@app.route('/team_skills1.png')
def team_skills1():
	try:
		cnx = mysql.connector.connect(host=db_creds['host'],port=db_creds['port'],user=db_creds['username'],password=db_creds['password'],database=db_creds['name'],client_flags=[ClientFlag.SSL])
		cursor = cnx.cursor(buffered=True)
		cursor.execute("SELECT * FROM SurveyResults")
		result = cursor.fetchall()
	except mysql.connector.Error as err:
		return str(err)
	else:
		cursor.close()
		cnx.close()

	analysisdf = pd.DataFrame(result, columns = ["EM1","TEAM",'AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP','TA1','TA2','TA3','TB1','TB2','TB3'])
  
	analysisdf[['AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP']] = analysisdf[['AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP']].astype(float)

	analysisdf["Analytical Skills"] = (analysisdf["AA"] + analysisdf["AB"] + analysisdf["AC"] + analysisdf["AD"] + analysisdf["AE"] + analysisdf["AF"])/6
	analysisdf["Academic Expertise"] = (analysisdf["AG"] + analysisdf["AH"] + analysisdf["AI"] + analysisdf["AJ"] + analysisdf["AK"] + analysisdf["AL"])/6
	analysisdf["Domain Expertise"] = (analysisdf["AM"] + analysisdf["AN"] + analysisdf["AO"] + analysisdf["AP"] + analysisdf["AQ"] + analysisdf["AR"])/6
	analysisdf["Collaboration"] = (analysisdf["AS"] + analysisdf["AT"] + analysisdf["AU"] + analysisdf["AV"] + analysisdf["AW"] + analysisdf["AX"])/6
	analysisdf["Communication"] = (analysisdf["AY"] + analysisdf["AZ"] + analysisdf["BA"] + analysisdf["BB"] + analysisdf["BC"] + analysisdf["BD"])/6
   	analysisdf["IT Expertise"] = (analysisdf["BE"] + analysisdf["BF"] + analysisdf["BG"] + analysisdf["BH"] + analysisdf["BI"] + analysisdf["BJ"])/6
	analysisdf["Analytical Tools"] = (analysisdf["BK"] + analysisdf["BL"] + analysisdf["BM"] + analysisdf["BN"] + analysisdf["BO"] + analysisdf["BP"])/6

 	summaryTeam = analysisdf.groupby('TEAM', as_index=False).agg({"Analytical Skills": "mean", "Academic Expertise": "mean", "Domain Expertise": "mean", "Collaboration": "mean", "Communication": "mean", "IT Expertise": "mean", "Analytical Tools": "mean"})

	summaryTeam2 = analysisdf.groupby('TEAM', as_index=False).agg({"AA": "mean", "AB": "mean", "AC": "mean", "AD": "mean", "AE": "mean", "AF": "mean","AG": "mean", "AH": "mean", "AI": "mean", "AJ": "mean", "AK": "mean", "AL": "mean","AM": "mean", "AN": "mean", "AO": "mean", "AP": "mean", "AQ": "mean", "AR": "mean","AS": "mean", "AT": "mean", "AU": "mean", "AV": "mean", "AW": "mean", "AX": "mean","AY": "mean", "AZ": "mean", "BA": "mean", "BB": "mean", "BC": "mean", "BD": "mean","BE": "mean", "BF": "mean", "BG": "mean", "BH": "mean", "BI": "mean", "BJ": "mean","BK": "mean", "BL": "mean", "BM": "mean", "BN": "mean", "BO": "mean", "BP": "mean"})
	summaryTeam2.columns = ["TEAM",'Descriptive Statistics','Structured Data','Sampling and Surveys','Predictive Analytics','Machine Learning','Unstructured Data','Social Research','Operational Research','Behavioural Economics','Econometrics','Geography and Mapping','Other Scientific Research','Tax Inspector or Risk Analyst','Trained Accountant','Legal Knowledge','Qualified Project Manager','Running my own business','Other HMRC functions','Working across teams in HMRC','Working in the policy partnership','Working with ministers','Working with contactors','Working cross government','Agile Project Management','Public Speaking','Data Visualisation','Dynamic Visualisation','Written Communication','Engaging the Public','Photoshop / Graphic Design','Database Systems','Software Engineering','Data Engineering','Cyber Security','IT Rollout','Other specific IT specialism','Database Query','Analytical Packages','Big Data Tools','Object Oriented Programming','Developing using and IDE','Other Programming Languages']     

	summaryTeam21 = summaryTeam2.iloc[0].drop(summaryTeam2.iloc[0].loc[summaryTeam2.iloc[0] == summaryTeam2.iloc[0][1:].max(axis=0)].axes[0][randint(0, len(summaryTeam2.iloc[0].loc[summaryTeam2.iloc[0] == summaryTeam2.iloc[0][1:].max(axis=0)])-1)])
	skill2 = summaryTeam21.loc[summaryTeam21 == summaryTeam21[1:].max(axis=0)].axes[0][randint(0, len(summaryTeam21.loc[summaryTeam21 == summaryTeam21[1:].max(axis=0)].axes[0])-1)]

	fig = Figure(figsize=(6.42,0.428))
	axis = fig.add_subplot(1, 1, 1)
	axis.set_axis_off()
	exec("axis.set_title('%ss team is really good at: %s and %s', size=9, y=0.5)")% (summaryTeam2["TEAM"][0],summaryTeam2.iloc[0].loc[summaryTeam2.iloc[0] == summaryTeam2.iloc[0][1:].max(axis=0)].axes[0][randint(0, len(summaryTeam2.iloc[0].loc[summaryTeam2.iloc[0] == summaryTeam2.iloc[0][1:].max(axis=0)])-1)],skill2)

	canvas = FigureCanvas(fig)
	output = StringIO.StringIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	
	return response

@app.route('/team_skills2.png')
def team_skills2():
	try:
		cnx = mysql.connector.connect(host=db_creds['host'],port=db_creds['port'],user=db_creds['username'],password=db_creds['password'],database=db_creds['name'],client_flags=[ClientFlag.SSL])
		cursor = cnx.cursor(buffered=True)
		cursor.execute("SELECT * FROM SurveyResults")
		result = cursor.fetchall()
	except mysql.connector.Error as err:
		return str(err)
	else:
		cursor.close()
		cnx.close()

	analysisdf = pd.DataFrame(result, columns = ["EM1","TEAM",'AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP','TA1','TA2','TA3','TB1','TB2','TB3'])
  
	analysisdf[['AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP']] = analysisdf[['AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP']].astype(float)

	analysisdf["Analytical Skills"] = (analysisdf["AA"] + analysisdf["AB"] + analysisdf["AC"] + analysisdf["AD"] + analysisdf["AE"] + analysisdf["AF"])/6
	analysisdf["Academic Expertise"] = (analysisdf["AG"] + analysisdf["AH"] + analysisdf["AI"] + analysisdf["AJ"] + analysisdf["AK"] + analysisdf["AL"])/6
	analysisdf["Domain Expertise"] = (analysisdf["AM"] + analysisdf["AN"] + analysisdf["AO"] + analysisdf["AP"] + analysisdf["AQ"] + analysisdf["AR"])/6
	analysisdf["Collaboration"] = (analysisdf["AS"] + analysisdf["AT"] + analysisdf["AU"] + analysisdf["AV"] + analysisdf["AW"] + analysisdf["AX"])/6
	analysisdf["Communication"] = (analysisdf["AY"] + analysisdf["AZ"] + analysisdf["BA"] + analysisdf["BB"] + analysisdf["BC"] + analysisdf["BD"])/6
   	analysisdf["IT Expertise"] = (analysisdf["BE"] + analysisdf["BF"] + analysisdf["BG"] + analysisdf["BH"] + analysisdf["BI"] + analysisdf["BJ"])/6
	analysisdf["Analytical Tools"] = (analysisdf["BK"] + analysisdf["BL"] + analysisdf["BM"] + analysisdf["BN"] + analysisdf["BO"] + analysisdf["BP"])/6

 	summaryTeam = analysisdf.groupby('TEAM', as_index=False).agg({"Analytical Skills": "mean", "Academic Expertise": "mean", "Domain Expertise": "mean", "Collaboration": "mean", "Communication": "mean", "IT Expertise": "mean", "Analytical Tools": "mean"})

	summaryTeam2 = analysisdf.groupby('TEAM', as_index=False).agg({"AA": "mean", "AB": "mean", "AC": "mean", "AD": "mean", "AE": "mean", "AF": "mean","AG": "mean", "AH": "mean", "AI": "mean", "AJ": "mean", "AK": "mean", "AL": "mean","AM": "mean", "AN": "mean", "AO": "mean", "AP": "mean", "AQ": "mean", "AR": "mean","AS": "mean", "AT": "mean", "AU": "mean", "AV": "mean", "AW": "mean", "AX": "mean","AY": "mean", "AZ": "mean", "BA": "mean", "BB": "mean", "BC": "mean", "BD": "mean","BE": "mean", "BF": "mean", "BG": "mean", "BH": "mean", "BI": "mean", "BJ": "mean","BK": "mean", "BL": "mean", "BM": "mean", "BN": "mean", "BO": "mean", "BP": "mean"})
	summaryTeam2.columns = ["TEAM",'Descriptive Statistics','Structured Data','Sampling and Surveys','Predictive Analytics','Machine Learning','Unstructured Data','Social Research','Operational Research','Behavioural Economics','Econometrics','Geography and Mapping','Other Scientific Research','Tax Inspector or Risk Analyst','Trained Accountant','Legal Knowledge','Qualified Project Manager','Running my own business','Other HMRC functions','Working across teams in HMRC','Working in the policy partnership','Working with ministers','Working with contactors','Working cross government','Agile Project Management','Public Speaking','Data Visualisation','Dynamic Visualisation','Written Communication','Engaging the Public','Photoshop / Graphic Design','Database Systems','Software Engineering','Data Engineering','Cyber Security','IT Rollout','Other specific IT specialism','Database Query','Analytical Packages','Big Data Tools','Object Oriented Programming','Developing using and IDE','Other Programming Languages']     

	summaryTeam21 = summaryTeam2.iloc[1].drop(summaryTeam2.iloc[1].loc[summaryTeam2.iloc[1] == summaryTeam2.iloc[1][1:].max(axis=0)].axes[0][randint(0, len(summaryTeam2.iloc[1].loc[summaryTeam2.iloc[1] == summaryTeam2.iloc[1][1:].max(axis=0)])-1)])
	skill2 = summaryTeam21.loc[summaryTeam21 == summaryTeam21[1:].max(axis=0)].axes[0][randint(0, len(summaryTeam21.loc[summaryTeam21 == summaryTeam21[1:].max(axis=0)].axes[0])-1)]

	fig = Figure(figsize=(6.42,0.428))
	axis = fig.add_subplot(1, 1, 1)
	axis.set_axis_off()
	exec("axis.set_title('%ss team is really good at: %s and %s', size=9, y=0.5)")% (summaryTeam2["TEAM"][1],summaryTeam2.iloc[1].loc[summaryTeam2.iloc[1] == summaryTeam2.iloc[1][1:].max(axis=0)].axes[0][randint(0, len(summaryTeam2.iloc[1].loc[summaryTeam2.iloc[1] == summaryTeam2.iloc[1][1:].max(axis=0)])-1)],skill2)

	canvas = FigureCanvas(fig)
	output = StringIO.StringIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	
	return response

@app.route('/team_skills3.png')
def team_skills3():
	try:
		cnx = mysql.connector.connect(host=db_creds['host'],port=db_creds['port'],user=db_creds['username'],password=db_creds['password'],database=db_creds['name'],client_flags=[ClientFlag.SSL])
		cursor = cnx.cursor(buffered=True)
		cursor.execute("SELECT * FROM SurveyResults")
		result = cursor.fetchall()
	except mysql.connector.Error as err:
		return str(err)
	else:
		cursor.close()
		cnx.close()

	analysisdf = pd.DataFrame(result, columns = ["EM1","TEAM",'AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP','TA1','TA2','TA3','TB1','TB2','TB3'])
  
	analysisdf[['AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP']] = analysisdf[['AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP']].astype(float)

	analysisdf["Analytical Skills"] = (analysisdf["AA"] + analysisdf["AB"] + analysisdf["AC"] + analysisdf["AD"] + analysisdf["AE"] + analysisdf["AF"])/6
	analysisdf["Academic Expertise"] = (analysisdf["AG"] + analysisdf["AH"] + analysisdf["AI"] + analysisdf["AJ"] + analysisdf["AK"] + analysisdf["AL"])/6
	analysisdf["Domain Expertise"] = (analysisdf["AM"] + analysisdf["AN"] + analysisdf["AO"] + analysisdf["AP"] + analysisdf["AQ"] + analysisdf["AR"])/6
	analysisdf["Collaboration"] = (analysisdf["AS"] + analysisdf["AT"] + analysisdf["AU"] + analysisdf["AV"] + analysisdf["AW"] + analysisdf["AX"])/6
	analysisdf["Communication"] = (analysisdf["AY"] + analysisdf["AZ"] + analysisdf["BA"] + analysisdf["BB"] + analysisdf["BC"] + analysisdf["BD"])/6
   	analysisdf["IT Expertise"] = (analysisdf["BE"] + analysisdf["BF"] + analysisdf["BG"] + analysisdf["BH"] + analysisdf["BI"] + analysisdf["BJ"])/6
	analysisdf["Analytical Tools"] = (analysisdf["BK"] + analysisdf["BL"] + analysisdf["BM"] + analysisdf["BN"] + analysisdf["BO"] + analysisdf["BP"])/6

 	summaryTeam = analysisdf.groupby('TEAM', as_index=False).agg({"Analytical Skills": "mean", "Academic Expertise": "mean", "Domain Expertise": "mean", "Collaboration": "mean", "Communication": "mean", "IT Expertise": "mean", "Analytical Tools": "mean"})

	summaryTeam2 = analysisdf.groupby('TEAM', as_index=False).agg({"AA": "mean", "AB": "mean", "AC": "mean", "AD": "mean", "AE": "mean", "AF": "mean","AG": "mean", "AH": "mean", "AI": "mean", "AJ": "mean", "AK": "mean", "AL": "mean","AM": "mean", "AN": "mean", "AO": "mean", "AP": "mean", "AQ": "mean", "AR": "mean","AS": "mean", "AT": "mean", "AU": "mean", "AV": "mean", "AW": "mean", "AX": "mean","AY": "mean", "AZ": "mean", "BA": "mean", "BB": "mean", "BC": "mean", "BD": "mean","BE": "mean", "BF": "mean", "BG": "mean", "BH": "mean", "BI": "mean", "BJ": "mean","BK": "mean", "BL": "mean", "BM": "mean", "BN": "mean", "BO": "mean", "BP": "mean"})
	summaryTeam2.columns = ["TEAM",'Descriptive Statistics','Structured Data','Sampling and Surveys','Predictive Analytics','Machine Learning','Unstructured Data','Social Research','Operational Research','Behavioural Economics','Econometrics','Geography and Mapping','Other Scientific Research','Tax Inspector or Risk Analyst','Trained Accountant','Legal Knowledge','Qualified Project Manager','Running my own business','Other HMRC functions','Working across teams in HMRC','Working in the policy partnership','Working with ministers','Working with contactors','Working cross government','Agile Project Management','Public Speaking','Data Visualisation','Dynamic Visualisation','Written Communication','Engaging the Public','Photoshop / Graphic Design','Database Systems','Software Engineering','Data Engineering','Cyber Security','IT Rollout','Other specific IT specialism','Database Query','Analytical Packages','Big Data Tools','Object Oriented Programming','Developing using and IDE','Other Programming Languages']     

	summaryTeam21 = summaryTeam2.iloc[2].drop(summaryTeam2.iloc[2].loc[summaryTeam2.iloc[2] == summaryTeam2.iloc[2][1:].max(axis=0)].axes[0][randint(0, len(summaryTeam2.iloc[2].loc[summaryTeam2.iloc[2] == summaryTeam2.iloc[2][1:].max(axis=0)])-1)])
	skill2 = summaryTeam21.loc[summaryTeam21 == summaryTeam21[1:].max(axis=0)].axes[0][randint(0, len(summaryTeam21.loc[summaryTeam21 == summaryTeam21[1:].max(axis=0)].axes[0])-1)]

	fig = Figure(figsize=(6.42,0.428))
	axis = fig.add_subplot(1, 1, 1)
	axis.set_axis_off()
	exec("axis.set_title('%ss team is really good at: %s and %s', size=9, y=0.5)")% (summaryTeam2["TEAM"][2],summaryTeam2.iloc[2].loc[summaryTeam2.iloc[2] == summaryTeam2.iloc[2][1:].max(axis=0)].axes[0][randint(0, len(summaryTeam2.iloc[2].loc[summaryTeam2.iloc[2] == summaryTeam2.iloc[2][1:].max(axis=0)])-1)],skill2)

	canvas = FigureCanvas(fig)
	output = StringIO.StringIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	
	return response

@app.route('/last_person.png')
def last_person():
	try:
		cnx = mysql.connector.connect(host=db_creds['host'],port=db_creds['port'],user=db_creds['username'],password=db_creds['password'],database=db_creds['name'],client_flags=[ClientFlag.SSL])
		cursor = cnx.cursor(buffered=True)
		cursor.execute("SELECT * FROM SurveyResults")
		result = cursor.fetchall()
	except mysql.connector.Error as err:
		return str(err)
	else:
		cursor.close()
		cnx.close()

	analysisdf = pd.DataFrame(result, columns = ["EM1","TEAM",'Descriptive Statistics','Structured Data','Sampling and Surveys','Predictive Analytics','Machine Learning','Unstructured Data','Social Research','Operational Research','Behavioural Economics','Econometrics','Geography and Mapping','Other Scientific Research','Tax Inspector or Risk Analyst','Trained Accountant','Legal Knowledge','Qualified Project Manager','Running my own business','Other HMRC functions','Working across teams in HMRC','Working in the policy partnership','Working with ministers','Working with contactors','Working cross government','Agile Project Management','Public Speaking','Data Visualisation','Dynamic Visualisation','Written Communication','Engaging the Public','Photoshop / Graphic Design','Database Systems','Software Engineering','Data Engineering','Cyber Security','IT Rollout','Other specific IT specialism','Database Query','Analytical Packages','Big Data Tools','Object Oriented Programming','Developing using and IDE','Other Programming Languages','TA1','TA2','TA3','TB1','TB2','TB3'])    

	rec = len(analysisdf)-1

	fig = Figure(figsize=(6.42,0.428))
	axis = fig.add_subplot(1, 1, 1)
	axis.set_axis_off()
	exec("axis.set_title('The last person to fill in the survey was good at: %s and %s', size=9, y=0.5)") % (analysisdf.iloc[rec].loc[analysisdf.iloc[rec] == analysisdf.iloc[rec][2:43].max(axis=0)].axes[0][randint(0, len(analysisdf.iloc[rec].loc[analysisdf.iloc[rec] == analysisdf.iloc[rec][2:43].max(axis=0)])-1)],analysisdf.iloc[rec]["TB1"])

	canvas = FigureCanvas(fig)
	output = StringIO.StringIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	
	return response

@app.route('/radargraph1.png')
def plot1():
	try:
		cnx = mysql.connector.connect(host=db_creds['host'],port=db_creds['port'],user=db_creds['username'],password=db_creds['password'],database=db_creds['name'],client_flags=[ClientFlag.SSL])
		cursor = cnx.cursor(buffered=True)
		cursor.execute("SELECT * FROM SurveyResults")
		result = cursor.fetchall()
	except mysql.connector.Error as err:
		return str(err)
	else:
		cursor.close()
		cnx.close()

	analysisdf = pd.DataFrame(result, columns = ["EM1","TEAM",'AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP','TA1','TA2','TA3','TB1','TB2','TB3'])
  
	analysisdf[['AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP']] = analysisdf[['AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP']].astype(float)

	analysisdf["Analytical Skills"] = (analysisdf["AA"] + analysisdf["AB"] + analysisdf["AC"] + analysisdf["AD"] + analysisdf["AE"] + analysisdf["AF"])/6
	analysisdf["Academic Expertise"] = (analysisdf["AG"] + analysisdf["AH"] + analysisdf["AI"] + analysisdf["AJ"] + analysisdf["AK"] + analysisdf["AL"])/6
	analysisdf["Domain Expertise"] = (analysisdf["AM"] + analysisdf["AN"] + analysisdf["AO"] + analysisdf["AP"] + analysisdf["AQ"] + analysisdf["AR"])/6
	analysisdf["Collaboration"] = (analysisdf["AS"] + analysisdf["AT"] + analysisdf["AU"] + analysisdf["AV"] + analysisdf["AW"] + analysisdf["AX"])/6
	analysisdf["Communication"] = (analysisdf["AY"] + analysisdf["AZ"] + analysisdf["BA"] + analysisdf["BB"] + analysisdf["BC"] + analysisdf["BD"])/6
   	analysisdf["IT Expertise"] = (analysisdf["BE"] + analysisdf["BF"] + analysisdf["BG"] + analysisdf["BH"] + analysisdf["BI"] + analysisdf["BJ"])/6
	analysisdf["Analytical Tools"] = (analysisdf["BK"] + analysisdf["BL"] + analysisdf["BM"] + analysisdf["BN"] + analysisdf["BO"] + analysisdf["BP"])/6

 	summaryTeam = analysisdf.groupby('TEAM', as_index=False).agg({"Analytical Skills": "mean", "Academic Expertise": "mean", "Domain Expertise": "mean", "Collaboration": "mean", "Communication": "mean", "IT Expertise": "mean", "Analytical Tools": "mean"})

        angles = [n / float(7) * 2 * pi for n in range(7)]
        angles += angles[:1]

 	values1 = summaryTeam.loc[0].drop('TEAM').values.flatten().tolist()
	values1 += values1[:1]

	fig = Figure()
	axis = fig.add_subplot(1, 1, 1, polar=True)
	axis.set_title(summaryTeam["TEAM"][0]+"'s Team", size=20, fontweight='bold')
	axis.set_xticks(angles[:-1])
	axis.set_xticklabels(list(summaryTeam)[1:])
	axis.set_rlabel_position(0)
	axis.set_ylim(0, 5)
	axis.set_yticks([1,2,3,4,5])
	axis.set_yticklabels(["1","2","3","4","5"])
	axis.plot(angles, values1, linewidth=1, linestyle='solid')
	axis.fill(angles, values1, 'b', alpha=0.1)

	canvas = FigureCanvas(fig)
	output = StringIO.StringIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	
	return response

@app.route('/radargraph2.png')
def plot2():
	try:
		cnx = mysql.connector.connect(host=db_creds['host'],port=db_creds['port'],user=db_creds['username'],password=db_creds['password'],database=db_creds['name'],client_flags=[ClientFlag.SSL])
		cursor = cnx.cursor(buffered=True)
		cursor.execute("SELECT * FROM SurveyResults")
		result = cursor.fetchall()
	except mysql.connector.Error as err:
		return str(err)
	else:
		cursor.close()
		cnx.close()

	analysisdf = pd.DataFrame(result, columns = ["EM1","TEAM",'AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP','TA1','TA2','TA3','TB1','TB2','TB3'])

	analysisdf[['AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP']] = analysisdf[['AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP']].astype(float)

	analysisdf["Analytical Skills"] = (analysisdf["AA"] + analysisdf["AB"] + analysisdf["AC"] + analysisdf["AD"] + analysisdf["AE"] + analysisdf["AF"])/6
	analysisdf["Academic Expertise"] = (analysisdf["AG"] + analysisdf["AH"] + analysisdf["AI"] + analysisdf["AJ"] + analysisdf["AK"] + analysisdf["AL"])/6
	analysisdf["Domain Expertise"] = (analysisdf["AM"] + analysisdf["AN"] + analysisdf["AO"] + analysisdf["AP"] + analysisdf["AQ"] + analysisdf["AR"])/6
	analysisdf["Collaboration"] = (analysisdf["AS"] + analysisdf["AT"] + analysisdf["AU"] + analysisdf["AV"] + analysisdf["AW"] + analysisdf["AX"])/6
	analysisdf["Communication"] = (analysisdf["AY"] + analysisdf["AZ"] + analysisdf["BA"] + analysisdf["BB"] + analysisdf["BC"] + analysisdf["BD"])/6
   	analysisdf["IT Expertise"] = (analysisdf["BE"] + analysisdf["BF"] + analysisdf["BG"] + analysisdf["BH"] + analysisdf["BI"] + analysisdf["BJ"])/6
	analysisdf["Analytical Tools"] = (analysisdf["BK"] + analysisdf["BL"] + analysisdf["BM"] + analysisdf["BN"] + analysisdf["BO"] + analysisdf["BP"])/6

 	summaryTeam = analysisdf.groupby('TEAM', as_index=False).agg({"Analytical Skills": "mean", "Academic Expertise": "mean", "Domain Expertise": "mean", "Collaboration": "mean", "Communication": "mean", "IT Expertise": "mean", "Analytical Tools": "mean"})

        angles = [n / float(7) * 2 * pi for n in range(7)]
        angles += angles[:1]

 	values2 = summaryTeam.loc[1].drop('TEAM').values.flatten().tolist()
	values2 += values2[:1]

	fig = Figure()
	axis = fig.add_subplot(1, 1, 1, polar=True)
	axis.set_title(summaryTeam["TEAM"][1]+"'s Team", size=20, fontweight='bold')
	axis.set_xticks(angles[:-1])
	axis.set_xticklabels(list(summaryTeam)[1:])
	axis.set_rlabel_position(0)
	axis.set_ylim(0, 5)
	axis.set_yticks([1,2,3,4,5])
	axis.set_yticklabels(["1","2","3","4","5"])
	axis.plot(angles, values2, linewidth=1, linestyle='solid')
	axis.fill(angles, values2, 'b', alpha=0.1)

	canvas = FigureCanvas(fig)
	output = StringIO.StringIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	
	return response

@app.route('/radargraph3.png')
def plot3():
	try:
		cnx = mysql.connector.connect(host=db_creds['host'],port=db_creds['port'],user=db_creds['username'],password=db_creds['password'],database=db_creds['name'],client_flags=[ClientFlag.SSL])
		cursor = cnx.cursor(buffered=True)
		cursor.execute("SELECT * FROM SurveyResults")
		result = cursor.fetchall()
	except mysql.connector.Error as err:
		return str(err)
	else:
		cursor.close()
		cnx.close()

	analysisdf = pd.DataFrame(result, columns = ["EM1","TEAM",'AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP','TA1','TA2','TA3','TB1','TB2','TB3'])
  
	analysisdf[['AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP']] = analysisdf[['AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP']].astype(float)

	analysisdf["Analytical Skills"] = (analysisdf["AA"] + analysisdf["AB"] + analysisdf["AC"] + analysisdf["AD"] + analysisdf["AE"] + analysisdf["AF"])/6
	analysisdf["Academic Expertise"] = (analysisdf["AG"] + analysisdf["AH"] + analysisdf["AI"] + analysisdf["AJ"] + analysisdf["AK"] + analysisdf["AL"])/6
	analysisdf["Domain Expertise"] = (analysisdf["AM"] + analysisdf["AN"] + analysisdf["AO"] + analysisdf["AP"] + analysisdf["AQ"] + analysisdf["AR"])/6
	analysisdf["Collaboration"] = (analysisdf["AS"] + analysisdf["AT"] + analysisdf["AU"] + analysisdf["AV"] + analysisdf["AW"] + analysisdf["AX"])/6
	analysisdf["Communication"] = (analysisdf["AY"] + analysisdf["AZ"] + analysisdf["BA"] + analysisdf["BB"] + analysisdf["BC"] + analysisdf["BD"])/6
   	analysisdf["IT Expertise"] = (analysisdf["BE"] + analysisdf["BF"] + analysisdf["BG"] + analysisdf["BH"] + analysisdf["BI"] + analysisdf["BJ"])/6
	analysisdf["Analytical Tools"] = (analysisdf["BK"] + analysisdf["BL"] + analysisdf["BM"] + analysisdf["BN"] + analysisdf["BO"] + analysisdf["BP"])/6

 	summaryTeam = analysisdf.groupby('TEAM', as_index=False).agg({"Analytical Skills": "mean", "Academic Expertise": "mean", "Domain Expertise": "mean", "Collaboration": "mean", "Communication": "mean", "IT Expertise": "mean", "Analytical Tools": "mean"})

        angles = [n / float(7) * 2 * pi for n in range(7)]
        angles += angles[:1]

 	values3 = summaryTeam.loc[2].drop('TEAM').values.flatten().tolist()
	values3 += values3[:1]

	fig = Figure()
	axis = fig.add_subplot(1, 1, 1, polar=True)
	axis.set_title(summaryTeam["TEAM"][2]+"'s Team", size=20, fontweight='bold')
	axis.set_xticks(angles[:-1])
	axis.set_xticklabels(list(summaryTeam)[1:])
	axis.set_rlabel_position(0)
	axis.set_ylim(0, 5)
	axis.set_yticks([1,2,3,4,5])
	axis.set_yticklabels(["1","2","3","4","5"])
	axis.plot(angles, values3, linewidth=1, linestyle='solid')
	axis.fill(angles, values3, 'b', alpha=0.1)

	canvas = FigureCanvas(fig)
	output = StringIO.StringIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	
	return response

if __name__ == '__main__':
	app.run(host= '0.0.0.0',port=port)
