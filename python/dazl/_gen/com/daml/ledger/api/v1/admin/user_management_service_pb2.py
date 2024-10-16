# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/admin/user_management_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/admin/user_management_service.proto',
  package='com.daml.ledger.api.v1.admin',
  syntax='proto3',
  serialized_options=b'\n\034com.daml.ledger.api.v1.adminB\037UserManagementServiceOuterClassZKgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1/admin\252\002\034Com.Daml.Ledger.Api.V1.Admin',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n:com/daml/ledger/api/v1/admin/user_management_service.proto\x12\x1c\x63om.daml.ledger.api.v1.admin\";\n\x04User\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12#\n\rprimary_party\x18\x02 \x01(\tR\x0cprimaryParty\"\xec\x02\n\x05Right\x12\x63\n\x11participant_admin\x18\x01 \x01(\x0b\x32\x34.com.daml.ledger.api.v1.admin.Right.ParticipantAdminH\x00R\x10participantAdmin\x12L\n\ncan_act_as\x18\x02 \x01(\x0b\x32,.com.daml.ledger.api.v1.admin.Right.CanActAsH\x00R\x08\x63\x61nActAs\x12O\n\x0b\x63\x61n_read_as\x18\x03 \x01(\x0b\x32-.com.daml.ledger.api.v1.admin.Right.CanReadAsH\x00R\tcanReadAs\x1a\x12\n\x10ParticipantAdmin\x1a \n\x08\x43\x61nActAs\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x1a!\n\tCanReadAs\x12\x14\n\x05party\x18\x01 \x01(\tR\x05partyB\x06\n\x04kind\"\x88\x01\n\x11\x43reateUserRequest\x12\x36\n\x04user\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.admin.UserR\x04user\x12;\n\x06rights\x18\x02 \x03(\x0b\x32#.com.daml.ledger.api.v1.admin.RightR\x06rights\"L\n\x12\x43reateUserResponse\x12\x36\n\x04user\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.admin.UserR\x04user\")\n\x0eGetUserRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"I\n\x0fGetUserResponse\x12\x36\n\x04user\x18\x01 \x01(\x0b\x32\".com.daml.ledger.api.v1.admin.UserR\x04user\",\n\x11\x44\x65leteUserRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\x14\n\x12\x44\x65leteUserResponse\"N\n\x10ListUsersRequest\x12\x1d\n\npage_token\x18\x02 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\"u\n\x11ListUsersResponse\x12\x38\n\x05users\x18\x01 \x03(\x0b\x32\".com.daml.ledger.api.v1.admin.UserR\x05users\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"n\n\x16GrantUserRightsRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12;\n\x06rights\x18\x02 \x03(\x0b\x32#.com.daml.ledger.api.v1.admin.RightR\x06rights\"p\n\x17GrantUserRightsResponse\x12U\n\x14newly_granted_rights\x18\x01 \x03(\x0b\x32#.com.daml.ledger.api.v1.admin.RightR\x12newlyGrantedRights\"o\n\x17RevokeUserRightsRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12;\n\x06rights\x18\x02 \x03(\x0b\x32#.com.daml.ledger.api.v1.admin.RightR\x06rights\"q\n\x18RevokeUserRightsResponse\x12U\n\x14newly_revoked_rights\x18\x01 \x03(\x0b\x32#.com.daml.ledger.api.v1.admin.RightR\x12newlyRevokedRights\"0\n\x15ListUserRightsRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"U\n\x16ListUserRightsResponse\x12;\n\x06rights\x18\x01 \x03(\x0b\x32#.com.daml.ledger.api.v1.admin.RightR\x06rights2\xd0\x06\n\x15UserManagementService\x12o\n\nCreateUser\x12/.com.daml.ledger.api.v1.admin.CreateUserRequest\x1a\x30.com.daml.ledger.api.v1.admin.CreateUserResponse\x12\x66\n\x07GetUser\x12,.com.daml.ledger.api.v1.admin.GetUserRequest\x1a-.com.daml.ledger.api.v1.admin.GetUserResponse\x12o\n\nDeleteUser\x12/.com.daml.ledger.api.v1.admin.DeleteUserRequest\x1a\x30.com.daml.ledger.api.v1.admin.DeleteUserResponse\x12l\n\tListUsers\x12..com.daml.ledger.api.v1.admin.ListUsersRequest\x1a/.com.daml.ledger.api.v1.admin.ListUsersResponse\x12~\n\x0fGrantUserRights\x12\x34.com.daml.ledger.api.v1.admin.GrantUserRightsRequest\x1a\x35.com.daml.ledger.api.v1.admin.GrantUserRightsResponse\x12\x81\x01\n\x10RevokeUserRights\x12\x35.com.daml.ledger.api.v1.admin.RevokeUserRightsRequest\x1a\x36.com.daml.ledger.api.v1.admin.RevokeUserRightsResponse\x12{\n\x0eListUserRights\x12\x33.com.daml.ledger.api.v1.admin.ListUserRightsRequest\x1a\x34.com.daml.ledger.api.v1.admin.ListUserRightsResponseB\xab\x01\n\x1c\x63om.daml.ledger.api.v1.adminB\x1fUserManagementServiceOuterClassZKgithub.com/digital-asset/dazl-client/v7/go/api/com/daml/ledger/api/v1/admin\xaa\x02\x1c\x43om.Daml.Ledger.Api.V1.Adminb\x06proto3'
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='com.daml.ledger.api.v1.admin.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.daml.ledger.api.v1.admin.User.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='primary_party', full_name='com.daml.ledger.api.v1.admin.User.primary_party', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='primaryParty', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=92,
  serialized_end=151,
)


_RIGHT_PARTICIPANTADMIN = _descriptor.Descriptor(
  name='ParticipantAdmin',
  full_name='com.daml.ledger.api.v1.admin.Right.ParticipantAdmin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=423,
  serialized_end=441,
)

_RIGHT_CANACTAS = _descriptor.Descriptor(
  name='CanActAs',
  full_name='com.daml.ledger.api.v1.admin.Right.CanActAs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='party', full_name='com.daml.ledger.api.v1.admin.Right.CanActAs.party', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='party', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=443,
  serialized_end=475,
)

_RIGHT_CANREADAS = _descriptor.Descriptor(
  name='CanReadAs',
  full_name='com.daml.ledger.api.v1.admin.Right.CanReadAs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='party', full_name='com.daml.ledger.api.v1.admin.Right.CanReadAs.party', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='party', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=477,
  serialized_end=510,
)

_RIGHT = _descriptor.Descriptor(
  name='Right',
  full_name='com.daml.ledger.api.v1.admin.Right',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='participant_admin', full_name='com.daml.ledger.api.v1.admin.Right.participant_admin', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='participantAdmin', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='can_act_as', full_name='com.daml.ledger.api.v1.admin.Right.can_act_as', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='canActAs', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='can_read_as', full_name='com.daml.ledger.api.v1.admin.Right.can_read_as', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='canReadAs', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RIGHT_PARTICIPANTADMIN, _RIGHT_CANACTAS, _RIGHT_CANREADAS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='com.daml.ledger.api.v1.admin.Right.kind',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=154,
  serialized_end=518,
)


_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='com.daml.ledger.api.v1.admin.CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='com.daml.ledger.api.v1.admin.CreateUserRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='user', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rights', full_name='com.daml.ledger.api.v1.admin.CreateUserRequest.rights', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rights', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=521,
  serialized_end=657,
)


