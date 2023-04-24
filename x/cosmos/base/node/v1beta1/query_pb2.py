# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/node/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from x.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/base/node/v1beta1/query.proto\x12\x18\x63osmos.base.node.v1beta1\x1a\x1cgoogle/api/annotations.proto\"\x0f\n\rConfigRequest\"+\n\x0e\x43onfigResponse\x12\x19\n\x11minimum_gas_price\x18\x01 \x01(\t2\x91\x01\n\x07Service\x12\x85\x01\n\x06\x43onfig\x12\'.cosmos.base.node.v1beta1.ConfigRequest\x1a(.cosmos.base.node.v1beta1.ConfigResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /cosmos/base/node/v1beta1/configB/Z-github.com/cosmos/cosmos-sdk/client/grpc/nodeb\x06proto3')



_CONFIGREQUEST = DESCRIPTOR.message_types_by_name['ConfigRequest']
_CONFIGRESPONSE = DESCRIPTOR.message_types_by_name['ConfigResponse']
ConfigRequest = _reflection.GeneratedProtocolMessageType('ConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGREQUEST,
  '__module__' : 'cosmos.base.node.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.node.v1beta1.ConfigRequest)
  })
_sym_db.RegisterMessage(ConfigRequest)

ConfigResponse = _reflection.GeneratedProtocolMessageType('ConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGRESPONSE,
  '__module__' : 'cosmos.base.node.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.node.v1beta1.ConfigResponse)
  })
_sym_db.RegisterMessage(ConfigResponse)

_SERVICE = DESCRIPTOR.services_by_name['Service']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/client/grpc/node'
  _SERVICE.methods_by_name['Config']._options = None
  _SERVICE.methods_by_name['Config']._serialized_options = b'\202\323\344\223\002\"\022 /cosmos/base/node/v1beta1/config'
  _CONFIGREQUEST._serialized_start=96
  _CONFIGREQUEST._serialized_end=111
  _CONFIGRESPONSE._serialized_start=113
  _CONFIGRESPONSE._serialized_end=156
  _SERVICE._serialized_start=159
  _SERVICE._serialized_end=304
# @@protoc_insertion_point(module_scope)
