# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import warnings

import grpc

from pactus.proto import network_pb2 as pactus_dot_proto_dot_network__pb2

GRPC_GENERATED_VERSION = "1.66.0"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in pactus/proto/network_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class NetworkStub(object):
    """Network service provides RPCs for retrieving information about the network."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetNetworkInfo = channel.unary_unary(
            "/pactus.Network/GetNetworkInfo",
            request_serializer=pactus_dot_proto_dot_network__pb2.GetNetworkInfoRequest.SerializeToString,
            response_deserializer=pactus_dot_proto_dot_network__pb2.GetNetworkInfoResponse.FromString,
            _registered_method=True,
        )
        self.GetNodeInfo = channel.unary_unary(
            "/pactus.Network/GetNodeInfo",
            request_serializer=pactus_dot_proto_dot_network__pb2.GetNodeInfoRequest.SerializeToString,
            response_deserializer=pactus_dot_proto_dot_network__pb2.GetNodeInfoResponse.FromString,
            _registered_method=True,
        )


class NetworkServicer(object):
    """Network service provides RPCs for retrieving information about the network."""

    def GetNetworkInfo(self, request, context):
        """GetNetworkInfo retrieves information about the overall network."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetNodeInfo(self, request, context):
        """GetNodeInfo retrieves information about a specific node in the network."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_NetworkServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetNetworkInfo": grpc.unary_unary_rpc_method_handler(
            servicer.GetNetworkInfo,
            request_deserializer=pactus_dot_proto_dot_network__pb2.GetNetworkInfoRequest.FromString,
            response_serializer=pactus_dot_proto_dot_network__pb2.GetNetworkInfoResponse.SerializeToString,
        ),
        "GetNodeInfo": grpc.unary_unary_rpc_method_handler(
            servicer.GetNodeInfo,
            request_deserializer=pactus_dot_proto_dot_network__pb2.GetNodeInfoRequest.FromString,
            response_serializer=pactus_dot_proto_dot_network__pb2.GetNodeInfoResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pactus.Network", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("pactus.Network", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Network(object):
    """Network service provides RPCs for retrieving information about the network."""

    @staticmethod
    def GetNetworkInfo(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pactus.Network/GetNetworkInfo",
            pactus_dot_proto_dot_network__pb2.GetNetworkInfoRequest.SerializeToString,
            pactus_dot_proto_dot_network__pb2.GetNetworkInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def GetNodeInfo(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pactus.Network/GetNodeInfo",
            pactus_dot_proto_dot_network__pb2.GetNodeInfoRequest.SerializeToString,
            pactus_dot_proto_dot_network__pb2.GetNodeInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
