# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .party_management_service_pb2 import AllocatePartyRequest, AllocatePartyResponse, GetParticipantIdRequest, GetParticipantIdResponse, GetPartiesRequest, GetPartiesResponse, ListKnownPartiesRequest, ListKnownPartiesResponse

__all__ = [
    "PartyManagementServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class PartyManagementServiceStub:
    @classmethod
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _PartyManagementServiceBlockingStub: ...  # type: ignore
    @classmethod
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _PartyManagementServiceAsyncStub: ...  # type: ignore
    def GetParticipantId(self, __1: GetParticipantIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetParticipantIdResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetParticipantIdResponse]]: ...
    def GetParties(self, __1: GetPartiesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetPartiesResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetPartiesResponse]]: ...
    def ListKnownParties(self, __1: ListKnownPartiesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[ListKnownPartiesResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, ListKnownPartiesResponse]]: ...
    def AllocateParty(self, __1: AllocatePartyRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[AllocatePartyResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, AllocatePartyResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _PartyManagementServiceBlockingStub(PartyManagementServiceStub):
    def GetParticipantId(self, __1: GetParticipantIdRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetParticipantIdResponse: ...
    def GetParties(self, __1: GetPartiesRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetPartiesResponse: ...
    def ListKnownParties(self, __1: ListKnownPartiesRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ListKnownPartiesResponse: ...
    def AllocateParty(self, __1: AllocatePartyRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AllocatePartyResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _PartyManagementServiceAsyncStub(PartyManagementServiceStub):
    def GetParticipantId(self, __1: GetParticipantIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetParticipantIdResponse]: ...
    def GetParties(self, __1: GetPartiesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetPartiesResponse]: ...
    def ListKnownParties(self, __1: ListKnownPartiesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, ListKnownPartiesResponse]: ...
    def AllocateParty(self, __1: AllocatePartyRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, AllocatePartyResponse]: ...
