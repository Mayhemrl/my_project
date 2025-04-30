# School Management System

Веб-приложение для управления учебным заведением с использованием Flask и SQLAlchemy.

## Требуемые исправления

1. **Конфликт роутов**  
Дублирующийся endpoint `/add_student` в app.py:
```python
@app.route('/add_student', methods=['GET', 'POST'])  # Два обработчика для одного URL
@app.route('/add_student', methods=['GET', 'POST'])


Статус разработки
Категория	Элементы
✅ Завершено	Базовые CRUD, SQLite интеграция, тесты
🛠 В разработке	Валидация форм, обработка ошибок
📅 Планируется	Авторизация, REST API, интерфейс админа

Установка и запуск
bash
# 1. Установите зависимости
pip install flask flask-sqlalchemy pytest

# 2. Инициализируйте БД
flask shell
>>> from app import db
>>> db.create_all()

# 3. Запустите приложение
flask run --host=0.0.0.0 --port=5000

# 4. Запустите тесты
pytest tests/ -v