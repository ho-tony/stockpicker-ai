# StockPicker AI Backend

This is a scalable Python backend API endpoint that uses Google's Gemini AI to perform due diligence on stock tickers.

## Setup

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Variables:**
    Copy `.env.example` to `.env` and add your Gemini API key.
    ```bash
    cp .env.example .env
    ```
    Edit `.env` and set `GEMINI_API_KEY`.

3.  **Run the server:**
    ```bash
    uvicorn app.main:app --reload
    ```

## API Usage

**Endpoint:** `POST /api/v1/analyze`

**Request Body:**
```json
{
  "ticker": "AAPL"
}
```
