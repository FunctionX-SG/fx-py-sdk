# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/staking/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from x.cosmos.staking.v1beta1 import genesis_pb2 as cosmos_dot_staking_dot_v1beta1_dot_genesis__pb2
from x.cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
from x.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n fx/staking/v1beta1/genesis.proto\x12\x12\x66x.staking.v1beta1\x1a$cosmos/staking/v1beta1/genesis.proto\x1a$cosmos/staking/v1beta1/staking.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\"\xbb\x04\n\x0cGenesisState\x12\x34\n\x06params\x18\x01 \x01(\x0b\x32\x1e.cosmos.staking.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12H\n\x10last_total_power\x18\x02 \x01(\x0c\x42.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12O\n\x15last_validator_powers\x18\x03 \x03(\x0b\x32*.cosmos.staking.v1beta1.LastValidatorPowerB\x04\xc8\xde\x1f\x00\x12;\n\nvalidators\x18\x04 \x03(\x0b\x32!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00\x12=\n\x0b\x64\x65legations\x18\x05 \x03(\x0b\x32\".cosmos.staking.v1beta1.DelegationB\x04\xc8\xde\x1f\x00\x12P\n\x15unbonding_delegations\x18\x06 \x03(\x0b\x32+.cosmos.staking.v1beta1.UnbondingDelegationB\x04\xc8\xde\x1f\x00\x12\x41\n\rredelegations\x18\x07 \x03(\x0b\x32$.cosmos.staking.v1beta1.RedelegationB\x04\xc8\xde\x1f\x00\x12\x10\n\x08\x65xported\x18\x08 \x01(\x08\x12\x37\n\nallowances\x18\t \x03(\x0b\x32\x1d.fx.staking.v1beta1.AllowanceB\x04\xc8\xde\x1f\x00\"\xed\x01\n\tAllowance\x12\x33\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12/\n\rowner_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x31\n\x0fspender_address\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x41\n\tallowance\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x00\x42.Z,github.com/functionx/fx-core/x/staking/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_ALLOWANCE = DESCRIPTOR.message_types_by_name['Allowance']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'fx.staking.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:fx.staking.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

Allowance = _reflection.GeneratedProtocolMessageType('Allowance', (_message.Message,), {
  'DESCRIPTOR' : _ALLOWANCE,
  '__module__' : 'fx.staking.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:fx.staking.v1beta1.Allowance)
  })
_sym_db.RegisterMessage(Allowance)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/functionx/fx-core/x/staking/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['last_total_power']._options = None
  _GENESISSTATE.fields_by_name['last_total_power']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _GENESISSTATE.fields_by_name['last_validator_powers']._options = None
  _GENESISSTATE.fields_by_name['last_validator_powers']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['validators']._options = None
  _GENESISSTATE.fields_by_name['validators']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['delegations']._options = None
  _GENESISSTATE.fields_by_name['delegations']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['unbonding_delegations']._options = None
  _GENESISSTATE.fields_by_name['unbonding_delegations']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['redelegations']._options = None
  _GENESISSTATE.fields_by_name['redelegations']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['allowances']._options = None
  _GENESISSTATE.fields_by_name['allowances']._serialized_options = b'\310\336\037\000'
  _ALLOWANCE.fields_by_name['validator_address']._options = None
  _ALLOWANCE.fields_by_name['validator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _ALLOWANCE.fields_by_name['owner_address']._options = None
  _ALLOWANCE.fields_by_name['owner_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _ALLOWANCE.fields_by_name['spender_address']._options = None
  _ALLOWANCE.fields_by_name['spender_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _ALLOWANCE.fields_by_name['allowance']._options = None
  _ALLOWANCE.fields_by_name['allowance']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
  _ALLOWANCE._options = None
  _ALLOWANCE._serialized_options = b'\350\240\037\000'
  _GENESISSTATE._serialized_start=182
  _GENESISSTATE._serialized_end=753
  _ALLOWANCE._serialized_start=756
  _ALLOWANCE._serialized_end=993
# @@protoc_insertion_point(module_scope)