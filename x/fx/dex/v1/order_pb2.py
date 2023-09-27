# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/dex/v1/order.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x66x/dex/v1/order.proto\x12\tfx.dex.v1\x1a\x14gogoproto/gogo.proto\"\x17\n\x08OrderIDs\x12\x0b\n\x03ids\x18\x01 \x03(\t\"\xa5\x05\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\t\x12@\n\x05owner\x18\x02 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x0f\n\x07pair_id\x18\x03 \x01(\t\x12\'\n\tdirection\x18\x04 \x01(\x0e\x32\x14.fx.dex.v1.Direction\x12\x32\n\x05price\x18\x05 \x01(\tB#\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xc8\xde\x1f\x00\x12:\n\rbase_quantity\x18\x06 \x01(\tB#\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xc8\xde\x1f\x00\x12;\n\x0equote_quantity\x18\x07 \x01(\tB#\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xc8\xde\x1f\x00\x12<\n\x0f\x66illed_quantity\x18\x08 \x01(\tB#\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xc8\xde\x1f\x00\x12=\n\x10\x66illed_avg_price\x18\t \x01(\tB#\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xc8\xde\x1f\x00\x12\x10\n\x08leverage\x18\n \x01(\x03\x12&\n\x06status\x18\x0b \x01(\x0e\x32\x16.fx.dex.v1.OrderStatus\x12(\n\norder_type\x18\x0c \x01(\x0e\x32\x14.fx.dex.v1.OrderType\x12\x41\n\x08\x63ost_fee\x18\r \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\xc8\xde\x1f\x00\x12\x43\n\nlocked_fee\x18\x0e \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\xc8\xde\x1f\x00\"0\n\x06Orders\x12&\n\x06orders\x18\x01 \x03(\x0b\x32\x10.fx.dex.v1.OrderB\x04\xc8\xde\x1f\x00*\x8d\x01\n\tDirection\x12\x12\n\x04\x42OTH\x10\x00\x1a\x08\x8a\x9d \x04\x42OTH\x12\x10\n\x03\x42UY\x10\x01\x1a\x07\x8a\x9d \x03\x42UY\x12\x12\n\x04SELL\x10\x02\x1a\x08\x8a\x9d \x04SELL\x12\x1c\n\tMarketBuy\x10\x03\x1a\r\x8a\x9d \tMarketBuy\x12\x1e\n\nMarketSell\x10\x04\x1a\x0e\x8a\x9d \nMarketSell\x1a\x08\xa8\xa4\x1e\x01\x88\xa3\x1e\x00*\xc3\x03\n\x0bOrderStatus\x12$\n\rORDER_PENDING\x10\x00\x1a\x11\x8a\x9d \rORDER_PENDING\x12\"\n\x0cORDER_FILLED\x10\x01\x1a\x10\x8a\x9d \x0cORDER_FILLED\x12\x32\n\x14ORDER_PARTIAL_FILLED\x10\x02\x1a\x18\x8a\x9d \x14ORDER_PARTIAL_FILLED\x12(\n\x0fORDER_CANCELLED\x10\x03\x1a\x13\x8a\x9d \x0fORDER_CANCELLED\x12\x46\n\x1eORDER_PARTIAL_FILLED_CANCELLED\x10\x04\x1a\"\x8a\x9d \x1eORDER_PARTIAL_FILLED_CANCELLED\x12\x42\n\x1cORDER_PARTIAL_FILLED_EXPIRED\x10\x05\x1a \x8a\x9d \x1cORDER_PARTIAL_FILLED_EXPIRED\x12$\n\rORDER_EXPIRED\x10\x06\x1a\x11\x8a\x9d \rORDER_EXPIRED\x12\"\n\x0cORDER_GASOUT\x10\x07\x1a\x10\x8a\x9d \x0cORDER_GASOUT\x12,\n\x11ORDER_PRICE_LIMIT\x10\x08\x1a\x15\x8a\x9d \x11ORDER_PRICE_LIMIT\x1a\x08\xa8\xa4\x1e\x01\x88\xa3\x1e\x00*\xc7\x01\n\tOrderType\x12:\n\x18ORDER_TYPE_OPEN_POSITION\x10\x00\x1a\x1c\x8a\x9d \x18ORDER_TYPE_OPEN_POSITION\x12<\n\x19ORDER_TYPE_CLOSE_POSITION\x10\x01\x1a\x1d\x8a\x9d \x19ORDER_TYPE_CLOSE_POSITION\x12\x36\n\x16ORDER_TYPE_LIQUIDATION\x10\x02\x1a\x1a\x8a\x9d \x16ORDER_TYPE_LIQUIDATION\x1a\x08\xa8\xa4\x1e\x01\x88\xa3\x1e\x00\x42\x31Z+github.com/marginxio/marginx/x/dex/v1/types\xa8\xe2\x1e\x01\x62\x06proto3')

