# Create Flask Application
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'ORCA', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ', 'likes': 10, 'image_url': ''},
    {'id': 2, 'name': 'EKS Health', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit', 'likes': 30, 'image_url': ''},
    {'id': 3, 'name': 'AHEAD', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit', 'likes': 25, 'image_url': ''},
    {'id': 4, 'name': 'Pluto', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit', 'likes': 2, 'image_url': ''},
    {'id': 5, 'name': 'VPC Log Replay', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit', 'likes': 1, 'image_url': ''},
    {'id': 6, 'name': 'Bingo', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit', 'likes': 5, 'image_url': ''},
    {'id': 7, 'name': 'InfraSpec', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit', 'likes': 1, 'image_url': ''},
    {'id': 8, 'name': 'Markets Type-2', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit', 'likes': 1, 'image_url': ''},
]

# Create default route which returns a flask template
@app.route('/')
def index():
    return render_template('index.html', products=products)

# Create Product details
@app.route('/product/<product_id>')
def product(product_id):
    return f'Product {product_id}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)


