# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/interchain_accounts/host/v1/host.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7ibc/applications/interchain_accounts/host/v1/host.proto\x12,ibc.applications.interchain_accounts.host.v1\x1a\x14gogoproto/gogo.proto\"j\n\x06Params\x12-\n\x0chost_enabled\x18\x01 \x01(\x08\x42\x17\xf2\xde\x1f\x13yaml:\"host_enabled\"\x12\x31\n\x0e\x61llow_messages\x18\x02 \x03(\tB\x19\xf2\xde\x1f\x15yaml:\"allow_messages\"BLZJgithub.com/cosmos/ibc-go/v6/modules/apps/27-interchain-accounts/host/typesb\x06proto3')



_PARAMS = DESCRIPTOR.message_types_by_name['Params']
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'ibc.applications.interchain_accounts.host.v1.host_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.interchain_accounts.host.v1.Params)
  })
_sym_db.RegisterMessage(Params)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZJgithub.com/cosmos/ibc-go/v6/modules/apps/27-interchain-accounts/host/types'
  _PARAMS.fields_by_name['host_enabled']._options = None
  _PARAMS.fields_by_name['host_enabled']._serialized_options = b'\362\336\037\023yaml:\"host_enabled\"'
  _PARAMS.fields_by_name['allow_messages']._options = None
  _PARAMS.fields_by_name['allow_messages']._serialized_options = b'\362\336\037\025yaml:\"allow_messages\"'
  _PARAMS._serialized_start=127
  _PARAMS._serialized_end=233
# @@protoc_insertion_point(module_scope)
