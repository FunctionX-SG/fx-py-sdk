from fxsdk.client.grpc_client import Client
from fxsdk.msg.dex import new_position_from_proto, new_order_from_proto, Order, Position
from fxsdk.x.fx.dex.v1.funding_pb2 import Funding

from fxsdk.x.marginx.oracle.v1.query_pb2 import QueryPriceRequest, QueryMarketRequest
from fxsdk.x.marginx.oracle.v1.query_pb2_grpc import QueryStub as OracleClient

from fxsdk.x.fx.dex.v1.query_pb2_grpc import QueryStub as DexClient
from fxsdk.x.fx.dex.v1.query_pb2 import QueryPositionReq, QueryOrderRequest, QueryOrdersRequest, QueryFundingReq
from fxsdk.x.marginx.oracle.v1.types_pb2 import Market


class MxClient(Client):

    def __init__(self, url: str = 'localhost:9090'):
        super().__init__(url)

    def query_oracle_price(self, pair_id: str) -> str:
        response = OracleClient(self.channel).Price(QueryPriceRequest(pair_id=pair_id))
        return response.price

    def query_oracle_prices(self):  # need fix return type
        response = OracleClient(self.channel).Prices(QueryPriceRequest())
        return response.prices

    def query_oracle_market(self, pair_id: str) -> Market:
        response = OracleClient(self.channel).Market(QueryMarketRequest(pair_id=pair_id))
        return response.market

    def query_oracle_markets(self) -> [Market]:
        response = OracleClient(self.channel).Markets(QueryMarketRequest())
        return response.markets

    def query_positions(self, owner: str, pair_id: str) -> [Position]:
        positions = []
        response = DexClient(self.channel).QueryPosition(QueryPositionReq(owner=owner, pair_id=pair_id))
        for pos in response.positions:
            position = new_position_from_proto(pos)
            positions.append(position)
        return positions

    def query_order(self, order_id: str) -> Order:
        response = DexClient(self.channel).QueryOrder(QueryOrderRequest(order_id=order_id))
        order = new_order_from_proto(response.order)
        return order

    def query_orders(self, owner: str, pair_id: str) -> [Order]:
        orders = []
        response = DexClient(self.channel).QueryOrders(QueryOrdersRequest(owner=owner, pair_id=pair_id))
        for order in response.orders:
            order = new_order_from_proto(order)
            orders.append(order)
        return orders
