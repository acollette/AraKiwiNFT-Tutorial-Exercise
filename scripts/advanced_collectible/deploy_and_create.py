from brownie import AdvancedCollectible, accounts, network, config
from scripts.helpful_scripts import fund_with_link

def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    advanced_collectible = AdvancedCollectible.deploy(
        config["networks"][network.show_active()]["vrf_coordinator"],
        config["networks"][network.show_active()]["link_token"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": dev},
        publish_source=True,
    )
    fund_with_link(advanced_collectible.address)
    return advanced_collectible
