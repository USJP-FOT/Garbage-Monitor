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


Build the image:

```bash
docker build -t garbage-monitor .
```

Start the container:

```bash
docker run -p 8000:8000 garbage-monitor
```



Response:

```json
{
  "label": "metal | plastic | paper | glass | mix | other",
  "confidence": 0.0,
  "reason": "short phrase"
}
```
