import pandas as pd
from flask import Flask, render_template, jsonify
from utils import load_data, compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, get_top_customers

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/monthly_revenue')
def api_monthly_revenue():
    df = load_data('data/orders.csv')
    monthly_revenue = compute_monthly_revenue(df)
    return jsonify(monthly_revenue.to_dict())

@app.route('/api/product_revenue')
def api_product_revenue():
    df = load_data('data/orders.csv')
    product_revenue = compute_product_revenue(df)
    return jsonify(product_revenue.to_dict())

@app.route('/api/customer_revenue')
def api_customer_revenue():
    df = load_data('data/orders.csv')
    customer_revenue = compute_customer_revenue(df)
    return jsonify(customer_revenue.to_dict())

@app.route('/api/top_customers')
def api_top_customers():
    df = load_data('data/orders.csv')
    top_10_customers = get_top_customers(df, 10)
    return jsonify(top_10_customers.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
