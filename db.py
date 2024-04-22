from flask import g, current_app, Flask
import sqlite3


def get_db():
    """Функция для подключения к базе данных"""
    db = getattr(g, '_database', None)
    if db is None:
        g._database = sqlite3.connect('db.sqlite')
        g._database.row_factory = sqlite3.Row
        db = g._database
    return db


def close_db(e=None):
    db = g.pop('_database', None)
    if db is not None:
        db.close()


def init_db(app: Flask):
    """Инициализация базы данных"""
    app.teardown_appcontext(close_db)

    with app.app_context():
        db = get_db()
        db.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                phone TEXT
            )
        """)
        db.commit()
