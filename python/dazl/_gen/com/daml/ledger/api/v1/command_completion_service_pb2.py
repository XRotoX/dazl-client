# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/command_completion_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import completion_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_completion__pb2
from . import ledger_offset_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__offset__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/command_completion_service.proto',
  package='com.daml.ledger.api.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.daml.ledger.api.v1B\"CommandCompletionServiceOuterClassZOgithub.com/digital-asset/dazl-client/go/v7/pkg/generated/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7com/daml/ledger/api/v1/command_completion_service.proto\x12\x16\x63om.daml.ledger.api.v1\x1a\'com/daml/ledger/api/v1/completion.proto\x1a*com/daml/ledger/api/v1/ledger_offset.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb5\x01\n\x17\x43ompletionStreamRequest\x12\x1b\n\tledger_id\x18\x01 \x01(\tR\x08ledgerId\x12%\n\x0e\x61pplication_id\x18\x02 \x01(\tR\rapplicationId\x12\x18\n\x07parties\x18\x03 \x03(\tR\x07parties\x12<\n\x06offset\x18\x04 \x01(\x0b\x32$.com.daml.ledger.api.v1.LedgerOffsetR\x06offset\"\xa4\x01\n\x18\x43ompletionStreamResponse\x12\x42\n\ncheckpoint\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.CheckpointR\ncheckpoint\x12\x44\n\x0b\x63ompletions\x18\x02 \x03(\x0b\x32\".com.daml.ledger.api.v1.CompletionR\x0b\x63ompletions\"\x87\x01\n\nCheckpoint\x12;\n\x0brecord_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nrecordTime\x12<\n\x06offset\x18\x02 \x01(\x0b\x32$.com.daml.ledger.api.v1.LedgerOffsetR\x06offset\"3\n\x14\x43ompletionEndRequest\x12\x1b\n\tledger_id\x18\x01 \x01(\tR\x08ledgerId\"U\n\x15\x43ompletionEndResponse\x12<\n\x06offset\x18\x01 \x01(\x0b\x32$.com.daml.ledger.api.v1.LedgerOffsetR\x06offset2\x81\x02\n\x18\x43ommandCompletionService\x12w\n\x10\x43ompletionStream\x12/.com.daml.ledger.api.v1.CompletionStreamRequest\x1a\x30.com.daml.ledger.api.v1.CompletionStreamResponse0\x01\x12l\n\rCompletionEnd\x12,.com.daml.ledger.api.v1.CompletionEndRequest\x1a-.com.daml.ledger.api.v1.CompletionEndResponseB\xa6\x01\n\x16\x63om.daml.ledger.api.v1B\"CommandCompletionServiceOuterClassZOgithub.com/digital-asset/dazl-client/go/v7/pkg/generated/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3'
  ,
  dependencies=[com_dot_daml_dot_ledger_dot_api_dot_v1_dot_completion__pb2.DESCRIPTOR,com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__offset__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_COMPLETIONSTREAMREQUEST = _descriptor.Descriptor(
  name='CompletionStreamRequest',
  full_name='com.daml.ledger.api.v1.CompletionStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_id', full_name='com.daml.ledger.api.v1.CompletionStreamRequest.ledger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ledgerId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='application_id', full_name='com.daml.ledger.api.v1.CompletionStreamRequest.application_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='applicationId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parties', full_name='com.daml.ledger.api.v1.CompletionStreamRequest.parties', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parties', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='com.daml.ledger.api.v1.CompletionStreamRequest.offset', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='offset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=383,
)


_COMPLETIONSTREAMRESPONSE = _descriptor.Descriptor(
  name='CompletionStreamResponse',
  full_name='com.daml.ledger.api.v1.CompletionStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='checkpoint', full_name='com.daml.ledger.api.v1.CompletionStreamResponse.checkpoint', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='checkpoint', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completions', full_name='com.daml.ledger.api.v1.CompletionStreamResponse.completions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='completions', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=386,
  serialized_end=550,
)


_CHECKPOINT = _descriptor.Descriptor(
  name='Checkpoint',
  full_name='com.daml.ledger.api.v1.Checkpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_time', full_name='com.daml.ledger.api.v1.Checkpoint.record_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='recordTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='com.daml.ledger.api.v1.Checkpoint.offset', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='offset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=553,
  serialized_end=688,
)


_COMPLETIONENDREQUEST = _descriptor.Descriptor(
  name='CompletionEndRequest',
  full_name='com.daml.ledger.api.v1.CompletionEndRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_id', full_name='com.daml.ledger.api.v1.CompletionEndRequest.ledger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ledgerId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=690,
  serialized_end=741,
)


_COMPLETIONENDRESPONSE = _descriptor.Descriptor(
  name='CompletionEndResponse',
  full_name='com.daml.ledger.api.v1.CompletionEndResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='com.daml.ledger.api.v1.CompletionEndResponse.offset', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='offset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=743,
  serialized_end=828,
)

_COMPLETIONSTREAMREQUEST.fields_by_name['offset'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__offset__pb2._LEDGEROFFSET
_COMPLETIONSTREAMRESPONSE.fields_by_name['checkpoint'].message_type = _CHECKPOINT
_COMPLETIONSTREAMRESPONSE.fields_by_name['completions'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_completion__pb2._COMPLETION
_CHECKPOINT.fields_by_name['record_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CHECKPOINT.fields_by_name['offset'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__offset__pb2._LEDGEROFFSET
_COMPLETIONENDRESPONSE.fields_by_name['offset'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__offset__pb2._LEDGEROFFSET
DESCRIPTOR.message_types_by_name['CompletionStreamRequest'] = _COMPLETIONSTREAMREQUEST
DESCRIPTOR.message_types_by_name['CompletionStreamResponse'] = _COMPLETIONSTREAMRESPONSE
DESCRIPTOR.message_types_by_name['Checkpoint'] = _CHECKPOINT
DESCRIPTOR.message_types_by_name['CompletionEndRequest'] = _COMPLETIONENDREQUEST
DESCRIPTOR.message_types_by_name['CompletionEndResponse'] = _COMPLETIONENDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CompletionStreamRequest = _reflection.GeneratedProtocolMessageType('CompletionStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETIONSTREAMREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.command_completion_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.CompletionStreamRequest)
  })
_sym_db.RegisterMessage(CompletionStreamRequest)

CompletionStreamResponse = _reflection.GeneratedProtocolMessageType('CompletionStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETIONSTREAMRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.command_completion_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.CompletionStreamResponse)
  })
_sym_db.RegisterMessage(CompletionStreamResponse)

Checkpoint = _reflection.GeneratedProtocolMessageType('Checkpoint', (_message.Message,), {
  'DESCRIPTOR' : _CHECKPOINT,
  '__module__' : 'com.daml.ledger.api.v1.command_completion_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.Checkpoint)
  })
_sym_db.RegisterMessage(Checkpoint)

CompletionEndRequest = _reflection.GeneratedProtocolMessageType('CompletionEndRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETIONENDREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.command_completion_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.CompletionEndRequest)
  })
_sym_db.RegisterMessage(CompletionEndRequest)

CompletionEndResponse = _reflection.GeneratedProtocolMessageType('CompletionEndResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETIONENDRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.command_completion_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.CompletionEndResponse)
  })
_sym_db.RegisterMessage(CompletionEndResponse)


DESCRIPTOR._options = None

_COMMANDCOMPLETIONSERVICE = _descriptor.ServiceDescriptor(
  name='CommandCompletionService',
  full_name='com.daml.ledger.api.v1.CommandCompletionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=831,
  serialized_end=1088,
  methods=[
  _descriptor.MethodDescriptor(
    name='CompletionStream',
    full_name='com.daml.ledger.api.v1.CommandCompletionService.CompletionStream',
    index=0,
    containing_service=None,
    input_type=_COMPLETIONSTREAMREQUEST,
    output_type=_COMPLETIONSTREAMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CompletionEnd',
    full_name='com.daml.ledger.api.v1.CommandCompletionService.CompletionEnd',
    index=1,
    containing_service=None,
    input_type=_COMPLETIONENDREQUEST,
    output_type=_COMPLETIONENDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMANDCOMPLETIONSERVICE)

DESCRIPTOR.services_by_name['CommandCompletionService'] = _COMMANDCOMPLETIONSERVICE

# @@protoc_insertion_point(module_scope)
