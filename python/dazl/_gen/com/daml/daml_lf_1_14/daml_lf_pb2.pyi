# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

import typing as _typing

from google.protobuf.descriptor import FieldDescriptor as __FieldDescriptor
from google.protobuf.message import Message as __Message

from .....damlast.daml_lf_1 import PackageRef

__all__ = [
    "ArchivePayload",
    "Archive",
]

class ArchivePayload(__Message):
    # TODO: This is NOT yet a code-generated file. If we gave daml_lf_1 its real type, we would
    #  also need to type the entirety of the Daml-LF spec's protobuf file too. The only real fix
    #  to this is codegen.
    daml_lf_1: _typing.Any
    def __init__(self, *, daml_lf_1: _typing.Optional[_typing.Any] = ...): ...
    def __eq__(self, other_msg: _typing.Optional[_typing.Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: ArchivePayload) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def ParseFromString(self, serialized: bytes) -> int: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> _typing.Sequence[_typing.Tuple[__FieldDescriptor, _typing.Any]]: ...
    def HasField(self, field_name: _typing.Literal["daml_lf_1"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["daml_lf_1"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
    def HasExtension(self, extension_handle: _typing.Any) -> bool: ...
    def ClearExtension(self, extension_handle: _typing.Any) -> None: ...
    def UnknownFields(self) -> _typing.Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: _typing.Any) -> None: ...

class Archive(__Message):
    payload: bytes
    hash: PackageRef
    def __init__(self, *, payload: _typing.Optional[bytes] = ..., hash: _typing.Optional[PackageRef] = ...): ...
    def __eq__(self, other_msg: _typing.Optional[_typing.Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: Archive) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def ParseFromString(self, serialized: bytes) -> int: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> _typing.Sequence[_typing.Tuple[__FieldDescriptor, _typing.Any]]: ...
    def HasField(self, field_name: _typing.Literal["payload", "hash"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["payload", "hash"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
    def HasExtension(self, extension_handle: _typing.Any) -> bool: ...
    def ClearExtension(self, extension_handle: _typing.Any) -> None: ...
    def UnknownFields(self) -> _typing.Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: _typing.Any) -> None: ...
