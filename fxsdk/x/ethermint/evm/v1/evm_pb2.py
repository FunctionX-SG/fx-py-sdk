# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethermint/evm/v1/evm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x65thermint/evm/v1/evm.proto\x12\x10\x65thermint.evm.v1\x1a\x14gogoproto/gogo.proto\"\xb8\x02\n\x06Params\x12\'\n\tevm_denom\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"evm_denom\"\x12/\n\renable_create\x18\x02 \x01(\x08\x42\x18\xf2\xde\x1f\x14yaml:\"enable_create\"\x12+\n\x0b\x65nable_call\x18\x03 \x01(\x08\x42\x16\xf2\xde\x1f\x12yaml:\"enable_call\"\x12\x36\n\nextra_eips\x18\x04 \x03(\x03\x42\"\xe2\xde\x1f\tExtraEIPs\xf2\xde\x1f\x11yaml:\"extra_eips\"\x12P\n\x0c\x63hain_config\x18\x05 \x01(\x0b\x32\x1d.ethermint.evm.v1.ChainConfigB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:\"chain_config\"\x12\x1d\n\x15\x61llow_unprotected_txs\x18\x06 \x01(\x08\"\xf7\x0e\n\x0b\x43hainConfig\x12]\n\x0fhomestead_block\x18\x01 \x01(\tBD\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:\"homestead_block\"\x12k\n\x0e\x64\x61o_fork_block\x18\x02 \x01(\tBS\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x0c\x44\x41OForkBlock\xf2\xde\x1f\x15yaml:\"dao_fork_block\"\x12G\n\x10\x64\x61o_fork_support\x18\x03 \x01(\x08\x42-\xe2\xde\x1f\x0e\x44\x41OForkSupport\xf2\xde\x1f\x17yaml:\"dao_fork_support\"\x12\x66\n\x0c\x65ip150_block\x18\x04 \x01(\tBP\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x0b\x45IP150Block\xf2\xde\x1f\x13yaml:\"eip150_block\"\x12=\n\x0b\x65ip150_hash\x18\x05 \x01(\tB(\xe2\xde\x1f\nEIP150Hash\xf2\xde\x1f\x16yaml:\"byzantium_block\"\x12\x66\n\x0c\x65ip155_block\x18\x06 \x01(\tBP\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x0b\x45IP155Block\xf2\xde\x1f\x13yaml:\"eip155_block\"\x12\x66\n\x0c\x65ip158_block\x18\x07 \x01(\tBP\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x0b\x45IP158Block\xf2\xde\x1f\x13yaml:\"eip158_block\"\x12]\n\x0f\x62yzantium_block\x18\x08 \x01(\tBD\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:\"byzantium_block\"\x12g\n\x14\x63onstantinople_block\x18\t \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1byaml:\"constantinople_block\"\x12_\n\x10petersburg_block\x18\n \x01(\tBE\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x17yaml:\"petersburg_block\"\x12[\n\x0eistanbul_block\x18\x0b \x01(\tBC\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x15yaml:\"istanbul_block\"\x12\x63\n\x12muir_glacier_block\x18\x0c \x01(\tBG\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x19yaml:\"muir_glacier_block\"\x12W\n\x0c\x62\x65rlin_block\x18\r \x01(\tBA\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x13yaml:\"berlin_block\"\x12W\n\x0clondon_block\x18\x11 \x01(\tBA\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x13yaml:\"london_block\"\x12\x65\n\x13\x61rrow_glacier_block\x18\x12 \x01(\tBH\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:\"arrow_glacier_block\"\x12\x63\n\x12gray_glacier_block\x18\x14 \x01(\tBG\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x19yaml:\"gray_glacier_block\"\x12g\n\x14merge_netsplit_block\x18\x15 \x01(\tBI\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1byaml:\"merge_netsplit_block\"\x12[\n\x0eshanghai_block\x18\x16 \x01(\tBC\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x15yaml:\"shanghai_block\"\x12W\n\x0c\x63\x61ncun_block\x18\x17 \x01(\tBA\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x13yaml:\"cancun_block\"J\x04\x08\x0e\x10\x0fJ\x04\x08\x0f\x10\x10J\x04\x08\x10\x10\x11J\x04\x08\x13\x10\x14R\ryolo_v3_blockR\x0b\x65wasm_blockR\x0e\x63\x61talyst_blockR\x10merge_fork_block\"#\n\x05State\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"D\n\x0fTransactionLogs\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12#\n\x04logs\x18\x02 \x03(\x0b\x32\x15.ethermint.evm.v1.Log\"\xfa\x01\n\x03Log\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0e\n\x06topics\x18\x02 \x03(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12%\n\x0c\x62lock_number\x18\x04 \x01(\x04\x42\x0f\xea\xde\x1f\x0b\x62lockNumber\x12$\n\x07tx_hash\x18\x05 \x01(\tB\x13\xea\xde\x1f\x0ftransactionHash\x12&\n\x08tx_index\x18\x06 \x01(\x04\x42\x14\xea\xde\x1f\x10transactionIndex\x12!\n\nblock_hash\x18\x07 \x01(\tB\r\xea\xde\x1f\tblockHash\x12\x1b\n\x05index\x18\x08 \x01(\x04\x42\x0c\xea\xde\x1f\x08logIndex\x12\x0f\n\x07removed\x18\t \x01(\x08\"\xd3\x01\n\x08TxResult\x12\x35\n\x10\x63ontract_address\x18\x01 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:\"contract_address\"\x12\r\n\x05\x62loom\x18\x02 \x01(\x0c\x12J\n\x07tx_logs\x18\x03 \x01(\x0b\x32!.ethermint.evm.v1.TransactionLogsB\x16\xc8\xde\x1f\x00\xf2\xde\x1f\x0eyaml:\"tx_logs\"\x12\x0b\n\x03ret\x18\x04 \x01(\x0c\x12\x10\n\x08reverted\x18\x05 \x01(\x08\x12\x10\n\x08gas_used\x18\x06 \x01(\x04:\x04\x88\xa0\x1f\x00\"K\n\x0b\x41\x63\x63\x65ssTuple\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12%\n\x0cstorage_keys\x18\x02 \x03(\tB\x0f\xea\xde\x1f\x0bstorageKeys:\x04\x88\xa0\x1f\x00\"\x9e\x03\n\x0bTraceConfig\x12\x0e\n\x06tracer\x18\x01 \x01(\t\x12\x0f\n\x07timeout\x18\x02 \x01(\t\x12\x0e\n\x06reexec\x18\x03 \x01(\x04\x12\'\n\rdisable_stack\x18\x05 \x01(\x08\x42\x10\xea\xde\x1f\x0c\x64isableStack\x12+\n\x0f\x64isable_storage\x18\x06 \x01(\x08\x42\x12\xea\xde\x1f\x0e\x64isableStorage\x12\r\n\x05\x64\x65\x62ug\x18\x08 \x01(\x08\x12\r\n\x05limit\x18\t \x01(\x05\x12\x30\n\toverrides\x18\n \x01(\x0b\x32\x1d.ethermint.evm.v1.ChainConfig\x12\'\n\renable_memory\x18\x0b \x01(\x08\x42\x10\xea\xde\x1f\x0c\x65nableMemory\x12\x30\n\x12\x65nable_return_data\x18\x0c \x01(\x08\x42\x14\xea\xde\x1f\x10\x65nableReturnData\x12,\n\x12tracer_json_config\x18\r \x01(\tB\x10\xea\xde\x1f\x0ctracerConfigJ\x04\x08\x04\x10\x05J\x04\x08\x07\x10\x08R\x0e\x64isable_memoryR\x13\x64isable_return_dataB(Z&github.com/evmos/ethermint/x/evm/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.evm.v1.evm_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/evmos/ethermint/x/evm/types'
  _PARAMS.fields_by_name['evm_denom']._options = None
  _PARAMS.fields_by_name['evm_denom']._serialized_options = b'\362\336\037\020yaml:\"evm_denom\"'
  _PARAMS.fields_by_name['enable_create']._options = None
  _PARAMS.fields_by_name['enable_create']._serialized_options = b'\362\336\037\024yaml:\"enable_create\"'
  _PARAMS.fields_by_name['enable_call']._options = None
  _PARAMS.fields_by_name['enable_call']._serialized_options = b'\362\336\037\022yaml:\"enable_call\"'
  _PARAMS.fields_by_name['extra_eips']._options = None
  _PARAMS.fields_by_name['extra_eips']._serialized_options = b'\342\336\037\tExtraEIPs\362\336\037\021yaml:\"extra_eips\"'
  _PARAMS.fields_by_name['chain_config']._options = None
  _PARAMS.fields_by_name['chain_config']._serialized_options = b'\310\336\037\000\362\336\037\023yaml:\"chain_config\"'
  _CHAINCONFIG.fields_by_name['homestead_block']._options = None
  _CHAINCONFIG.fields_by_name['homestead_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\026yaml:\"homestead_block\"'
  _CHAINCONFIG.fields_by_name['dao_fork_block']._options = None
  _CHAINCONFIG.fields_by_name['dao_fork_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\342\336\037\014DAOForkBlock\362\336\037\025yaml:\"dao_fork_block\"'
  _CHAINCONFIG.fields_by_name['dao_fork_support']._options = None
  _CHAINCONFIG.fields_by_name['dao_fork_support']._serialized_options = b'\342\336\037\016DAOForkSupport\362\336\037\027yaml:\"dao_fork_support\"'
  _CHAINCONFIG.fields_by_name['eip150_block']._options = None
  _CHAINCONFIG.fields_by_name['eip150_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\342\336\037\013EIP150Block\362\336\037\023yaml:\"eip150_block\"'
  _CHAINCONFIG.fields_by_name['eip150_hash']._options = None
  _CHAINCONFIG.fields_by_name['eip150_hash']._serialized_options = b'\342\336\037\nEIP150Hash\362\336\037\026yaml:\"byzantium_block\"'
  _CHAINCONFIG.fields_by_name['eip155_block']._options = None
  _CHAINCONFIG.fields_by_name['eip155_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\342\336\037\013EIP155Block\362\336\037\023yaml:\"eip155_block\"'
  _CHAINCONFIG.fields_by_name['eip158_block']._options = None
  _CHAINCONFIG.fields_by_name['eip158_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\342\336\037\013EIP158Block\362\336\037\023yaml:\"eip158_block\"'
  _CHAINCONFIG.fields_by_name['byzantium_block']._options = None
  _CHAINCONFIG.fields_by_name['byzantium_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\026yaml:\"byzantium_block\"'
  _CHAINCONFIG.fields_by_name['constantinople_block']._options = None
  _CHAINCONFIG.fields_by_name['constantinople_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\033yaml:\"constantinople_block\"'
  _CHAINCONFIG.fields_by_name['petersburg_block']._options = None
  _CHAINCONFIG.fields_by_name['petersburg_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\027yaml:\"petersburg_block\"'
  _CHAINCONFIG.fields_by_name['istanbul_block']._options = None
  _CHAINCONFIG.fields_by_name['istanbul_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\025yaml:\"istanbul_block\"'
  _CHAINCONFIG.fields_by_name['muir_glacier_block']._options = None
  _CHAINCONFIG.fields_by_name['muir_glacier_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\031yaml:\"muir_glacier_block\"'
  _CHAINCONFIG.fields_by_name['berlin_block']._options = None
  _CHAINCONFIG.fields_by_name['berlin_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\023yaml:\"berlin_block\"'
  _CHAINCONFIG.fields_by_name['london_block']._options = None
  _CHAINCONFIG.fields_by_name['london_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\023yaml:\"london_block\"'
  _CHAINCONFIG.fields_by_name['arrow_glacier_block']._options = None
  _CHAINCONFIG.fields_by_name['arrow_glacier_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\032yaml:\"arrow_glacier_block\"'
  _CHAINCONFIG.fields_by_name['gray_glacier_block']._options = None
  _CHAINCONFIG.fields_by_name['gray_glacier_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\031yaml:\"gray_glacier_block\"'
  _CHAINCONFIG.fields_by_name['merge_netsplit_block']._options = None
  _CHAINCONFIG.fields_by_name['merge_netsplit_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\033yaml:\"merge_netsplit_block\"'
  _CHAINCONFIG.fields_by_name['shanghai_block']._options = None
  _CHAINCONFIG.fields_by_name['shanghai_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\025yaml:\"shanghai_block\"'
  _CHAINCONFIG.fields_by_name['cancun_block']._options = None
  _CHAINCONFIG.fields_by_name['cancun_block']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\362\336\037\023yaml:\"cancun_block\"'
  _LOG.fields_by_name['block_number']._options = None
  _LOG.fields_by_name['block_number']._serialized_options = b'\352\336\037\013blockNumber'
  _LOG.fields_by_name['tx_hash']._options = None
  _LOG.fields_by_name['tx_hash']._serialized_options = b'\352\336\037\017transactionHash'
  _LOG.fields_by_name['tx_index']._options = None
  _LOG.fields_by_name['tx_index']._serialized_options = b'\352\336\037\020transactionIndex'
  _LOG.fields_by_name['block_hash']._options = None
  _LOG.fields_by_name['block_hash']._serialized_options = b'\352\336\037\tblockHash'
  _LOG.fields_by_name['index']._options = None
  _LOG.fields_by_name['index']._serialized_options = b'\352\336\037\010logIndex'
  _TXRESULT.fields_by_name['contract_address']._options = None
  _TXRESULT.fields_by_name['contract_address']._serialized_options = b'\362\336\037\027yaml:\"contract_address\"'
  _TXRESULT.fields_by_name['tx_logs']._options = None
  _TXRESULT.fields_by_name['tx_logs']._serialized_options = b'\310\336\037\000\362\336\037\016yaml:\"tx_logs\"'
  _TXRESULT._options = None
  _TXRESULT._serialized_options = b'\210\240\037\000'
  _ACCESSTUPLE.fields_by_name['storage_keys']._options = None
  _ACCESSTUPLE.fields_by_name['storage_keys']._serialized_options = b'\352\336\037\013storageKeys'
  _ACCESSTUPLE._options = None
  _ACCESSTUPLE._serialized_options = b'\210\240\037\000'
  _TRACECONFIG.fields_by_name['disable_stack']._options = None
  _TRACECONFIG.fields_by_name['disable_stack']._serialized_options = b'\352\336\037\014disableStack'
  _TRACECONFIG.fields_by_name['disable_storage']._options = None
  _TRACECONFIG.fields_by_name['disable_storage']._serialized_options = b'\352\336\037\016disableStorage'
  _TRACECONFIG.fields_by_name['enable_memory']._options = None
  _TRACECONFIG.fields_by_name['enable_memory']._serialized_options = b'\352\336\037\014enableMemory'
  _TRACECONFIG.fields_by_name['enable_return_data']._options = None
  _TRACECONFIG.fields_by_name['enable_return_data']._serialized_options = b'\352\336\037\020enableReturnData'
  _TRACECONFIG.fields_by_name['tracer_json_config']._options = None
  _TRACECONFIG.fields_by_name['tracer_json_config']._serialized_options = b'\352\336\037\014tracerConfig'
  _globals['_PARAMS']._serialized_start=71
  _globals['_PARAMS']._serialized_end=383
  _globals['_CHAINCONFIG']._serialized_start=386
  _globals['_CHAINCONFIG']._serialized_end=2297
  _globals['_STATE']._serialized_start=2299
  _globals['_STATE']._serialized_end=2334
  _globals['_TRANSACTIONLOGS']._serialized_start=2336
  _globals['_TRANSACTIONLOGS']._serialized_end=2404
  _globals['_LOG']._serialized_start=2407
  _globals['_LOG']._serialized_end=2657
  _globals['_TXRESULT']._serialized_start=2660
  _globals['_TXRESULT']._serialized_end=2871
  _globals['_ACCESSTUPLE']._serialized_start=2873
  _globals['_ACCESSTUPLE']._serialized_end=2948
  _globals['_TRACECONFIG']._serialized_start=2951
  _globals['_TRACECONFIG']._serialized_end=3365
# @@protoc_insertion_point(module_scope)