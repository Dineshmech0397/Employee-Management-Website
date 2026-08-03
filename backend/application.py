from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import os

application = Flask(__name__)
CORS(application)


def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor
    )


@application.route("/")
def home():
    return "Employee Management API Running"


# ===========================
# CREATE EMPLOYEE
# ===========================
@application.route("/employees", methods=["POST"])
def add_employee():
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO employees
    (employee_id, full_name, email, phone, department, designation, salary, joining_date)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(sql, (
        data["employee_id"],
        data["full_name"],
        data["email"],
        data["phone"],
        data["department"],
        data["designation"],
        data["salary"],
        data["joining_date"]
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Employee added successfully"})


# ===========================
# GET ALL EMPLOYEES
# ===========================
@application.route("/employees", methods=["GET"])
def get_employees():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees ORDER BY id DESC")

    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(employees)


# ===========================
# UPDATE EMPLOYEE
# ===========================
@application.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):

    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE employees
    SET
        employee_id=%s,
        full_name=%s,
        email=%s,
        phone=%s,
        department=%s,
        designation=%s,
        salary=%s,
        joining_date=%s
    WHERE id=%s
    """

    cursor.execute(sql, (
        data["employee_id"],
        data["full_name"],
        data["email"],
        data["phone"],
        data["department"],
        data["designation"],
        data["salary"],
        data["joining_date"],
        id
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Employee updated successfully"})


# ===========================
# DELETE EMPLOYEE
# ===========================
@application.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Employee deleted successfully"})


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
