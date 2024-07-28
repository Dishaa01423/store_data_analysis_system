import pandas as pd
import pytest
from src.utils import load_data, compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, \
    get_top_customers


@pytest.fixture
def sample_data():
    data = {
        'order_id': [1, 2, 3, 4],
        'customer_id': [101, 102, 101, 103],
        'order_date': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-15'],
        'product_id': [1, 2, 1, 3],
        'product_name': ['A', 'B', 'A', 'C'],
        'product_price': [10, 20, 10, 30],
        'quantity': [2, 1, 3, 2]
    }
    return pd.DataFrame(data)


def test_load_data(tmp_path):
    # Create a temporary CSV file
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    file_path = tmp_path / "test.csv"
    df.to_csv(file_path, index=False)

    # Test loading the data
    loaded_df = load_data(file_path)
    assert loaded_df.equals(df)


def test_compute_monthly_revenue(sample_data):
    monthly_revenue = compute_monthly_revenue(sample_data)
    assert len(monthly_revenue) == 2
    assert monthly_revenue['2023-01'] == 40
    assert monthly_revenue['2023-02'] == 90


def test_compute_product_revenue(sample_data):
    product_revenue = compute_product_revenue(sample_data)
    assert len(product_revenue) == 3
    assert product_revenue[1] == 50
    assert product_revenue[2] == 20
    assert product_revenue[3] == 60


def test_compute_customer_revenue(sample_data):
    customer_revenue = compute_customer_revenue(sample_data)
    assert len(customer_revenue) == 3
    assert customer_revenue[101] == 50
    assert customer_revenue[102] == 20
    assert customer_revenue[103] == 60


def test_get_top_customers(sample_data):
    customer_revenue = compute_customer_revenue(sample_data)
    top_customers = get_top_customers(customer_revenue, 2)
    assert len(top_customers) == 2
    assert top_customers.index[0] == 103
    assert top_customers.index[1] == 101
