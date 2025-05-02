from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
import psycopg2
import os
from dotenv import load_dotenv
import math
from fastapi.responses import JSONResponse

# Load environment variables
load_dotenv()

# Database config
db_config = {
    'host': os.getenv("DB_HOST"),
    'dbname': os.getenv("DB_NAME"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'port': os.getenv("DB_PORT")
}

app = FastAPI(title="HealthSense API", description="COVID Data API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Response model
class CountryCases(BaseModel):
    country: str
    total_infected: int

class GeoData(BaseModel):
    country: str
    lat: float
    long: float
    total_infected: int

# Root
@app.get("/")
def read_root():
    return {"message": "Welcome to the HealthSense API 🚀"}

# /cases – Total cases per country
@app.get("/cases", response_model=List[CountryCases])
def get_cases_by_country():
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT country, SUM(total_infected) AS total_infected
            FROM covid_cases
            WHERE country IS NOT NULL
            GROUP BY country
            ORDER BY total_infected DESC;
        """)
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        return [{"country": r[0], "total_infected": int(r[1])} for r in results]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# /map – For geo-plotting
@app.get("/map")
def get_map():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        cursor = conn.cursor()
        cursor.execute("""
            SELECT lat, long, country, total_infected
            FROM covid_cases
        """)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            lat, lon, country, infected = row
            # Clean up non-JSON-compliant values
            if not isinstance(lat, (int, float)) or math.isnan(lat) or math.isinf(lat):
                lat = None
            if not isinstance(lon, (int, float)) or math.isnan(lon) or math.isinf(lon):
                lon = None
            result.append({
                "lat": lat,
                "lon": lon,
                "country": country,
                "infected": infected
            })
        return result

    except psycopg2.Error as e:
        return JSONResponse(status_code=500, content={"error": str(e)})