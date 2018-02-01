import tornado.web

import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract
from MyAdvancedTokenCreator import MyAdvancedTokenCreator

class NewUserHandler(tornado.web.RequestHandler):
    def get(self):
        privateKey = self.get_argument('privateKey', None)
        if privateKey is None:
            self.write('failed')
        w3, contract_instance = self.getInstance()
        self.write(w3.personal.newAccount(privateKey))
    def getInstance(self):
        myAdvancedTokenCreator = MyAdvancedTokenCreator()
        w3, contract_instance = myAdvancedTokenCreator.getInstance()
        return w3, contract_instance

if __name__ == '__main__':
    newUserHandler = NewUserHandler()
    w3, contract_instance = newUserHandler.getInstance()
    print(w3.personal.newAccount('privateKey'))
