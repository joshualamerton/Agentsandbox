```python
class Sandbox:
    """
    A sandbox environment for testing and training agents.

    Attributes:
        agent (Agent): The agent being tested or trained.
        environment (Environment): The environment in which the agent operates.
        tools (dict): Additional tools or resources available to the agent.
        history (list): A record of actions taken by the agent during a run.
    """

    def __init__(self, agent, environment, tools):
        """
        Initialize the sandbox environment.

        Args:
            agent (Agent): The agent being tested or trained.
            environment (Environment): The environment in which the agent operates.
            tools (dict): Additional tools or resources available to the agent.
        """
        self.agent = agent
        self.environment = environment
        self.tools = tools
        self.history = []  # Initialize history as an empty list

    def run(self, max_steps: int = 10) -> dict:
        """
        Run the agent in the environment for a specified number of steps.

        Args:
            max_steps (int, optional): The maximum number of steps to run. Defaults to 10.

        Returns:
            dict: The final state of the environment.
        """
        # Get the initial state of the environment
        state = self.environment.state

        # Run the agent in the environment for max_steps
        for _ in range(max_steps):
            # Have the agent decide on an action based on the current state and tools
            action = self.agent.decide(state, self.tools)

            # Apply the action to the environment
            state = self.environment.apply_action(action)

            # Record the action in the history
            self.history.append(action)

            # If the environment has completed, stop running
            if state["completed"]:
                break

        return state

def load_environment(environment_name: str) -> Environment:
    """
    Load an environment based on its name.

    Args:
        environment_name (str): The name of the environment to load.

    Returns:
        Environment: The loaded environment.

    Raises:
        ValueError: If the environment name is unknown.
    """
    if environment_name == "ecommerce":
        from environments.ecommerce.scenario import EcommerceScenario
        return EcommerceScenario()

    elif environment_name == "devops":
        from environments.devops.scenario import DevOpsScenario
        return DevOpsScenario()

    else:
        raise ValueError(f"Unknown environment: {environment_name}")
```

Note that I've added type hints for function arguments and return types, which can help with code readability and catch type-related errors. I've also added docstrings to explain the purpose and behavior of each function and class. Additionally, I've reformatted the code to follow PEP 8 conventions and improved variable and function names for better readability.