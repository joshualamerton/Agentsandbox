```python
from core.scenario import Scenario

class EcommerceScenario(Scenario):
    """
    A scenario where a user buys a laptop under $2000.
    """

    def __init__(self):
        """
        Initializes the EcommerceScenario with a description and goal.
        """
        super().__init__(
            description="Buy a laptop under $2000",
            goal="purchase_laptop"
        )

    def initial_state(self) -> dict:
        """
        Returns the initial state of the scenario.

        The initial state includes the step number, inventory, budget, and completion status.

        Returns:
            dict: The initial state of the scenario.
        """
        return {
            "step": 0,
            "inventory": [],
            "budget": 2000,
            "completed": False
        }
```