import logging
import argparse
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Any, Optional
from dateutil import parser as dateparser
from policy import *


from dojo.common.constants import Chain
from dojo.environments import UniswapV3Env
from dojo.runners import backtest_run

from policy import buy_bitcoins






  
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)  

def main(
    *,
    dashboard_server_port: Optional[int] = 8768,
    simulation_status_bar: bool = False,
    auto_close: bool,
    backend_type,
    **kwargs: dict[str, Any],
):

    # SNIPPET 1 START
    
    pools = ["USDC/WETH-0.05", "WBTC/WETH-0.05"]
    start_time = dateparser.parse("2024-06-20 00:00:00 UTC")
    end_time = dateparser.parse("2024-06-21 01:01:00 UTC")


    # Agents

    agent1 = UniswapV3PoolWealthAgent(
        initial_portfolio= {"USDC": Decimal(50_000), "WETH": Decimal(25),"WBTC": Decimal(1)},
        name="bitcoin_buyer")

    # Simulation environment (Uniswap V3)
    env = UniswapV3Env(
        chain=Chain.ETHEREUM,
        date_range=(start_time, end_time),
        agents=[agent1],
        pools=pools,
        backend_type = backend_type,
        market_impact="replay",
    )

    # Policies
    policy=buy_bitcoins(agent = agent1)

    backtest_run(
        env,
        [policy],
        dashboard_server_port=dashboard_server_port,
        auto_close=auto_close,
        simulation_status_bar=simulation_status_bar,
    )
    # SNIPPET 1 END


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="add something")
    parser.add_argument(
        "--backend",
        required=True,
        help="BACKEND type"
    )
    parser.add_argument(
        "--time",
        required=True,
        help="BACKEND type"
    )
    args = parser.parse_args()
    print(args)
    print(args.backend)
    #print(args.run_length)
    print(type(args.time))
    t = float(args.time)
    

    #logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.ERROR)

    main(
        dashboard_server_port=8768,
        simulation_status_bar=True,
        auto_close=False,
        run_length=timedelta(hours=t),
        backend_type=args.backend
    )
    # Parse the arguments
    

    # # Convert the provided SQLite database file to JSON
    # convert_db_file_to_json(args.db)