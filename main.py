from flask import Flask, render_template, g
from db import get_db
from products import products
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField
from wtforms.validators import InputRequired, Length


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-keylalaolala312'

    from db import init_db
    init_db(app)

    return app


app = create_app()


class AppointmentForm(FlaskForm):
    """Форма для записи на примерку"""

    name = StringField('Name', validators=[
        InputRequired(message='Пожалуйста, введите ваше имя'),
        Length(min=4, max=45)
    ])
    email = EmailField('Email', validators=[
        InputRequired(message='Пожалуйста, введите ваш email'),
        Length(min=5, max=50)
    ])
    phone = TelField('Phone', validators=[
        InputRequired(message='Пожалуйста, введите ваш телефон'),
        Length(min=9, max=15)
    ])


# маршруты для основных страниц

@app.route('/')
def index_page():
    return render_template('kurs.html')


@app.route('/wedding')
def wedding_page():
    return render_template('1.html', products=products)


@app.route('/evening')
def evening_page():
    return render_template('2.html')


@app.route('/fata')
def fata_page():
    return render_template('3.html')


@app.route('/accessories')
def accessories_page():
    return render_template('4.html')


@app.route('/contacts')
def contacts_page():
    return render_template('5.html')


@app.route('/product/<product_id>')
def product_page(product_id):
    """Страница одного(любого) товара"""
    # return render_template(f'{product_id}.html')
    product = products[product_id]
    return render_template('product-page.html', product=product)


@app.route('/form', methods=['GET', 'POST'])
def get_form():
    """Форма для записи на примерку"""
    form = AppointmentForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        print(name, email, phone)
        db = get_db()
        db.execute(
            'INSERT INTO appointments (name, email, phone) VALUES (?, ?, ?)',
            (name, email, phone)
        )
        db.commit()
        return render_template('thank_you.html')
    return render_template('form.html', form=form)


@app.route('/appointments')
def appointments():
    """Страница с записями на примерку"""
    db = get_db()
    cursor = db.execute('SELECT * FROM appointments')
    appointments = cursor.fetchall()
    return render_template('appointments.html', appointments=appointments)


if __name__ == '__main__':
    app.run(debug=True)
