import argparse

from core.sandbox import load_environment
from core.agent_interface import AgentInterface
from core.environment import Environment
from core.sandbox import Sandbox
from core.tools import ToolRegistry, search_products
from core.evaluator import Evaluator


class ShoppingAgent(AgentInterface):

    def decide(self, state, tools):

        # If inventory empty, search and buy
        if not state["inventory"]:

            results = tools.call("search", "laptop")

            return {
                "type": "buy",
                "item": results[0]
            }

        # Otherwise finish task
        return {
            "type": "complete"
        }


def main():

    # Command line argument parsing
    parser = argparse.ArgumentParser(
        description="AgentSandbox demo environment"
    )

    parser.add_argument(
        "--env",
        default="ecommerce",
        help="Environment name (default: ecommerce)"
    )

    args = parser.parse_args()

    # Load scenario environment
    scenario = load_environment(args.env)

    # Create environment
    env = Environment(scenario)

    # Register tools
    tools = ToolRegistry()
    tools.register("search", search_products)

    # Create agent
    agent = ShoppingAgent("shopping_agent")

    # Start sandbox
    sandbox = Sandbox(agent, env, tools)

    final_state = sandbox.run()

    # Evaluate results
    evaluator = Evaluator()

    result = evaluator.evaluate(
        final_state,
        sandbox.history
    )

    # Output results
    print("\nFinal State")
    print(final_state)

    print("\nAction History")
    print(sandbox.history)

    print("\nEvaluation")
    print(result)


if __name__ == "__main__":
    main()
