from typing import List

from dojo.actions.base_action import BaseAction
from dojo.agents.base_agent import BaseAgent
from dojo.observations import BaseObservation
from dojo.policies import BasePolicy


########################################################################
########################################################################
#
# START: 
from colorama import Fore, Style
from collections import deque
from decimal import Decimal
from typing import Any, List, Optional
import numpy as np
from dojo.actions.base_action import BaseAction
from dojo.actions.uniswapV3 import UniswapV3Trade
from dojo.agents import BaseAgent
from dojo.environments.uniswapV3 import UniswapV3Observation
from dojo.policies import BasePolicy
from dojo.agents import UniswapV3Agent
from decimal import Decimal
from typing import Optional
from dojo.agents import UniswapV3Agent
from dojo.environments.uniswapV3 import UniswapV3Observation

#######################################################################
# helper functions:
########################################################################

class SingleAction(BasePolicy):  # type: ignore
    """A policy that executes a single action.

    This is useful for testing the impact of a single action in an environment. For
    example, you might want to see what the final price in a UniswapV3 pool would be if
    you executed a single swap.
    """

    def __init__(self, agent: BaseAgent) -> None:  # type: ignore
        """Initialize the policy.

        :param agent: The agent which is using this policy.
        :param action: The action to execute.
        """
        super().__init__(agent)
        #self.action = action
    

    def predict(self, obs):
        #echo(self.agent.erc20_portfolio()['WBTC'],'self.agent.erc20_portfolio()[\'WBTC\']')

        # action_sequence = flatten([
        #         self.dump_dollars(self.agent),
        #         self.buy_bitcoin(self.agent)
        #         ])
        
        #add_signals(obs = obs, agent=self.agent)
        
        return [UniswapV3Trade(agent=self.agent,
                              pool = "WBTC/WETH-0.05",
                              quantities=(Decimal(0), Decimal(0.01))
                              )]




























########################################################################
########## Agent to be used:
########################################################################

class UniswapV3PoolWealthAgent(UniswapV3Agent):
    """This agent implements a pool wealth reward function for a single UniswapV3 pool.

    The agent should not be given any tokens that are not in the UniswapV3Env pool.
    """

    def __init__(
        self, initial_portfolio: dict[str, Decimal], name: Optional[str] = None
    ):
        """Initialize the agent."""
        super().__init__(name=name, initial_portfolio=initial_portfolio)

    def reward(self, obs: UniswapV3Observation) -> float:  # type: ignore
        """The agent wealth in units of asset y according to the UniswapV3 pool."""
        # define your PnL here, I'm happy to supply my own if asked.

        return Decimal(1_000_000_000)
