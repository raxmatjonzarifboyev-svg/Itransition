
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import math

app = FastAPI()

# Shunchaki tekshirish uchun (Asosiy sahifa)
@app.get("/", response_class=PlainTextResponse)
def home():
    return "Server ishlamoqda. Manzilni tekshiring: /raxmatjon_zarifboyev_gmail_com"

# Topshiriq manzili
@app.get("/raxmatjon_zarifboyev_gmail_com", response_class=PlainTextResponse)
def calculate_lcm(x: str = None, y: str = None):
    try:
        if x is None or y is None:
            return "NaN"
        
        val_x = float(x)
        val_y = float(y)
        
        # Natural son bo'lmasa yoki manfiy bo'lsa NaN
        if val_x < 0 or val_y < 0 or not val_x.is_integer() or not val_y.is_integer():
            return "NaN"
            
        result = math.lcm(int(val_x), int(val_y))
        return str(result)
        
    except (ValueError, TypeError):
        return "NaN"
