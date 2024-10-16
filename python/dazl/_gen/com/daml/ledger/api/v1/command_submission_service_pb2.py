# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/command_submission_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import commands_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_commands__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/command_submission_service.proto',
  package='com.daml.ledger.api.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.daml.ledger.api.v1B\"CommandSubmissionServiceOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7com/daml/ledger/api/v1/command_submission_service.proto\x12\x16\x63om.daml.ledger.api.v1\x1a%com/daml/ledger/api/v1/commands.proto\x1a\x1bgoogle/protobuf/empty.proto\"M\n\rSubmitRequest\x12<\n\x08\x63ommands\x18\x01 \x01(\x0b\x32 .com.daml.ledger.api.v1.CommandsR\x08\x63ommands2c\n\x18\x43ommandSubmissionService\x12G\n\x06Submit\x12%.com.daml.ledger.api.v1.SubmitRequest\x1a\x16.google.protobuf.EmptyB\x9c\x01\n\x16\x63om.daml.ledger.api.v1B\"CommandSubmissionServiceOuterClassZEgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3'
  ,
  dependencies=[com_dot_daml_dot_ledger_dot_api_dot_v1_dot_commands__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_SUBMITREQUEST = _descriptor.Descriptor(
  name='SubmitRequest',
  full_name='com.daml.ledger.api.v1.SubmitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='commands', full_name='com.daml.ledger.api.v1.SubmitRequest.commands', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='commands', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=151,
  serialized_end=228,
)

_SUBMITREQUEST.fields_by_name['commands'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_commands__pb2._COMMANDS
DESCRIPTOR.message_types_by_name['SubmitRequest'] = _SUBMITREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmitRequest = _reflection.GeneratedProtocolMessageType('SubmitRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.command_submission_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.SubmitRequest)
  })
_sym_db.RegisterMessage(SubmitRequest)


DESCRIPTOR._options = None

_COMMANDSUBMISSIONSERVICE = _descriptor.ServiceDescriptor(
  name='CommandSubmissionService',
  full_name='com.daml.ledger.api.v1.CommandSubmissionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=230,
  serialized_end=329,
  methods=[
  _descriptor.MethodDescriptor(
    name='Submit',
    full_name='com.daml.ledger.api.v1.CommandSubmissionService.Submit',
    index=0,
    containing_service=None,
    input_type=_SUBMITREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMANDSUBMISSIONSERVICE)

DESCRIPTOR.services_by_name['CommandSubmissionService'] = _COMMANDSUBMISSIONSERVICE

# @@protoc_insertion_point(module_scope)
