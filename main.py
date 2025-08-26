from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import base64
from io import BytesIO
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel

app = FastAPI(title="Garbage Monitor")

# Load CLIP model and processor once at startup
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

# Candidate labels
CANDIDATE_LABELS = ["metal", "plastic", "paper", "glass", "mix", "other"]

class PredictRequest(BaseModel):
    image_b64: str
    return_reason: bool = True

class PredictResponse(BaseModel):
    label: str
    confidence: float
    reason: Optional[str] = None

@app.post("/classify", response_model=PredictResponse)
async def classify(req: PredictRequest):
    # Decode image
    try:
        image_data = base64.b64decode(req.image_b64)
        image = Image.open(BytesIO(image_data)).convert("RGB")
    except Exception:
        return PredictResponse(label="other", confidence=0.0, reason="invalid image data" if req.return_reason else None)

    # Prepare inputs for CLIP
    texts = [f"a photo of {label}" for label in CANDIDATE_LABELS]
    inputs = processor(text=texts, images=image, return_tensors="pt", padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = outputs.logits_per_image.softmax(dim=1).cpu().numpy()[0]

    best_idx = int(probs.argmax())
    best_label = CANDIDATE_LABELS[best_idx]
    confidence = float(probs[best_idx])

    # Simple heuristic for mix/other
    sorted_probs = sorted(probs, reverse=True)
    top1, top2 = sorted_probs[0], sorted_probs[1]
    if best_label != "other":
        if top1 < 0.3:
            best_label = "other"
        elif top1 - top2 < 0.05 and top2 > 0.25:
            best_label = "mix"

    reason = f"highest similarity to '{best_label}'" if req.return_reason else None
    return PredictResponse(label=best_label, confidence=confidence, reason=reason)