_CREATEUSERRESPONSE = _descriptor.Descriptor(
  name='CreateUserResponse',
  full_name='com.daml.ledger.api.v1.admin.CreateUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='com.daml.ledger.api.v1.admin.CreateUserResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='user', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=659,
  serialized_end=735,
)


_GETUSERREQUEST = _descriptor.Descriptor(
  name='GetUserRequest',
  full_name='com.daml.ledger.api.v1.admin.GetUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='com.daml.ledger.api.v1.admin.GetUserRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='userId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=737,
  serialized_end=778,
)


_GETUSERRESPONSE = _descriptor.Descriptor(
  name='GetUserResponse',
  full_name='com.daml.ledger.api.v1.admin.GetUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='com.daml.ledger.api.v1.admin.GetUserResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='user', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=780,
  serialized_end=853,
)


_DELETEUSERREQUEST = _descriptor.Descriptor(
  name='DeleteUserRequest',
  full_name='com.daml.ledger.api.v1.admin.DeleteUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='com.daml.ledger.api.v1.admin.DeleteUserRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='userId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=855,
  serialized_end=899,
)


_DELETEUSERRESPONSE = _descriptor.Descriptor(
  name='DeleteUserResponse',
  full_name='com.daml.ledger.api.v1.admin.DeleteUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=901,
  serialized_end=921,
)


