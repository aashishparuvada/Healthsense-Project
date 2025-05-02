import pandas as pd
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def transform_data():
    input_path = 'data/raw_covid_data.csv'
    output_path = 'data/transformed_covid_data.csv'

    try:
        df_start = pd.read_csv(input_path)
        logging.info(f"Loaded raw data with shape: {df_start.shape}")

        # Transformation (I assumed those were cases on that particular date but they are actually appending everyday, 
        # so the last column would contain aggregate, logic for the same is written below this logic)

        # columns_excluded = ['Province/State', 'Country/Region', 'Lat', 'Long']
        # columns_to_sum = df.columns.difference(columns_excluded)
        # columns_to_sum = [col for col in columns_to_sum if pd.api.types.is_numeric_dtype(df[col])]
        # df['total_infected'] = df[columns_to_sum].sum(axis=1)
        # df = df[columns_excluded + ['total_infected']]

        columns_included = ['Province/State', 'Country/Region', 'Lat', 'Long']   
        last_column = df_start.columns[-1]
        columns_to_select = columns_included + [last_column]
        df = df_start[columns_to_select].copy()
        df = df.rename(columns={last_column: 'total_infected'})     

        # Normalising column names
        df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

        # Drop rows with missing country or date
        df = df.dropna(subset=['country/region'])

        df.to_csv(output_path, index=False)
        logging.info(f"Transformed data saved to {output_path} with shape: {df.shape}")
    
    except Exception as e:
        logging.error(f"Failed to transform data: {e}")

if __name__ == "__main__":
    transform_data()
