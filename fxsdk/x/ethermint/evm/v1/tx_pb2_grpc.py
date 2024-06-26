# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fxpysdk.fxsdk.x.ethermint.evm.v1 import tx_pb2 as ethermint_dot_evm_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the evm Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EthereumTx = channel.unary_unary(
                '/ethermint.evm.v1.Msg/EthereumTx',
                request_serializer=ethermint_dot_evm_dot_v1_dot_tx__pb2.MsgEthereumTx.SerializeToString,
                response_deserializer=ethermint_dot_evm_dot_v1_dot_tx__pb2.MsgEthereumTxResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the evm Msg service.
    """

    def EthereumTx(self, request, context):
        """EthereumTx defines a method submitting Ethereum transactions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EthereumTx': grpc.unary_unary_rpc_method_handler(
                    servicer.EthereumTx,
                    request_deserializer=ethermint_dot_evm_dot_v1_dot_tx__pb2.MsgEthereumTx.FromString,
                    response_serializer=ethermint_dot_evm_dot_v1_dot_tx__pb2.MsgEthereumTxResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ethermint.evm.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the evm Msg service.
    """

    @staticmethod
    def EthereumTx(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ethermint.evm.v1.Msg/EthereumTx',
            ethermint_dot_evm_dot_v1_dot_tx__pb2.MsgEthereumTx.SerializeToString,
            ethermint_dot_evm_dot_v1_dot_tx__pb2.MsgEthereumTxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