_LISTUSERSREQUEST = _descriptor.Descriptor(
  name='ListUsersRequest',
  full_name='com.daml.ledger.api.v1.admin.ListUsersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_token', full_name='com.daml.ledger.api.v1.admin.ListUsersRequest.page_token', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='com.daml.ledger.api.v1.admin.ListUsersRequest.page_size', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=923,
  serialized_end=1001,
)


_LISTUSERSRESPONSE = _descriptor.Descriptor(
  name='ListUsersResponse',
  full_name='com.daml.ledger.api.v1.admin.ListUsersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='com.daml.ledger.api.v1.admin.ListUsersResponse.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='users', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='com.daml.ledger.api.v1.admin.ListUsersResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nextPageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1003,
  serialized_end=1120,
)


_GRANTUSERRIGHTSREQUEST = _descriptor.Descriptor(
  name='GrantUserRightsRequest',
  full_name='com.daml.ledger.api.v1.admin.GrantUserRightsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='com.daml.ledger.api.v1.admin.GrantUserRightsRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='userId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rights', full_name='com.daml.ledger.api.v1.admin.GrantUserRightsRequest.rights', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rights', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1122,
  serialized_end=1232,
)


_GRANTUSERRIGHTSRESPONSE = _descriptor.Descriptor(
  name='GrantUserRightsResponse',
  full_name='com.daml.ledger.api.v1.admin.GrantUserRightsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='newly_granted_rights', full_name='com.daml.ledger.api.v1.admin.GrantUserRightsResponse.newly_granted_rights', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='newlyGrantedRights', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1234,
  serialized_end=1346,
)


_REVOKEUSERRIGHTSREQUEST = _descriptor.Descriptor(
  name='RevokeUserRightsRequest',
  full_name='com.daml.ledger.api.v1.admin.RevokeUserRightsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='com.daml.ledger.api.v1.admin.RevokeUserRightsRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='userId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rights', full_name='com.daml.ledger.api.v1.admin.RevokeUserRightsRequest.rights', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rights', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1348,
  serialized_end=1459,
)


_REVOKEUSERRIGHTSRESPONSE = _descriptor.Descriptor(
  name='RevokeUserRightsResponse',
  full_name='com.daml.ledger.api.v1.admin.RevokeUserRightsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='newly_revoked_rights', full_name='com.daml.ledger.api.v1.admin.RevokeUserRightsResponse.newly_revoked_rights', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='newlyRevokedRights', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1461,
  serialized_end=1574,
)


_LISTUSERRIGHTSREQUEST = _descriptor.Descriptor(
  name='ListUserRightsRequest',
  full_name='com.daml.ledger.api.v1.admin.ListUserRightsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='com.daml.ledger.api.v1.admin.ListUserRightsRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='userId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1576,
  serialized_end=1624,
)


_LISTUSERRIGHTSRESPONSE = _descriptor.Descriptor(
  name='ListUserRightsResponse',
  full_name='com.daml.ledger.api.v1.admin.ListUserRightsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rights', full_name='com.daml.ledger.api.v1.admin.ListUserRightsResponse.rights', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rights', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1626,
  serialized_end=1711,
)

_RIGHT_PARTICIPANTADMIN.containing_type = _RIGHT
_RIGHT_CANACTAS.containing_type = _RIGHT
_RIGHT_CANREADAS.containing_type = _RIGHT
_RIGHT.fields_by_name['participant_admin'].message_type = _RIGHT_PARTICIPANTADMIN
_RIGHT.fields_by_name['can_act_as'].message_type = _RIGHT_CANACTAS
_RIGHT.fields_by_name['can_read_as'].message_type = _RIGHT_CANREADAS
_RIGHT.oneofs_by_name['kind'].fields.append(
  _RIGHT.fields_by_name['participant_admin'])
_RIGHT.fields_by_name['participant_admin'].containing_oneof = _RIGHT.oneofs_by_name['kind']
_RIGHT.oneofs_by_name['kind'].fields.append(
  _RIGHT.fields_by_name['can_act_as'])
_RIGHT.fields_by_name['can_act_as'].containing_oneof = _RIGHT.oneofs_by_name['kind']
_RIGHT.oneofs_by_name['kind'].fields.append(
  _RIGHT.fields_by_name['can_read_as'])
