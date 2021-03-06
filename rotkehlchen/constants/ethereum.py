# flake8: noqa

import json
import os
from typing import Any, Dict, List, NamedTuple, Optional

from rotkehlchen.serialization.deserialize import deserialize_ethereum_address
from rotkehlchen.typing import ChecksumEthAddress

ZERO_ADDRESS = deserialize_ethereum_address('0x0000000000000000000000000000000000000000')
AAVE_ETH_RESERVE_ADDRESS = deserialize_ethereum_address('0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE')


class EthereumContract(NamedTuple):
    address: ChecksumEthAddress
    abi: List[Dict[str, Any]]
    deployed_block: int


class EthereumConstants():
    __instance = None
    contracts: Dict[str, Dict[str, Any]] = {}
    abi_entries: Dict[str, List[Dict[str, Any]]] = {}

    def __new__(cls) -> 'EthereumConstants':
        if EthereumConstants.__instance is not None:
            return EthereumConstants.__instance  # type: ignore

        EthereumConstants.__instance = object.__new__(cls)

        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        with open(os.path.join(dir_path, 'data', 'eth_contracts.json'), 'r') as f:
            contracts = json.loads(f.read())

        with open(os.path.join(dir_path, 'data', 'eth_abi.json'), 'r') as f:
            abi_entries = json.loads(f.read())

        EthereumConstants.__instance.contracts = contracts
        EthereumConstants.__instance.abi_entries = abi_entries
        return EthereumConstants.__instance

    @staticmethod
    def get() -> Dict[str, Dict[str, Any]]:
        return EthereumConstants().contracts

    @staticmethod
    def contract_or_none(name: str) -> Optional[EthereumContract]:
        """Gets details of an ethereum contract from the contracts json file

        Returns None if missing
        """
        contract = EthereumConstants().contracts.get(name, None)
        if contract is None:
            return None

        return EthereumContract(
            address=contract['address'],
            abi=contract['abi'],
            deployed_block=contract['deployed_block'],
        )

    @staticmethod
    def contract(name: str) -> EthereumContract:
        """Gets details of an ethereum contract from the contracts json file

        Missing contract is an error
        """
        contract = EthereumConstants().contract_or_none(name)
        assert contract, f'No contract data for {name} found'
        return contract

    @staticmethod
    def abi_or_none(name: str) -> Optional[List[Dict[str, Any]]]:
        """Gets abi of an ethereum contract from the abi json file

        Returns None if missing
        """
        return EthereumConstants().abi_entries.get(name, None)

    @staticmethod
    def abi(name: str) -> List[Dict[str, Any]]:
        abi = EthereumConstants().abi_or_none(name)
        assert abi, f'No abi for {name} found'
        return abi

# Latest contract addresses are in the makerdao changelog. These values are taken from here:
# https://changelog.makerdao.com/releases/mainnet/1.0.6/contracts.json


MAKERDAO_DAI_JOIN = EthereumConstants().contract('MAKERDAO_DAI_JOIN')
MAKERDAO_CDP_MANAGER = EthereumConstants().contract('MAKERDAO_CDP_MANAGER')
MAKERDAO_GET_CDPS = EthereumConstants().contract('MAKERDAO_GET_CDPS')
MAKERDAO_PROXY_REGISTRY = EthereumConstants().contract('MAKERDAO_PROXY_REGISTRY')
MAKERDAO_SPOT = EthereumConstants().contract('MAKERDAO_SPOT')
MAKERDAO_POT = EthereumConstants().contract('MAKERDAO_POT')
MAKERDAO_VAT = EthereumConstants().contract('MAKERDAO_VAT')
MAKERDAO_ETH_A_JOIN = EthereumConstants().contract('MAKERDAO_ETH_A_JOIN')
MAKERDAO_BAT_A_JOIN = EthereumConstants().contract('MAKERDAO_BAT_A_JOIN')
MAKERDAO_USDC_A_JOIN = EthereumConstants().contract('MAKERDAO_USDC_A_JOIN')
MAKERDAO_USDC_B_JOIN = EthereumConstants().contract('MAKERDAO_USDC_B_JOIN')
MAKERDAO_WBTC_A_JOIN = EthereumConstants().contract('MAKERDAO_WBTC_A_JOIN')
MAKERDAO_KNC_A_JOIN = EthereumConstants().contract('MAKERDAO_KNC_A_JOIN')
MAKERDAO_TUSD_A_JOIN = EthereumConstants().contract('MAKERDAO_TUSD_A_JOIN')
MAKERDAO_ZRX_A_JOIN = EthereumConstants().contract('MAKERDAO_ZRX_A_JOIN')

MAKERDAO_CAT = EthereumConstants().contract('MAKERDAO_CAT')
MAKERDAO_JUG = EthereumConstants().contract('MAKERDAO_JUG')

ETH_SCAN = EthereumConstants().contract('ETH_SCAN')


AAVE_LENDING_POOL = EthereumConstants().contract('AAVE_LENDING_POOL')

ATOKEN_ABI = EthereumConstants.abi('ATOKEN')
ZERION_ABI = EthereumConstants.abi('ZERION_ADAPTER')
