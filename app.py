from flask import*
from flask import render_template
import requests
import mysql.connector
from google.cloud.sql.connector import Connector,IPTypes
import sqlalchemy


app = Flask(__name__, static_folder="assets", template_folder="templates")


connector = Connector()
		
def getconn():
    conn = connector.connect(
        "website-deployment-demo:asia-south2:gcp-demo",
        "pymysql",
        user="root",
        password="admin123",
        db="info"
    )
    return conn


@app.route("/")
def k():
	return render_template("index.html")

@app.route("/<a>")
def k1(a):
	t=a+".html"
	return render_template(t)

@app.route("/submit",methods=["POST"])
def k2():
	k="\n\nEmail: "+request.form["email"]+"\nName: "+request.form["name"]+"\nPhone number: "+request.form["phone"]+"\nMessage: "+request.form["message"]
	print(k)
	name = request.form["name"]
	email = request.form['email']
	phonenumber = request.form['phone']
	message = request.form['message']
	try:
		pool = sqlalchemy.create_engine(
		"mysql+pymysql://",
		creator=getconn,)
		insert_stmt = sqlalchemy.text(
      "INSERT INTO INFO (name, email, phonenumber,message) VALUES (:name, :email, :phonenumber,:message)",
  		)	
		with pool.connect() as db_conn:
			db_conn.execute(insert_stmt, parameters={"name": name, "email":email, "phonenumber": phonenumber,"message":message})
			db_conn.commit()
	except:
		print("Error Occured")
	
	return render_template("contact.html")

# @app.errorhandler(404)
# def k3():
# 	return render_template("err.html")

# @app.errorhandler(Exception)
# def k4(Exception):
# 	return render_template("err_5.html")

# @app.route("/")
# def homePage():
# 	return "<h1>Hello World</h1>"

if __name__ == '__main__':
	app.run(host = "0.0.0.0",port = 8080)
# 	app.run(debug = True)
