# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/interchain_accounts/genesis/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from fxpysdk.fxsdk.x.ibc.applications.interchain_accounts.controller.v1 import controller_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_controller__pb2
from fxpysdk.fxsdk.x.ibc.applications.interchain_accounts.host.v1 import host_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_host__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=ibc/applications/interchain_accounts/genesis/v1/genesis.proto\x12/ibc.applications.interchain_accounts.genesis.v1\x1a\x14gogoproto/gogo.proto\x1a\x43ibc/applications/interchain_accounts/controller/v1/controller.proto\x1a\x37ibc/applications/interchain_accounts/host/v1/host.proto\"\xa6\x02\n\x0cGenesisState\x12\x92\x01\n\x18\x63ontroller_genesis_state\x18\x01 \x01(\x0b\x32G.ibc.applications.interchain_accounts.genesis.v1.ControllerGenesisStateB\'\xc8\xde\x1f\x00\xf2\xde\x1f\x1fyaml:\"controller_genesis_state\"\x12\x80\x01\n\x12host_genesis_state\x18\x02 \x01(\x0b\x32\x41.ibc.applications.interchain_accounts.genesis.v1.HostGenesisStateB!\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:\"host_genesis_state\"\"\x82\x03\n\x16\x43ontrollerGenesisState\x12w\n\x0f\x61\x63tive_channels\x18\x01 \x03(\x0b\x32>.ibc.applications.interchain_accounts.genesis.v1.ActiveChannelB\x1e\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:\"active_channels\"\x12\x8d\x01\n\x13interchain_accounts\x18\x02 \x03(\x0b\x32L.ibc.applications.interchain_accounts.genesis.v1.RegisteredInterchainAccountB\"\xc8\xde\x1f\x00\xf2\xde\x1f\x1ayaml:\"interchain_accounts\"\x12\r\n\x05ports\x18\x03 \x03(\t\x12P\n\x06params\x18\x04 \x01(\x0b\x32:.ibc.applications.interchain_accounts.controller.v1.ParamsB\x04\xc8\xde\x1f\x00\"\xf5\x02\n\x10HostGenesisState\x12w\n\x0f\x61\x63tive_channels\x18\x01 \x03(\x0b\x32>.ibc.applications.interchain_accounts.genesis.v1.ActiveChannelB\x1e\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:\"active_channels\"\x12\x8d\x01\n\x13interchain_accounts\x18\x02 \x03(\x0b\x32L.ibc.applications.interchain_accounts.genesis.v1.RegisteredInterchainAccountB\"\xc8\xde\x1f\x00\xf2\xde\x1f\x1ayaml:\"interchain_accounts\"\x12\x0c\n\x04port\x18\x03 \x01(\t\x12J\n\x06params\x18\x04 \x01(\x0b\x32\x34.ibc.applications.interchain_accounts.host.v1.ParamsB\x04\xc8\xde\x1f\x00\"\xd1\x01\n\rActiveChannel\x12/\n\rconnection_id\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:\"connection_id\"\x12#\n\x07port_id\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12)\n\nchannel_id\x18\x03 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\"\x12?\n\x15is_middleware_enabled\x18\x04 \x01(\x08\x42 \xf2\xde\x1f\x1cyaml:\"is_middleware_enabled\"\"\xa8\x01\n\x1bRegisteredInterchainAccount\x12/\n\rconnection_id\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:\"connection_id\"\x12#\n\x07port_id\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12\x33\n\x0f\x61\x63\x63ount_address\x18\x03 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:\"account_address\"BOZMgithub.com/cosmos/ibc-go/v6/modules/apps/27-interchain-accounts/genesis/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.interchain_accounts.genesis.v1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZMgithub.com/cosmos/ibc-go/v6/modules/apps/27-interchain-accounts/genesis/types'
  _GENESISSTATE.fields_by_name['controller_genesis_state']._options = None
  _GENESISSTATE.fields_by_name['controller_genesis_state']._serialized_options = b'\310\336\037\000\362\336\037\037yaml:\"controller_genesis_state\"'
  _GENESISSTATE.fields_by_name['host_genesis_state']._options = None
  _GENESISSTATE.fields_by_name['host_genesis_state']._serialized_options = b'\310\336\037\000\362\336\037\031yaml:\"host_genesis_state\"'
  _CONTROLLERGENESISSTATE.fields_by_name['active_channels']._options = None
  _CONTROLLERGENESISSTATE.fields_by_name['active_channels']._serialized_options = b'\310\336\037\000\362\336\037\026yaml:\"active_channels\"'
  _CONTROLLERGENESISSTATE.fields_by_name['interchain_accounts']._options = None
  _CONTROLLERGENESISSTATE.fields_by_name['interchain_accounts']._serialized_options = b'\310\336\037\000\362\336\037\032yaml:\"interchain_accounts\"'
  _CONTROLLERGENESISSTATE.fields_by_name['params']._options = None
  _CONTROLLERGENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _HOSTGENESISSTATE.fields_by_name['active_channels']._options = None
  _HOSTGENESISSTATE.fields_by_name['active_channels']._serialized_options = b'\310\336\037\000\362\336\037\026yaml:\"active_channels\"'
  _HOSTGENESISSTATE.fields_by_name['interchain_accounts']._options = None
  _HOSTGENESISSTATE.fields_by_name['interchain_accounts']._serialized_options = b'\310\336\037\000\362\336\037\032yaml:\"interchain_accounts\"'
  _HOSTGENESISSTATE.fields_by_name['params']._options = None
  _HOSTGENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _ACTIVECHANNEL.fields_by_name['connection_id']._options = None
  _ACTIVECHANNEL.fields_by_name['connection_id']._serialized_options = b'\362\336\037\024yaml:\"connection_id\"'
  _ACTIVECHANNEL.fields_by_name['port_id']._options = None
  _ACTIVECHANNEL.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _ACTIVECHANNEL.fields_by_name['channel_id']._options = None
  _ACTIVECHANNEL.fields_by_name['channel_id']._serialized_options = b'\362\336\037\021yaml:\"channel_id\"'
  _ACTIVECHANNEL.fields_by_name['is_middleware_enabled']._options = None
  _ACTIVECHANNEL.fields_by_name['is_middleware_enabled']._serialized_options = b'\362\336\037\034yaml:\"is_middleware_enabled\"'
  _REGISTEREDINTERCHAINACCOUNT.fields_by_name['connection_id']._options = None
  _REGISTEREDINTERCHAINACCOUNT.fields_by_name['connection_id']._serialized_options = b'\362\336\037\024yaml:\"connection_id\"'
  _REGISTEREDINTERCHAINACCOUNT.fields_by_name['port_id']._options = None
  _REGISTEREDINTERCHAINACCOUNT.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _REGISTEREDINTERCHAINACCOUNT.fields_by_name['account_address']._options = None
  _REGISTEREDINTERCHAINACCOUNT.fields_by_name['account_address']._serialized_options = b'\362\336\037\026yaml:\"account_address\"'
  _globals['_GENESISSTATE']._serialized_start=263
  _globals['_GENESISSTATE']._serialized_end=557
  _globals['_CONTROLLERGENESISSTATE']._serialized_start=560
  _globals['_CONTROLLERGENESISSTATE']._serialized_end=946
  _globals['_HOSTGENESISSTATE']._serialized_start=949
  _globals['_HOSTGENESISSTATE']._serialized_end=1322
  _globals['_ACTIVECHANNEL']._serialized_start=1325
  _globals['_ACTIVECHANNEL']._serialized_end=1534
  _globals['_REGISTEREDINTERCHAINACCOUNT']._serialized_start=1537
  _globals['_REGISTEREDINTERCHAINACCOUNT']._serialized_end=1705
# @@protoc_insertion_point(module_scope)
