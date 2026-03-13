```python
class AgentInterface:
    """
    Interface for agents to interact with the environment.

    Attributes:
        name (str): Name of the agent.
    """

    def __init__(self, name: str):
        """
        Initializes the agent with a name.

        Args:
            name (str): Name of the agent.
        """
        self.name = name

    def decide(self, state: dict, tools: dict) -> dict:
        """
        Returns an action dictionary based on the current state and available tools.

        Args:
            state (dict): Current state of the environment.
            tools (dict): Available tools for the agent.

        Returns:
            dict: Action dictionary.

        Raises:
            NotImplementedError: If the decide method is not implemented by the subclass.
        """
        raise NotImplementedError
```