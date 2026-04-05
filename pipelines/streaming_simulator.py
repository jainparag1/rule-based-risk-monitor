import pandas as pd
import time
import random

def generate_transaction():
    return {
        "transaction_id": random.randint(1000, 9999),
        "amount": random.randint(10, 20000),
        "timestamp": pd.Timestamp.now(),
        "customer_id": random.randint(1, 100),
    }

def stream_data(batch_size=10):
    data = [generate_transaction() for _ in range(batch_size)]
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    while True:
        df = stream_data()
        print(df.head())
        time.sleep(2)