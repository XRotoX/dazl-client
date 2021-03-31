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

from ........damlast.daml_types import Party

__all__ = [
    "GetParticipantIdRequest",
    "GetParticipantIdResponse",
    "GetPartiesRequest",
    "GetPartiesResponse",
    "ListKnownPartiesRequest",
    "ListKnownPartiesResponse",
    "AllocatePartyRequest",
    "AllocatePartyResponse",
    "PartyDetails",
]

T = __TypeVar("T")

class __List(_List[T]):
    def add(self) -> T: ...

class GetParticipantIdRequest(__Message):
    def __init__(self) -> None: ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: GetParticipantIdRequest) -> None: ...
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

class GetParticipantIdResponse(__Message):
    participant_id: str
    def __init__(self, participant_id: str = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: GetParticipantIdResponse) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["participant_id"]) -> bool: ...
    def ClearField(self, field_name: __Literal["participant_id"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class GetPartiesRequest(__Message):
    parties: __List[Party]
    def __init__(self, parties: __Sequence[Party] = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: GetPartiesRequest) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["parties"]) -> bool: ...
    def ClearField(self, field_name: __Literal["parties"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class GetPartiesResponse(__Message):
    party_details: __List[PartyDetails]
    def __init__(self, party_details: __Sequence[PartyDetails] = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: GetPartiesResponse) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["party_details"]) -> bool: ...
    def ClearField(self, field_name: __Literal["party_details"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class ListKnownPartiesRequest(__Message):
    def __init__(self) -> None: ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: ListKnownPartiesRequest) -> None: ...
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

class ListKnownPartiesResponse(__Message):
    party_details: __List[PartyDetails]
    def __init__(self, party_details: __Sequence[PartyDetails] = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: ListKnownPartiesResponse) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["party_details"]) -> bool: ...
    def ClearField(self, field_name: __Literal["party_details"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class AllocatePartyRequest(__Message):
    party_id_hint: Party
    display_name: str
    def __init__(self, party_id_hint: Party = ..., display_name: str = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: AllocatePartyRequest) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["party_id_hint", "display_name"]) -> bool: ...
    def ClearField(self, field_name: __Literal["party_id_hint", "display_name"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class AllocatePartyResponse(__Message):
    party_details: __List[PartyDetails]
    def __init__(self, party_details: __Sequence[PartyDetails] = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: AllocatePartyResponse) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["party_details"]) -> bool: ...
    def ClearField(self, field_name: __Literal["party_details"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class PartyDetails(__Message):
    party: Party
    display_name: str
    is_local: bool
    def __init__(self, party: Party = ..., display_name: str = ..., is_local: bool = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: PartyDetails) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["party", "display_name", "is_local"]) -> bool: ...
    def ClearField(self, field_name: __Literal["party", "display_name", "is_local"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...
