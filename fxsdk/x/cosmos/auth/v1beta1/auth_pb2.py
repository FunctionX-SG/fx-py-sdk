# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/auth/v1beta1/auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63osmos/auth/v1beta1/auth.proto\x12\x13\x63osmos.auth.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\"\xbd\x01\n\x0b\x42\x61seAccount\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12?\n\x07pub_key\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\x18\xea\xde\x1f\x14public_key,omitempty\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x03 \x01(\x04\x12\x10\n\x08sequence\x18\x04 \x01(\x04:\x18\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x08\x41\x63\x63ountI\"\x8c\x01\n\rModuleAccount\x12<\n\x0c\x62\x61se_account\x18\x01 \x01(\x0b\x32 .cosmos.auth.v1beta1.BaseAccountB\x04\xd0\xde\x1f\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bpermissions\x18\x03 \x03(\t:\x1a\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x0eModuleAccountI\"\xde\x01\n\x06Params\x12\x1b\n\x13max_memo_characters\x18\x01 \x01(\x04\x12\x14\n\x0ctx_sig_limit\x18\x02 \x01(\x04\x12\x1d\n\x15tx_size_cost_per_byte\x18\x03 \x01(\x04\x12\x39\n\x17sig_verify_cost_ed25519\x18\x04 \x01(\x04\x42\x18\xe2\xde\x1f\x14SigVerifyCostED25519\x12=\n\x19sig_verify_cost_secp256k1\x18\x05 \x01(\x04\x42\x1a\xe2\xde\x1f\x16SigVerifyCostSecp256k1:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01\x42+Z)github.com/cosmos/cosmos-sdk/x/auth/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.auth.v1beta1.auth_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/auth/types'
  _BASEACCOUNT.fields_by_name['address']._options = None
  _BASEACCOUNT.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _BASEACCOUNT.fields_by_name['pub_key']._options = None
  _BASEACCOUNT.fields_by_name['pub_key']._serialized_options = b'\352\336\037\024public_key,omitempty'
  _BASEACCOUNT._options = None
  _BASEACCOUNT._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000\312\264-\010AccountI'
  _MODULEACCOUNT.fields_by_name['base_account']._options = None
  _MODULEACCOUNT.fields_by_name['base_account']._serialized_options = b'\320\336\037\001'
  _MODULEACCOUNT._options = None
  _MODULEACCOUNT._serialized_options = b'\210\240\037\000\230\240\037\000\312\264-\016ModuleAccountI'
  _PARAMS.fields_by_name['sig_verify_cost_ed25519']._options = None
  _PARAMS.fields_by_name['sig_verify_cost_ed25519']._serialized_options = b'\342\336\037\024SigVerifyCostED25519'
  _PARAMS.fields_by_name['sig_verify_cost_secp256k1']._options = None
  _PARAMS.fields_by_name['sig_verify_cost_secp256k1']._serialized_options = b'\342\336\037\026SigVerifyCostSecp256k1'
  _PARAMS._options = None
  _PARAMS._serialized_options = b'\230\240\037\000\350\240\037\001'
  _globals['_BASEACCOUNT']._serialized_start=132
  _globals['_BASEACCOUNT']._serialized_end=321
  _globals['_MODULEACCOUNT']._serialized_start=324
  _globals['_MODULEACCOUNT']._serialized_end=464
  _globals['_PARAMS']._serialized_start=467
  _globals['_PARAMS']._serialized_end=689
# @@protoc_insertion_point(module_scope)
