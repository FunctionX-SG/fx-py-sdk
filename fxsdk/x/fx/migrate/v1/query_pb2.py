# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/migrate/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxpysdk.fxsdk.x.fx.migrate.v1 import migrate_pb2 as fx_dot_migrate_dot_v1_dot_migrate__pb2
from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x66x/migrate/v1/query.proto\x12\rfx.migrate.v1\x1a\x1b\x66x/migrate/v1/migrate.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\",\n\x19QueryMigrateRecordRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"f\n\x1aQueryMigrateRecordResponse\x12\r\n\x05\x66ound\x18\x01 \x01(\x08\x12\x39\n\rmigrateRecord\x18\x02 \x01(\x0b\x32\x1c.fx.migrate.v1.MigrateRecordB\x04\xc8\xde\x1f\x00\";\n\x1fQueryMigrateCheckAccountRequest\x12\x0c\n\x04\x66rom\x18\x01 \x01(\t\x12\n\n\x02to\x18\x02 \x01(\t\"\"\n QueryMigrateCheckAccountResponse2\xb6\x02\n\x05Query\x12\x8d\x01\n\rMigrateRecord\x12(.fx.migrate.v1.QueryMigrateRecordRequest\x1a).fx.migrate.v1.QueryMigrateRecordResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/fx/migrate/v1/record/{address}\x12\x9c\x01\n\x13MigrateCheckAccount\x12..fx.migrate.v1.QueryMigrateCheckAccountRequest\x1a/.fx.migrate.v1.QueryMigrateCheckAccountResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/fx/migrate/v1/check/accountB.Z,github.com/functionx/fx-core/x/migrate/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fx.migrate.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/functionx/fx-core/x/migrate/types'
  _QUERYMIGRATERECORDRESPONSE.fields_by_name['migrateRecord']._options = None
  _QUERYMIGRATERECORDRESPONSE.fields_by_name['migrateRecord']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['MigrateRecord']._options = None
  _QUERY.methods_by_name['MigrateRecord']._serialized_options = b'\202\323\344\223\002!\022\037/fx/migrate/v1/record/{address}'
  _QUERY.methods_by_name['MigrateCheckAccount']._options = None
  _QUERY.methods_by_name['MigrateCheckAccount']._serialized_options = b'\202\323\344\223\002\036\022\034/fx/migrate/v1/check/account'
  _globals['_QUERYMIGRATERECORDREQUEST']._serialized_start=125
  _globals['_QUERYMIGRATERECORDREQUEST']._serialized_end=169
  _globals['_QUERYMIGRATERECORDRESPONSE']._serialized_start=171
  _globals['_QUERYMIGRATERECORDRESPONSE']._serialized_end=273
  _globals['_QUERYMIGRATECHECKACCOUNTREQUEST']._serialized_start=275
  _globals['_QUERYMIGRATECHECKACCOUNTREQUEST']._serialized_end=334
  _globals['_QUERYMIGRATECHECKACCOUNTRESPONSE']._serialized_start=336
  _globals['_QUERYMIGRATECHECKACCOUNTRESPONSE']._serialized_end=370
  _globals['_QUERY']._serialized_start=373
  _globals['_QUERY']._serialized_end=683
# @@protoc_insertion_point(module_scope)
