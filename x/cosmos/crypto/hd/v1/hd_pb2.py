# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crypto/hd/v1/hd.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63osmos/crypto/hd/v1/hd.proto\x12\x13\x63osmos.crypto.hd.v1\x1a\x14gogoproto/gogo.proto\"o\n\x0b\x42IP44Params\x12\x0f\n\x07purpose\x18\x01 \x01(\r\x12\x11\n\tcoin_type\x18\x02 \x01(\r\x12\x0f\n\x07\x61\x63\x63ount\x18\x03 \x01(\r\x12\x0e\n\x06\x63hange\x18\x04 \x01(\x08\x12\x15\n\raddress_index\x18\x05 \x01(\r:\x04\x98\xa0\x1f\x00\x42,Z&github.com/cosmos/cosmos-sdk/crypto/hd\xc8\xe1\x1e\x00\x62\x06proto3')



_BIP44PARAMS = DESCRIPTOR.message_types_by_name['BIP44Params']
BIP44Params = _reflection.GeneratedProtocolMessageType('BIP44Params', (_message.Message,), {
  'DESCRIPTOR' : _BIP44PARAMS,
  '__module__' : 'cosmos.crypto.hd.v1.hd_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.crypto.hd.v1.BIP44Params)
  })
_sym_db.RegisterMessage(BIP44Params)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/cosmos/cosmos-sdk/crypto/hd\310\341\036\000'
  _BIP44PARAMS._options = None
  _BIP44PARAMS._serialized_options = b'\230\240\037\000'
  _BIP44PARAMS._serialized_start=75
  _BIP44PARAMS._serialized_end=186
# @@protoc_insertion_point(module_scope)
