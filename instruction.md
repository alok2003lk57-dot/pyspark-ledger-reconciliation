# Financial Ledger Reconciliation Pipeline

Build a PySpark ETL application that processes raw financial transaction logs and account dimension data to calculate exact account balances as of `2024-01-01T00:00:00Z` UTC.

### Inputs
1. `/app/data/transactions_raw.parquet`
2. `/app/data/accounts_dim.csv`

### Business Rules
1. **Filtering & Normalization**: Exclude `status == 'CLOSED'`. Convert `event_timestamp` to UTC based on timezone. Drop events `>= 2024-01-01T00:00:00Z`.
2. **Deduplication**: Group by `(tx_id, event_type, seq_num)`. Keep highest `event_timestamp`, tie-break `retry_flag == False`, then max `amount_cents`.
3. **Output**: Save to `/app/output/account_balances/final_balances.parquet`. Schema: `account_id`, `settled_balance_cents`, `pending_balance_cents`, `last_processed_seq_num`.
