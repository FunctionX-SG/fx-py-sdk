# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/authz/v1beta1/authz.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxpysdk.fxsdk.x.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/authz/v1beta1/authz.proto\x12\x14\x63osmos.authz.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\"6\n\x14GenericAuthorization\x12\x0b\n\x03msg\x18\x01 \x01(\t:\x11\xca\xb4-\rAuthorization\"\x81\x01\n\x05Grant\x12>\n\rauthorization\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x11\xca\xb4-\rAuthorization\x12\x38\n\nexpiration\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x01\x90\xdf\x1f\x01\"\xe0\x01\n\x12GrantAuthorization\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12>\n\rauthorization\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyB\x11\xca\xb4-\rAuthorization\x12\x34\n\nexpiration\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\"\'\n\x0eGrantQueueItem\x12\x15\n\rmsg_type_urls\x18\x01 \x03(\tB*Z$github.com/cosmos/cosmos-sdk/x/authz\xc8\xe1\x1e\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.authz.v1beta1.authz_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/authz\310\341\036\000'
  _GENERICAUTHORIZATION._options = None
  _GENERICAUTHORIZATION._serialized_options = b'\312\264-\rAuthorization'
  _GRANT.fields_by_name['authorization']._options = None
  _GRANT.fields_by_name['authorization']._serialized_options = b'\312\264-\rAuthorization'
  _GRANT.fields_by_name['expiration']._options = None
  _GRANT.fields_by_name['expiration']._serialized_options = b'\310\336\037\001\220\337\037\001'
  _GRANTAUTHORIZATION.fields_by_name['granter']._options = None
  _GRANTAUTHORIZATION.fields_by_name['granter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _GRANTAUTHORIZATION.fields_by_name['grantee']._options = None
  _GRANTAUTHORIZATION.fields_by_name['grantee']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _GRANTAUTHORIZATION.fields_by_name['authorization']._options = None
  _GRANTAUTHORIZATION.fields_by_name['authorization']._serialized_options = b'\312\264-\rAuthorization'
  _GRANTAUTHORIZATION.fields_by_name['expiration']._options = None
  _GRANTAUTHORIZATION.fields_by_name['expiration']._serialized_options = b'\220\337\037\001'
  _globals['_GENERICAUTHORIZATION']._serialized_start=167
  _globals['_GENERICAUTHORIZATION']._serialized_end=221
  _globals['_GRANT']._serialized_start=224
  _globals['_GRANT']._serialized_end=353
  _globals['_GRANTAUTHORIZATION']._serialized_start=356
  _globals['_GRANTAUTHORIZATION']._serialized_end=580
  _globals['_GRANTQUEUEITEM']._serialized_start=582
  _globals['_GRANTQUEUEITEM']._serialized_end=621
# @@protoc_insertion_point(module_scope)
