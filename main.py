from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

app = FastAPI()


class ImageSearchRequest(BaseModel):
    id: int
    title: str
    image: str
    remarks: str


@app.post("/reverse-image-search/")
async def google_reverse_image(data: ImageSearchRequest):
    # return {
    #     "status": True,
    #     "code": 200,
    #     "message": "API key is set, proceeding with reverse image search.",
    #     "data": data.image
    # }
    if not API_KEY:
        return { 
            "status": False,
            "code": 500,
            "message": "API key is not set."
            }

    params = {
        "engine": "google_reverse_image",
        "image_url": data.image,
        "api_key": API_KEY,
        "gl": "us",
        "hl": "en",
        "location": "United States"
    }


    try:
        search = GoogleSearch(params)

        # return {
        #     "status": True,
        #     "code": 200,
        #     # "searchData": search.get_json(),
        #     "searchData": search.get_dict()
        # }
        
        results = search.get_dict()
        if not results or 'image_results' not in results:
            raise HTTPException(status_code=404, detail="No image results found.")
        
        #return {"message": "Search completed successfully.", "results": results}

        results_list = []

        if 'image_results' in results:
            for result in results['image_results']:
                results_list.append({
                    "id": data.id,
                    "title": result.get('title'),
                    "thumbnail": result.get('thumbnail') or data.image,
                    "displayed_link": result.get('displayed_link'),
                    "link": result.get('link'),
                    "redirect_link": result.get('redirect_link'),
                    "favicon": result.get('favicon'),
                    "snippet": result.get('snippet'),
                    "source": result.get('source'),
                    "status": "ready",
                    "remarks": data.remarks
                })
            return {
                "status": True,
                "message": "Search completed successfully.",
                "code": 200,
                "data": results_list
            }
        else:
            return {"status": False, "message": "No image results found.",  "code": 200, "data": []}


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

