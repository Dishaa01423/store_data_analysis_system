import pandas as pd
from utils import load_data, compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, get_top_customers

def main():
    try:
        # Load data
        df = load_data('data/orders.csv')

        # Compute monthly revenue
        monthly_revenue = compute_monthly_revenue(df)
        print("Monthly Revenue:")
        print(monthly_revenue)

        # Compute product revenue
        product_revenue = compute_product_revenue(df)
        print("\nProduct Revenue:")
        print(product_revenue)

        # Compute customer revenue
        customer_revenue = compute_customer_revenue(df)
        print("\nCustomer Revenue:")
        print(customer_revenue)

        # Get top 10 customers
        top_10_customers = get_top_customers(df, 10)
        print("\nTop 10 Customers by Revenue:")
        print(top_10_customers)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()