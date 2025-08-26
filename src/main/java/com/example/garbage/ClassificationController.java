package com.example.garbage;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ClassificationController {

    @PostMapping("/classify")
    public PredictResponse classify(@RequestBody PredictRequest req) {
        String label = "other";
        double confidence = 0.0;
        String reason = req.returnReason() ? "classification not implemented" : null;
        return new PredictResponse(label, confidence, reason);
    }
}
