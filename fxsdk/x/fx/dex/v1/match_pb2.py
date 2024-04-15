# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/dex/v1/match.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from fxpysdk.fxsdk.x.fx.dex.v1 import order_pb2 as fx_dot_dex_dot_v1_dot_order__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x66x/dex/v1/match.proto\x12\tfx.dex.v1\x1a\x14gogoproto/gogo.proto\x1a\x15\x66x/dex/v1/order.proto\"\xe9\x01\n\tOrderFill\x12%\n\x05order\x18\x01 \x01(\x0b\x32\x10.fx.dex.v1.OrderB\x04\xc8\xde\x1f\x00\x12\x37\n\ndeal_price\x18\x02 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12<\n\x0fquantity_filled\x18\x03 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12>\n\x11quantity_unfilled\x18\x04 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\"<\n\nOrderFills\x12.\n\norder_fill\x18\x01 \x03(\x0b\x32\x14.fx.dex.v1.OrderFillB\x04\xc8\xde\x1f\x00\";\n\x05Price\x12\x32\n\x05price\x18\x01 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\"w\n\nOrderDepth\x12\x32\n\x05price\x18\x01 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12\x35\n\x08quantity\x18\x02 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\"W\n\tOrderBook\x12$\n\x03\x62id\x18\x01 \x01(\x0b\x32\x11.fx.dex.v1.OrdersB\x04\xc8\xde\x1f\x00\x12$\n\x03\x61sk\x18\x02 \x01(\x0b\x32\x11.fx.dex.v1.OrdersB\x04\xc8\xde\x1f\x00\"\xba\x01\n\rDepthBookItem\x12\x32\n\x05price\x18\x01 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12\x39\n\x0c\x62uy_quantity\x18\x02 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12:\n\rsell_quantity\x18\x03 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\":\n\tDepthBook\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x18.fx.dex.v1.DepthBookItemB\x04\xc8\xde\x1f\x00\"\xbc\x01\n\x07Matcher\x12\x0f\n\x07pair_id\x18\x01 \x01(\t\x12.\n\norder_book\x18\x02 \x01(\x0b\x32\x14.fx.dex.v1.OrderBookB\x04\xc8\xde\x1f\x00\x12<\n\x0flast_deal_price\x18\x03 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12\x32\n\x0c\x64\x65pth_curves\x18\x04 \x01(\x0b\x32\x16.fx.dex.v1.DepthCurvesB\x04\xc8\xde\x1f\x00\"\xab\x03\n\x0bMatchResult\x12\x0f\n\x07pair_id\x18\x01 \x01(\t\x12\x11\n\tbid_count\x18\x02 \x01(\x03\x12\x11\n\task_count\x18\x03 \x01(\x03\x12\x37\n\ndeal_price\x18\x04 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12?\n\x12matched_bid_volume\x18\x05 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12?\n\x12matched_ask_volume\x18\x06 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12;\n\x0emax_bid_volume\x18\x07 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12;\n\x0emax_ask_volume\x18\x08 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12\x30\n\x0border_fills\x18\t \x01(\x0b\x32\x15.fx.dex.v1.OrderFillsB\x04\xc8\xde\x1f\x00\"B\n\x0cMatchResults\x12\x32\n\x0cmatch_result\x18\x01 \x03(\x0b\x32\x16.fx.dex.v1.MatchResultB\x04\xc8\xde\x1f\x00\"U\n\tDealPrice\x12\x0f\n\x07pair_id\x18\x01 \x01(\t\x12\x37\n\ndeal_price\x18\x02 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\"\xbb\x01\n\x0e\x44\x65pthCurveItem\x12\x32\n\x05price\x18\x01 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12:\n\rsell_quantity\x18\x02 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12\x39\n\x0c\x62uy_quantity\x18\x03 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\"=\n\x0b\x44\x65pthCurves\x12.\n\x05items\x18\x01 \x03(\x0b\x32\x19.fx.dex.v1.DepthCurveItemB\x04\xc8\xde\x1f\x00\x42-Z+github.com/marginxio/marginx/x/dex/v1/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fx.dex.v1.match_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/marginxio/marginx/x/dex/v1/types'
  _ORDERFILL.fields_by_name['order']._options = None
  _ORDERFILL.fields_by_name['order']._serialized_options = b'\310\336\037\000'
  _ORDERFILL.fields_by_name['deal_price']._options = None
  _ORDERFILL.fields_by_name['deal_price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _ORDERFILL.fields_by_name['quantity_filled']._options = None
  _ORDERFILL.fields_by_name['quantity_filled']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _ORDERFILL.fields_by_name['quantity_unfilled']._options = None
  _ORDERFILL.fields_by_name['quantity_unfilled']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _ORDERFILLS.fields_by_name['order_fill']._options = None
  _ORDERFILLS.fields_by_name['order_fill']._serialized_options = b'\310\336\037\000'
  _PRICE.fields_by_name['price']._options = None
  _PRICE.fields_by_name['price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _ORDERDEPTH.fields_by_name['price']._options = None
  _ORDERDEPTH.fields_by_name['price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _ORDERDEPTH.fields_by_name['quantity']._options = None
  _ORDERDEPTH.fields_by_name['quantity']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _ORDERBOOK.fields_by_name['bid']._options = None
  _ORDERBOOK.fields_by_name['bid']._serialized_options = b'\310\336\037\000'
  _ORDERBOOK.fields_by_name['ask']._options = None
  _ORDERBOOK.fields_by_name['ask']._serialized_options = b'\310\336\037\000'
  _DEPTHBOOKITEM.fields_by_name['price']._options = None
  _DEPTHBOOKITEM.fields_by_name['price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _DEPTHBOOKITEM.fields_by_name['buy_quantity']._options = None
  _DEPTHBOOKITEM.fields_by_name['buy_quantity']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _DEPTHBOOKITEM.fields_by_name['sell_quantity']._options = None
  _DEPTHBOOKITEM.fields_by_name['sell_quantity']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _DEPTHBOOK.fields_by_name['items']._options = None
  _DEPTHBOOK.fields_by_name['items']._serialized_options = b'\310\336\037\000'
  _MATCHER.fields_by_name['order_book']._options = None
  _MATCHER.fields_by_name['order_book']._serialized_options = b'\310\336\037\000'
  _MATCHER.fields_by_name['last_deal_price']._options = None
  _MATCHER.fields_by_name['last_deal_price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _MATCHER.fields_by_name['depth_curves']._options = None
  _MATCHER.fields_by_name['depth_curves']._serialized_options = b'\310\336\037\000'
  _MATCHRESULT.fields_by_name['deal_price']._options = None
  _MATCHRESULT.fields_by_name['deal_price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _MATCHRESULT.fields_by_name['matched_bid_volume']._options = None
  _MATCHRESULT.fields_by_name['matched_bid_volume']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _MATCHRESULT.fields_by_name['matched_ask_volume']._options = None
  _MATCHRESULT.fields_by_name['matched_ask_volume']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _MATCHRESULT.fields_by_name['max_bid_volume']._options = None
  _MATCHRESULT.fields_by_name['max_bid_volume']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _MATCHRESULT.fields_by_name['max_ask_volume']._options = None
  _MATCHRESULT.fields_by_name['max_ask_volume']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _MATCHRESULT.fields_by_name['order_fills']._options = None
  _MATCHRESULT.fields_by_name['order_fills']._serialized_options = b'\310\336\037\000'
  _MATCHRESULTS.fields_by_name['match_result']._options = None
  _MATCHRESULTS.fields_by_name['match_result']._serialized_options = b'\310\336\037\000'
  _DEALPRICE.fields_by_name['deal_price']._options = None
  _DEALPRICE.fields_by_name['deal_price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _DEPTHCURVEITEM.fields_by_name['price']._options = None
  _DEPTHCURVEITEM.fields_by_name['price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _DEPTHCURVEITEM.fields_by_name['sell_quantity']._options = None
  _DEPTHCURVEITEM.fields_by_name['sell_quantity']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _DEPTHCURVEITEM.fields_by_name['buy_quantity']._options = None
  _DEPTHCURVEITEM.fields_by_name['buy_quantity']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _DEPTHCURVES.fields_by_name['items']._options = None
  _DEPTHCURVES.fields_by_name['items']._serialized_options = b'\310\336\037\000'
  _globals['_ORDERFILL']._serialized_start=82
  _globals['_ORDERFILL']._serialized_end=315
  _globals['_ORDERFILLS']._serialized_start=317
  _globals['_ORDERFILLS']._serialized_end=377
  _globals['_PRICE']._serialized_start=379
  _globals['_PRICE']._serialized_end=438
  _globals['_ORDERDEPTH']._serialized_start=440
  _globals['_ORDERDEPTH']._serialized_end=559
  _globals['_ORDERBOOK']._serialized_start=561
  _globals['_ORDERBOOK']._serialized_end=648
  _globals['_DEPTHBOOKITEM']._serialized_start=651
  _globals['_DEPTHBOOKITEM']._serialized_end=837
  _globals['_DEPTHBOOK']._serialized_start=839
  _globals['_DEPTHBOOK']._serialized_end=897
  _globals['_MATCHER']._serialized_start=900
  _globals['_MATCHER']._serialized_end=1088
  _globals['_MATCHRESULT']._serialized_start=1091
  _globals['_MATCHRESULT']._serialized_end=1518
  _globals['_MATCHRESULTS']._serialized_start=1520
  _globals['_MATCHRESULTS']._serialized_end=1586
  _globals['_DEALPRICE']._serialized_start=1588
  _globals['_DEALPRICE']._serialized_end=1673
  _globals['_DEPTHCURVEITEM']._serialized_start=1676
  _globals['_DEPTHCURVEITEM']._serialized_end=1863
  _globals['_DEPTHCURVES']._serialized_start=1865
  _globals['_DEPTHCURVES']._serialized_end=1926
# @@protoc_insertion_point(module_scope)
