# tests/test_agent_interface.py

import pytest
from . import agent_interface  # Import the module under test


class TestAgentInterface:
    def test_init(self):
        """Test initializing an AgentInterface instance."""
        name = "test_agent"
        agent = agent_interface.AgentInterface(name)
        assert agent.name == name

    def test_init_empty_name(self):
        """Test initializing an AgentInterface instance with an empty name."""
        with pytest.raises(TypeError):
            agent_interface.AgentInterface("")

    def test_init_non_string_name(self):
        """Test initializing an AgentInterface instance with a non-string name."""
        with pytest.raises(TypeError):
            agent_interface.AgentInterface(123)

    def test_decide(self):
        """Test calling the decide method on an AgentInterface instance."""
        name = "test_agent"
        agent = agent_interface.AgentInterface(name)
        with pytest.raises(
            agent_interface.AgentInterface.decide.__func__.__name__
            + " must be implemented"
        ):
            agent.decide({}, {})

    def test_decide_with_state(self):
        """Test calling the decide method on an AgentInterface instance with a state."""
        name = "test_agent"
        agent = agent_interface.AgentInterface(name)
        with pytest.raises(
            agent_interface.AgentInterface.decide.__func__.__name__
            + " must be implemented"
        ):
            agent.decide({"key": "value"}, {})

    def test_decide_with_tools(self):
        """Test calling the decide method on an AgentInterface instance with tools."""
        name = "test_agent"
        agent = agent_interface.AgentInterface(name)
        with pytest.raises(
            agent_interface.AgentInterface.decide.__func__.__name__
            + " must be implemented"
        ):
            agent.decide({}, {"tool": "value"})

    def test_decide_with_state_and_tools(self):
        """Test calling the decide method on an AgentInterface instance with a state and tools."""
        name = "test_agent"
        agent = agent_interface.AgentInterface(name)
        with pytest.raises(
            agent_interface.AgentInterface.decide.__func__.__name__
            + " must be implemented"
        ):
            agent.decide({"key": "value"}, {"tool": "value"})
