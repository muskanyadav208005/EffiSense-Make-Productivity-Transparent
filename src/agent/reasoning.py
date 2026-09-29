from .schema import AgentObservation, AgentDecision
from typing import List, Dict, Any, Optional
from datetime import datetime

class ProductivityAgent:
    def __init__(self):
        self.history: List[AgentObservation] = []
        self.last_decision: Optional[AgentDecision] = None
        self.intervention_count: Dict[str, int] = {}

    def observe(self, obs: AgentObservation) -> AgentDecision:
        obs.validate()
        self.history.append(obs)
        
        decision = self._reason(obs)
        
        # Avoid repetitive interventions for the same condition
        if self.last_decision and self.last_decision.action == decision.action:
            # Only repeat if the state has significantly changed or if it's a high priority alert
            if not self._has_state_shifted(obs):
                decision = self._generate_neutral_decision(obs, "Condition persists; monitoring without repetition.")

        self.last_decision = decision
        return decision

    def _has_state_shifted(self, current: AgentObservation) -> bool:
        if len(self.history) < 2:
            return True
        prev = self.history[-2]
        # Significant shift if productivity changes by > 15% or engagement by > 0.2
        return abs(current.productivity_score - prev.productivity_score) > 15 or \
               abs(current.engagement_score - prev.engagement_score) > 0.2

    def _reason(self, obs: AgentObservation) -> AgentDecision:
        # Reasoning Layer: Analyzing combined metrics
        
        # 1. High Productivity & Engaged
        if obs.productivity_score > 80 and obs.engagement_score > 0.7 and obs.efficiency_score > 0.7:
            return AgentDecision(
                action="MAINTAIN_FLOW",
                reason="User is in a high-productivity flow state with strong engagement and efficiency.",
                relevant_state={"state": "FLOW"},
                confidence=0.95
            )

        # 2. Low Engagement / High Idle
        if obs.idle_percentage > 40 or obs.engagement_score < 0.3:
            return AgentDecision(
                action="NUDGE_ENGAGEMENT",
                reason="High idle time or low engagement detected. Potential distraction or burnout.",
                relevant_state={"idle": obs.idle_percentage, "engagement": obs.engagement_score},
                confidence=0.85
            )

        # 3. High Activity but Poor Efficiency (Churning)
        if obs.mean_velocity > 500 and obs.efficiency_score < 0.4:
            return AgentDecision(
                action="SUGGEST_STRATEGY",
                reason="High physical activity (velocity) but low efficiency suggests inefficient work patterns or 'churning'.",
                relevant_state={"velocity": obs.mean_velocity, "efficiency": obs.efficiency_score},
                confidence=0.80
            )

        # 4. Inconsistent Activity
        if obs.consistency_score < 0.4:
            return AgentDecision(
                action="STABILIZE_FOCUS",
                reason="Productivity is inconsistent. Suggesting a structured break or time-blocking.",
                relevant_state={"consistency": obs.consistency_score},
                confidence=0.75
            )

        # 5. Declining Productivity (Trend Analysis)
        if len(self.history) >= 3:
            recent = self.history[-3:]
            if recent[0].productivity_score > recent[1].productivity_score > recent[2].productivity_score:
                return AgentDecision(
                    action="PREVENT_DECLINE",
                    reason="Consistent decline in productivity observed over last 3 observations.",
                    relevant_state={"trend": "DECLINING"},
                    confidence=0.70
                )

        # 6. Improving Productivity (Positive Reinforcement)
        if len(self.history) >= 3:
            recent = self.history[-3:]
            if recent[0].productivity_score < recent[1].productivity_score < recent[2].productivity_score:
                return AgentDecision(
                    action="POSITIVE_REINFORCEMENT",
                    reason="Steady improvement in productivity detected.",
                    relevant_state={"trend": "IMPROVING"},
                    confidence=0.70
                )

        # 7. Unusual Activity Patterns (Acceleration/Smoothness)
        if abs(obs.acceleration) > 1000 and obs.smoothness < 0.3:
            return AgentDecision(
                action="CHECK_WELLBEING",
                reason="Erratic activity patterns detected (high acceleration, low smoothness).",
                relevant_state={"acceleration": obs.acceleration, "smoothness": obs.smoothness},
                confidence=0.60
            )

        # Default: Neutral monitoring
        return self._generate_neutral_decision(obs, "Activity levels are within nominal ranges.")

    def _generate_neutral_decision(self, obs: AgentObservation, reason: str) -> AgentDecision:
        return AgentDecision(
            action="MONITOR",
            reason=reason,
            relevant_state={"state": "NOMINAL"},
            confidence=1.0
        )