_RIGHT.fields_by_name['can_read_as'].containing_oneof = _RIGHT.oneofs_by_name['kind']
_CREATEUSERREQUEST.fields_by_name['user'].message_type = _USER
_CREATEUSERREQUEST.fields_by_name['rights'].message_type = _RIGHT
_CREATEUSERRESPONSE.fields_by_name['user'].message_type = _USER
_GETUSERRESPONSE.fields_by_name['user'].message_type = _USER
_LISTUSERSRESPONSE.fields_by_name['users'].message_type = _USER
_GRANTUSERRIGHTSREQUEST.fields_by_name['rights'].message_type = _RIGHT
_GRANTUSERRIGHTSRESPONSE.fields_by_name['newly_granted_rights'].message_type = _RIGHT
_REVOKEUSERRIGHTSREQUEST.fields_by_name['rights'].message_type = _RIGHT
_REVOKEUSERRIGHTSRESPONSE.fields_by_name['newly_revoked_rights'].message_type = _RIGHT
_LISTUSERRIGHTSRESPONSE.fields_by_name['rights'].message_type = _RIGHT
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Right'] = _RIGHT
DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name['CreateUserResponse'] = _CREATEUSERRESPONSE
DESCRIPTOR.message_types_by_name['GetUserRequest'] = _GETUSERREQUEST
DESCRIPTOR.message_types_by_name['GetUserResponse'] = _GETUSERRESPONSE
DESCRIPTOR.message_types_by_name['DeleteUserRequest'] = _DELETEUSERREQUEST
DESCRIPTOR.message_types_by_name['DeleteUserResponse'] = _DELETEUSERRESPONSE
DESCRIPTOR.message_types_by_name['ListUsersRequest'] = _LISTUSERSREQUEST
DESCRIPTOR.message_types_by_name['ListUsersResponse'] = _LISTUSERSRESPONSE
DESCRIPTOR.message_types_by_name['GrantUserRightsRequest'] = _GRANTUSERRIGHTSREQUEST
DESCRIPTOR.message_types_by_name['GrantUserRightsResponse'] = _GRANTUSERRIGHTSRESPONSE
DESCRIPTOR.message_types_by_name['RevokeUserRightsRequest'] = _REVOKEUSERRIGHTSREQUEST
DESCRIPTOR.message_types_by_name['RevokeUserRightsResponse'] = _REVOKEUSERRIGHTSRESPONSE
DESCRIPTOR.message_types_by_name['ListUserRightsRequest'] = _LISTUSERRIGHTSREQUEST
DESCRIPTOR.message_types_by_name['ListUserRightsResponse'] = _LISTUSERRIGHTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.User)
  })
_sym_db.RegisterMessage(User)

Right = _reflection.GeneratedProtocolMessageType('Right', (_message.Message,), {

  'ParticipantAdmin' : _reflection.GeneratedProtocolMessageType('ParticipantAdmin', (_message.Message,), {
    'DESCRIPTOR' : _RIGHT_PARTICIPANTADMIN,
    '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
    # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.Right.ParticipantAdmin)
    })
  ,

  'CanActAs' : _reflection.GeneratedProtocolMessageType('CanActAs', (_message.Message,), {
    'DESCRIPTOR' : _RIGHT_CANACTAS,
    '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
    # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.Right.CanActAs)
    })
  ,

  'CanReadAs' : _reflection.GeneratedProtocolMessageType('CanReadAs', (_message.Message,), {
    'DESCRIPTOR' : _RIGHT_CANREADAS,
    '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
    # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.Right.CanReadAs)
    })
  ,
  'DESCRIPTOR' : _RIGHT,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.Right)
  })
_sym_db.RegisterMessage(Right)
_sym_db.RegisterMessage(Right.ParticipantAdmin)
_sym_db.RegisterMessage(Right.CanActAs)
_sym_db.RegisterMessage(Right.CanReadAs)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

CreateUserResponse = _reflection.GeneratedProtocolMessageType('CreateUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.CreateUserResponse)
  })
_sym_db.RegisterMessage(CreateUserResponse)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

GetUserResponse = _reflection.GeneratedProtocolMessageType('GetUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.GetUserResponse)
  })
_sym_db.RegisterMessage(GetUserResponse)

DeleteUserRequest = _reflection.GeneratedProtocolMessageType('DeleteUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.DeleteUserRequest)
  })
_sym_db.RegisterMessage(DeleteUserRequest)

