from flask import Flask, render_template, jsonify,request
import mysql.connector

app = Flask(__name__)

# Database Connection Function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="mayur",
        password="",
        database="joviancreers"
    )

@app.route("/")
def hello_jovian():
    con = get_db_connection()
    cmd = con.cursor(dictionary=True)
    cmd.execute("SELECT * FROM jobs")
    jobs = cmd.fetchall()
    con.close()
    
    return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    con = get_db_connection()
    cmd = con.cursor(dictionary=True)
    cmd.execute("SELECT * FROM jobs")
    jobs = cmd.fetchall()
    con.close()
    
    return jsonify(jobs)

@app.route("/jobs/<int:id>")
def show_jobs(id):
    con = get_db_connection()
    cmd = con.cursor(dictionary=True)
    cmd.execute("SELECT * FROM jobs WHERE id = %s", (id,))
    job = cmd.fetchone()
    con.close()
    
    if job:
        return render_template('jobpage.html', job=job)
    else:
        return "Job Not Found", 404
    
@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    data = request.form
    return jsonify(data)     

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
