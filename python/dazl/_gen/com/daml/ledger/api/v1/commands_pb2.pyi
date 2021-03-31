# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

from typing import (
    Any as __Any,
    Dict as __Map,
    List as __List,
    Literal as __Literal,
    NoReturn as __Void,
    Optional as __Optional,
    Sequence as __Sequence,
    Tuple as __Tuple,
    overload,
)

from google.protobuf.descriptor import FieldDescriptor as __FieldDescriptor
from google.protobuf.duration_pb2 import Duration
from google.protobuf.message import Message as __Message
from google.protobuf.timestamp_pb2 import Timestamp

from .......damlast.daml_types import Party
from .value_pb2 import Identifier, Record, Value

__all__ = [
    "Commands",
    "Command",
    "CreateCommand",
    "ExerciseCommand",
    "ExerciseByKeyCommand",
    "CreateAndExerciseCommand",
]

class Commands(__Message):
    ledger_id: str
    workflow_id: str
    application_id: str
    command_id: str
    party: Party
    commands: __List[Command]
    deduplication_time: Duration
    min_ledger_time_abs: Timestamp
    min_ledger_time_rel: Timestamp
    act_as: __List[Party]
    read_as: __List[Party]
    def __init__(self, ledger_id: str = ..., workflow_id: str = ..., application_id: str = ..., command_id: str = ..., party: Party = ..., commands: __Sequence[Command] = ..., deduplication_time: Duration = ..., min_ledger_time_abs: Timestamp = ..., min_ledger_time_rel: Timestamp = ..., act_as: __Sequence[Party] = ..., read_as: __Sequence[Party] = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: Commands) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def ParseFromString(self, serialized: bytes) -> int: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["ledger_id", "workflow_id", "application_id", "command_id", "party", "commands", "deduplication_time", "min_ledger_time_abs", "min_ledger_time_rel", "act_as", "read_as"]) -> bool: ...
    def ClearField(self, field_name: __Literal["ledger_id", "workflow_id", "application_id", "command_id", "party", "commands", "deduplication_time", "min_ledger_time_abs", "min_ledger_time_rel", "act_as", "read_as"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class Command(__Message):
    create: CreateCommand
    exercise: ExerciseCommand
    exerciseByKey: ExerciseByKeyCommand
    createAndExercise: CreateAndExerciseCommand
    @overload
    def __init__(self, create: CreateCommand = ...): ...
    @overload
    def __init__(self, exercise: ExerciseCommand = ...): ...
    @overload
    def __init__(self, exerciseByKey: ExerciseByKeyCommand = ...): ...
    @overload
    def __init__(self, createAndExercise: CreateAndExerciseCommand = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: Command) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["command", "create", "exercise", "exerciseByKey", "createAndExercise"]) -> bool: ...
    def ClearField(self, field_name: __Literal["command", "create", "exercise", "exerciseByKey", "createAndExercise"]) -> None: ...
    def WhichOneof(self, oneof_group: __Literal["command"]) -> __Literal["create", "exercise", "exerciseByKey", "createAndExercise"]: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class CreateCommand(__Message):
    template_id: Identifier
    create_arguments: Record
    def __init__(self, template_id: Identifier = ..., create_arguments: Record = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: CreateCommand) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["template_id", "create_arguments"]) -> bool: ...
    def ClearField(self, field_name: __Literal["template_id", "create_arguments"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class ExerciseCommand(__Message):
    template_id: Identifier
    contract_id: str
    choice: str
    choice_argument: Value
    def __init__(self, template_id: Identifier = ..., contract_id: str = ..., choice: str = ..., choice_argument: Value = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: ExerciseCommand) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["template_id", "contract_id", "choice", "choice_argument"]) -> bool: ...
    def ClearField(self, field_name: __Literal["template_id", "contract_id", "choice", "choice_argument"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class ExerciseByKeyCommand(__Message):
    template_id: Identifier
    contract_key: Value
    choice: str
    choice_argument: Value
    def __init__(self, template_id: Identifier = ..., contract_key: Value = ..., choice: str = ..., choice_argument: Value = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: ExerciseByKeyCommand) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["template_id", "contract_key", "choice", "choice_argument"]) -> bool: ...
    def ClearField(self, field_name: __Literal["template_id", "contract_key", "choice", "choice_argument"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...

class CreateAndExerciseCommand(__Message):
    template_id: Identifier
    create_arguments: Record
    choice: str
    choice_argument: Value
    def __init__(self, template_id: Identifier = ..., create_arguments: Record = ..., choice: str = ..., choice_argument: Value = ...): ...
    def __eq__(self, other_msg: __Optional[__Any]) -> bool: ...
    def __str__(self) -> str: ...
    def __unicode__(self) -> str: ...
    def MergeFrom(self, other_msg: CreateAndExerciseCommand) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> __Sequence[__Tuple[__FieldDescriptor, __Any]]: ...
    def HasField(self, field_name: __Literal["template_id", "create_arguments", "choice", "choice_argument"]) -> bool: ...
    def ClearField(self, field_name: __Literal["template_id", "create_arguments", "choice", "choice_argument"]) -> None: ...
    def WhichOneof(self, oneof_group: __Void) -> __Void: ...
    def HasExtension(self, extension_handle: __Any) -> bool: ...
    def ClearExtension(self, extension_handle: __Any) -> None: ...
    def UnknownFields(self) -> __Any: ...
    def DiscardUnknownFields(self) -> None: ...
    def ByteSize(self) -> int: ...
    def _SetListener(self, message_listener: __Any) -> None: ...
