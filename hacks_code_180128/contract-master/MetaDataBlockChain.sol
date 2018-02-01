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