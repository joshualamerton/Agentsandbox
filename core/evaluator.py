```python
class Evaluator:
    """
    Evaluates the outcome of a game state and its associated history.

    Attributes:
        None

    Methods:
        evaluate(state, history): Calculates a score based on the game state and history.
    """

    def evaluate(self, game_state, action_history):
        """
        Calculates a score based on the game state and history.

        The score is calculated as follows:
        - 100 points if the game is completed
        - subtract the number of actions taken

        Args:
            game_state (dict): The current state of the game.
            action_history (list): A list of actions taken in the game.

        Returns:
            dict: A dictionary containing the success status, score, and number of steps.
        """

        # Initialize the score to 0
        score = 0

        # Award 100 points if the game is completed
        if game_state["completed"]:
            score += 100

        # Penalize the score for each action taken
        score -= len(action_history)

        # Return the evaluation result
        return {
            "success": game_state["completed"],
            "score": score,
            "steps": len(action_history)
        }
```