# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/transaction_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import ledger_offset_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__offset__pb2
from . import transaction_filter_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__filter__pb2
from . import transaction_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__pb2
from . import trace_context_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/transaction_service.proto',
  package='com.daml.ledger.api.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.daml.ledger.api.v1B\034TransactionServiceOuterClass\252\002\026Com.Daml.Ledger.Api.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0com/daml/ledger/api/v1/transaction_service.proto\x12\x16\x63om.daml.ledger.api.v1\x1a*com/daml/ledger/api/v1/ledger_offset.proto\x1a/com/daml/ledger/api/v1/transaction_filter.proto\x1a(com/daml/ledger/api/v1/transaction.proto\x1a*com/daml/ledger/api/v1/trace_context.proto\"\x9d\x02\n\x16GetTransactionsRequest\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x33\n\x05\x62\x65gin\x18\x02 \x01(\x0b\x32$.com.daml.ledger.api.v1.LedgerOffset\x12\x31\n\x03\x65nd\x18\x03 \x01(\x0b\x32$.com.daml.ledger.api.v1.LedgerOffset\x12\x39\n\x06\x66ilter\x18\x04 \x01(\x0b\x32).com.daml.ledger.api.v1.TransactionFilter\x12\x0f\n\x07verbose\x18\x05 \x01(\x08\x12<\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32$.com.daml.ledger.api.v1.TraceContext\"T\n\x17GetTransactionsResponse\x12\x39\n\x0ctransactions\x18\x01 \x03(\x0b\x32#.com.daml.ledger.api.v1.Transaction\"\\\n\x1bGetTransactionTreesResponse\x12=\n\x0ctransactions\x18\x01 \x03(\x0b\x32\'.com.daml.ledger.api.v1.TransactionTree\"\x9f\x01\n\x1eGetTransactionByEventIdRequest\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\t\x12\x1a\n\x12requesting_parties\x18\x03 \x03(\t\x12<\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32$.com.daml.ledger.api.v1.TraceContext\"\xa0\x01\n\x19GetTransactionByIdRequest\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x16\n\x0etransaction_id\x18\x02 \x01(\t\x12\x1a\n\x12requesting_parties\x18\x03 \x03(\t\x12<\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32$.com.daml.ledger.api.v1.TraceContext\"V\n\x16GetTransactionResponse\x12<\n\x0btransaction\x18\x01 \x01(\x0b\x32\'.com.daml.ledger.api.v1.TransactionTree\"V\n\x1aGetFlatTransactionResponse\x12\x38\n\x0btransaction\x18\x01 \x01(\x0b\x32#.com.daml.ledger.api.v1.Transaction\"f\n\x13GetLedgerEndRequest\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12<\n\rtrace_context\x18\xe8\x07 \x01(\x0b\x32$.com.daml.ledger.api.v1.TraceContext\"L\n\x14GetLedgerEndResponse\x12\x34\n\x06offset\x18\x01 \x01(\x0b\x32$.com.daml.ledger.api.v1.LedgerOffset2\xfd\x06\n\x12TransactionService\x12t\n\x0fGetTransactions\x12..com.daml.ledger.api.v1.GetTransactionsRequest\x1a/.com.daml.ledger.api.v1.GetTransactionsResponse0\x01\x12|\n\x13GetTransactionTrees\x12..com.daml.ledger.api.v1.GetTransactionsRequest\x1a\x33.com.daml.ledger.api.v1.GetTransactionTreesResponse0\x01\x12\x81\x01\n\x17GetTransactionByEventId\x12\x36.com.daml.ledger.api.v1.GetTransactionByEventIdRequest\x1a..com.daml.ledger.api.v1.GetTransactionResponse\x12w\n\x12GetTransactionById\x12\x31.com.daml.ledger.api.v1.GetTransactionByIdRequest\x1a..com.daml.ledger.api.v1.GetTransactionResponse\x12\x89\x01\n\x1bGetFlatTransactionByEventId\x12\x36.com.daml.ledger.api.v1.GetTransactionByEventIdRequest\x1a\x32.com.daml.ledger.api.v1.GetFlatTransactionResponse\x12\x7f\n\x16GetFlatTransactionById\x12\x31.com.daml.ledger.api.v1.GetTransactionByIdRequest\x1a\x32.com.daml.ledger.api.v1.GetFlatTransactionResponse\x12i\n\x0cGetLedgerEnd\x12+.com.daml.ledger.api.v1.GetLedgerEndRequest\x1a,.com.daml.ledger.api.v1.GetLedgerEndResponseBO\n\x16\x63om.daml.ledger.api.v1B\x1cTransactionServiceOuterClass\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3'
  ,
  dependencies=[com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__offset__pb2.DESCRIPTOR,com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__filter__pb2.DESCRIPTOR,com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__pb2.DESCRIPTOR,com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2.DESCRIPTOR,])




