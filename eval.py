import os
import pandas as pd

def evaluate():
    output_path = "/app/output/account_balances/final_balances.parquet"
    if not os.path.exists(output_path):
        print("pass@1: 0.0")
        return

    df_actual = pd.read_parquet(output_path)
    if len(df_actual) > 0 and list(df_actual.columns) == ["account_id", "settled_balance_cents", "pending_balance_cents", "last_processed_seq_num"]:
        print("pass@1: 1.0")
    else:
        print("pass@1: 0.0")

if __name__ == "__main__":
    evaluate()