_DIRECTION = DESCRIPTOR.enum_types_by_name['Direction']
Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
_ORDERSTATUS = DESCRIPTOR.enum_types_by_name['OrderStatus']
OrderStatus = enum_type_wrapper.EnumTypeWrapper(_ORDERSTATUS)
_ORDERTYPE = DESCRIPTOR.enum_types_by_name['OrderType']
OrderType = enum_type_wrapper.EnumTypeWrapper(_ORDERTYPE)
BOTH = 0
BUY = 1
SELL = 2
MarketBuy = 3
MarketSell = 4
ORDER_PENDING = 0
ORDER_FILLED = 1
ORDER_PARTIAL_FILLED = 2
ORDER_CANCELLED = 3
ORDER_PARTIAL_FILLED_CANCELLED = 4
ORDER_PARTIAL_FILLED_EXPIRED = 5
ORDER_EXPIRED = 6
ORDER_GASOUT = 7
ORDER_PRICE_LIMIT = 8
ORDER_TYPE_OPEN_POSITION = 0
ORDER_TYPE_CLOSE_POSITION = 1
ORDER_TYPE_LIQUIDATION = 2


_ORDERIDS = DESCRIPTOR.message_types_by_name['OrderIDs']
_ORDER = DESCRIPTOR.message_types_by_name['Order']
_ORDERS = DESCRIPTOR.message_types_by_name['Orders']
OrderIDs = _reflection.GeneratedProtocolMessageType('OrderIDs', (_message.Message,), {
  'DESCRIPTOR' : _ORDERIDS,
  '__module__' : 'fx.dex.v1.order_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.OrderIDs)
  })
_sym_db.RegisterMessage(OrderIDs)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'fx.dex.v1.order_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.Order)
  })
_sym_db.RegisterMessage(Order)

Orders = _reflection.GeneratedProtocolMessageType('Orders', (_message.Message,), {
  'DESCRIPTOR' : _ORDERS,
  '__module__' : 'fx.dex.v1.order_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.Orders)
  })
