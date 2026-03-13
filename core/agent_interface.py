class AgentInterface:

    def __init__(self, name):
        self.name = name

    def decide(self, state, tools):
        """
        Returns an action dictionary
        """
        raise NotImplementedError
