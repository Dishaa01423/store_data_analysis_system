import os
import logging
from flask import Flask, render_template, jsonify
from werkzeug.exceptions import HTTPException
from .utils import load_data, compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, get_top_customers

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def index():
    logger.debug("Index route accessed")
    try:
        return render_template('index.html')
    except Exception as e:
        logger.exception(f"Error rendering index template: {str(e)}")
        return jsonify({"error": f"Error rendering page: {str(e)}"}), 500

@app.route('/api/monthly_revenue')
def api_monthly_revenue():
    logger.debug("Monthly revenue route accessed")
    try:
        df = load_data('data/orders.csv')
        monthly_revenue = compute_monthly_revenue(df)
        return jsonify(monthly_revenue.to_dict())
    except Exception as e:
        logger.exception(f"Error computing monthly revenue: {str(e)}")
        return jsonify({"error": f"Error computing monthly revenue: {str(e)}"}), 500

@app.route('/api/product_revenue')
def api_product_revenue():
    logger.debug("Product revenue route accessed")
    try:
        df = load_data('data/orders.csv')
        product_revenue = compute_product_revenue(df)
        return jsonify(product_revenue.to_dict())
    except Exception as e:
        logger.exception("Error computing product revenue: %s", str(e))
        return jsonify({"error": "Error computing product revenue"}), 500

@app.route('/api/customer_revenue')
def api_customer_revenue():
    logger.debug("Customer revenue route accessed")
    try:
        df = load_data('data/orders.csv')
        customer_revenue = compute_customer_revenue(df)
        return jsonify(customer_revenue.to_dict())
    except Exception as e:
        logger.exception("Error computing customer revenue: %s", str(e))
        return jsonify({"error": "Error computing customer revenue"}), 500

@app.route('/api/top_customers')
def api_top_customers():
    logger.debug("Top customers route accessed")
    try:
        df = load_data('data/orders.csv')
        top_10_customers = get_top_customers(df, 10)
        return jsonify(top_10_customers.to_dict())
    except Exception as e:
        logger.exception("Error getting top customers: %s", str(e))
        return jsonify({"error": "Error getting top customers"}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    # Pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    # Now you're handling non-HTTP exceptions only
    logger.exception("An unhandled error occurred: %s", str(e))
    return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    logger.debug(f"Starting Flask app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)
