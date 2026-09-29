import unittest
from src.agent.interface import AgentInterface
from src.agent.synthetic_data import SyntheticMLProvider
from src.agent.schema import AgentObservation

class TestProductivityAgent(unittest.TestCase):
    def setUp(self):
        self.interface = AgentInterface()

    def test_high_productivity_healthy(self):
        obs = SyntheticMLProvider.get_scenario("HEALTHY")
        # Convert obs to dict to test interface
        data = vars(obs)
        decision = self.interface.process_ml_output(data)
        self.assertEqual(decision.action, "MAINTAIN_FLOW")
        self.assertIn("high-productivity flow", decision.reason)

    def test_low_engagement_high_idle(self):
        obs = SyntheticMLProvider.get_scenario("LOW_ENGAGEMENT")
        data = vars(obs)
        decision = self.interface.process_ml_output(data)
        self.assertEqual(decision.action, "NUDGE_ENGAGEMENT")
        self.assertIn("distraction or burnout", decision.reason)

    def test_high_activity_poor_efficiency(self):
        obs = SyntheticMLProvider.get_scenario("CHURNING")
        data = vars(obs)
        decision = self.interface.process_ml_output(data)
        self.assertEqual(decision.action, "SUGGEST_STRATEGY")
        self.assertIn("inefficient work patterns", decision.reason)

    def test_inconsistent_activity(self):
        obs = SyntheticMLProvider.get_scenario("INCONSISTENT")
        data = vars(obs)
        decision = self.interface.process_ml_output(data)
        self.assertEqual(decision.action, "STABILIZE_FOCUS")
        self.assertIn("inconsistent", decision.reason)

    def test_productivity_decline(self):
        sequence = SyntheticMLProvider.get_decline_sequence()
        decisions = []
        for obs in sequence:
            decisions.append(self.interface.agent.observe(obs))
        
        self.assertEqual(decisions[-1].action, "PREVENT_DECLINE")
        self.assertIn("Consistent decline", decisions[-1].reason)

    def test_productivity_improvement(self):
        sequence = SyntheticMLProvider.get_improvement_sequence()
        decisions = []
        for obs in sequence:
            decisions.append(self.interface.agent.observe(obs))
        
        self.assertEqual(decisions[-1].action, "POSITIVE_REINFORCEMENT")
        self.assertIn("Steady improvement", decisions[-1].reason)

    def test_invalid_ml_input(self):
        obs = SyntheticMLProvider.get_scenario("INVALID")
        data = vars(obs)
        decision = self.interface.process_ml_output(data)
        self.assertIsNone(decision)

    def test_repetitive_intervention_avoidance(self):
        obs = SyntheticMLProvider.get_scenario("LOW_ENGAGEMENT")
        data = vars(obs)
        
        # First observation
        d1 = self.interface.process_ml_output(data)
        self.assertEqual(d1.action, "NUDGE_ENGAGEMENT")
        
        # Second observation with same data
        d2 = self.interface.process_ml_output(data)
        self.assertEqual(d2.action, "MONITOR")
        self.assertIn("Condition persists", d2.reason)

if __name__ == "__main__":
    unittest.main()
