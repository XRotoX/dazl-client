# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.duration_pb2 import Duration
from google.protobuf.message import Message as _Message

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "GetLedgerConfigurationRequest",
    "GetLedgerConfigurationResponse",
    "LedgerConfiguration",
]


class GetLedgerConfigurationRequest(_Message):
    ledger_id: _builtins.str
    def __init__(self, *, ledger_id: _typing.Optional[_builtins.str] = ...): ...
    def HasField(self, field_name: _L["ledger_id"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["ledger_id"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetLedgerConfigurationResponse(_Message):
    @property
    def ledger_configuration(self) -> LedgerConfiguration: ...
    def __init__(self, *, ledger_configuration: _typing.Optional[LedgerConfiguration] = ...): ...
    def HasField(self, field_name: _L["ledger_configuration"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["ledger_configuration"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class LedgerConfiguration(_Message):
    @property
    def max_deduplication_duration(self) -> Duration: ...
    def __init__(self, *, max_deduplication_duration: _typing.Optional[Duration] = ...): ...
    def HasField(self, field_name: _L["max_deduplication_duration"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["max_deduplication_duration"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
