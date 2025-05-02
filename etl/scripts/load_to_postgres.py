from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas as pd

def load_to_postgres(**kwargs):
    try:

        hook = PostgresHook(postgres_conn_id="gcp_postgres_conn")
        conn = hook.get_conn()
        cursor = conn.cursor()

        df = pd.read_csv("data/transformed_covid_data.csv")
        df.rename(columns={
            'province/state': 'province',
            'country/region': 'country'
        }, inplace=True)

        records = [
            (
                row['province'],
                row['country'],
                row['lat'],
                row['long'],
                int(row['total_infected']) if pd.notnull(row['total_infected']) else 0
            )
            for _, row in df.iterrows()
        ]

        cursor.executemany("""
            INSERT INTO covid_cases (province, country, lat, long, total_infected)
            VALUES (%s, %s, %s, %s, %s)
        """, records)

        conn.commit()
        cursor.close()
        conn.close()

        print("Data successfully loaded into PostgreSQL.")
    except Exception as e:
        print(f"Failed to load data into PostgreSQL: {e}")
        raise