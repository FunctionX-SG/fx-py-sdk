# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/dex/v1/proposal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fxpysdk.fxsdk.x.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from fxpysdk.fxsdk.x.fx.dex.v1 import funding_pb2 as fx_dot_dex_dot_v1_dot_funding__pb2
from fxpysdk.fxsdk.x.fx.dex.v1 import margin_pb2 as fx_dot_dex_dot_v1_dot_margin__pb2
from fxpysdk.fxsdk.x.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x66x/dex/v1/proposal.proto\x12\tfx.dex.v1\x1a\x14gogoproto/gogo.proto\x1a\x17\x66x/dex/v1/funding.proto\x1a\x16\x66x/dex/v1/margin.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"z\n\x18ResetFundingTimeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12,\n\x0c\x66unding_time\x18\x03 \x01(\x0b\x32\x16.fx.dex.v1.FundingTime:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"z\n\x1aResetFundingParamsProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12*\n\x0e\x66unding_params\x18\x03 \x01(\x0b\x32\x12.fx.dex.v1.Funding:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"\x81\x01\n\x15ResetMMATableProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x36\n\x12margin_rate_tables\x18\x03 \x03(\x0b\x32\x1a.fx.dex.v1.MarginRateTable:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"e\n\x12\x43reatePairProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1d\n\x04pair\x18\x03 \x01(\x0b\x32\x0f.fx.dex.v1.Pair:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xa0\x01\n\x04Pair\x12\x12\n\nbase_asset\x18\x01 \x01(\t\x12\x13\n\x0bquote_asset\x18\x02 \x01(\t\x12\x15\n\rmarket_status\x18\x03 \x01(\x03\x12\x15\n\rprice_decimal\x18\x04 \x01(\x03\x12\x18\n\x10position_decimal\x18\x05 \x01(\x03\x12\x12\n\ninit_price\x18\x06 \x01(\t\x12\x13\n\x0bmarket_type\x18\x07 \x01(\t\"\x8c\x01\n\x1fResetPremiumIndexConfigProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x37\n\x12premium_index_conf\x18\x03 \x01(\x0b\x32\x1b.fx.dex.v1.PremiumIndexConf:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"k\n\x12ShareSplitProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x12\n\nmultiplier\x18\x03 \x01(\t\x12\x0f\n\x07pair_id\x18\x04 \x01(\t:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xbb\x01\n\x17TradingFeeSpendProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12[\n\x06\x61mount\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xed\x01\n\"TradingFeeSpendProposalWithDeposit\x12\x1f\n\x05title\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"title\"\x12+\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"description\"\x12\'\n\trecipient\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"recipient\"\x12!\n\x06\x61mount\x18\x04 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"amount\"\x12#\n\x07\x64\x65posit\x18\x05 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"deposit\":\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01\"m\n\x12UnlistPairProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07pair_id\x18\x03 \x01(\t\x12\x14\n\x0c\x66\x65\x65_receiver\x18\x04 \x01(\t:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\"o\n\x14SendToFxcoreProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x14\n\x0c\x66\x65\x65_receiver\x18\x03 \x01(\t\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\t:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x42-Z+github.com/marginxio/marginx/x/dex/v1/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fx.dex.v1.proposal_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/marginxio/marginx/x/dex/v1/types'
  _RESETFUNDINGTIMEPROPOSAL._options = None
  _RESETFUNDINGTIMEPROPOSAL._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _RESETFUNDINGPARAMSPROPOSAL._options = None
  _RESETFUNDINGPARAMSPROPOSAL._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _RESETMMATABLEPROPOSAL._options = None
  _RESETMMATABLEPROPOSAL._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _CREATEPAIRPROPOSAL._options = None
  _CREATEPAIRPROPOSAL._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _RESETPREMIUMINDEXCONFIGPROPOSAL._options = None
  _RESETPREMIUMINDEXCONFIGPROPOSAL._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _SHARESPLITPROPOSAL._options = None
  _SHARESPLITPROPOSAL._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _TRADINGFEESPENDPROPOSAL.fields_by_name['amount']._options = None
  _TRADINGFEESPENDPROPOSAL.fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _TRADINGFEESPENDPROPOSAL._options = None
  _TRADINGFEESPENDPROPOSAL._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _TRADINGFEESPENDPROPOSALWITHDEPOSIT.fields_by_name['title']._options = None
  _TRADINGFEESPENDPROPOSALWITHDEPOSIT.fields_by_name['title']._serialized_options = b'\362\336\037\014yaml:\"title\"'
  _TRADINGFEESPENDPROPOSALWITHDEPOSIT.fields_by_name['description']._options = None
  _TRADINGFEESPENDPROPOSALWITHDEPOSIT.fields_by_name['description']._serialized_options = b'\362\336\037\022yaml:\"description\"'
  _TRADINGFEESPENDPROPOSALWITHDEPOSIT.fields_by_name['recipient']._options = None
  _TRADINGFEESPENDPROPOSALWITHDEPOSIT.fields_by_name['recipient']._serialized_options = b'\362\336\037\020yaml:\"recipient\"'
  _TRADINGFEESPENDPROPOSALWITHDEPOSIT.fields_by_name['amount']._options = None
  _TRADINGFEESPENDPROPOSALWITHDEPOSIT.fields_by_name['amount']._serialized_options = b'\362\336\037\ryaml:\"amount\"'
  _TRADINGFEESPENDPROPOSALWITHDEPOSIT.fields_by_name['deposit']._options = None
  _TRADINGFEESPENDPROPOSALWITHDEPOSIT.fields_by_name['deposit']._serialized_options = b'\362\336\037\016yaml:\"deposit\"'
  _TRADINGFEESPENDPROPOSALWITHDEPOSIT._options = None
  _TRADINGFEESPENDPROPOSALWITHDEPOSIT._serialized_options = b'\210\240\037\000\230\240\037\001'
  _UNLISTPAIRPROPOSAL._options = None
  _UNLISTPAIRPROPOSAL._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _SENDTOFXCOREPROPOSAL._options = None
  _SENDTOFXCOREPROPOSAL._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000'
  _globals['_RESETFUNDINGTIMEPROPOSAL']._serialized_start=142
  _globals['_RESETFUNDINGTIMEPROPOSAL']._serialized_end=264
  _globals['_RESETFUNDINGPARAMSPROPOSAL']._serialized_start=266
  _globals['_RESETFUNDINGPARAMSPROPOSAL']._serialized_end=388
  _globals['_RESETMMATABLEPROPOSAL']._serialized_start=391
  _globals['_RESETMMATABLEPROPOSAL']._serialized_end=520
  _globals['_CREATEPAIRPROPOSAL']._serialized_start=522
  _globals['_CREATEPAIRPROPOSAL']._serialized_end=623
  _globals['_PAIR']._serialized_start=626
  _globals['_PAIR']._serialized_end=786
  _globals['_RESETPREMIUMINDEXCONFIGPROPOSAL']._serialized_start=789
  _globals['_RESETPREMIUMINDEXCONFIGPROPOSAL']._serialized_end=929
  _globals['_SHARESPLITPROPOSAL']._serialized_start=931
  _globals['_SHARESPLITPROPOSAL']._serialized_end=1038
  _globals['_TRADINGFEESPENDPROPOSAL']._serialized_start=1041
  _globals['_TRADINGFEESPENDPROPOSAL']._serialized_end=1228
  _globals['_TRADINGFEESPENDPROPOSALWITHDEPOSIT']._serialized_start=1231
  _globals['_TRADINGFEESPENDPROPOSALWITHDEPOSIT']._serialized_end=1468
  _globals['_UNLISTPAIRPROPOSAL']._serialized_start=1470
  _globals['_UNLISTPAIRPROPOSAL']._serialized_end=1579
  _globals['_SENDTOFXCOREPROPOSAL']._serialized_start=1581
  _globals['_SENDTOFXCOREPROPOSAL']._serialized_end=1692
# @@protoc_insertion_point(module_scope)
