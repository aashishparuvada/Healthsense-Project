import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def fetch_data():
    source_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    dest_path ="data/raw_covid_data.csv"

    try:

        cmd = ["curl", "-L", "-o", dest_path, source_url]
        
        result = subprocess.run(cmd, check=True)

        logging.info(f"File downloaded using curl to {dest_path}")

    except subprocess.CalledProcessError as e:
        logging.error(f"Curl failed with return code {e.returncode}")
    except Exception as e:
        logging.error(f"General error occurred: {e}")

if __name__ == "__main__":
    fetch_data()