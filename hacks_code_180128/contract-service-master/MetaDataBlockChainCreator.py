import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

from ContractCreator import ContractCreator

# Solidity source code
contract_source_code = '''
pragma solidity ^0.4.16;

contract MetaDataBlockChain {

    mapping (address => string[]) public userMeta;

    function addMeta (address _user, string _metadata) public returns (bool) {
        userMeta[_user].push(_metadata);
        return true;
    }

    function checkMeta (address _user, string _metadata) public returns (bool) {
        uint i = 0;
        for (i=0; i<userMeta[_user].length; i++)
        {
            if (keccak256(userMeta[_user][i]) == keccak256(_metadata))
            {
                return true;
            }
        }
        return false;
    }

    function removeMeta (address _user, string _metadata) public returns (bool) {
        uint i = 0;
        for (i=0; i<userMeta[_user].length; i++)
        {
            if (keccak256(userMeta[_user][i]) == keccak256(_metadata))
            {
                userMeta[_user][i] = "-1";
                return true;
            }
        }
        return false;
    }

    function updateMeta (address _user, string _oldmetadata, string _newmetadata) public returns (bool) {
        uint i = 0;
        for (i=0; i<userMeta[_user].length; i++)
        {
            if (keccak256(userMeta[_user][i]) == keccak256(_oldmetadata))
            {
                userMeta[_user][i] = _newmetadata;
                return true;
            }
        }
        return false;
    }
}
'''

contract_instance = None
w3 = None

class MetaDataBlockChainCreator(ContractCreator):
    def __init__(self):
        super(MetaDataBlockChainCreator, self).__init__()
    def getInstance(self):
        global contract_instance, w3
        if contract_instance is None:
            w3, contract_instance = self.create(contract_source_code, '<stdin>:MetaDataBlockChain', None)
        return w3, contract_instance

