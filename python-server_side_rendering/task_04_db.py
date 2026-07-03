#!/usr/bin/env python3
"""
Module: task_04_db
A Flask application displaying product data read from JSON, CSV,
or a SQLite database.
"""
import csv
import json
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filename):
    """Read a list of products from a JSON file."""
    with open(filename, encoding='utf-8') as json_file:
        return json.load(json_file)


def read_csv(filename):
    """Read a list of products from a CSV file."""
    products = []
    with open(filename, newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql(filename):
    """Read a list of products from a SQLite database."""
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()

    return [
        {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
        for row in rows
    ]


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


@app.route('/products')
def products():
    """Render a page listing products read from JSON, CSV or SQL."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        product_list = read_json('products.json')
    elif source == 'csv':
        product_list = read_csv('products.csv')
    elif source == 'sql':
        try:
            product_list = read_sql('products.db')
        except sqlite3.Error:
            return render_template(
                'product_display.html', error='Database error')
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error='Invalid product ID')

        product_list = [
            product for product in product_list
            if product['id'] == product_id
        ]

        if not product_list:
            return render_template(
                'product_display.html', error='Product not found')

    return render_template('product_display.html', products=product_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
