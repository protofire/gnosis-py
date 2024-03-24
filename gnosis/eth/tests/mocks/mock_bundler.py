from eth_typing import ChecksumAddress, HexAddress, HexStr
from hexbytes import HexBytes

# Module address and chainId used for the following mocks
safe_4337_address = ChecksumAddress(
    HexStr(HexAddress("0xB0B5c0578Aa134b0496a6C0e51A7aae47C522861"))
)
safe_4337_user_operation_hash_mock = HexBytes(
    "0x39b3e2171c04539d9b3f848d04364dfaa42cc0b412ff65ce2a85c566cf8bf281"
)
safe_4337_module_address_mock = "0xa581c4A4DB7175302464fF3C06380BC3270b4037"
safe_4337_module_domain_separator_mock = HexBytes(
    "0x90c9c46bd4637f021a7ad976568aa4e00f6099277502df804cb980d5a1bb3d9f"
)
safe_4337_safe_operation_hash_mock = HexBytes(
    "0xb34556b3564ad04e472ca0f846afe44e0cfff8ceb0f94302792fdd1b9aff1351"
)
safe_4337_chain_id_mock = 11155111

user_operation_mock = {
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "userOperation": {
            "sender": "0xB0B5c0578Aa134b0496a6C0e51A7aae47C522861",
            "nonce": "0x0",
            "initCode": "0x4e1dcf7ad4e460cfd30791ccc4f9c8a4f820ec671688f0b900000000000000000000000029fcb43b46531bca003ddc8fcb67ffe91900c7620000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001e4b63e800d000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000010000000000000000000000008ecd4ec46d4d2a6b64fe960b3d64e8b94b2234eb0000000000000000000000000000000000000000000000000000000000000140000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b403700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000005ac255889882acd3da2aa939679e3f3d4cea221e00000000000000000000000000000000000000000000000000000000000000648d0dc49f00000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000001000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b40370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "callData": "0x7bb3742800000000000000000000000002270bd144e70ce6963ba02f575776a16184e1e600000000000000000000000000000000000000000000000000005af3107a4000000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "callGasLimit": "0x6000",
            "verificationGasLimit": "0x76766",
            "preVerificationGas": "0xc814",
            "maxFeePerGas": "0x50bd27ea",
            "maxPriorityFeePerGas": "0x3b9aca00",
            "paymasterAndData": "0x",
            "signature": "0x000000000000000000000000ce4599307d2e53cf78c31a110c6930e41a2b46bceda18c88416000ff13be239c7afdcef5c22ee68bc7ad70cdf27da35160f14ceba88336e686e0533fcc293f3f1b",
        },
        "entryPoint": "0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789",
        "blockNumber": "0x50b0da",
        "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
        "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
    },
}


