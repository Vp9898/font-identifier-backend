# file: app/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
from app import smart_analyzer

logging.basicConfig(level=logging.INFO)
app = FastAPI(
    title="Font Identifier API",
    description="An API to identify fonts from images.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For deployment, we allow all origins.
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Font Identifier API is running."}

@app.post("/api/v1/identify")
async def identify_font_endpoint(image: UploadFile = File(...)):
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type.")
    logging.info(f"Received file: {image.filename}")
    try:
        image_bytes = await image.read()
        results = await smart_analyzer.analyze_and_identify_font(image_bytes)
        return {"filename": image.filename, "results": results}
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")