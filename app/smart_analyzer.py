# file: app/smart_analyzer.py
import io
from PIL import Image
import asyncio

MOCK_FONT_DATABASE = {
    "dark_mode_fonts": [
        {
            "font_name": "Helvetica Neue", "foundry": "Linotype",
            "purchase_url": "https://www.myfonts.com/collections/neue-helvetica-font-family", "similarity": 0.97
        },
        {
            "font_name": "Proxima Nova", "foundry": "Mark Simonson",
            "purchase_url": "https://www.myfonts.com/collections/proxima-nova-font-foundry-select", "similarity": 0.91
        },
    ],
    "light_mode_fonts": [
        {
            "font_name": "Roboto", "foundry": "Google",
            "purchase_url": "https://fonts.google.com/specimen/Roboto", "similarity": 0.98
        },
        {
            "font_name": "Montserrat", "foundry": "Julieta Ulanovsky",
            "purchase_url": "https://fonts.google.com/specimen/Montserrat", "similarity": 0.94
        }
    ]
}

async def analyze_and_identify_font(image_bytes: bytes):
    await asyncio.sleep(1.5)
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert('L')
        pixels = image.getdata()
        avg_brightness = sum(pixels) / len(pixels)
        if avg_brightness < 128:
            return MOCK_FONT_DATABASE["dark_mode_fonts"]
        else:
            return MOCK_FONT_DATABASE["light_mode_fonts"]
    except Exception as e:
        print(f"Error during image analysis: {e}")
        return MOCK_FONT_DATABASE["light_mode_fonts"]