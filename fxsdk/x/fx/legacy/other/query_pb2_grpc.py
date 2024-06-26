# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fxpysdk.fxsdk.x.fx.legacy.other import query_pb2 as fx_dot_legacy_dot_other_dot_query__pb2


class QueryStub(object):
    """Deprecated: Query
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FxGasPrice = channel.unary_unary(
                '/fx.other.Query/FxGasPrice',
                request_serializer=fx_dot_legacy_dot_other_dot_query__pb2.GasPriceRequest.SerializeToString,
                response_deserializer=fx_dot_legacy_dot_other_dot_query__pb2.GasPriceResponse.FromString,
                )
        self.GasPrice = channel.unary_unary(
                '/fx.other.Query/GasPrice',
                request_serializer=fx_dot_legacy_dot_other_dot_query__pb2.GasPriceRequest.SerializeToString,
                response_deserializer=fx_dot_legacy_dot_other_dot_query__pb2.GasPriceResponse.FromString,
                )


class QueryServicer(object):
    """Deprecated: Query
    """

    def FxGasPrice(self, request, context):
        """Deprecated: please use cosmos.base.node.v1beta1.Service.Config
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GasPrice(self, request, context):
        """Deprecated: please use cosmos.base.node.v1beta1.Service.Config
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FxGasPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.FxGasPrice,
                    request_deserializer=fx_dot_legacy_dot_other_dot_query__pb2.GasPriceRequest.FromString,
                    response_serializer=fx_dot_legacy_dot_other_dot_query__pb2.GasPriceResponse.SerializeToString,
            ),
            'GasPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.GasPrice,
                    request_deserializer=fx_dot_legacy_dot_other_dot_query__pb2.GasPriceRequest.FromString,
                    response_serializer=fx_dot_legacy_dot_other_dot_query__pb2.GasPriceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fx.other.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Deprecated: Query
    """

    @staticmethod
    def FxGasPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.other.Query/FxGasPrice',
            fx_dot_legacy_dot_other_dot_query__pb2.GasPriceRequest.SerializeToString,
            fx_dot_legacy_dot_other_dot_query__pb2.GasPriceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GasPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.other.Query/GasPrice',
            fx_dot_legacy_dot_other_dot_query__pb2.GasPriceRequest.SerializeToString,
            fx_dot_legacy_dot_other_dot_query__pb2.GasPriceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
