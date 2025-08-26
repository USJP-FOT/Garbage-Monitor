# Garbage-Monitor

Spring Boot backend for classifying garbage images into material types.

## Running

Build and run with Maven:

```bash
mvn spring-boot:run
```

This starts the server on port 8080.

## Docker

Build the image:

```bash
docker build -t garbage-monitor .
```

Run the container:

```bash
docker run -p 8080:8080 garbage-monitor
```

## Response

```json
{
  "label": "metal | plastic | paper | glass | mix | other",
  "confidence": 0.0,
  "reason": "classification not implemented"
}
```

> **Note:** The current implementation uses placeholder classification logic. Integrate a real model for actual predictions.
