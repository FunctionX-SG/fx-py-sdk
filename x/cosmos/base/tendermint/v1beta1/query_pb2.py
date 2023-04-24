# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/tendermint/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from x.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from x.tendermint.p2p import types_pb2 as tendermint_dot_p2p_dot_types__pb2
from x.tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from x.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from x.cosmos.base.tendermint.v1beta1 import types_pb2 as cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_types__pb2
from x.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from x.tendermint.types import block_pb2 as tendermint_dot_types_dot_block__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*cosmos/base/tendermint/v1beta1/query.proto\x12\x1e\x63osmos.base.tendermint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1atendermint/p2p/types.proto\x1a\x1ctendermint/types/types.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a*cosmos/base/tendermint/v1beta1/types.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1ctendermint/types/block.proto\"l\n\x1eGetValidatorSetByHeightRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xb3\x01\n\x1fGetValidatorSetByHeightResponse\x12\x14\n\x0c\x62lock_height\x18\x01 \x01(\x03\x12=\n\nvalidators\x18\x02 \x03(\x0b\x32).cosmos.base.tendermint.v1beta1.Validator\x12;\n\npagination\x18\x03 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"Z\n\x1cGetLatestValidatorSetRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xb1\x01\n\x1dGetLatestValidatorSetResponse\x12\x14\n\x0c\x62lock_height\x18\x01 \x01(\x03\x12=\n\nvalidators\x18\x02 \x03(\x0b\x32).cosmos.base.tendermint.v1beta1.Validator\x12;\n\npagination\x18\x03 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x8e\x01\n\tValidator\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12%\n\x07pub_key\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x14\n\x0cvoting_power\x18\x03 \x01(\x03\x12\x19\n\x11proposer_priority\x18\x04 \x01(\x03\")\n\x17GetBlockByHeightRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03\"\xa9\x01\n\x18GetBlockByHeightResponse\x12+\n\x08\x62lock_id\x18\x01 \x01(\x0b\x32\x19.tendermint.types.BlockID\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tendermint.types.Block\x12\x38\n\tsdk_block\x18\x03 \x01(\x0b\x32%.cosmos.base.tendermint.v1beta1.Block\"\x17\n\x15GetLatestBlockRequest\"\xa7\x01\n\x16GetLatestBlockResponse\x12+\n\x08\x62lock_id\x18\x01 \x01(\x0b\x32\x19.tendermint.types.BlockID\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tendermint.types.Block\x12\x38\n\tsdk_block\x18\x03 \x01(\x0b\x32%.cosmos.base.tendermint.v1beta1.Block\"\x13\n\x11GetSyncingRequest\"%\n\x12GetSyncingResponse\x12\x0f\n\x07syncing\x18\x01 \x01(\x08\"\x14\n\x12GetNodeInfoRequest\"\x9b\x01\n\x13GetNodeInfoResponse\x12:\n\x11\x64\x65\x66\x61ult_node_info\x18\x01 \x01(\x0b\x32\x1f.tendermint.p2p.DefaultNodeInfo\x12H\n\x13\x61pplication_version\x18\x02 \x01(\x0b\x32+.cosmos.base.tendermint.v1beta1.VersionInfo\"\xd2\x01\n\x0bVersionInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x61pp_name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x12\n\ngit_commit\x18\x04 \x01(\t\x12\x12\n\nbuild_tags\x18\x05 \x01(\t\x12\x12\n\ngo_version\x18\x06 \x01(\t\x12:\n\nbuild_deps\x18\x07 \x03(\x0b\x32&.cosmos.base.tendermint.v1beta1.Module\x12\x1a\n\x12\x63osmos_sdk_version\x18\x08 \x01(\t\"4\n\x06Module\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0b\n\x03sum\x18\x03 \x01(\t\"M\n\x10\x41\x42\x43IQueryRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\r\n\x05prove\x18\x04 \x01(\x08\"\xcd\x01\n\x11\x41\x42\x43IQueryResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0b\n\x03log\x18\x03 \x01(\t\x12\x0c\n\x04info\x18\x04 \x01(\t\x12\r\n\x05index\x18\x05 \x01(\x03\x12\x0b\n\x03key\x18\x06 \x01(\x0c\x12\r\n\x05value\x18\x07 \x01(\x0c\x12;\n\tproof_ops\x18\x08 \x01(\x0b\x32(.cosmos.base.tendermint.v1beta1.ProofOps\x12\x0e\n\x06height\x18\t \x01(\x03\x12\x11\n\tcodespace\x18\n \x01(\tJ\x04\x08\x02\x10\x03\"2\n\x07ProofOp\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"F\n\x08ProofOps\x12:\n\x03ops\x18\x01 \x03(\x0b\x32\'.cosmos.base.tendermint.v1beta1.ProofOpB\x04\xc8\xde\x1f\x00\x32\xaf\n\n\x07Service\x12\xa9\x01\n\x0bGetNodeInfo\x12\x32.cosmos.base.tendermint.v1beta1.GetNodeInfoRequest\x1a\x33.cosmos.base.tendermint.v1beta1.GetNodeInfoResponse\"1\x82\xd3\xe4\x93\x02+\x12)/cosmos/base/tendermint/v1beta1/node_info\x12\xa4\x01\n\nGetSyncing\x12\x31.cosmos.base.tendermint.v1beta1.GetSyncingRequest\x1a\x32.cosmos.base.tendermint.v1beta1.GetSyncingResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/base/tendermint/v1beta1/syncing\x12\xb6\x01\n\x0eGetLatestBlock\x12\x35.cosmos.base.tendermint.v1beta1.GetLatestBlockRequest\x1a\x36.cosmos.base.tendermint.v1beta1.GetLatestBlockResponse\"5\x82\xd3\xe4\x93\x02/\x12-/cosmos/base/tendermint/v1beta1/blocks/latest\x12\xbe\x01\n\x10GetBlockByHeight\x12\x37.cosmos.base.tendermint.v1beta1.GetBlockByHeightRequest\x1a\x38.cosmos.base.tendermint.v1beta1.GetBlockByHeightResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//cosmos/base/tendermint/v1beta1/blocks/{height}\x12\xd2\x01\n\x15GetLatestValidatorSet\x12<.cosmos.base.tendermint.v1beta1.GetLatestValidatorSetRequest\x1a=.cosmos.base.tendermint.v1beta1.GetLatestValidatorSetResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/cosmos/base/tendermint/v1beta1/validatorsets/latest\x12\xda\x01\n\x17GetValidatorSetByHeight\x12>.cosmos.base.tendermint.v1beta1.GetValidatorSetByHeightRequest\x1a?.cosmos.base.tendermint.v1beta1.GetValidatorSetByHeightResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/cosmos/base/tendermint/v1beta1/validatorsets/{height}\x12\xa4\x01\n\tABCIQuery\x12\x30.cosmos.base.tendermint.v1beta1.ABCIQueryRequest\x1a\x31.cosmos.base.tendermint.v1beta1.ABCIQueryResponse\"2\x82\xd3\xe4\x93\x02,\x12*/cosmos/base/tendermint/v1beta1/abci_queryB4Z2github.com/cosmos/cosmos-sdk/client/grpc/tmserviceb\x06proto3')



_GETVALIDATORSETBYHEIGHTREQUEST = DESCRIPTOR.message_types_by_name['GetValidatorSetByHeightRequest']
_GETVALIDATORSETBYHEIGHTRESPONSE = DESCRIPTOR.message_types_by_name['GetValidatorSetByHeightResponse']
_GETLATESTVALIDATORSETREQUEST = DESCRIPTOR.message_types_by_name['GetLatestValidatorSetRequest']
_GETLATESTVALIDATORSETRESPONSE = DESCRIPTOR.message_types_by_name['GetLatestValidatorSetResponse']
_VALIDATOR = DESCRIPTOR.message_types_by_name['Validator']
_GETBLOCKBYHEIGHTREQUEST = DESCRIPTOR.message_types_by_name['GetBlockByHeightRequest']
_GETBLOCKBYHEIGHTRESPONSE = DESCRIPTOR.message_types_by_name['GetBlockByHeightResponse']
_GETLATESTBLOCKREQUEST = DESCRIPTOR.message_types_by_name['GetLatestBlockRequest']
_GETLATESTBLOCKRESPONSE = DESCRIPTOR.message_types_by_name['GetLatestBlockResponse']
_GETSYNCINGREQUEST = DESCRIPTOR.message_types_by_name['GetSyncingRequest']
_GETSYNCINGRESPONSE = DESCRIPTOR.message_types_by_name['GetSyncingResponse']
_GETNODEINFOREQUEST = DESCRIPTOR.message_types_by_name['GetNodeInfoRequest']
_GETNODEINFORESPONSE = DESCRIPTOR.message_types_by_name['GetNodeInfoResponse']
_VERSIONINFO = DESCRIPTOR.message_types_by_name['VersionInfo']
_MODULE = DESCRIPTOR.message_types_by_name['Module']
_ABCIQUERYREQUEST = DESCRIPTOR.message_types_by_name['ABCIQueryRequest']
_ABCIQUERYRESPONSE = DESCRIPTOR.message_types_by_name['ABCIQueryResponse']
_PROOFOP = DESCRIPTOR.message_types_by_name['ProofOp']
_PROOFOPS = DESCRIPTOR.message_types_by_name['ProofOps']
GetValidatorSetByHeightRequest = _reflection.GeneratedProtocolMessageType('GetValidatorSetByHeightRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVALIDATORSETBYHEIGHTREQUEST,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.GetValidatorSetByHeightRequest)
  })
_sym_db.RegisterMessage(GetValidatorSetByHeightRequest)

GetValidatorSetByHeightResponse = _reflection.GeneratedProtocolMessageType('GetValidatorSetByHeightResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETVALIDATORSETBYHEIGHTRESPONSE,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.GetValidatorSetByHeightResponse)
  })
_sym_db.RegisterMessage(GetValidatorSetByHeightResponse)

GetLatestValidatorSetRequest = _reflection.GeneratedProtocolMessageType('GetLatestValidatorSetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLATESTVALIDATORSETREQUEST,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.GetLatestValidatorSetRequest)
  })
