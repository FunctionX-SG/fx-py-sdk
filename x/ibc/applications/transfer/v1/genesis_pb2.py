# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ibc.applications.transfer.v1 import transfer_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2
from x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*ibc/applications/transfer/v1/genesis.proto\x12\x1cibc.applications.transfer.v1\x1a+ibc/applications/transfer/v1/transfer.proto\x1a\x14gogoproto/gogo.proto\"\xd6\x01\n\x0cGenesisState\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12\x65\n\x0c\x64\x65nom_traces\x18\x02 \x03(\x0b\x32(.ibc.applications.transfer.v1.DenomTraceB%\xaa\xdf\x1f\x06Traces\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:\"denom_traces\"\x12:\n\x06params\x18\x03 \x01(\x0b\x32$.ibc.applications.transfer.v1.ParamsB\x04\xc8\xde\x1f\x00\x42\x39Z7github.com/cosmos/ibc-go/v6/modules/apps/transfer/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'ibc.applications.transfer.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z7github.com/cosmos/ibc-go/v6/modules/apps/transfer/types'
  _GENESISSTATE.fields_by_name['port_id']._options = None
  _GENESISSTATE.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _GENESISSTATE.fields_by_name['denom_traces']._options = None
  _GENESISSTATE.fields_by_name['denom_traces']._serialized_options = b'\252\337\037\006Traces\310\336\037\000\362\336\037\023yaml:\"denom_traces\"'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE._serialized_start=144
  _GENESISSTATE._serialized_end=358
# @@protoc_insertion_point(module_scope)