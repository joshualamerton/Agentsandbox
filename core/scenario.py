```python
class Scenario:
    """
    Represents a scenario with a description and a goal.

    Attributes:
        description (str): A brief description of the scenario.
        goal (str): The objective of the scenario.
    """

    def __init__(self, description: str, goal: str):
        """
        Initializes a Scenario instance.

        Args:
            description (str): A brief description of the scenario.
            goal (str): The objective of the scenario.
        """
        self.description = description
        self.goal = goal

    def initial_state(self) -> dict:
        """
        Returns the initial state of the scenario.

        The initial state includes the current step, the scenario's goal,
        an empty inventory, and a completion status of False.

        Returns:
            dict: The initial state of the scenario.
        """
        return {
            "step": 0,
            "goal": self.goal,
            "inventory": [],
            "completed": False
        }
```