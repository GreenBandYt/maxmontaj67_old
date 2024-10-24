from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Настройка соединения с базой данных
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'greenbandyt'
app.config['MYSQL_PASSWORD'] = 'byv'
app.config['MYSQL_DB'] = 'maxmontaj67'

mysql = MySQL(app)

# Маршрут для создания нового заказчика
@app.route('/api/customers', methods=['POST'])
def create_customer():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Нет данных"}), 400

    try:
        cur = mysql.connection.cursor()
        query = """
            INSERT INTO customers (name, phone, email, address)
            VALUES (%s, %s, %s, %s)
        """
        cur.execute(query, (data['name'], data.get('phone'), data.get('email'), data.get('address')))
        mysql.connection.commit()
        cur.close()

        return jsonify({"message": "Заказчик успешно создан"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Маршрут для создания заказа
@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Нет данных"}), 400

    try:
        cur = mysql.connection.cursor()
        query = """
            INSERT INTO orders (customer_id, work_type, address, status)
            VALUES (%s, %s, %s, %s)
        """
        cur.execute(query, (data['customer_id'], data['work_type'], data['address'], 'new'))
        mysql.connection.commit()
        cur.close()

        return jsonify({"message": "Заказ успешно создан"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Нет данных"}), 400

    try:
        cur = mysql.connection.cursor()
        query = """
            UPDATE orders SET status = %s WHERE id = %s
        """
        cur.execute(query, (data['status'], order_id))
        mysql.connection.commit()
        cur.close()

        return jsonify({"message": "Статус заказа обновлен"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
