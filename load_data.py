import pandas as pd

def load_customer_data():
    customers = pd.read_csv(
        "dataset/olist_customers_dataset.csv"
    )

    return customers