_GETTRANSACTIONSREQUEST = _descriptor.Descriptor(
  name='GetTransactionsRequest',
  full_name='com.daml.ledger.api.v1.GetTransactionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_id', full_name='com.daml.ledger.api.v1.GetTransactionsRequest.ledger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='begin', full_name='com.daml.ledger.api.v1.GetTransactionsRequest.begin', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='com.daml.ledger.api.v1.GetTransactionsRequest.end', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='com.daml.ledger.api.v1.GetTransactionsRequest.filter', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='verbose', full_name='com.daml.ledger.api.v1.GetTransactionsRequest.verbose', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.daml.ledger.api.v1.GetTransactionsRequest.trace_context', index=5,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=256,
  serialized_end=541,
)


_GETTRANSACTIONSRESPONSE = _descriptor.Descriptor(
  name='GetTransactionsResponse',
  full_name='com.daml.ledger.api.v1.GetTransactionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='com.daml.ledger.api.v1.GetTransactionsResponse.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=543,
  serialized_end=627,
)


_GETTRANSACTIONTREESRESPONSE = _descriptor.Descriptor(
  name='GetTransactionTreesResponse',
  full_name='com.daml.ledger.api.v1.GetTransactionTreesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='com.daml.ledger.api.v1.GetTransactionTreesResponse.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=629,
  serialized_end=721,
)


_GETTRANSACTIONBYEVENTIDREQUEST = _descriptor.Descriptor(
  name='GetTransactionByEventIdRequest',
  full_name='com.daml.ledger.api.v1.GetTransactionByEventIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_id', full_name='com.daml.ledger.api.v1.GetTransactionByEventIdRequest.ledger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_id', full_name='com.daml.ledger.api.v1.GetTransactionByEventIdRequest.event_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requesting_parties', full_name='com.daml.ledger.api.v1.GetTransactionByEventIdRequest.requesting_parties', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.daml.ledger.api.v1.GetTransactionByEventIdRequest.trace_context', index=3,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=724,
  serialized_end=883,
)


_GETTRANSACTIONBYIDREQUEST = _descriptor.Descriptor(
  name='GetTransactionByIdRequest',
  full_name='com.daml.ledger.api.v1.GetTransactionByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_id', full_name='com.daml.ledger.api.v1.GetTransactionByIdRequest.ledger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='com.daml.ledger.api.v1.GetTransactionByIdRequest.transaction_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requesting_parties', full_name='com.daml.ledger.api.v1.GetTransactionByIdRequest.requesting_parties', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.daml.ledger.api.v1.GetTransactionByIdRequest.trace_context', index=3,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=886,
  serialized_end=1046,
)


_GETTRANSACTIONRESPONSE = _descriptor.Descriptor(
  name='GetTransactionResponse',
  full_name='com.daml.ledger.api.v1.GetTransactionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='com.daml.ledger.api.v1.GetTransactionResponse.transaction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1048,
  serialized_end=1134,
)


