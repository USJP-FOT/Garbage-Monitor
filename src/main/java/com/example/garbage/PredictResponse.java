package com.example.garbage;

public record PredictResponse(String label, double confidence, String reason) {
}
