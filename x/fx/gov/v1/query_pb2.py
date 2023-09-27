# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/gov/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from x.fx.gov.v1 import params_pb2 as fx_dot_gov_dot_v1_dot_params__pb2
from x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from x.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x66x/gov/v1/query.proto\x12\tfx.gov.v1\x1a\x16\x66x/gov/v1/params.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\"&\n\x12QueryParamsRequest\x12\x10\n\x08msg_type\x18\x01 \x01(\t\">\n\x13QueryParamsResponse\x12\'\n\x06params\x18\x01 \x01(\x0b\x32\x11.fx.gov.v1.ParamsB\x04\xc8\xde\x1f\x00\"\x17\n\x15QueryEGFParamsRequest\"D\n\x16QueryEGFParamsResponse\x12*\n\x06params\x18\x01 \x01(\x0b\x32\x14.fx.gov.v1.EGFParamsB\x04\xc8\xde\x1f\x00\x32\xdc\x01\n\x05Query\x12\x62\n\x06Params\x12\x1d.fx.gov.v1.QueryParamsRequest\x1a\x1e.fx.gov.v1.QueryParamsResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/fx/gov/v1/Params\x12o\n\tEGFParams\x12 .fx.gov.v1.QueryEGFParamsRequest\x1a!.fx.gov.v1.QueryEGFParamsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/fx/gov/v1/egf_paramsB*Z(github.com/functionx/fx-core/x/gov/typesb\x06proto3')



_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYEGFPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryEGFParamsRequest']
_QUERYEGFPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryEGFParamsResponse']
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'fx.gov.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:fx.gov.v1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'fx.gov.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:fx.gov.v1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)

QueryEGFParamsRequest = _reflection.GeneratedProtocolMessageType('QueryEGFParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYEGFPARAMSREQUEST,
  '__module__' : 'fx.gov.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:fx.gov.v1.QueryEGFParamsRequest)
  })
_sym_db.RegisterMessage(QueryEGFParamsRequest)

QueryEGFParamsResponse = _reflection.GeneratedProtocolMessageType('QueryEGFParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYEGFPARAMSRESPONSE,
  '__module__' : 'fx.gov.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:fx.gov.v1.QueryEGFParamsResponse)
  })
_sym_db.RegisterMessage(QueryEGFParamsResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z(github.com/functionx/fx-core/x/gov/types'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERYEGFPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYEGFPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\023\022\021/fx/gov/v1/Params'
  _QUERY.methods_by_name['EGFParams']._options = None
  _QUERY.methods_by_name['EGFParams']._serialized_options = b'\202\323\344\223\002\027\022\025/fx/gov/v1/egf_params'
  _QUERYPARAMSREQUEST._serialized_start=112
  _QUERYPARAMSREQUEST._serialized_end=150
  _QUERYPARAMSRESPONSE._serialized_start=152
  _QUERYPARAMSRESPONSE._serialized_end=214
  _QUERYEGFPARAMSREQUEST._serialized_start=216
  _QUERYEGFPARAMSREQUEST._serialized_end=239
  _QUERYEGFPARAMSRESPONSE._serialized_start=241
  _QUERYEGFPARAMSRESPONSE._serialized_end=309
  _QUERY._serialized_start=312
  _QUERY._serialized_end=532
# @@protoc_insertion_point(module_scope)