_sym_db.RegisterMessage(GetLatestValidatorSetRequest)

GetLatestValidatorSetResponse = _reflection.GeneratedProtocolMessageType('GetLatestValidatorSetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLATESTVALIDATORSETRESPONSE,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.GetLatestValidatorSetResponse)
  })
_sym_db.RegisterMessage(GetLatestValidatorSetResponse)

Validator = _reflection.GeneratedProtocolMessageType('Validator', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATOR,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.Validator)
  })
_sym_db.RegisterMessage(Validator)

GetBlockByHeightRequest = _reflection.GeneratedProtocolMessageType('GetBlockByHeightRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKBYHEIGHTREQUEST,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.GetBlockByHeightRequest)
  })
_sym_db.RegisterMessage(GetBlockByHeightRequest)

GetBlockByHeightResponse = _reflection.GeneratedProtocolMessageType('GetBlockByHeightResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKBYHEIGHTRESPONSE,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.GetBlockByHeightResponse)
  })
_sym_db.RegisterMessage(GetBlockByHeightResponse)

GetLatestBlockRequest = _reflection.GeneratedProtocolMessageType('GetLatestBlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLATESTBLOCKREQUEST,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.GetLatestBlockRequest)
  })
_sym_db.RegisterMessage(GetLatestBlockRequest)

