import os
import logging
from flask import Flask, render_template, jsonify
from utils import load_data, compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, get_top_customers

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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
    
@app.route('/')
def hello():
    logger.debug("Hello route accessed")
    return "Hello, World!"

if __name__ == "__main__":
    logger.debug(f"Starting Flask app on port {os.environ.get('PORT', 8000)}")
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
