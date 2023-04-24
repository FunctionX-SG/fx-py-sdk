# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from x.fx.gov.v1 import query_pb2 as fx_dot_gov_dot_v1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service for fx/x/gov module
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary(
                '/fx.gov.v1.Query/Params',
                request_serializer=fx_dot_gov_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
                response_deserializer=fx_dot_gov_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
                )
        self.EGFParams = channel.unary_unary(
                '/fx.gov.v1.Query/EGFParams',
                request_serializer=fx_dot_gov_dot_v1_dot_query__pb2.QueryEGFParamsRequest.SerializeToString,
                response_deserializer=fx_dot_gov_dot_v1_dot_query__pb2.QueryEGFParamsResponse.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service for fx/x/gov module
    """

    def Params(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EGFParams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=fx_dot_gov_dot_v1_dot_query__pb2.QueryParamsRequest.FromString,
                    response_serializer=fx_dot_gov_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
            'EGFParams': grpc.unary_unary_rpc_method_handler(
                    servicer.EGFParams,
                    request_deserializer=fx_dot_gov_dot_v1_dot_query__pb2.QueryEGFParamsRequest.FromString,
                    response_serializer=fx_dot_gov_dot_v1_dot_query__pb2.QueryEGFParamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fx.gov.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service for fx/x/gov module
    """

    @staticmethod
    def Params(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.gov.v1.Query/Params',
            fx_dot_gov_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
            fx_dot_gov_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EGFParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.gov.v1.Query/EGFParams',
            fx_dot_gov_dot_v1_dot_query__pb2.QueryEGFParamsRequest.SerializeToString,
            fx_dot_gov_dot_v1_dot_query__pb2.QueryEGFParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
