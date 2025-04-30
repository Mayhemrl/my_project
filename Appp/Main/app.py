from flask import Flask, render_template, request, redirect, url_for
from models import db, Student, Course, Teacher

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    students = Student.query.all()
    teachers = Teacher.query.all()
    courses = Course.query.all()  # Получение всех курсов из базы данных
    return render_template('index.html', teachers=teachers, students=students, courses=courses)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        new_student = Student(name=name)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/add_student', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        name = request.form['name']
        new_student = Student(name=name)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        new_teacher = Teacher(name=name)
        db.session.add(new_teacher)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_teacher.html')

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    teachers = Teacher.query.all() 
    if request.method == 'POST':
        name = request.form['name']
        teacher_id = request.form['teacher_id']
        new_course = Course(name=name, teacher_id=teacher_id)
        db.session.add(new_course)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_course.html', teachers=teachers)

if __name__ == '__main__':
    app.run(debug=True)
