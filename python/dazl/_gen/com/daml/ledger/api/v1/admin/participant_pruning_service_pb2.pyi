# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

from typing import (
    Any as __Any,
    Dict as __Map,
    List as _List,
    Literal as __Literal,
    NoReturn as __Void,
    Optional as __Optional,
    Sequence as __Sequence,
    Tuple as __Tuple,
    TypeVar as __TypeVar,
)

from google.protobuf.descriptor import FieldDescriptor as __FieldDescriptor
from google.protobuf.message import Message as __Message

__all__ = [
    "PruneRequest",
    "PruneResponse",
]

class PruneRequest(__Message):
    prune_up_to: str
    submission_id: str
    def __init__(self, prune_up_to: str = ..., submission_id: str = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: PruneRequest) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["prune_up_to", "submission_id"]) -> bool: ...
    def ClearField(self, field_name: __Literal["prune_up_to", "submission_id"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class PruneResponse(__Message):
    def __init__(self) -> None: ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: PruneResponse) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Void) -> __Void: ...
    def ClearField(self, field_name: __Void) -> __Void: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...
