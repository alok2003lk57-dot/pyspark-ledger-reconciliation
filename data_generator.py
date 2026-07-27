import os, random
import pandas as pd
import numpy as np

def generate_data(output_dir="/app/data"):
    seed = int(os.environ.get("DYNAMO_SEED", 42))
    random.seed(seed)
    np.random.seed(seed)

    os.makedirs(output_dir, exist_ok=True)

    accounts = [
        {"account_id": f"ACC_{i:04d}", "timezone": random.choice(["America/New_York", "Europe/London", "Asia/Tokyo"]), "status": "ACTIVE" if i % 10 != 0 else "CLOSED"}
        for i in range(1, 101)
    ]
    pd.DataFrame(accounts).to_csv(os.path.join(output_dir, "accounts_dim.csv"), index=False)

    tx_rows = []
    for i in range(1, 500):
        acc = random.choice([a for a in accounts if a["status"] == "ACTIVE"])
        tx_id = f"TX_{i:05d}"
        auth_amt = random.randint(1000, 50000)

        tx_rows.append({
            "tx_id": tx_id, "account_id": acc["account_id"], "event_type": "AUTH",
            "amount_cents": auth_amt, "event_timestamp": "2023-12-15 10:00:00",
            "seq_num": 1, "retry_flag": False
        })
        tx_rows.append({
            "tx_id": tx_id, "account_id": acc["account_id"], "event_type": "CAPTURE",
            "amount_cents": int(auth_amt * 0.6), "event_timestamp": "2023-12-15 10:05:00",
            "seq_num": 2, "retry_flag": False
        })

    df_tx = pd.DataFrame(tx_rows)
    df_tx.to_parquet(os.path.join(output_dir, "transactions_raw.parquet"), index=False)
    print("Data generation complete.")

if __name__ == "__main__":
    generate_data()
