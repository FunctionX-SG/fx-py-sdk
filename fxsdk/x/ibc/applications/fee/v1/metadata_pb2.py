# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/fee/v1/metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&ibc/applications/fee/v1/metadata.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto\"d\n\x08Metadata\x12+\n\x0b\x66\x65\x65_version\x18\x01 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"fee_version\"\x12+\n\x0b\x61pp_version\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"app_version\"B7Z5github.com/cosmos/ibc-go/v6/modules/apps/29-fee/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.fee.v1.metadata_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z5github.com/cosmos/ibc-go/v6/modules/apps/29-fee/types'
  _METADATA.fields_by_name['fee_version']._options = None
  _METADATA.fields_by_name['fee_version']._serialized_options = b'\362\336\037\022yaml:\"fee_version\"'
  _METADATA.fields_by_name['app_version']._options = None
  _METADATA.fields_by_name['app_version']._serialized_options = b'\362\336\037\022yaml:\"app_version\"'
  _globals['_METADATA']._serialized_start=89
  _globals['_METADATA']._serialized_end=189
# @@protoc_insertion_point(module_scope)
