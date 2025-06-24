from fastapi import HTTPException

# Yahan apni API keys add karo
API_KEYS = ["369", "zapremoverbg"]

def verify_api_key(api_key: str):
    if api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")