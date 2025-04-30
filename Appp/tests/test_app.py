import unittest
from flask import url_for
from flask_testing import TestCase
from app import app, db, Student, Teacher, Course

class TestApp(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:',
            TESTING=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        
        # Добавляем тестовые данные
        test_teacher = Teacher(name="John Doe")
        test_student = Student(name="Alice Smith")
        test_course = Course(name="Mathematics", teacher_id=1)
        
        db.session.add(test_teacher)
        db.session.add(test_student)
        db.session.add(test_course)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index_route(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Alice Smith', response.data)
        self.assertIn(b'John Doe', response.data)
        self.assertIn(b'Mathematics', response.data)

    def test_add_student(self):
        # Тестирование POST-запроса
        response = self.client.post(
            url_for('add_student'),
            data={'name': 'Bob Johnson'},
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bob Johnson', response.data)
        
        # Проверка записи в БД
        student = Student.query.filter_by(name='Bob Johnson').first()
        self.assertIsNotNone(student)

    def test_add_teacher(self):
        response = self.client.post(
            url_for('add_teacher'),
            data={'name': 'Jane Smith'},
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jane Smith', response.data)
        
        teacher = Teacher.query.filter_by(name='Jane Smith').first()
        self.assertIsNotNone(teacher)

    def test_add_course(self):
        response = self.client.post(
            url_for('add_course'),
            data={'name': 'Physics', 'teacher_id': 1},
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Physics', response.data)
        
        course = Course.query.filter_by(name='Physics').first()
        self.assertIsNotNone(course)
        self.assertEqual(course.teacher_id, 1)

    def test_invalid_form_submission(self):
        # Тест пустой формы
        response = self.client.post(
            url_for('add_student'),
            data={'name': ''},
            follow_redirects=True
        )
        self.assertIn(b'This field is required', response.data)

if __name__ == '__main__':
    unittest.main()