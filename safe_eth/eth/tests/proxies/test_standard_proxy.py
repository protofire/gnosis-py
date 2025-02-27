from unittest import TestCase

from eth_typing import ChecksumAddress
from hexbytes import HexBytes

from safe_eth.eth.proxies import StandardProxy
from safe_eth.safe import Safe
from safe_eth.safe.tests.safe_test_case import SafeTestCaseMixin


class TestStandardProxy(SafeTestCaseMixin, TestCase):
    standard_proxy_bytecode = HexBytes(
        "0x608060405234801561001057600080fd5b506040516106f63803806106f683398181016040528101906100329190610523565b8181610044828261004d60201b60201c565b50505050610607565b61005c826100d260201b60201c565b8173ffffffffffffffffffffffffffffffffffffffff167fbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b60405160405180910390a26000815111156100bf576100b982826101a560201b60201c565b506100ce565b6100cd61022f60201b60201c565b5b5050565b60008173ffffffffffffffffffffffffffffffffffffffff163b0361012e57806040517f4c9c8ce3000000000000000000000000000000000000000000000000000000008152600401610125919061058e565b60405180910390fd5b806101617f360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc60001b61026c60201b60201c565b60000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b60606000808473ffffffffffffffffffffffffffffffffffffffff16846040516101cf91906105f0565b600060405180830381855af49150503d806000811461020a576040519150601f19603f3d011682016040523d82523d6000602084013e61020f565b606091505b509150915061022585838361027660201b60201c565b9250505092915050565b600034111561026a576040517fb398979f00000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b565b6000819050919050565b6060826102915761028c8261030b60201b60201c565b610303565b600082511480156102b9575060008473ffffffffffffffffffffffffffffffffffffffff163b145b156102fb57836040517f9996b3150000000000000000000000000000000000000000000000000000000081526004016102f2919061058e565b60405180910390fd5b819050610304565b5b9392505050565b60008151111561031e5780518082602001fd5b6040517f1425ea4200000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b6000604051905090565b600080fd5b600080fd5b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600061038f82610364565b9050919050565b61039f81610384565b81146103aa57600080fd5b50565b6000815190506103bc81610396565b92915050565b600080fd5b600080fd5b6000601f19601f8301169050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b610415826103cc565b810181811067ffffffffffffffff82111715610434576104336103dd565b5b80604052505050565b6000610447610350565b9050610453828261040c565b919050565b600067ffffffffffffffff821115610473576104726103dd565b5b61047c826103cc565b9050602081019050919050565b60005b838110156104a757808201518184015260208101905061048c565b60008484015250505050565b60006104c66104c184610458565b61043d565b9050828152602081018484840111156104e2576104e16103c7565b5b6104ed848285610489565b509392505050565b600082601f83011261050a576105096103c2565b5b815161051a8482602086016104b3565b91505092915050565b6000806040838503121561053a5761053961035a565b5b6000610548858286016103ad565b925050602083015167ffffffffffffffff8111156105695761056861035f565b5b610575858286016104f5565b9150509250929050565b61058881610384565b82525050565b60006020820190506105a3600083018461057f565b92915050565b600081519050919050565b600081905092915050565b60006105ca826105a9565b6105d481856105b4565b93506105e4818560208601610489565b80840191505092915050565b60006105fc82846105bf565b915081905092915050565b60e1806106156000396000f3fe6080604052600a600c565b005b60186014601a565b6027565b565b60006022604c565b905090565b3660008037600080366000845af43d6000803e80600081146047573d6000f35b3d6000fd5b600060787f360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc60001b60a1565b60000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b600081905091905056fea26469706673582212209a40f50a4ff13192312765b2f472363e3ca8c8f25fbefc2363ea1ad3850c61dc64736f6c634300081b0033"
    )
    standard_proxy_abi = [
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_implementation",
                    "type": "address",
                },
                {"internalType": "bytes", "name": "_data", "type": "bytes"},
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "target", "type": "address"}
            ],
            "name": "AddressEmptyCode",
            "type": "error",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "implementation", "type": "address"}
            ],
            "name": "ERC1967InvalidImplementation",
            "type": "error",
        },
        {"inputs": [], "name": "ERC1967NonPayable", "type": "error"},
        {"inputs": [], "name": "FailedInnerCall", "type": "error"},
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "implementation",
                    "type": "address",
                }
            ],
            "name": "Upgraded",
            "type": "event",
        },
        {"stateMutability": "payable", "type": "fallback"},
    ]

    def deploy_standard_proxy(
        self, singleton_address: ChecksumAddress
    ) -> StandardProxy:
        """
        Deploy a EIP-1967 proxy

        :param singleton_address: Address the proxy will point to
        :return: StandardProxy deployed
        """
        standard_proxy = self.w3.eth.contract(
            abi=self.standard_proxy_abi, bytecode=self.standard_proxy_bytecode
        )
        tx_hash = standard_proxy.constructor(singleton_address, b"").transact(
            {"from": self.ethereum_test_account.address}
        )
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        proxy_address = tx_receipt["contractAddress"]
        assert proxy_address is not None

        return StandardProxy(proxy_address, self.ethereum_client)

    def test_get_implementation_address(self):
        singleton_address = self.safe_contract_V1_4_1.address
        standard_proxy = self.deploy_standard_proxy(singleton_address)
        self.assertEqual(standard_proxy.get_implementation_address(), singleton_address)

        # Test Safe class supports the Proxy
        safe = Safe(standard_proxy.address, self.ethereum_client)
        self.assertEqual(safe.retrieve_master_copy_address(), singleton_address)
