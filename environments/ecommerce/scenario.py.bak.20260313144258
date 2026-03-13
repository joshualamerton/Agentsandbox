from core.scenario import Scenario


class EcommerceScenario(Scenario):

    def __init__(self):

        super().__init__(
            description="Buy a laptop under $2000",
            goal="purchase_laptop"
        )

    def initial_state(self):

        return {
            "step": 0,
            "inventory": [],
            "budget": 2000,
            "completed": False
        }
