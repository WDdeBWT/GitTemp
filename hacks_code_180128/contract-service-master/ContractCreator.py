import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

w3 = None
class ContractCreator(object):
	"""docstring for ClassName"""
	def __init__(self):
		super(ContractCreator, self).__init__()

	def create(self, contract_source_code, contract, args):
		compiled_sol = compile_source(contract_source_code) # Compiled source code
		contract_interface = compiled_sol[contract]
		global w3
		if w3 is None:
			w3 = self.getWeb3()
		# Instantiate and deploy contract
		contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
		# Get transaction hash from deployed contract
		tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 4000000}, args=args)
		# Get tx receipt to get contract address
		tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
		contract_address = tx_receipt['contractAddress']
		contract_instance = w3.eth.contract(address=contract_address, abi=contract_interface['abi'], ContractFactoryClass=ConciseContract)
		return w3, contract_instance
	def getWeb3(self):
		# web3.py instance
		w3 = Web3(TestRPCProvider())
		return w3


