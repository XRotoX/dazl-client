# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.duration_pb2 import Duration
from google.protobuf.internal.containers import RepeatedCompositeFieldContainer, RepeatedScalarFieldContainer
from google.protobuf.message import Message as _Message
from google.protobuf.timestamp_pb2 import Timestamp

from .value_pb2 import Identifier, Record, Value

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "Commands",
    "Command",
    "CreateCommand",
    "ExerciseCommand",
    "ExerciseByKeyCommand",
    "CreateAndExerciseCommand",
]


class Commands(_Message):
    ledger_id: _builtins.str
    workflow_id: _builtins.str
    application_id: _builtins.str
    command_id: _builtins.str
    party: _builtins.str
    @property
    def commands(self) -> RepeatedCompositeFieldContainer[Command]: ...
    @property
    def deduplication_time(self) -> Duration: ...
    @property
    def deduplication_duration(self) -> Duration: ...
    @property
    def min_ledger_time_abs(self) -> Timestamp: ...
    @property
    def min_ledger_time_rel(self) -> Duration: ...
    @property
    def act_as(self) -> RepeatedScalarFieldContainer[_builtins.str]: ...
    @property
    def read_as(self) -> RepeatedScalarFieldContainer[_builtins.str]: ...
    submission_id: _builtins.str
    @_typing.overload
    def __init__(self, *, ledger_id: _typing.Optional[_builtins.str] = ..., workflow_id: _typing.Optional[_builtins.str] = ..., application_id: _typing.Optional[_builtins.str] = ..., command_id: _typing.Optional[_builtins.str] = ..., party: _typing.Optional[_builtins.str] = ..., commands: _typing.Optional[_typing.Iterable[Command]] = ..., min_ledger_time_abs: _typing.Optional[Timestamp] = ..., min_ledger_time_rel: _typing.Optional[Duration] = ..., act_as: _typing.Optional[_typing.Iterable[_builtins.str]] = ..., read_as: _typing.Optional[_typing.Iterable[_builtins.str]] = ..., submission_id: _typing.Optional[_builtins.str] = ...): ...
    @_typing.overload
    def __init__(self, *, ledger_id: _typing.Optional[_builtins.str] = ..., workflow_id: _typing.Optional[_builtins.str] = ..., application_id: _typing.Optional[_builtins.str] = ..., command_id: _typing.Optional[_builtins.str] = ..., party: _typing.Optional[_builtins.str] = ..., commands: _typing.Optional[_typing.Iterable[Command]] = ..., deduplication_time: Duration = ..., min_ledger_time_abs: _typing.Optional[Timestamp] = ..., min_ledger_time_rel: _typing.Optional[Duration] = ..., act_as: _typing.Optional[_typing.Iterable[_builtins.str]] = ..., read_as: _typing.Optional[_typing.Iterable[_builtins.str]] = ..., submission_id: _typing.Optional[_builtins.str] = ...): ...
    @_typing.overload
    def __init__(self, *, ledger_id: _typing.Optional[_builtins.str] = ..., workflow_id: _typing.Optional[_builtins.str] = ..., application_id: _typing.Optional[_builtins.str] = ..., command_id: _typing.Optional[_builtins.str] = ..., party: _typing.Optional[_builtins.str] = ..., commands: _typing.Optional[_typing.Iterable[Command]] = ..., deduplication_duration: Duration = ..., min_ledger_time_abs: _typing.Optional[Timestamp] = ..., min_ledger_time_rel: _typing.Optional[Duration] = ..., act_as: _typing.Optional[_typing.Iterable[_builtins.str]] = ..., read_as: _typing.Optional[_typing.Iterable[_builtins.str]] = ..., submission_id: _typing.Optional[_builtins.str] = ...): ...
    def HasField(self, field_name: _L["ledger_id", "workflow_id", "application_id", "command_id", "party", "commands", "deduplication_period", "deduplication_time", "deduplication_duration", "min_ledger_time_abs", "min_ledger_time_rel", "act_as", "read_as", "submission_id"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["ledger_id", "workflow_id", "application_id", "command_id", "party", "commands", "deduplication_period", "deduplication_time", "deduplication_duration", "min_ledger_time_abs", "min_ledger_time_rel", "act_as", "read_as", "submission_id"]) -> None: ...
    def WhichOneof(self, oneof_group: _L["deduplication_period"]) -> _L[None, "deduplication_time", "deduplication_duration"]: ...

class Command(_Message):
    @property
    def create(self) -> CreateCommand: ...
    @property
    def exercise(self) -> ExerciseCommand: ...
    @property
    def exerciseByKey(self) -> ExerciseByKeyCommand: ...
    @property
    def createAndExercise(self) -> CreateAndExerciseCommand: ...
    @_typing.overload
    def __init__(self): ...
    @_typing.overload
    def __init__(self, *, create: CreateCommand = ...): ...
    @_typing.overload
    def __init__(self, *, exercise: ExerciseCommand = ...): ...
    @_typing.overload
    def __init__(self, *, exerciseByKey: ExerciseByKeyCommand = ...): ...
    @_typing.overload
    def __init__(self, *, createAndExercise: CreateAndExerciseCommand = ...): ...
    def HasField(self, field_name: _L["command", "create", "exercise", "exerciseByKey", "createAndExercise"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["command", "create", "exercise", "exerciseByKey", "createAndExercise"]) -> None: ...
    def WhichOneof(self, oneof_group: _L["command"]) -> _L[None, "create", "exercise", "exerciseByKey", "createAndExercise"]: ...

class CreateCommand(_Message):
    @property
    def template_id(self) -> Identifier: ...
    @property
    def create_arguments(self) -> Record: ...
    def __init__(self, *, template_id: _typing.Optional[Identifier] = ..., create_arguments: _typing.Optional[Record] = ...): ...
    def HasField(self, field_name: _L["template_id", "create_arguments"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["template_id", "create_arguments"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ExerciseCommand(_Message):
    @property
    def template_id(self) -> Identifier: ...
    contract_id: _builtins.str
    choice: _builtins.str
    @property
    def choice_argument(self) -> Value: ...
    def __init__(self, *, template_id: _typing.Optional[Identifier] = ..., contract_id: _typing.Optional[_builtins.str] = ..., choice: _typing.Optional[_builtins.str] = ..., choice_argument: _typing.Optional[Value] = ...): ...
    def HasField(self, field_name: _L["template_id", "contract_id", "choice", "choice_argument"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["template_id", "contract_id", "choice", "choice_argument"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ExerciseByKeyCommand(_Message):
    @property
    def template_id(self) -> Identifier: ...
    @property
    def contract_key(self) -> Value: ...
    choice: _builtins.str
    @property
    def choice_argument(self) -> Value: ...
    def __init__(self, *, template_id: _typing.Optional[Identifier] = ..., contract_key: _typing.Optional[Value] = ..., choice: _typing.Optional[_builtins.str] = ..., choice_argument: _typing.Optional[Value] = ...): ...
    def HasField(self, field_name: _L["template_id", "contract_key", "choice", "choice_argument"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["template_id", "contract_key", "choice", "choice_argument"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class CreateAndExerciseCommand(_Message):
    @property
    def template_id(self) -> Identifier: ...
    @property
    def create_arguments(self) -> Record: ...
    choice: _builtins.str
    @property
    def choice_argument(self) -> Value: ...
    def __init__(self, *, template_id: _typing.Optional[Identifier] = ..., create_arguments: _typing.Optional[Record] = ..., choice: _typing.Optional[_builtins.str] = ..., choice_argument: _typing.Optional[Value] = ...): ...
    def HasField(self, field_name: _L["template_id", "create_arguments", "choice", "choice_argument"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["template_id", "create_arguments", "choice", "choice_argument"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
