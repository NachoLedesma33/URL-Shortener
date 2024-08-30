from flask import render_template, request, redirect, url_for
from app import app, db
from app.forms import URLForm
from app.models import URL
import string
import random


def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        original_url = form.original_url.data
        short_url = generate_short_url()

        # Asegúrate de que el short_url sea único
        existing_url = URL.query.filter_by(short_url=short_url).first()
        while existing_url:
            short_url = generate_short_url()
            existing_url = URL.query.filter_by(short_url=short_url).first()

        new_url = URL(original_url=original_url, short_url=short_url)
        db.session.add(new_url)
        db.session.commit()

        return render_template('success.html', short_url=short_url)
    return render_template('index.html', form=form)


@app.route('/<short_url>')
def redirect_to_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)

