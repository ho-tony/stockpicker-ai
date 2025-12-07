from pydantic import BaseModel, Field
from typing import List

class StockAnalysis(BaseModel):
    ticker: str = Field(description="The stock ticker symbol")
    company_name: str = Field(description="Name of the company")
    summary: str = Field(description="Summary of the company")
    bull_case: str = Field(description="Detailed paragraph explaining the bullish case for the company")
    bear_case: str = Field(description="Detailed paragraph explaining the bearish case for the company")
    financial_health: str = Field(description="Assessment of financial health")
    verdict: str = Field(description="Buy/Sell/Hold recommendation based on analysis")
    