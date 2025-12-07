import asyncio
from app.schemas.stock import StockAnalysis

class MockGeminiService:
    async def analyze_stock(self, ticker: str) -> dict:
        # Simulate network delay
        await asyncio.sleep(1)
        
        # Return mock data based on the ticker to make it feel slightly dynamic
        # or just generic mock data.
        
        mock_data = {
            "ticker": ticker.upper(),
            "company_name": f"Mock Company for {ticker.upper()}",
            "summary": f"This is a mock summary for {ticker.upper()}. The company is performing well in the mock market.",
            "bull_case": "The company has shown strong revenue growth over the last few quarters, driven by its dominant position in the mock industry. Profit margins are high, and the company is expanding into new markets which should drive future growth.",
            "bear_case": "Despite the strong growth, the company's valuation is quite high compared to its peers. There are also potential regulatory risks in the mock sector that could impact future profitability, and competition is intensifying.",
            "financial_health": "Strong",
            "verdict": "Buy"
        }
        
        # Ensure it matches the structure expected (although the real service returns a dict from json.loads)
        # The real service returns a dict that matches StockAnalysis schema.
        
        return mock_data
