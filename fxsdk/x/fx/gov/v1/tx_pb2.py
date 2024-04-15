# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/gov/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxsdk.x.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from fxsdk.x.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from fxsdk.x.fx.gov.v1 import params_pb2 as fx_dot_gov_dot_v1_dot_params__pb2
from fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x66x/gov/v1/tx.proto\x12\tfx.gov.v1\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x16\x66x/gov/v1/params.proto\x1a\x14gogoproto/gogo.proto\"w\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\'\n\x06params\x18\x02 \x01(\x0b\x32\x11.fx.gov.v1.ParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x19\n\x17MsgUpdateParamsResponse\"}\n\x12MsgUpdateEGFParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12*\n\x06params\x18\x02 \x01(\x0b\x32\x14.fx.gov.v1.EGFParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x1c\n\x1aMsgUpdateEGFParamsResponse2\xae\x01\n\x03Msg\x12N\n\x0cUpdateParams\x12\x1a.fx.gov.v1.MsgUpdateParams\x1a\".fx.gov.v1.MsgUpdateParamsResponse\x12W\n\x0fUpdateEGFParams\x12\x1d.fx.gov.v1.MsgUpdateEGFParams\x1a%.fx.gov.v1.MsgUpdateEGFParamsResponseB*Z(github.com/functionx/fx-core/x/gov/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fx.gov.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z(github.com/functionx/fx-core/x/gov/types'
  _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
  _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS._options = None
  _MSGUPDATEPARAMS._serialized_options = b'\202\347\260*\tauthority'
  _MSGUPDATEEGFPARAMS.fields_by_name['authority']._options = None
  _MSGUPDATEEGFPARAMS.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEEGFPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEEGFPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEEGFPARAMS._options = None
  _MSGUPDATEEGFPARAMS._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSGUPDATEPARAMS']._serialized_start=131
  _globals['_MSGUPDATEPARAMS']._serialized_end=250
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=252
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=277
  _globals['_MSGUPDATEEGFPARAMS']._serialized_start=279
  _globals['_MSGUPDATEEGFPARAMS']._serialized_end=404
  _globals['_MSGUPDATEEGFPARAMSRESPONSE']._serialized_start=406
  _globals['_MSGUPDATEEGFPARAMSRESPONSE']._serialized_end=434
  _globals['_MSG']._serialized_start=437
  _globals['_MSG']._serialized_end=611
# @@protoc_insertion_point(module_scope)
