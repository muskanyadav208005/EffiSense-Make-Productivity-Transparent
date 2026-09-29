from dataclasses import dataclass
from typing import Optional, Dict, Any
from datetime import datetime

@dataclass
class AgentObservation:
    productivity_score: float
    engagement_score: float
    efficiency_score: float
    consistency_score: float
    mean_velocity: float
    acceleration: float
    idle_percentage: float
    smoothness: float
    timestamp: datetime = datetime.now()

    def validate(self):
        # Basic range validation
        if not (0 <= self.productivity_score <= 100):
            raise ValueError("productivity_score must be between 0 and 100")
        if not (0 <= self.engagement_score <= 1):
            raise ValueError("engagement_score must be between 0 and 1")
        if not (0 <= self.efficiency_score <= 1):
            raise ValueError("efficiency_score must be between 0 and 1")
        if not (0 <= self.consistency_score <= 1):
            raise ValueError("consistency_score must be between 0 and 1")
        if not (0 <= self.idle_percentage <= 100):
            raise ValueError("idle_percentage must be between 0 and 100")

@dataclass
class AgentDecision:
    action: str
    reason: str
    relevant_state: Dict[str, Any]
    confidence: float
    timestamp: datetime = datetime.now()
