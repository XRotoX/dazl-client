# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import transaction_service_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2


class TransactionServiceStub(object):
    """Allows clients to read transactions from the ledger.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTransactions = channel.unary_stream(
                '/com.daml.ledger.api.v1.TransactionService/GetTransactions',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionsRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionsResponse.FromString,
                )
        self.GetTransactionTrees = channel.unary_stream(
                '/com.daml.ledger.api.v1.TransactionService/GetTransactionTrees',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionsRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionTreesResponse.FromString,
                )
        self.GetTransactionByEventId = channel.unary_unary(
                '/com.daml.ledger.api.v1.TransactionService/GetTransactionByEventId',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionByEventIdRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionResponse.FromString,
                )
        self.GetTransactionById = channel.unary_unary(
                '/com.daml.ledger.api.v1.TransactionService/GetTransactionById',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionByIdRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionResponse.FromString,
                )
        self.GetFlatTransactionByEventId = channel.unary_unary(
                '/com.daml.ledger.api.v1.TransactionService/GetFlatTransactionByEventId',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionByEventIdRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetFlatTransactionResponse.FromString,
                )
        self.GetFlatTransactionById = channel.unary_unary(
                '/com.daml.ledger.api.v1.TransactionService/GetFlatTransactionById',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionByIdRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetFlatTransactionResponse.FromString,
                )
        self.GetLedgerEnd = channel.unary_unary(
                '/com.daml.ledger.api.v1.TransactionService/GetLedgerEnd',
                request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetLedgerEndRequest.SerializeToString,
                response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetLedgerEndResponse.FromString,
                )


class TransactionServiceServicer(object):
    """Allows clients to read transactions from the ledger.
    """

    def GetTransactions(self, request, context):
        """Read the ledger's filtered transaction stream for a set of parties.
        Lists only creates and archives, but not other events.
        Omits all events on transient contracts, i.e., contracts that were both created and archived in the same transaction.
        Errors:
        - ``UNAUTHENTICATED``: if the request does not include a valid access token
        - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
        - ``NOT_FOUND``: if the request does not include a valid ledger id or if the ledger has been pruned before ``begin``
        - ``INVALID_ARGUMENT``: if the payload is malformed or is missing required fields (e.g. if ``before`` is not before ``end``)
        - ``OUT_OF_RANGE``: if the ``begin`` parameter value is not before the end of the ledger
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTransactionTrees(self, request, context):
        """Read the ledger's complete transaction tree stream for a set of parties.
        The stream can be filtered only by parties, but not templates (template filter must be empty).
        Errors:
        - ``UNAUTHENTICATED``: if the request does not include a valid access token
        - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
        - ``NOT_FOUND``: if the request does not include a valid ledger id or if the ledger has been pruned before ``begin``
        - ``INVALID_ARGUMENT``: if the payload is malformed or is missing required fields (e.g. if ``before`` is not before ``end``)
        - ``OUT_OF_RANGE``: if the ``begin`` parameter value is not before the end of the ledger
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTransactionByEventId(self, request, context):
        """Lookup a transaction tree by the ID of an event that appears within it.
        For looking up a transaction instead of a transaction tree, please see GetFlatTransactionByEventId
        Errors:
        - ``UNAUTHENTICATED``: if the request does not include a valid access token
        - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
        - ``NOT_FOUND``: if the request does not include a valid ledger id or no such transaction exists
        - ``INVALID_ARGUMENT``: if the payload is malformed or is missing required fields (e.g. if requesting parties are invalid or empty)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTransactionById(self, request, context):
        """Lookup a transaction tree by its ID.
        For looking up a transaction instead of a transaction tree, please see GetFlatTransactionById
        Errors:
        - ``UNAUTHENTICATED``: if the request does not include a valid access token
        - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
        - ``NOT_FOUND``: if the request does not include a valid ledger id or no such transaction exists
        - ``INVALID_ARGUMENT``: if the payload is malformed or is missing required fields (e.g. if requesting parties are invalid or empty)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFlatTransactionByEventId(self, request, context):
        """Lookup a transaction by the ID of an event that appears within it.
        Errors:
        - ``UNAUTHENTICATED``: if the request does not include a valid access token
        - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
        - ``NOT_FOUND``: if the request does not include a valid ledger id or no such transaction exists
        - ``INVALID_ARGUMENT``: if the payload is malformed or is missing required fields (e.g. if requesting parties are invalid or empty)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFlatTransactionById(self, request, context):
        """Lookup a transaction by its ID.
        Errors:
        - ``UNAUTHENTICATED``: if the request does not include a valid access token
        - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
        - ``NOT_FOUND``: if the request does not include a valid ledger id or no such transaction exists
        - ``INVALID_ARGUMENT``: if the payload is malformed or is missing required fields (e.g. if requesting parties are invalid or empty)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLedgerEnd(self, request, context):
        """Get the current ledger end.
        Subscriptions started with the returned offset will serve transactions created after this RPC was called.
        Errors:
        - ``UNAUTHENTICATED``: if the request does not include a valid access token
        - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
        - ``NOT_FOUND``: if the request does not include a valid ledger id or no such transaction exists
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransactionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTransactions': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTransactions,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionsRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionsResponse.SerializeToString,
            ),
            'GetTransactionTrees': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTransactionTrees,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionsRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionTreesResponse.SerializeToString,
            ),
            'GetTransactionByEventId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTransactionByEventId,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionByEventIdRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionResponse.SerializeToString,
            ),
            'GetTransactionById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTransactionById,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionByIdRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionResponse.SerializeToString,
            ),
            'GetFlatTransactionByEventId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFlatTransactionByEventId,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionByEventIdRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetFlatTransactionResponse.SerializeToString,
            ),
            'GetFlatTransactionById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFlatTransactionById,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionByIdRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetFlatTransactionResponse.SerializeToString,
            ),
            'GetLedgerEnd': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLedgerEnd,
                    request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetLedgerEndRequest.FromString,
                    response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetLedgerEndResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.daml.ledger.api.v1.TransactionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TransactionService(object):
    """Allows clients to read transactions from the ledger.
    """

    @staticmethod
    def GetTransactions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/com.daml.ledger.api.v1.TransactionService/GetTransactions',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionsRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTransactionTrees(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/com.daml.ledger.api.v1.TransactionService/GetTransactionTrees',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionsRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionTreesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTransactionByEventId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.TransactionService/GetTransactionByEventId',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionByEventIdRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTransactionById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.TransactionService/GetTransactionById',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionByIdRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFlatTransactionByEventId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.TransactionService/GetFlatTransactionByEventId',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionByEventIdRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetFlatTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFlatTransactionById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.TransactionService/GetFlatTransactionById',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetTransactionByIdRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetFlatTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLedgerEnd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.daml.ledger.api.v1.TransactionService/GetLedgerEnd',
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetLedgerEndRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__service__pb2.GetLedgerEndResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
