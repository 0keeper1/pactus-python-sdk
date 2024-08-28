"""apis."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .proto import (
    network_pb2,
    network_pb2_grpc,
    transaction_pb2,
    transaction_pb2_grpc,
    utils_pb2,
    utils_pb2_grpc,
)

if TYPE_CHECKING:
    from pactus import PactusConnect


class Transaction:
    @staticmethod
    def get_transaction(connection: PactusConnect) -> Any:
        stub = transaction_pb2_grpc.TransactionStub(connection._channel)
        req = transaction_pb2.GetTransactionRequest()
        return stub.GetTransaction(req)

    @staticmethod
    def calculate_fee(connection: PactusConnect) -> Any:
        stub = transaction_pb2_grpc.TransactionStub(connection._channel)
        req = transaction_pb2.CalculateFeeRequest()
        return stub.CalculateFee(req)

    @staticmethod
    def broadcast_transaction(connection: PactusConnect) -> Any:
        stub = transaction_pb2_grpc.TransactionStub(connection._channel)
        req = transaction_pb2.BroadcastTransactionRequest()
        return stub.BroadcastTransaction(req)

    @staticmethod
    def get_raw_transfer_transaction(connection: PactusConnect) -> Any:
        stub = transaction_pb2_grpc.TransactionStub(connection._channel)
        req = transaction_pb2.BroadcastTransactionRequest()
        return stub.BroadcastTransaction(req)

    @staticmethod
    def get_raw_bond_transaction(connection: PactusConnect) -> Any:
        stub = transaction_pb2_grpc.TransactionStub(connection._channel)
        req = transaction_pb2.GetRawBondTransactionRequest()
        return stub.GetRawBondTransaction(req)

    @staticmethod
    def get_raw_unbond_transaction(connection: PactusConnect) -> Any:
        stub = transaction_pb2_grpc.TransactionStub(connection._channel)
        req = transaction_pb2.GetRawUnbondTransactionRequest()
        return stub.GetRawUnbondTransaction(req)

    @staticmethod
    def get_raw_withdraw_transaction(connection: PactusConnect) -> Any:
        stub = transaction_pb2_grpc.TransactionStub(connection._channel)
        req = transaction_pb2.GetRawWithdrawTransactionRequest()
        return stub.GetRawWithdrawTransaction(req)


class Utils:
    @staticmethod
    def sign_message_with_privatekey(connection: PactusConnect) -> Any:
        stub = utils_pb2_grpc.UtilsStub(connection._channel)
        req = utils_pb2.SignMessageWithPrivateKeyRequest()
        return stub.SignMessageWithPrivateKey(req)

    @staticmethod
    def verify_message(connection: PactusConnect) -> Any:
        stub = utils_pb2_grpc.UtilsStub(connection._channel)
        req = utils_pb2.VerifyMessageRequest()
        return stub.VerifyMessage(req)


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
