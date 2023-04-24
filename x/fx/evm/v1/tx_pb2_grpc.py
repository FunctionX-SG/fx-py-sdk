# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from x.fx.evm.v1 import tx_pb2 as fx_dot_evm_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the x/evm Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CallContract = channel.unary_unary(
                '/fx.evm.v1.Msg/CallContract',
                request_serializer=fx_dot_evm_dot_v1_dot_tx__pb2.MsgCallContract.SerializeToString,
                response_deserializer=fx_dot_evm_dot_v1_dot_tx__pb2.MsgCallContractResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the x/evm Msg service.
    """

    def CallContract(self, request, context):
        """CallContract defines a (governance) operation for updating the x/evm module
        callContract. The authority defaults to the x/gov module account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CallContract': grpc.unary_unary_rpc_method_handler(
                    servicer.CallContract,
                    request_deserializer=fx_dot_evm_dot_v1_dot_tx__pb2.MsgCallContract.FromString,
                    response_serializer=fx_dot_evm_dot_v1_dot_tx__pb2.MsgCallContractResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fx.evm.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the x/evm Msg service.
    """

    @staticmethod
    def CallContract(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.evm.v1.Msg/CallContract',
            fx_dot_evm_dot_v1_dot_tx__pb2.MsgCallContract.SerializeToString,
            fx_dot_evm_dot_v1_dot_tx__pb2.MsgCallContractResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
