# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethermint/types/v1/indexer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n ethermint/types/v1/indexer.proto\x12\x12\x65thermint.types.v1\x1a\x14gogoproto/gogo.proto\"\x9a\x01\n\x08TxResult\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\x10\n\x08tx_index\x18\x02 \x01(\r\x12\x11\n\tmsg_index\x18\x03 \x01(\r\x12\x14\n\x0c\x65th_tx_index\x18\x04 \x01(\x05\x12\x0e\n\x06\x66\x61iled\x18\x05 \x01(\x08\x12\x10\n\x08gas_used\x18\x06 \x01(\x04\x12\x1b\n\x13\x63umulative_gas_used\x18\x07 \x01(\x04:\x04\x88\xa0\x1f\x00\x42\"Z github.com/evmos/ethermint/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.types.v1.indexer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z github.com/evmos/ethermint/types'
  _TXRESULT._options = None
  _TXRESULT._serialized_options = b'\210\240\037\000'
  _globals['_TXRESULT']._serialized_start=79
  _globals['_TXRESULT']._serialized_end=233
# @@protoc_insertion_point(module_scope)
