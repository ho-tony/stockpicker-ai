from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.gemini_service import GeminiService, get_gemini_service
from app.schemas.stock import StockAnalysis

router = APIRouter()

class StockRequest(BaseModel):
    ticker: str

@router.post("/analyze", response_model=StockAnalysis)
async def analyze_stock(request: StockRequest, service: GeminiService = Depends(get_gemini_service)):
    result = await service.analyze_stock(request.ticker)
    
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["details"])
        
    return result