DeleteUserResponse = _reflection.GeneratedProtocolMessageType('DeleteUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.DeleteUserResponse)
  })
_sym_db.RegisterMessage(DeleteUserResponse)

ListUsersRequest = _reflection.GeneratedProtocolMessageType('ListUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERSREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.ListUsersRequest)
  })
_sym_db.RegisterMessage(ListUsersRequest)

ListUsersResponse = _reflection.GeneratedProtocolMessageType('ListUsersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERSRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.ListUsersResponse)
  })
_sym_db.RegisterMessage(ListUsersResponse)

GrantUserRightsRequest = _reflection.GeneratedProtocolMessageType('GrantUserRightsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRANTUSERRIGHTSREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.GrantUserRightsRequest)
  })
_sym_db.RegisterMessage(GrantUserRightsRequest)

GrantUserRightsResponse = _reflection.GeneratedProtocolMessageType('GrantUserRightsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GRANTUSERRIGHTSRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.GrantUserRightsResponse)
  })
_sym_db.RegisterMessage(GrantUserRightsResponse)

RevokeUserRightsRequest = _reflection.GeneratedProtocolMessageType('RevokeUserRightsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVOKEUSERRIGHTSREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.RevokeUserRightsRequest)
  })
_sym_db.RegisterMessage(RevokeUserRightsRequest)

RevokeUserRightsResponse = _reflection.GeneratedProtocolMessageType('RevokeUserRightsResponse', (_message.Message,), {
  'DESCRIPTOR' : _REVOKEUSERRIGHTSRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.RevokeUserRightsResponse)
  })
_sym_db.RegisterMessage(RevokeUserRightsResponse)

ListUserRightsRequest = _reflection.GeneratedProtocolMessageType('ListUserRightsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERRIGHTSREQUEST,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.ListUserRightsRequest)
  })
_sym_db.RegisterMessage(ListUserRightsRequest)

ListUserRightsResponse = _reflection.GeneratedProtocolMessageType('ListUserRightsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERRIGHTSRESPONSE,
  '__module__' : 'com.daml.ledger.api.v1.admin.user_management_service_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.ListUserRightsResponse)
  })
_sym_db.RegisterMessage(ListUserRightsResponse)


DESCRIPTOR._options = None

_USERMANAGEMENTSERVICE = _descriptor.ServiceDescriptor(
  name='UserManagementService',
  full_name='com.daml.ledger.api.v1.admin.UserManagementService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1714,
  serialized_end=2562,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateUser',
    full_name='com.daml.ledger.api.v1.admin.UserManagementService.CreateUser',
    index=0,
    containing_service=None,
    input_type=_CREATEUSERREQUEST,
    output_type=_CREATEUSERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUser',
    full_name='com.daml.ledger.api.v1.admin.UserManagementService.GetUser',
    index=1,
    containing_service=None,
    input_type=_GETUSERREQUEST,
    output_type=_GETUSERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteUser',
    full_name='com.daml.ledger.api.v1.admin.UserManagementService.DeleteUser',
    index=2,
    containing_service=None,
    input_type=_DELETEUSERREQUEST,
    output_type=_DELETEUSERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListUsers',
    full_name='com.daml.ledger.api.v1.admin.UserManagementService.ListUsers',
    index=3,
    containing_service=None,
    input_type=_LISTUSERSREQUEST,
    output_type=_LISTUSERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GrantUserRights',
    full_name='com.daml.ledger.api.v1.admin.UserManagementService.GrantUserRights',
    index=4,
    containing_service=None,
    input_type=_GRANTUSERRIGHTSREQUEST,
    output_type=_GRANTUSERRIGHTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RevokeUserRights',
    full_name='com.daml.ledger.api.v1.admin.UserManagementService.RevokeUserRights',
    index=5,
    containing_service=None,
    input_type=_REVOKEUSERRIGHTSREQUEST,
    output_type=_REVOKEUSERRIGHTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListUserRights',
    full_name='com.daml.ledger.api.v1.admin.UserManagementService.ListUserRights',
    index=6,
    containing_service=None,
    input_type=_LISTUSERRIGHTSREQUEST,
    output_type=_LISTUSERRIGHTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERMANAGEMENTSERVICE)

DESCRIPTOR.services_by_name['UserManagementService'] = _USERMANAGEMENTSERVICE

# @@protoc_insertion_point(module_scope)
