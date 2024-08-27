"""apis."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .proto import network_pb2, network_pb2_grpc

if TYPE_CHECKING:
    from pactus import PactusConnect


class Network:
    @staticmethod
    def get_network_info(connection: PactusConnect):
        stub = network_pb2_grpc.NetworkStub(connection._channel)
        req = network_pb2.GetNetworkInfoRequest()
        return stub.GetNetworkInfo(req)

    @staticmethod
    def get_node_info(connection: PactusConnect):
        stub = network_pb2_grpc.NetworkStub(connection._channel)
        req = network_pb2.GetNodeInfoRequest()
        return stub.GetNodeInfo(req)
