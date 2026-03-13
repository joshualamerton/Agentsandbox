```python
class ToolRegistry:
    """
    A registry for tools, allowing registration and invocation of functions by name.
    """

    def __init__(self):
        """
        Initializes an empty registry.
        """
        # Store registered tools in a dictionary for efficient lookup
        self.tools = {}

    def register_tool(self, name: str, func):
        """
        Registers a function in the registry under the given name.

        Args:
            name (str): The name under which to register the function.
            func: The function to register.
        """
        # Store the function in the registry with its name as key
        self.tools[name] = func

    def invoke_tool(self, name: str, *args):
        """
        Invokes a registered function by its name, passing the provided arguments.

        Args:
            name (str): The name of the function to invoke.
            *args: The arguments to pass to the function.

        Returns:
            The result of the function invocation.
        """
        # Retrieve the registered function and call it with the provided arguments
        return self.tools[name](*args)


def search_products(query: str) -> list:
    """
    Searches for products matching the given query.

    Args:
        query (str): The query to search for.

    Returns:
        A list of products matching the query, or an empty list if no matches are found.
    """
    # Define a dictionary mapping query names to their corresponding product lists
    products = {
        "laptop": ["MacBook", "ThinkPad"],
        "phone": ["iPhone", "Pixel"]
    }

    # Return the list of products matching the query, or an empty list if no matches are found
    return products.get(query, [])
```