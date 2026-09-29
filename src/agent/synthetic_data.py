from .schema import AgentObservation
from typing import List, Dict

class SyntheticMLProvider:
    """
    DEMO / SYNTHETIC ML INPUT
    Provides deterministic synthetic data to simulate ML model output for agent testing.
    """
    
    SCENARIOS = {
        "HEALTHY": AgentObservation(
            productivity_score=90.0,
            engagement_score=0.85,
            efficiency_score=0.8,
            consistency_score=0.9,
            mean_velocity=200.0,
            acceleration=10.0,
            idle_percentage=5.0,
            smoothness=0.8
        ),
        "LOW_ENGAGEMENT": AgentObservation(
            productivity_score=30.0,
            engagement_score=0.2,
            efficiency_score=0.4,
            consistency_score=0.5,
            mean_velocity=50.0,
            acceleration=5.0,
            idle_percentage=60.0,
            smoothness=0.5
        ),
        "CHURNING": AgentObservation(
            productivity_score=50.0,
            engagement_score=0.6,
            efficiency_score=0.2,
            consistency_score=0.7,
            mean_velocity=800.0,
            acceleration=200.0,
            idle_percentage=10.0,
            smoothness=0.4
        ),
        "INCONSISTENT": AgentObservation(
            productivity_score=60.0,
            engagement_score=0.5,
            efficiency_score=0.6,
            consistency_score=0.2,
            mean_velocity=150.0,
            acceleration=50.0,
            idle_percentage=20.0,
            smoothness=0.6
        ),
        "ERRATIC": AgentObservation(
            productivity_score=40.0,
            engagement_score=0.4,
            efficiency_score=0.3,
            consistency_score=0.6,
            mean_velocity=300.0,
            acceleration=1200.0,
            idle_percentage=15.0,
            smoothness=0.2
        ),
        "INVALID": AgentObservation(
            productivity_score=150.0, # Invalid
            engagement_score=0.5,
            efficiency_score=0.5,
            consistency_score=0.5,
            mean_velocity=100.0,
            acceleration=10.0,
            idle_percentage=5.0,
            smoothness=0.5
        )
    }

    @classmethod
    def get_scenario(cls, scenario_name: str) -> AgentObservation:
        if scenario_name not in cls.SCENARIOS:
            raise ValueError(f"Unknown scenario: {scenario_name}")
        return cls.SCENARIOS[scenario_name]

    @classmethod
    def get_decline_sequence(cls) -> List[AgentObservation]:
        return [
            AgentObservation(80, 0.8, 0.8, 0.8, 200, 10, 10, 0.8),
            AgentObservation(60, 0.6, 0.6, 0.6, 200, 10, 20, 0.7),
            AgentObservation(40, 0.4, 0.4, 0.4, 200, 10, 30, 0.6),
        ]

    @classmethod
    def get_improvement_sequence(cls) -> List[AgentObservation]:
        return [
            AgentObservation(40, 0.4, 0.4, 0.4, 200, 10, 30, 0.6),
            AgentObservation(60, 0.6, 0.6, 0.6, 200, 10, 20, 0.7),
            AgentObservation(80, 0.8, 0.8, 0.8, 200, 10, 10, 0.8),
        ]
