# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crypto/multisig/keys.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cosmos/crypto/multisig/keys.proto\x12\x16\x63osmos.crypto.multisig\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\"d\n\x11LegacyAminoPubKey\x12\x11\n\tthreshold\x18\x01 \x01(\r\x12\x36\n\x0bpublic_keys\x18\x02 \x03(\x0b\x32\x14.google.protobuf.AnyB\x0b\xe2\xde\x1f\x07PubKeys:\x04\x88\xa0\x1f\x00\x42\x33Z1github.com/cosmos/cosmos-sdk/crypto/keys/multisigb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crypto.multisig.keys_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/crypto/keys/multisig'
  _LEGACYAMINOPUBKEY.fields_by_name['public_keys']._options = None
  _LEGACYAMINOPUBKEY.fields_by_name['public_keys']._serialized_options = b'\342\336\037\007PubKeys'
  _LEGACYAMINOPUBKEY._options = None
  _LEGACYAMINOPUBKEY._serialized_options = b'\210\240\037\000'
  _globals['_LEGACYAMINOPUBKEY']._serialized_start=110
  _globals['_LEGACYAMINOPUBKEY']._serialized_end=210
# @@protoc_insertion_point(module_scope)
