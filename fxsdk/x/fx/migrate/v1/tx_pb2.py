# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/migrate/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x66x/migrate/v1/tx.proto\x12\rfx.migrate.v1\"@\n\x11MsgMigrateAccount\x12\x0c\n\x04\x66rom\x18\x01 \x01(\t\x12\n\n\x02to\x18\x02 \x01(\t\x12\x11\n\tsignature\x18\x03 \x01(\t\"\x1b\n\x19MsgMigrateAccountResponse2c\n\x03Msg\x12\\\n\x0eMigrateAccount\x12 .fx.migrate.v1.MsgMigrateAccount\x1a(.fx.migrate.v1.MsgMigrateAccountResponseB.Z,github.com/functionx/fx-core/x/migrate/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fx.migrate.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/functionx/fx-core/x/migrate/types'
  _globals['_MSGMIGRATEACCOUNT']._serialized_start=41
  _globals['_MSGMIGRATEACCOUNT']._serialized_end=105
  _globals['_MSGMIGRATEACCOUNTRESPONSE']._serialized_start=107
  _globals['_MSGMIGRATEACCOUNTRESPONSE']._serialized_end=134
  _globals['_MSG']._serialized_start=136
  _globals['_MSG']._serialized_end=235
# @@protoc_insertion_point(module_scope)