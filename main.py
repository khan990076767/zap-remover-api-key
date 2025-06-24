from fastapi import FastAPI, UploadFile, File, Header, HTTPException
from fastapi.responses import StreamingResponse
from rembg import remove
import io
from auth import verify_api_key

app = FastAPI(
    title="ZAP Remover API",
    description="Remove image background using your own API key",
    version="1.0"
)

@app.post("/remove-bg", summary="Remove background from image")
async def remove_bg(file: UploadFile = File(...), x_api_key: str = Header(...)):
    verify_api_key(x_api_key)  # Check API Key
    image_data = await file.read()
    result = remove(image_data)
    return StreamingResponse(io.BytesIO(result), media_type="image/png")