GetLatestBlockResponse = _reflection.GeneratedProtocolMessageType('GetLatestBlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLATESTBLOCKRESPONSE,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.GetLatestBlockResponse)
  })
_sym_db.RegisterMessage(GetLatestBlockResponse)

GetSyncingRequest = _reflection.GeneratedProtocolMessageType('GetSyncingRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSYNCINGREQUEST,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.GetSyncingRequest)
  })
_sym_db.RegisterMessage(GetSyncingRequest)

GetSyncingResponse = _reflection.GeneratedProtocolMessageType('GetSyncingResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSYNCINGRESPONSE,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.GetSyncingResponse)
  })
_sym_db.RegisterMessage(GetSyncingResponse)

GetNodeInfoRequest = _reflection.GeneratedProtocolMessageType('GetNodeInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNODEINFOREQUEST,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.GetNodeInfoRequest)
  })
_sym_db.RegisterMessage(GetNodeInfoRequest)

GetNodeInfoResponse = _reflection.GeneratedProtocolMessageType('GetNodeInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETNODEINFORESPONSE,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.GetNodeInfoResponse)
  })
_sym_db.RegisterMessage(GetNodeInfoResponse)

VersionInfo = _reflection.GeneratedProtocolMessageType('VersionInfo', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONINFO,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.VersionInfo)
  })
_sym_db.RegisterMessage(VersionInfo)

Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), {
  'DESCRIPTOR' : _MODULE,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.Module)
  })
_sym_db.RegisterMessage(Module)

ABCIQueryRequest = _reflection.GeneratedProtocolMessageType('ABCIQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _ABCIQUERYREQUEST,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.ABCIQueryRequest)
  })
_sym_db.RegisterMessage(ABCIQueryRequest)

ABCIQueryResponse = _reflection.GeneratedProtocolMessageType('ABCIQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _ABCIQUERYRESPONSE,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.ABCIQueryResponse)
  })
_sym_db.RegisterMessage(ABCIQueryResponse)

ProofOp = _reflection.GeneratedProtocolMessageType('ProofOp', (_message.Message,), {
  'DESCRIPTOR' : _PROOFOP,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.ProofOp)
  })
_sym_db.RegisterMessage(ProofOp)

ProofOps = _reflection.GeneratedProtocolMessageType('ProofOps', (_message.Message,), {
  'DESCRIPTOR' : _PROOFOPS,
  '__module__' : 'cosmos.base.tendermint.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.tendermint.v1beta1.ProofOps)
  })
_sym_db.RegisterMessage(ProofOps)

