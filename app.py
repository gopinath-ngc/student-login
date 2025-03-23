from flask import Flask, request, render_template
app= Flask(__name__)
students = {
    "814724243046": {
        "name": "gopinath .N",
        "password": "pass123",
        "attendance": ["2025-03-21: Present", "2025-03-22: Absent"],
        "details": {
            "department": "B.tech . ai&ds",
            "email": "gopinathnantheeshwaran@gmail.com"
        }
    },
    "814724243043": {
        "name": "fadil hammed .N",
        "password": "gay420",
        "attendance": ["2025-03-21: Present", "2025-03-22: Present"],
        "details": {
            "department": "B.tech AI&DS",
            "email": "fadilhammed@gmail.com"
        }
    }
}
@app.route('/')
def home():
    return render_template('login.html') 
@app.route('/login', methods=['POST'])
def login():
    reg_no = request.form.get("reg_no")
    password = request.form.get("password")

    student = students.get(reg_no) 
    if student and student['password'] == password:
        return render_template("student_data.html", student=student)
    else:
        return "Invalid registration number or password!", 420
if __name__ == '__main__':
    app.run(debug=True)
