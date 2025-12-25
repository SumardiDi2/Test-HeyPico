from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Place Search API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GOOGLE_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

@app.get("/search")
def search_place(query: str = Query(..., description="Search keyword")):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    
    params = {
        "query": query,
        "key": YOUR_API_KEY
    }

    res = requests.get(url, params=params)
    data = res.json()

    return {
        "query": query,
        "results": [
            {
                "name": p["name"],
                "address": p.get("formatted_address"),
                "lat": p["geometry"]["location"]["lat"],
                "lng": p["geometry"]["location"]["lng"],
                "map_url": f"https://www.google.com/maps/search/?api=1&query={p['geometry']['location']['lat']},{p['geometry']['location']['lng']}"
            }
            for p in data.get("results", [])
        ]
    }