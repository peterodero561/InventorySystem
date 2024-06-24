#!/usr/bin/python3
from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Peterodero561@'
app.config['MYSQL_DB'] = 'inventory'

mysql = MySQL(app)

@app.route('/add', methods=['POST'])
def add_equipment():
    data = request.get_json()
    serial = data['serial']
    Type = data['type']
    brand = data['brand']
    purchase_date = data['purchase_date']
    location = data['location']
    status = data['status']
    notes = data['status']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO ict (serial_num, type, brand, purchase_date, office_located, status, notes) VALUES (%s, %s, %s, %s, %s, %s, %s)", (serial, Type, brand, purchase_date, location, status, notes))
    mysql.connection.commit()
    cur.close

    return 'Equipment added', 200

@app.route('/equipments', methods=['GET'])
def get_equipments():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM ict')
    results = cur.fetchall()
    cur.close()

    equipments = []
    for row in results:
        equipment = {
                'id': row[0],
                'serial': row[1],
                'type': row[2],
                'brand': row[3],
                'purcahse_date': row[4],
                'location': row[5],
                'status': row[6],
                'notes': row[7]
                }
        equipments.append(equipment)
    
    return jsonify(equipments), 200

@app.route('/table')
def table():
    render_template('table.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
