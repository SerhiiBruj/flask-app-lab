from flask import render_template, request
from . import products

@products.route('/<string:name>')
def show_product(name):
    return render_template('products/prod.html', name=name)