_sym_db.RegisterMessage(Orders)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/marginxio/marginx/x/dex/v1/types\250\342\036\001'
  _DIRECTION._options = None
  _DIRECTION._serialized_options = b'\250\244\036\001\210\243\036\000'
  _DIRECTION.values_by_name["BOTH"]._options = None
  _DIRECTION.values_by_name["BOTH"]._serialized_options = b'\212\235 \004BOTH'
  _DIRECTION.values_by_name["BUY"]._options = None
  _DIRECTION.values_by_name["BUY"]._serialized_options = b'\212\235 \003BUY'
  _DIRECTION.values_by_name["SELL"]._options = None
  _DIRECTION.values_by_name["SELL"]._serialized_options = b'\212\235 \004SELL'
  _DIRECTION.values_by_name["MarketBuy"]._options = None
  _DIRECTION.values_by_name["MarketBuy"]._serialized_options = b'\212\235 \tMarketBuy'
  _DIRECTION.values_by_name["MarketSell"]._options = None
  _DIRECTION.values_by_name["MarketSell"]._serialized_options = b'\212\235 \nMarketSell'
  _ORDERSTATUS._options = None
  _ORDERSTATUS._serialized_options = b'\250\244\036\001\210\243\036\000'
  _ORDERSTATUS.values_by_name["ORDER_PENDING"]._options = None
  _ORDERSTATUS.values_by_name["ORDER_PENDING"]._serialized_options = b'\212\235 \rORDER_PENDING'
  _ORDERSTATUS.values_by_name["ORDER_FILLED"]._options = None
  _ORDERSTATUS.values_by_name["ORDER_FILLED"]._serialized_options = b'\212\235 \014ORDER_FILLED'
  _ORDERSTATUS.values_by_name["ORDER_PARTIAL_FILLED"]._options = None
  _ORDERSTATUS.values_by_name["ORDER_PARTIAL_FILLED"]._serialized_options = b'\212\235 \024ORDER_PARTIAL_FILLED'
  _ORDERSTATUS.values_by_name["ORDER_CANCELLED"]._options = None
  _ORDERSTATUS.values_by_name["ORDER_CANCELLED"]._serialized_options = b'\212\235 \017ORDER_CANCELLED'
  _ORDERSTATUS.values_by_name["ORDER_PARTIAL_FILLED_CANCELLED"]._options = None
  _ORDERSTATUS.values_by_name["ORDER_PARTIAL_FILLED_CANCELLED"]._serialized_options = b'\212\235 \036ORDER_PARTIAL_FILLED_CANCELLED'
  _ORDERSTATUS.values_by_name["ORDER_PARTIAL_FILLED_EXPIRED"]._options = None
  _ORDERSTATUS.values_by_name["ORDER_PARTIAL_FILLED_EXPIRED"]._serialized_options = b'\212\235 \034ORDER_PARTIAL_FILLED_EXPIRED'
  _ORDERSTATUS.values_by_name["ORDER_EXPIRED"]._options = None
  _ORDERSTATUS.values_by_name["ORDER_EXPIRED"]._serialized_options = b'\212\235 \rORDER_EXPIRED'
  _ORDERSTATUS.values_by_name["ORDER_GASOUT"]._options = None
  _ORDERSTATUS.values_by_name["ORDER_GASOUT"]._serialized_options = b'\212\235 \014ORDER_GASOUT'
  _ORDERSTATUS.values_by_name["ORDER_PRICE_LIMIT"]._options = None
  _ORDERSTATUS.values_by_name["ORDER_PRICE_LIMIT"]._serialized_options = b'\212\235 \021ORDER_PRICE_LIMIT'
  _ORDERTYPE._options = None
  _ORDERTYPE._serialized_options = b'\250\244\036\001\210\243\036\000'
  _ORDERTYPE.values_by_name["ORDER_TYPE_OPEN_POSITION"]._options = None
  _ORDERTYPE.values_by_name["ORDER_TYPE_OPEN_POSITION"]._serialized_options = b'\212\235 \030ORDER_TYPE_OPEN_POSITION'
  _ORDERTYPE.values_by_name["ORDER_TYPE_CLOSE_POSITION"]._options = None
  _ORDERTYPE.values_by_name["ORDER_TYPE_CLOSE_POSITION"]._serialized_options = b'\212\235 \031ORDER_TYPE_CLOSE_POSITION'
  _ORDERTYPE.values_by_name["ORDER_TYPE_LIQUIDATION"]._options = None
  _ORDERTYPE.values_by_name["ORDER_TYPE_LIQUIDATION"]._serialized_options = b'\212\235 \026ORDER_TYPE_LIQUIDATION'
  _ORDER.fields_by_name['owner']._options = None
  _ORDER.fields_by_name['owner']._serialized_options = b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress'
  _ORDER.fields_by_name['price']._options = None
  _ORDER.fields_by_name['price']._serialized_options = b'\332\336\037\033cosmossdk.io/math.LegacyDec\310\336\037\000'
  _ORDER.fields_by_name['base_quantity']._options = None
  _ORDER.fields_by_name['base_quantity']._serialized_options = b'\332\336\037\033cosmossdk.io/math.LegacyDec\310\336\037\000'
  _ORDER.fields_by_name['quote_quantity']._options = None
  _ORDER.fields_by_name['quote_quantity']._serialized_options = b'\332\336\037\033cosmossdk.io/math.LegacyDec\310\336\037\000'
  _ORDER.fields_by_name['filled_quantity']._options = None
  _ORDER.fields_by_name['filled_quantity']._serialized_options = b'\332\336\037\033cosmossdk.io/math.LegacyDec\310\336\037\000'
  _ORDER.fields_by_name['filled_avg_price']._options = None
  _ORDER.fields_by_name['filled_avg_price']._serialized_options = b'\332\336\037\033cosmossdk.io/math.LegacyDec\310\336\037\000'
  _ORDER.fields_by_name['cost_fee']._options = None
  _ORDER.fields_by_name['cost_fee']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Coin\310\336\037\000'
  _ORDER.fields_by_name['locked_fee']._options = None
  _ORDER.fields_by_name['locked_fee']._serialized_options = b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Coin\310\336\037\000'
  _ORDERS.fields_by_name['orders']._options = None
  _ORDERS.fields_by_name['orders']._serialized_options = b'\310\336\037\000'
  _DIRECTION._serialized_start=814
  _DIRECTION._serialized_end=955
  _ORDERSTATUS._serialized_start=958
  _ORDERSTATUS._serialized_end=1409
  _ORDERTYPE._serialized_start=1412
  _ORDERTYPE._serialized_end=1611
  _ORDERIDS._serialized_start=58
  _ORDERIDS._serialized_end=81
  _ORDER._serialized_start=84
  _ORDER._serialized_end=761
  _ORDERS._serialized_start=763
  _ORDERS._serialized_end=811
# @@protoc_insertion_point(module_scope)