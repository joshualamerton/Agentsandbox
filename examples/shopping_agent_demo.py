from core.agent_interface import AgentInterface
from core.environment import Environment
from core.scenario import Scenario
from core.sandbox import Sandbox
from core.tools import ToolRegistry, search_products
from core.evaluator import Evaluator


class ShoppingAgent(AgentInterface):

    def decide(self, state, tools):

        if not state["inventory"]:

            results = tools.call("search", "laptop")

            return {
                "type": "buy",
                "item": results[0]
            }

        return {
            "type": "complete"
        }


def main():

    scenario = Scenario(
        "Buy a laptop and finish task",
        goal="purchase_laptop"
    )

    env = Environment(scenario)

    tools = ToolRegistry()
    tools.register("search", search_products)

    agent = ShoppingAgent("shopping_agent")

    sandbox = Sandbox(agent, env, tools)

    final_state = sandbox.run()

    evaluator = Evaluator()

    result = evaluator.evaluate(final_state, sandbox.history)

    print("Final State")
    print(final_state)

    print("\nAction History")
    print(sandbox.history)

    print("\nEvaluation")
    print(result)


if __name__ == "__main__":
    main()