_GETFLATTRANSACTIONRESPONSE = _descriptor.Descriptor(
  name='GetFlatTransactionResponse',
  full_name='com.daml.ledger.api.v1.GetFlatTransactionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='com.daml.ledger.api.v1.GetFlatTransactionResponse.transaction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1136,
  serialized_end=1222,
)


_GETLEDGERENDREQUEST = _descriptor.Descriptor(
  name='GetLedgerEndRequest',
  full_name='com.daml.ledger.api.v1.GetLedgerEndRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ledger_id', full_name='com.daml.ledger.api.v1.GetLedgerEndRequest.ledger_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_context', full_name='com.daml.ledger.api.v1.GetLedgerEndRequest.trace_context', index=1,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1224,
  serialized_end=1326,
)


_GETLEDGERENDRESPONSE = _descriptor.Descriptor(
  name='GetLedgerEndResponse',
  full_name='com.daml.ledger.api.v1.GetLedgerEndResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='com.daml.ledger.api.v1.GetLedgerEndResponse.offset', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1328,
  serialized_end=1404,
)

_GETTRANSACTIONSREQUEST.fields_by_name['begin'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__offset__pb2._LEDGEROFFSET
_GETTRANSACTIONSREQUEST.fields_by_name['end'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__offset__pb2._LEDGEROFFSET
_GETTRANSACTIONSREQUEST.fields_by_name['filter'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__filter__pb2._TRANSACTIONFILTER
_GETTRANSACTIONSREQUEST.fields_by_name['trace_context'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
_GETTRANSACTIONSRESPONSE.fields_by_name['transactions'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__pb2._TRANSACTION
_GETTRANSACTIONTREESRESPONSE.fields_by_name['transactions'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__pb2._TRANSACTIONTREE
_GETTRANSACTIONBYEVENTIDREQUEST.fields_by_name['trace_context'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
_GETTRANSACTIONBYIDREQUEST.fields_by_name['trace_context'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
_GETTRANSACTIONRESPONSE.fields_by_name['transaction'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__pb2._TRANSACTIONTREE
_GETFLATTRANSACTIONRESPONSE.fields_by_name['transaction'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_transaction__pb2._TRANSACTION
_GETLEDGERENDREQUEST.fields_by_name['trace_context'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_trace__context__pb2._TRACECONTEXT
_GETLEDGERENDRESPONSE.fields_by_name['offset'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_ledger__offset__pb2._LEDGEROFFSET
DESCRIPTOR.message_types_by_name['GetTransactionsRequest'] = _GETTRANSACTIONSREQUEST
DESCRIPTOR.message_types_by_name['GetTransactionsResponse'] = _GETTRANSACTIONSRESPONSE
DESCRIPTOR.message_types_by_name['GetTransactionTreesResponse'] = _GETTRANSACTIONTREESRESPONSE
DESCRIPTOR.message_types_by_name['GetTransactionByEventIdRequest'] = _GETTRANSACTIONBYEVENTIDREQUEST
DESCRIPTOR.message_types_by_name['GetTransactionByIdRequest'] = _GETTRANSACTIONBYIDREQUEST
DESCRIPTOR.message_types_by_name['GetTransactionResponse'] = _GETTRANSACTIONRESPONSE
DESCRIPTOR.message_types_by_name['GetFlatTransactionResponse'] = _GETFLATTRANSACTIONRESPONSE
DESCRIPTOR.message_types_by_name['GetLedgerEndRequest'] = _GETLEDGERENDREQUEST
DESCRIPTOR.message_types_by_name['GetLedgerEndResponse'] = _GETLEDGERENDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTransactionsRequest = _reflection.GeneratedProtocolMessageType('GetTransactionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSACTIONSREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.transaction_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.GetTransactionsRequest)
  })
_sym_db.RegisterMessage(GetTransactionsRequest)

GetTransactionsResponse = _reflection.GeneratedProtocolMessageType('GetTransactionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSACTIONSRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.transaction_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.GetTransactionsResponse)
  })
_sym_db.RegisterMessage(GetTransactionsResponse)

GetTransactionTreesResponse = _reflection.GeneratedProtocolMessageType('GetTransactionTreesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSACTIONTREESRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.transaction_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.GetTransactionTreesResponse)
  })
_sym_db.RegisterMessage(GetTransactionTreesResponse)

GetTransactionByEventIdRequest = _reflection.GeneratedProtocolMessageType('GetTransactionByEventIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSACTIONBYEVENTIDREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.transaction_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.GetTransactionByEventIdRequest)
  })
_sym_db.RegisterMessage(GetTransactionByEventIdRequest)

GetTransactionByIdRequest = _reflection.GeneratedProtocolMessageType('GetTransactionByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSACTIONBYIDREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.transaction_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.GetTransactionByIdRequest)
  })
_sym_db.RegisterMessage(GetTransactionByIdRequest)

GetTransactionResponse = _reflection.GeneratedProtocolMessageType('GetTransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSACTIONRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.transaction_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.GetTransactionResponse)
  })
_sym_db.RegisterMessage(GetTransactionResponse)

GetFlatTransactionResponse = _reflection.GeneratedProtocolMessageType('GetFlatTransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFLATTRANSACTIONRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.transaction_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.GetFlatTransactionResponse)
  })
_sym_db.RegisterMessage(GetFlatTransactionResponse)

GetLedgerEndRequest = _reflection.GeneratedProtocolMessageType('GetLedgerEndRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLEDGERENDREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.transaction_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.GetLedgerEndRequest)
  })
_sym_db.RegisterMessage(GetLedgerEndRequest)

GetLedgerEndResponse = _reflection.GeneratedProtocolMessageType('GetLedgerEndResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLEDGERENDRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.transaction_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.GetLedgerEndResponse)
  })
_sym_db.RegisterMessage(GetLedgerEndResponse)


DESCRIPTOR._options = None

_TRANSACTIONSERVICE = _descriptor.ServiceDescriptor(
  name='TransactionService',
  full_name='com.daml.ledger.api.v1.TransactionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1407,
  serialized_end=2300,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTransactions',
    full_name='com.daml.ledger.api.v1.TransactionService.GetTransactions',
    index=0,
    containing_service=None,
    input_type=_GETTRANSACTIONSREQUEST,
    output_type=_GETTRANSACTIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTransactionTrees',
    full_name='com.daml.ledger.api.v1.TransactionService.GetTransactionTrees',
    index=1,
    containing_service=None,
    input_type=_GETTRANSACTIONSREQUEST,
    output_type=_GETTRANSACTIONTREESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTransactionByEventId',
    full_name='com.daml.ledger.api.v1.TransactionService.GetTransactionByEventId',
    index=2,
    containing_service=None,
    input_type=_GETTRANSACTIONBYEVENTIDREQUEST,
    output_type=_GETTRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTransactionById',
    full_name='com.daml.ledger.api.v1.TransactionService.GetTransactionById',
    index=3,
    containing_service=None,
    input_type=_GETTRANSACTIONBYIDREQUEST,
    output_type=_GETTRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetFlatTransactionByEventId',
    full_name='com.daml.ledger.api.v1.TransactionService.GetFlatTransactionByEventId',
    index=4,
    containing_service=None,
    input_type=_GETTRANSACTIONBYEVENTIDREQUEST,
    output_type=_GETFLATTRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetFlatTransactionById',
    full_name='com.daml.ledger.api.v1.TransactionService.GetFlatTransactionById',
    index=5,
    containing_service=None,
    input_type=_GETTRANSACTIONBYIDREQUEST,
    output_type=_GETFLATTRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLedgerEnd',
    full_name='com.daml.ledger.api.v1.TransactionService.GetLedgerEnd',
    index=6,
    containing_service=None,
    input_type=_GETLEDGERENDREQUEST,
    output_type=_GETLEDGERENDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSACTIONSERVICE)

DESCRIPTOR.services_by_name['TransactionService'] = _TRANSACTIONSERVICE

# @@protoc_insertion_point(module_scope)
