import tornado.web

import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

from MetaDataBlockChainCreator import MetaDataBlockChainCreator

class MetaDataBlockChainHandler(tornado.web.RequestHandler):
    def get(self):
        metadata = self.get_argument('metadata', None)
        if metadata is None:
            self.write("fail")
        self.addMetaData(metadata)
        if self.checkMetaData(metadata):
            self.write("success")
            return
        self.write("fail")
    def addMetaData(self, meatadata):
        w3, contract_instance = self.getInstance()
        contract_instance.addMeta(w3.eth.accounts[0], meatadata, transact={'from': w3.eth.accounts[0]})
    def checkMetaData(self, metadata):
        w3, contract_instance = self.getInstance()
        print(w3.eth.accounts[0])
        return contract_instance.checkMeta(w3.eth.accounts[0], metadata)
    def getInstance(self):
        metaDataBlockChainCreator = MetaDataBlockChainCreator()
        w3, contract_instance = metaDataBlockChainCreator.getInstance()
        return w3, contract_instance

if __name__ == '__main__':
    metaDataBlockChainHandler = MetaDataBlockChainHandler()
    metaDataBlockChainHandler.addMetaData("metadata")
    # w3, contract_instance = metaDataBlockChainHandler.getInstance()
    # contract_instance.addMeta(w3.eth.accounts[0], "meatadata", transact={'from': w3.eth.accounts[0]})
    print(metaDataBlockChainHandler.checkMetaData("metadata"))