user_operation_receipt_mock = {
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "userOpHash": "0x39b3e2171c04539d9b3f848d04364dfaa42cc0b412ff65ce2a85c566cf8bf281",
        "entryPoint": "0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789",
        "sender": "0xB0B5c0578Aa134b0496a6C0e51A7aae47C522861",
        "nonce": "0x0",
        "paymaster": "0x0000000000000000000000000000000000000000",
        "actualGasCost": "0x1c7f432341e24",
        "actualGasUsed": "0x68072",
        "success": True,
        "reason": "",
        "logs": [
            {
                "address": "0xb0b5c0578aa134b0496a6c0e51a7aae47c522861",
                "topics": [
                    "0xecdf3a3effea5783a3c4c2140e677577666428d44ed9d474a0b3a4c9943f8440",
                    "0x000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b4037",
                ],
                "data": "0x",
                "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                "blockNumber": "0x50b0da",
                "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                "transactionIndex": "0x85",
                "logIndex": "0xc2",
                "removed": False,
            },
            {
                "address": "0xb0b5c0578aa134b0496a6c0e51a7aae47c522861",
                "topics": [
                    "0x141df868a6331af528e38c83b7aa03edc19be66e37ae67f9285bf4f8e3c6a1a8",
                    "0x0000000000000000000000004e1dcf7ad4e460cfd30791ccc4f9c8a4f820ec67",
                ],
                "data": "0x000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000010000000000000000000000008ecd4ec46d4d2a6b64fe960b3d64e8b94b2234eb000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b403700000000000000000000000000000000000000000000000000000000000000010000000000000000000000005ac255889882acd3da2aa939679e3f3d4cea221e",
                "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                "blockNumber": "0x50b0da",
                "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                "transactionIndex": "0x85",
                "logIndex": "0xc3",
                "removed": False,
            },
            {
                "address": "0x4e1dcf7ad4e460cfd30791ccc4f9c8a4f820ec67",
                "topics": [
                    "0x4f51faf6c4561ff95f067657e43439f0f856d97c04d9ec9070a6199ad418e235",
                    "0x000000000000000000000000b0b5c0578aa134b0496a6c0e51a7aae47c522861",
                ],
                "data": "0x00000000000000000000000029fcb43b46531bca003ddc8fcb67ffe91900c762",
                "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                "blockNumber": "0x50b0da",
                "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                "transactionIndex": "0x85",
                "logIndex": "0xc4",
                "removed": False,
            },
            {
                "address": "0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789",
                "topics": [
                    "0xd51a9c61267aa6196961883ecf5ff2da6619c37dac0fa92122513fb32c032d2d",
                    "0x39b3e2171c04539d9b3f848d04364dfaa42cc0b412ff65ce2a85c566cf8bf281",
                    "0x000000000000000000000000b0b5c0578aa134b0496a6c0e51a7aae47c522861",
                ],
                "data": "0x0000000000000000000000004e1dcf7ad4e460cfd30791ccc4f9c8a4f820ec670000000000000000000000000000000000000000000000000000000000000000",
                "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                "blockNumber": "0x50b0da",
                "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                "transactionIndex": "0x85",
                "logIndex": "0xc5",
                "removed": False,
            },
            {
                "address": "0xb0b5c0578aa134b0496a6c0e51a7aae47c522861",
                "topics": [
                    "0xb648d3644f584ed1c2232d53c46d87e693586486ad0d1175f8656013110b714e"
                ],
                "data": "0x000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b40370000000000000000000000005ff137d4b0fdcd49dca30c7cf57e578a026d27890000000000000000000000000000000000000000000000000002b32962c0bb8400000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
                "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                "blockNumber": "0x50b0da",
                "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                "transactionIndex": "0x85",
                "logIndex": "0xc6",
                "removed": False,
            },
            {
                "address": "0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789",
                "topics": [
                    "0x2da466a7b24304f47e87fa2e1e5a81b9831ce54fec19055ce277ca2f39ba42c4",
                    "0x000000000000000000000000b0b5c0578aa134b0496a6c0e51a7aae47c522861",
                ],
                "data": "0x0000000000000000000000000000000000000000000000000002b32962c0bb84",
                "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                "blockNumber": "0x50b0da",
                "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                "transactionIndex": "0x85",
                "logIndex": "0xc7",
                "removed": False,
            },
            {
                "address": "0xb0b5c0578aa134b0496a6c0e51a7aae47c522861",
                "topics": [
                    "0x6895c13664aa4f67288b25d7a21d7aaa34916e355fb9b6fae0a139a9085becb8",
                    "0x000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b4037",
                ],
                "data": "0x",
                "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                "blockNumber": "0x50b0da",
                "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                "transactionIndex": "0x85",
                "logIndex": "0xc8",
                "removed": False,
            },
            {
                "address": "0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789",
                "topics": [
                    "0xbb47ee3e183a558b1a2ff0874b079f3fc5478b7454eacf2bfc5af2ff5878f972"
                ],
                "data": "0x",
                "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                "blockNumber": "0x50b0da",
                "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                "transactionIndex": "0x85",
                "logIndex": "0xc9",
                "removed": False,
            },
            {
                "address": "0xb0b5c0578aa134b0496a6c0e51a7aae47c522861",
                "topics": [
                    "0xb648d3644f584ed1c2232d53c46d87e693586486ad0d1175f8656013110b714e"
                ],
                "data": "0x000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b403700000000000000000000000002270bd144e70ce6963ba02f575776a16184e1e600000000000000000000000000000000000000000000000000005af3107a400000000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
                "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                "blockNumber": "0x50b0da",
                "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                "transactionIndex": "0x85",
                "logIndex": "0xca",
                "removed": False,
            },
            {
                "address": "0xb0b5c0578aa134b0496a6c0e51a7aae47c522861",
                "topics": [
                    "0x6895c13664aa4f67288b25d7a21d7aaa34916e355fb9b6fae0a139a9085becb8",
                    "0x000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b4037",
                ],
                "data": "0x",
                "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                "blockNumber": "0x50b0da",
                "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                "transactionIndex": "0x85",
                "logIndex": "0xcb",
                "removed": False,
            },
            {
                "address": "0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789",
                "topics": [
                    "0x49628fd1471006c1482da88028e9ce4dbb080b815c9b0344d39e5a8e6ec1419f",
                    "0x39b3e2171c04539d9b3f848d04364dfaa42cc0b412ff65ce2a85c566cf8bf281",
                    "0x000000000000000000000000b0b5c0578aa134b0496a6c0e51a7aae47c522861",
                    "0x0000000000000000000000000000000000000000000000000000000000000000",
                ],
                "data": "0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000001c7f432341e240000000000000000000000000000000000000000000000000000000000068072",
                "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                "blockNumber": "0x50b0da",
                "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                "transactionIndex": "0x85",
                "logIndex": "0xcc",
                "removed": False,
            },
        ],
        "receipt": {
            "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
            "transactionIndex": "0x85",
            "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
            "blockNumber": "0x50b0da",
            "from": "0xd53eb5203e367bbdd4f72338938224881fc501ab",
            "to": "0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789",
            "cumulativeGasUsed": "0xd2a354",
            "gasUsed": "0x67c20",
            "contractAddress": None,
            "logs": [
                {
                    "address": "0xb0b5c0578aa134b0496a6c0e51a7aae47c522861",
                    "topics": [
                        "0xecdf3a3effea5783a3c4c2140e677577666428d44ed9d474a0b3a4c9943f8440",
                        "0x000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b4037",
                    ],
                    "data": "0x",
                    "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                    "blockNumber": "0x50b0da",
                    "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                    "transactionIndex": "0x85",
                    "logIndex": "0xc2",
                    "removed": False,
                },
                {
                    "address": "0xb0b5c0578aa134b0496a6c0e51a7aae47c522861",
                    "topics": [
                        "0x141df868a6331af528e38c83b7aa03edc19be66e37ae67f9285bf4f8e3c6a1a8",
                        "0x0000000000000000000000004e1dcf7ad4e460cfd30791ccc4f9c8a4f820ec67",
                    ],
                    "data": "0x000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000010000000000000000000000008ecd4ec46d4d2a6b64fe960b3d64e8b94b2234eb000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b403700000000000000000000000000000000000000000000000000000000000000010000000000000000000000005ac255889882acd3da2aa939679e3f3d4cea221e",
                    "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                    "blockNumber": "0x50b0da",
                    "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                    "transactionIndex": "0x85",
                    "logIndex": "0xc3",
                    "removed": False,
                },
                {
                    "address": "0x4e1dcf7ad4e460cfd30791ccc4f9c8a4f820ec67",
                    "topics": [
                        "0x4f51faf6c4561ff95f067657e43439f0f856d97c04d9ec9070a6199ad418e235",
                        "0x000000000000000000000000b0b5c0578aa134b0496a6c0e51a7aae47c522861",
                    ],
                    "data": "0x00000000000000000000000029fcb43b46531bca003ddc8fcb67ffe91900c762",
                    "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                    "blockNumber": "0x50b0da",
                    "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                    "transactionIndex": "0x85",
                    "logIndex": "0xc4",
                    "removed": False,
                },
                {
                    "address": "0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789",
                    "topics": [
                        "0xd51a9c61267aa6196961883ecf5ff2da6619c37dac0fa92122513fb32c032d2d",
                        "0x39b3e2171c04539d9b3f848d04364dfaa42cc0b412ff65ce2a85c566cf8bf281",
                        "0x000000000000000000000000b0b5c0578aa134b0496a6c0e51a7aae47c522861",
                    ],
                    "data": "0x0000000000000000000000004e1dcf7ad4e460cfd30791ccc4f9c8a4f820ec670000000000000000000000000000000000000000000000000000000000000000",
                    "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                    "blockNumber": "0x50b0da",
                    "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                    "transactionIndex": "0x85",
                    "logIndex": "0xc5",
                    "removed": False,
                },
                {
                    "address": "0xb0b5c0578aa134b0496a6c0e51a7aae47c522861",
                    "topics": [
                        "0xb648d3644f584ed1c2232d53c46d87e693586486ad0d1175f8656013110b714e"
                    ],
                    "data": "0x000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b40370000000000000000000000005ff137d4b0fdcd49dca30c7cf57e578a026d27890000000000000000000000000000000000000000000000000002b32962c0bb8400000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
                    "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                    "blockNumber": "0x50b0da",
                    "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                    "transactionIndex": "0x85",
                    "logIndex": "0xc6",
                    "removed": False,
                },
                {
                    "address": "0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789",
                    "topics": [
                        "0x2da466a7b24304f47e87fa2e1e5a81b9831ce54fec19055ce277ca2f39ba42c4",
                        "0x000000000000000000000000b0b5c0578aa134b0496a6c0e51a7aae47c522861",
                    ],
                    "data": "0x0000000000000000000000000000000000000000000000000002b32962c0bb84",
                    "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                    "blockNumber": "0x50b0da",
                    "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                    "transactionIndex": "0x85",
                    "logIndex": "0xc7",
                    "removed": False,
                },
                {
                    "address": "0xb0b5c0578aa134b0496a6c0e51a7aae47c522861",
                    "topics": [
                        "0x6895c13664aa4f67288b25d7a21d7aaa34916e355fb9b6fae0a139a9085becb8",
                        "0x000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b4037",
                    ],
                    "data": "0x",
                    "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                    "blockNumber": "0x50b0da",
                    "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                    "transactionIndex": "0x85",
                    "logIndex": "0xc8",
                    "removed": False,
                },
                {
                    "address": "0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789",
                    "topics": [
                        "0xbb47ee3e183a558b1a2ff0874b079f3fc5478b7454eacf2bfc5af2ff5878f972"
                    ],
                    "data": "0x",
                    "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                    "blockNumber": "0x50b0da",
                    "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                    "transactionIndex": "0x85",
                    "logIndex": "0xc9",
                    "removed": False,
                },
                {
                    "address": "0xb0b5c0578aa134b0496a6c0e51a7aae47c522861",
                    "topics": [
                        "0xb648d3644f584ed1c2232d53c46d87e693586486ad0d1175f8656013110b714e"
                    ],
                    "data": "0x000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b403700000000000000000000000002270bd144e70ce6963ba02f575776a16184e1e600000000000000000000000000000000000000000000000000005af3107a400000000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
                    "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                    "blockNumber": "0x50b0da",
                    "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                    "transactionIndex": "0x85",
                    "logIndex": "0xca",
                    "removed": False,
                },
                {
                    "address": "0xb0b5c0578aa134b0496a6c0e51a7aae47c522861",
                    "topics": [
                        "0x6895c13664aa4f67288b25d7a21d7aaa34916e355fb9b6fae0a139a9085becb8",
                        "0x000000000000000000000000a581c4a4db7175302464ff3c06380bc3270b4037",
                    ],
                    "data": "0x",
                    "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                    "blockNumber": "0x50b0da",
                    "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                    "transactionIndex": "0x85",
                    "logIndex": "0xcb",
                    "removed": False,
                },
                {
                    "address": "0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789",
                    "topics": [
                        "0x49628fd1471006c1482da88028e9ce4dbb080b815c9b0344d39e5a8e6ec1419f",
                        "0x39b3e2171c04539d9b3f848d04364dfaa42cc0b412ff65ce2a85c566cf8bf281",
                        "0x000000000000000000000000b0b5c0578aa134b0496a6c0e51a7aae47c522861",
                        "0x0000000000000000000000000000000000000000000000000000000000000000",
                    ],
                    "data": "0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000001c7f432341e240000000000000000000000000000000000000000000000000000000000068072",
                    "blockHash": "0xcc466b284f4030ee3f5941a2c8e36892262bf583611c902fe5558a595af47e13",
                    "blockNumber": "0x50b0da",
                    "transactionHash": "0xf8dab30ed3c8814ee9a67770ee68f8fb83e6247706c24371a76e7cd8d348b0e3",
                    "transactionIndex": "0x85",
                    "logIndex": "0xcc",
                    "removed": False,
                },
            ],
            "status": "0x1",
            "logsBloom": "0x080004000000900000000000000000008000000000000000000000000200000000080000000000000002200100000000001000000000000080000200000000000000100000000000000000000000000000000000000004080040000000002000000000000a00000005000000000008000000000001000000000000000002000008000120204002000000000000400000000002000004000000000000000000000000000000000010005000000000000002000000000000000000020000000000000000000000000000010000000000000000000000200000000000000000200000400c0000010000000000000008100220000000000000080000000000000000",
            "type": "0x2",
            "effectiveGasPrice": "0xa85f9ad",
        },
    },
}

supported_entrypoint_mock = {
    "jsonrpc": "2.0",
    "id": 1,
    "result": [
        "0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789",
        "0x0000000071727De22E5E9d8BAf0edAc6f37da032",
    ],
}
