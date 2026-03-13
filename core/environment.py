```python
class Environment:
    """
    Represents an environment for a scenario, managing its state and applying actions.
    """

    def __init__(self, scenario):
        """
        Initializes the environment with the initial state of the scenario.

        Args:
            scenario: The scenario object that provides the initial state.
        """
        self.state = scenario.initial_state()  # Initialize the environment's state

    def apply_action(self, action: dict) -> dict:
        """
        Applies an action to the environment and updates its state accordingly.

        Args:
            action: A dictionary containing the action type and item (if applicable).

        Returns:
            The updated state of the environment.
        """
        # Update the environment's state based on the action type
        if action["type"] == "buy":
            # Add the item to the inventory
            item = action["item"]
            self.state["inventory"].append(item)
        elif action["type"] == "complete":
            # Mark the scenario as completed
            self.state["completed"] = True

        # Increment the step counter
        self.state["step"] += 1

        return self.state
```