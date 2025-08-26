# Garbage-Monitor

Simple FastAPI backend for classifying garbage images into material types.

## Running

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn main:app --reload
```

## API

`POST /classify`

Request body:

```json
{
  "image_b64": "<base64 encoded image>",
  "return_reason": true
}
```

Response:

```json
{
  "label": "metal | plastic | paper | glass | mix | other",
  "confidence": 0.0,
  "reason": "short phrase"
}
```
