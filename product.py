from flask import Blueprint, render_template
product = Blueprint('product', __name__)


@product.route('/product/<a>', methods=['GET'])
def product_page(a):
    return render_template("product.html", data=a)

