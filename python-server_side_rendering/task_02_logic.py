#!/usr/bin/env python3
"""
Module: task_02_logic
A Flask application demonstrating dynamic content with Jinja
loops and conditions.
"""
import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render a page listing items read from items.json."""
    with open('items.json', encoding='utf-8') as items_file:
        data = json.load(items_file)

    return render_template('items.html', items=data.get('items', []))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
