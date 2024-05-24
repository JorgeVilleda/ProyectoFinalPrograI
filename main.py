from flask import Flask, render_template
import psycopg2

app=Flask(__name__)

conn= psycopg2.connect(
    dbname="ProyectoFinal",
    user="postgres",
    password="M3y",
    host="localhost"
)

cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute("Select * from curso")
    data = cursor.fetchall()
    return render_template ('index.html', data=data)

if __name__ =="__main__":
    app.run(debug=True)