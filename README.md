# 🖼️ Reverse Image Search API using SerpAPI and FastAPI

This project provides an API to perform **Google Reverse Image Search** using [SerpAPI](https://serpapi.com/) with a FastAPI backend.

---

## Requirements

    fastapi
    uvicorn
    python-dotenv
    google-search-results

## Project Structure

reverse-image-search/
├── main.py
├── .env
├── requirements.txt
└── README.md

## Run the FastAPI Server

    uvicorn main:app --reload

## Visit Swagger UI at:

    http://127.0.0.1:8000/docs

## API Endpoint

    POST /reverse-image-search/

## 📥 Sample Input (JSON)

````json
{
  "id": 11,
  "title": "Tamim Iqbal",
  "image": "http://xyz.com/1747920556_Screenshot%20from%202025-05-22%2017-47-50.png",
  "remarks": "Tamim Iqbal reverse image searching"
}


## Sample Response (JSON)

```json
{
  "results": [
    {
      "id": 11,
      "title": "Tamim Iqbal Profile - ESPNcricinfo",
      "link": "https://www.espncricinfo.com/player/tamim-iqbal-103389",
      "redirect_link": "...",
      "displayed_link": "www.espncricinfo.com",
      "favicon": "...",
      "thumbnail": "https://example.com/thumb.jpg",
      "snippet": "Tamim Iqbal is a Bangladeshi cricketer...",
      "source": "ESPN Cricinfo",
      "status": "ready",
      "remarks": "Tamim Iqbal reverse image searching"
    }
    // more items...
  ]
}
````