_SERVICE = DESCRIPTOR.services_by_name['Service']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/cosmos/cosmos-sdk/client/grpc/tmservice'
  _VALIDATOR.fields_by_name['address']._options = None
  _VALIDATOR.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _PROOFOPS.fields_by_name['ops']._options = None
  _PROOFOPS.fields_by_name['ops']._serialized_options = b'\310\336\037\000'
  _SERVICE.methods_by_name['GetNodeInfo']._options = None
  _SERVICE.methods_by_name['GetNodeInfo']._serialized_options = b'\202\323\344\223\002+\022)/cosmos/base/tendermint/v1beta1/node_info'
  _SERVICE.methods_by_name['GetSyncing']._options = None
  _SERVICE.methods_by_name['GetSyncing']._serialized_options = b'\202\323\344\223\002)\022\'/cosmos/base/tendermint/v1beta1/syncing'
  _SERVICE.methods_by_name['GetLatestBlock']._options = None
  _SERVICE.methods_by_name['GetLatestBlock']._serialized_options = b'\202\323\344\223\002/\022-/cosmos/base/tendermint/v1beta1/blocks/latest'
  _SERVICE.methods_by_name['GetBlockByHeight']._options = None
  _SERVICE.methods_by_name['GetBlockByHeight']._serialized_options = b'\202\323\344\223\0021\022//cosmos/base/tendermint/v1beta1/blocks/{height}'
  _SERVICE.methods_by_name['GetLatestValidatorSet']._options = None
  _SERVICE.methods_by_name['GetLatestValidatorSet']._serialized_options = b'\202\323\344\223\0026\0224/cosmos/base/tendermint/v1beta1/validatorsets/latest'
  _SERVICE.methods_by_name['GetValidatorSetByHeight']._options = None
  _SERVICE.methods_by_name['GetValidatorSetByHeight']._serialized_options = b'\202\323\344\223\0028\0226/cosmos/base/tendermint/v1beta1/validatorsets/{height}'
  _SERVICE.methods_by_name['ABCIQuery']._options = None
  _SERVICE.methods_by_name['ABCIQuery']._serialized_options = b'\202\323\344\223\002,\022*/cosmos/base/tendermint/v1beta1/abci_query'
  _GETVALIDATORSETBYHEIGHTREQUEST._serialized_start=360
  _GETVALIDATORSETBYHEIGHTREQUEST._serialized_end=468
  _GETVALIDATORSETBYHEIGHTRESPONSE._serialized_start=471
  _GETVALIDATORSETBYHEIGHTRESPONSE._serialized_end=650
  _GETLATESTVALIDATORSETREQUEST._serialized_start=652
  _GETLATESTVALIDATORSETREQUEST._serialized_end=742
  _GETLATESTVALIDATORSETRESPONSE._serialized_start=745
  _GETLATESTVALIDATORSETRESPONSE._serialized_end=922
  _VALIDATOR._serialized_start=925
  _VALIDATOR._serialized_end=1067
  _GETBLOCKBYHEIGHTREQUEST._serialized_start=1069
  _GETBLOCKBYHEIGHTREQUEST._serialized_end=1110
  _GETBLOCKBYHEIGHTRESPONSE._serialized_start=1113
  _GETBLOCKBYHEIGHTRESPONSE._serialized_end=1282
  _GETLATESTBLOCKREQUEST._serialized_start=1284
  _GETLATESTBLOCKREQUEST._serialized_end=1307
  _GETLATESTBLOCKRESPONSE._serialized_start=1310
  _GETLATESTBLOCKRESPONSE._serialized_end=1477
  _GETSYNCINGREQUEST._serialized_start=1479
  _GETSYNCINGREQUEST._serialized_end=1498
  _GETSYNCINGRESPONSE._serialized_start=1500
  _GETSYNCINGRESPONSE._serialized_end=1537
  _GETNODEINFOREQUEST._serialized_start=1539
  _GETNODEINFOREQUEST._serialized_end=1559
  _GETNODEINFORESPONSE._serialized_start=1562
  _GETNODEINFORESPONSE._serialized_end=1717
  _VERSIONINFO._serialized_start=1720
  _VERSIONINFO._serialized_end=1930
  _MODULE._serialized_start=1932
  _MODULE._serialized_end=1984
  _ABCIQUERYREQUEST._serialized_start=1986
  _ABCIQUERYREQUEST._serialized_end=2063
  _ABCIQUERYRESPONSE._serialized_start=2066
  _ABCIQUERYRESPONSE._serialized_end=2271
  _PROOFOP._serialized_start=2273
  _PROOFOP._serialized_end=2323
  _PROOFOPS._serialized_start=2325
  _PROOFOPS._serialized_end=2395
  _SERVICE._serialized_start=2398
  _SERVICE._serialized_end=3725
# @@protoc_insertion_point(module_scope)
