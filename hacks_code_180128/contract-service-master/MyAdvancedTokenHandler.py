import tornado.web

import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

from MyAdvancedTokenCreator import MyAdvancedTokenCreator

class MyAdvancedTokenHandler(tornado.web.RequestHandler):
	def get(self):
		addr = self.get_argument('addr', None)
		count = self.get_argument('count', None)
		if addr is None or count is None:
			self.write("fail")
		self.transferTo(addr, count)
		self.write(str(self.getBalance(addr)))
	def transferTo(self, addr, count):
		w3, contract_instance = self.getInstance()
		contract_instance.transferFrom(w3.eth.accounts[0], addr, int(count), transact={'from': w3.eth.accounts[0]})
	def getBalance(self, addr):
		w3, contract_instance = self.getInstance()
		return contract_instance.getBalance(addr)
	def getInstance(self):
		myAdvancedTokenCreator = MyAdvancedTokenCreator()
		w3, contract_instance = myAdvancedTokenCreator.getInstance()
		return w3, contract_instance

if __name__ == '__main__':
	myAdvancedTokenHandler = MyAdvancedTokenHandler()
	w3, contract_instance = myAdvancedTokenHandler.getInstance()
	print(w3.eth.accounts[1])
	myAdvancedTokenHandler.transferTo(w3.eth.accounts[1], 100)
	myAdvancedTokenHandler.transferTo(w3.eth.accounts[1], 100)
	print(myAdvancedTokenHandler.getBalance(w3.eth.accounts[1]))
