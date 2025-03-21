from flask import Flask, render_template, jsonify
import mysql.connector
import mysql

app = Flask(__name__)

# Connect to MySQL database
con = mysql.connector.connect(
    host="localhost", user="mayur", password="", database="joviancreers")
cmd = con.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)  # Ensure results are returned as dictionaries
cmd.execute("SELECT * FROM jobs")
data = cmd.fetchall()
con.close()

# Convert database rows into a list of job dictionaries
jobs = []
for row in data:
    print("row", row)
    jobs.append(row)

@app.route("/")
def hello_jovian():
    return render_template('home.html', jobs=jobs, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)

@app.route("/jobs/<id>")
def show_jobs():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)