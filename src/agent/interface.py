from .reasoning import ProductivityAgent
from .schema import AgentObservation, AgentDecision
from typing import Optional

class AgentInterface:
    """
    Bridge between ML Output and Agent Reasoning.
    Ensures that synthetic or real ML data is properly converted to observations.
    """
    def __init__(self):
        self.agent = ProductivityAgent()

    def process_ml_output(self, ml_data: dict) -> Optional[AgentDecision]:
        try:
            # Convert raw dict to structured AgentObservation
            obs = AgentObservation(
                productivity_score=ml_data.get('productivity_score', 0.0),
                engagement_score=ml_data.get('engagement_score', 0.0),
                efficiency_score=ml_data.get('efficiency_score', 0.0),
                consistency_score=ml_data.get('consistency_score', 0.0),
                mean_velocity=ml_data.get('mean_velocity', 0.0),
                acceleration=ml_data.get('acceleration', 0.0),
                idle_percentage=ml_data.get('idle_percentage', 0.0),
                smoothness=ml_data.get('smoothness', 0.0)
            )
            return self.agent.observe(obs)
        except (ValueError, TypeError) as e:
            print(f"AgentInterface Error: Invalid ML input received: {e}")
            return None
