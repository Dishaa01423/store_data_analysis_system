import pandas as pd

def load_data(file_path):
    try:
        # df = pd.read_csv(file_path)
        # df['order_date'] = pd.to_datetime(df['order_date'])
        # return df
        return pd.read_csv(file_path, parse_dates=['order_date'])
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The CSV file is empty.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing the CSV file. Please check the file format.")

def compute_monthly_revenue(df):
    df['revenue'] = df['product_price'] * df['quantity']
    monthly_revenue = df.groupby(df['order_date'].dt.to_period('M'))['revenue'].sum()
    # Convert Period index to string
    monthly_revenue.index = monthly_revenue.index.astype(str)
    return monthly_revenue

# def compute_product_revenue(df):
#     product_revenue = df.groupby('product_id')['total_amount'].sum()
#     return product_revenue

# def compute_customer_revenue(df):
#     customer_revenue = df.groupby('customer_id')['total_amount'].sum()
#     return customer_revenue

# def get_top_customers(df, n=10):
#     top_customers = df.groupby('customer_id')['total_amount'].sum().nlargest(n)
#     return top_customers

# def compute_monthly_revenue(df):
#     df['revenue'] = df['product_price'] * df['quantity']
#     monthly_revenue = df.groupby(df['order_date'].dt.to_period('M'))['revenue'].sum()
#     return monthly_revenue.sort_index()

def compute_product_revenue(df):
    df['revenue'] = df['product_price'] * df['quantity']
    product_revenue = df.groupby('product_id')['revenue'].sum().sort_values(ascending=False)
    return product_revenue

def compute_customer_revenue(df):
    df['revenue'] = df['product_price'] * df['quantity']
    customer_revenue = df.groupby('customer_id')['revenue'].sum().sort_values(ascending=False)
    return customer_revenue


def get_top_customers(df, n=10):

    # Calculate revenue for each order
    df['revenue'] = df['product_price'] * df['quantity']

    # Group by customer and sum the revenue
    customer_revenue = df.groupby('customer_id')['revenue'].sum()

    # Sort customers by revenue in descending order and get the top n
    top_customers = customer_revenue.sort_values(ascending=False).head(n)

    return top_customers
