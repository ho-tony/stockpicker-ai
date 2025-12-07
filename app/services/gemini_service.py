import google.generativeai as genai
from app.core.config import get_settings
import json
from pydantic import BaseModel, Field
from typing import List
from app.schemas.stock import StockAnalysis
from app.services.mock_gemini_service import MockGeminiService

settings = get_settings()

# Configure the Gemini API
genai.configure(api_key=settings.GEMINI_API_KEY)

from functools import lru_cache

class GeminiService:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    async def analyze_stock(self, ticker: str) -> dict:
        prompt = f"Perform a comprehensive due diligence analysis for the stock ticker: {ticker}."
        
        try:
            # Generate content asynchronously with structured output
            response = await self.model.generate_content_async(
                contents=prompt, 
                generation_config=genai.GenerationConfig(
                    response_mime_type="application/json",
                    response_schema=StockAnalysis
                )
            )
            
            # The response text is guaranteed to be valid JSON matching the schema
            return json.loads(response.text)
        except Exception as e:
            # In a real production app, you'd want better error handling and logging here
            print(f"Error analyzing stock {ticker}: {e}")
            return {
                "error": "Failed to analyze stock",
                "details": str(e)
            }

@lru_cache()
def get_gemini_service():
    if settings.USE_MOCK_SERVICE:
        return MockGeminiService()
    return GeminiService()
