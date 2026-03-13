```python
import argparse

from core.sandbox import load_environment
from core.agent_interface import AgentInterface
from core.environment import Environment
from core.sandbox import Sandbox
from core.tools import ToolRegistry, search_products
from core.evaluator import Evaluator


class ShoppingAgent(AgentInterface):
    """
    Shopping agent that decides to buy a laptop if the inventory is empty.
    """

    def decide(self, state: dict, tools: ToolRegistry) -> dict:
        """
        Decide the next action based on the current state and available tools.

        Args:
            state (dict): Current state of the environment.
            tools (ToolRegistry): Registry of available tools.

        Returns:
            dict: Next action to take.
        """

        # If inventory is empty, search for and buy a laptop
        if not state["inventory"]:
            # Search for laptops using the search_products tool
            results = tools.call("search", "laptop")
            return {"type": "buy", "item": results[0]}

        # Otherwise, complete the task
        return {"type": "complete"}


def main():
    """
    Main entry point of the program.
    """

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="AgentSandbox demo environment")
    parser.add_argument("--env", default="ecommerce", help="Environment name (default: ecommerce)")
    args = parser.parse_args()

    # Load scenario environment
    scenario = load_environment(args.env)

    # Create environment
    env = Environment(scenario)

    # Register tools
    tools = ToolRegistry()
    tools.register("search", search_products)

    # Create shopping agent
    agent = ShoppingAgent("shopping_agent")

    # Start sandbox
    sandbox = Sandbox(agent, env, tools)

    # Run the sandbox and get the final state
    final_state = sandbox.run()

    # Evaluate the results
    evaluator = Evaluator()
    result = evaluator.evaluate(final_state, sandbox.history)

    # Output results
    print("\nFinal State")
    print(final_state)

    print("\nAction History")
    print(sandbox.history)

    print("\nEvaluation")
    print(result)


if __name__ == "__main__":
    main()
```