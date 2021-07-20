// Copyright (c) 2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.26.0
// 	protoc        v3.14.0
// source: com/daml/ledger/api/v1/admin/party_management_service.proto

package admin

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type GetParticipantIdRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *GetParticipantIdRequest) Reset() {
	*x = GetParticipantIdRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetParticipantIdRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetParticipantIdRequest) ProtoMessage() {}

func (x *GetParticipantIdRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetParticipantIdRequest.ProtoReflect.Descriptor instead.
func (*GetParticipantIdRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescGZIP(), []int{0}
}

type GetParticipantIdResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Identifier of the participant, which SHOULD be globally unique.
	// Must be a valid LedgerString (as describe in ``value.proto``).
	ParticipantId string `protobuf:"bytes,1,opt,name=participant_id,json=participantId,proto3" json:"participant_id,omitempty"`
}

func (x *GetParticipantIdResponse) Reset() {
	*x = GetParticipantIdResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetParticipantIdResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetParticipantIdResponse) ProtoMessage() {}

func (x *GetParticipantIdResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetParticipantIdResponse.ProtoReflect.Descriptor instead.
func (*GetParticipantIdResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescGZIP(), []int{1}
}

func (x *GetParticipantIdResponse) GetParticipantId() string {
	if x != nil {
		return x.ParticipantId
	}
	return ""
}

type GetPartiesRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The stable, unique identifier of the Daml parties.
	// Must be valid PartyIdStrings (as described in ``value.proto``).
	// Required
	Parties []string `protobuf:"bytes,1,rep,name=parties,proto3" json:"parties,omitempty"`
}

func (x *GetPartiesRequest) Reset() {
	*x = GetPartiesRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetPartiesRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetPartiesRequest) ProtoMessage() {}

func (x *GetPartiesRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetPartiesRequest.ProtoReflect.Descriptor instead.
func (*GetPartiesRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescGZIP(), []int{2}
}

func (x *GetPartiesRequest) GetParties() []string {
	if x != nil {
		return x.Parties
	}
	return nil
}

type GetPartiesResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The details of the requested Daml parties by the participant, if known.
	// The party details may not be in the same order as requested.
	// Required
	PartyDetails []*PartyDetails `protobuf:"bytes,1,rep,name=party_details,json=partyDetails,proto3" json:"party_details,omitempty"`
}

func (x *GetPartiesResponse) Reset() {
	*x = GetPartiesResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetPartiesResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetPartiesResponse) ProtoMessage() {}

func (x *GetPartiesResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetPartiesResponse.ProtoReflect.Descriptor instead.
func (*GetPartiesResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescGZIP(), []int{3}
}

func (x *GetPartiesResponse) GetPartyDetails() []*PartyDetails {
	if x != nil {
		return x.PartyDetails
	}
	return nil
}

type ListKnownPartiesRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *ListKnownPartiesRequest) Reset() {
	*x = ListKnownPartiesRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ListKnownPartiesRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListKnownPartiesRequest) ProtoMessage() {}

func (x *ListKnownPartiesRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListKnownPartiesRequest.ProtoReflect.Descriptor instead.
func (*ListKnownPartiesRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescGZIP(), []int{4}
}

type ListKnownPartiesResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The details of all Daml parties known by the participant.
	// Required
	PartyDetails []*PartyDetails `protobuf:"bytes,1,rep,name=party_details,json=partyDetails,proto3" json:"party_details,omitempty"`
}

func (x *ListKnownPartiesResponse) Reset() {
	*x = ListKnownPartiesResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ListKnownPartiesResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ListKnownPartiesResponse) ProtoMessage() {}

func (x *ListKnownPartiesResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ListKnownPartiesResponse.ProtoReflect.Descriptor instead.
func (*ListKnownPartiesResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescGZIP(), []int{5}
}

func (x *ListKnownPartiesResponse) GetPartyDetails() []*PartyDetails {
	if x != nil {
		return x.PartyDetails
	}
	return nil
}

type AllocatePartyRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// A hint to the backing participant which party ID to allocate. It can be
	// ignored.
	// Must be a valid PartyIdString (as described in ``value.proto``).
	// Optional
	PartyIdHint string `protobuf:"bytes,1,opt,name=party_id_hint,json=partyIdHint,proto3" json:"party_id_hint,omitempty"`
	// Human-readable name of the party to be added to the participant. It doesn't
	// have to be unique.
	// Optional
	DisplayName string `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
}

func (x *AllocatePartyRequest) Reset() {
	*x = AllocatePartyRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *AllocatePartyRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AllocatePartyRequest) ProtoMessage() {}

func (x *AllocatePartyRequest) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AllocatePartyRequest.ProtoReflect.Descriptor instead.
func (*AllocatePartyRequest) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescGZIP(), []int{6}
}

func (x *AllocatePartyRequest) GetPartyIdHint() string {
	if x != nil {
		return x.PartyIdHint
	}
	return ""
}

func (x *AllocatePartyRequest) GetDisplayName() string {
	if x != nil {
		return x.DisplayName
	}
	return ""
}

type AllocatePartyResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PartyDetails *PartyDetails `protobuf:"bytes,1,opt,name=party_details,json=partyDetails,proto3" json:"party_details,omitempty"`
}

func (x *AllocatePartyResponse) Reset() {
	*x = AllocatePartyResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[7]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *AllocatePartyResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*AllocatePartyResponse) ProtoMessage() {}

func (x *AllocatePartyResponse) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[7]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use AllocatePartyResponse.ProtoReflect.Descriptor instead.
func (*AllocatePartyResponse) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescGZIP(), []int{7}
}

func (x *AllocatePartyResponse) GetPartyDetails() *PartyDetails {
	if x != nil {
		return x.PartyDetails
	}
	return nil
}

type PartyDetails struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The stable unique identifier of a Daml party.
	// Must be a valid PartyIdString (as described in ``value.proto``).
	// Required
	Party string `protobuf:"bytes,1,opt,name=party,proto3" json:"party,omitempty"`
	// Human readable name associated with the party. Caution, it might not be
	// unique.
	// Optional
	DisplayName string `protobuf:"bytes,2,opt,name=display_name,json=displayName,proto3" json:"display_name,omitempty"`
	// true if party is hosted by the backing participant.
	// Required
	IsLocal bool `protobuf:"varint,3,opt,name=is_local,json=isLocal,proto3" json:"is_local,omitempty"`
}

func (x *PartyDetails) Reset() {
	*x = PartyDetails{}
	if protoimpl.UnsafeEnabled {
		mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[8]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PartyDetails) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PartyDetails) ProtoMessage() {}

func (x *PartyDetails) ProtoReflect() protoreflect.Message {
	mi := &file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[8]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PartyDetails.ProtoReflect.Descriptor instead.
func (*PartyDetails) Descriptor() ([]byte, []int) {
	return file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescGZIP(), []int{8}
}

func (x *PartyDetails) GetParty() string {
	if x != nil {
		return x.Party
	}
	return ""
}

func (x *PartyDetails) GetDisplayName() string {
	if x != nil {
		return x.DisplayName
	}
	return ""
}

func (x *PartyDetails) GetIsLocal() bool {
	if x != nil {
		return x.IsLocal
	}
	return false
}

var File_com_daml_ledger_api_v1_admin_party_management_service_proto protoreflect.FileDescriptor

var file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDesc = []byte{
	0x0a, 0x3b, 0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65,
	0x72, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2f, 0x70,
	0x61, 0x72, 0x74, 0x79, 0x5f, 0x6d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x5f,
	0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x1c, 0x63,
	0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61,
	0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x22, 0x19, 0x0a, 0x17, 0x47,
	0x65, 0x74, 0x50, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x49, 0x64, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x22, 0x41, 0x0a, 0x18, 0x47, 0x65, 0x74, 0x50, 0x61, 0x72,
	0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x49, 0x64, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e,
	0x73, 0x65, 0x12, 0x25, 0x0a, 0x0e, 0x70, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e,
	0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0d, 0x70, 0x61, 0x72, 0x74,
	0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x49, 0x64, 0x22, 0x2d, 0x0a, 0x11, 0x47, 0x65, 0x74,
	0x50, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x18,
	0x0a, 0x07, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x09, 0x52,
	0x07, 0x70, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x22, 0x65, 0x0a, 0x12, 0x47, 0x65, 0x74, 0x50,
	0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x4f,
	0x0a, 0x0d, 0x70, 0x61, 0x72, 0x74, 0x79, 0x5f, 0x64, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73, 0x18,
	0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x2a, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c,
	0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61,
	0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x50, 0x61, 0x72, 0x74, 0x79, 0x44, 0x65, 0x74, 0x61, 0x69, 0x6c,
	0x73, 0x52, 0x0c, 0x70, 0x61, 0x72, 0x74, 0x79, 0x44, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73, 0x22,
	0x19, 0x0a, 0x17, 0x4c, 0x69, 0x73, 0x74, 0x4b, 0x6e, 0x6f, 0x77, 0x6e, 0x50, 0x61, 0x72, 0x74,
	0x69, 0x65, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x22, 0x6b, 0x0a, 0x18, 0x4c, 0x69,
	0x73, 0x74, 0x4b, 0x6e, 0x6f, 0x77, 0x6e, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x52, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x4f, 0x0a, 0x0d, 0x70, 0x61, 0x72, 0x74, 0x79, 0x5f,
	0x64, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x2a, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x50, 0x61, 0x72,
	0x74, 0x79, 0x44, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73, 0x52, 0x0c, 0x70, 0x61, 0x72, 0x74, 0x79,
	0x44, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73, 0x22, 0x5d, 0x0a, 0x14, 0x41, 0x6c, 0x6c, 0x6f, 0x63,
	0x61, 0x74, 0x65, 0x50, 0x61, 0x72, 0x74, 0x79, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12,
	0x22, 0x0a, 0x0d, 0x70, 0x61, 0x72, 0x74, 0x79, 0x5f, 0x69, 0x64, 0x5f, 0x68, 0x69, 0x6e, 0x74,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x70, 0x61, 0x72, 0x74, 0x79, 0x49, 0x64, 0x48,
	0x69, 0x6e, 0x74, 0x12, 0x21, 0x0a, 0x0c, 0x64, 0x69, 0x73, 0x70, 0x6c, 0x61, 0x79, 0x5f, 0x6e,
	0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x64, 0x69, 0x73, 0x70, 0x6c,
	0x61, 0x79, 0x4e, 0x61, 0x6d, 0x65, 0x22, 0x68, 0x0a, 0x15, 0x41, 0x6c, 0x6c, 0x6f, 0x63, 0x61,
	0x74, 0x65, 0x50, 0x61, 0x72, 0x74, 0x79, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12,
	0x4f, 0x0a, 0x0d, 0x70, 0x61, 0x72, 0x74, 0x79, 0x5f, 0x64, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2a, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d,
	0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e,
	0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x50, 0x61, 0x72, 0x74, 0x79, 0x44, 0x65, 0x74, 0x61, 0x69,
	0x6c, 0x73, 0x52, 0x0c, 0x70, 0x61, 0x72, 0x74, 0x79, 0x44, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73,
	0x22, 0x62, 0x0a, 0x0c, 0x50, 0x61, 0x72, 0x74, 0x79, 0x44, 0x65, 0x74, 0x61, 0x69, 0x6c, 0x73,
	0x12, 0x14, 0x0a, 0x05, 0x70, 0x61, 0x72, 0x74, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x05, 0x70, 0x61, 0x72, 0x74, 0x79, 0x12, 0x21, 0x0a, 0x0c, 0x64, 0x69, 0x73, 0x70, 0x6c, 0x61,
	0x79, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x64, 0x69,
	0x73, 0x70, 0x6c, 0x61, 0x79, 0x4e, 0x61, 0x6d, 0x65, 0x12, 0x19, 0x0a, 0x08, 0x69, 0x73, 0x5f,
	0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x18, 0x03, 0x20, 0x01, 0x28, 0x08, 0x52, 0x07, 0x69, 0x73, 0x4c,
	0x6f, 0x63, 0x61, 0x6c, 0x32, 0x8b, 0x04, 0x0a, 0x16, 0x50, 0x61, 0x72, 0x74, 0x79, 0x4d, 0x61,
	0x6e, 0x61, 0x67, 0x65, 0x6d, 0x65, 0x6e, 0x74, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12,
	0x81, 0x01, 0x0a, 0x10, 0x47, 0x65, 0x74, 0x50, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61,
	0x6e, 0x74, 0x49, 0x64, 0x12, 0x35, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e,
	0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64,
	0x6d, 0x69, 0x6e, 0x2e, 0x47, 0x65, 0x74, 0x50, 0x61, 0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61,
	0x6e, 0x74, 0x49, 0x64, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x36, 0x2e, 0x63, 0x6f,
	0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70,
	0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x47, 0x65, 0x74, 0x50, 0x61,
	0x72, 0x74, 0x69, 0x63, 0x69, 0x70, 0x61, 0x6e, 0x74, 0x49, 0x64, 0x52, 0x65, 0x73, 0x70, 0x6f,
	0x6e, 0x73, 0x65, 0x12, 0x6f, 0x0a, 0x0a, 0x47, 0x65, 0x74, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65,
	0x73, 0x12, 0x2f, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64,
	0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e,
	0x2e, 0x47, 0x65, 0x74, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x1a, 0x30, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65,
	0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69,
	0x6e, 0x2e, 0x47, 0x65, 0x74, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x12, 0x81, 0x01, 0x0a, 0x10, 0x4c, 0x69, 0x73, 0x74, 0x4b, 0x6e, 0x6f,
	0x77, 0x6e, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x12, 0x35, 0x2e, 0x63, 0x6f, 0x6d, 0x2e,
	0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e,
	0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x4c, 0x69, 0x73, 0x74, 0x4b, 0x6e, 0x6f,
	0x77, 0x6e, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x1a, 0x36, 0x2e, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67,
	0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e,
	0x4c, 0x69, 0x73, 0x74, 0x4b, 0x6e, 0x6f, 0x77, 0x6e, 0x50, 0x61, 0x72, 0x74, 0x69, 0x65, 0x73,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x78, 0x0a, 0x0d, 0x41, 0x6c, 0x6c, 0x6f,
	0x63, 0x61, 0x74, 0x65, 0x50, 0x61, 0x72, 0x74, 0x79, 0x12, 0x32, 0x2e, 0x63, 0x6f, 0x6d, 0x2e,
	0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e,
	0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x41, 0x6c, 0x6c, 0x6f, 0x63, 0x61, 0x74,
	0x65, 0x50, 0x61, 0x72, 0x74, 0x79, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x33, 0x2e,
	0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0x2e, 0x41, 0x6c, 0x6c,
	0x6f, 0x63, 0x61, 0x74, 0x65, 0x50, 0x61, 0x72, 0x74, 0x79, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e,
	0x73, 0x65, 0x42, 0xb6, 0x01, 0x0a, 0x1c, 0x63, 0x6f, 0x6d, 0x2e, 0x64, 0x61, 0x6d, 0x6c, 0x2e,
	0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x61, 0x64,
	0x6d, 0x69, 0x6e, 0x42, 0x20, 0x50, 0x61, 0x72, 0x74, 0x79, 0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65,
	0x6d, 0x65, 0x6e, 0x74, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x4f, 0x75, 0x74, 0x65, 0x72,
	0x43, 0x6c, 0x61, 0x73, 0x73, 0x5a, 0x55, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f,
	0x6d, 0x2f, 0x64, 0x69, 0x67, 0x69, 0x74, 0x61, 0x6c, 0x2d, 0x61, 0x73, 0x73, 0x65, 0x74, 0x2f,
	0x64, 0x61, 0x7a, 0x6c, 0x2d, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f, 0x67, 0x6f, 0x2f, 0x76,
	0x37, 0x2f, 0x70, 0x6b, 0x67, 0x2f, 0x67, 0x65, 0x6e, 0x65, 0x72, 0x61, 0x74, 0x65, 0x64, 0x2f,
	0x63, 0x6f, 0x6d, 0x2f, 0x64, 0x61, 0x6d, 0x6c, 0x2f, 0x6c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2f,
	0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x61, 0x64, 0x6d, 0x69, 0x6e, 0xaa, 0x02, 0x1c, 0x43,
	0x6f, 0x6d, 0x2e, 0x44, 0x61, 0x6d, 0x6c, 0x2e, 0x4c, 0x65, 0x64, 0x67, 0x65, 0x72, 0x2e, 0x41,
	0x70, 0x69, 0x2e, 0x56, 0x31, 0x2e, 0x41, 0x64, 0x6d, 0x69, 0x6e, 0x62, 0x06, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x33,
}

var (
	file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescOnce sync.Once
	file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescData = file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDesc
)

func file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescGZIP() []byte {
	file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescOnce.Do(func() {
		file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescData = protoimpl.X.CompressGZIP(file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescData)
	})
	return file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDescData
}

var file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes = make([]protoimpl.MessageInfo, 9)
var file_com_daml_ledger_api_v1_admin_party_management_service_proto_goTypes = []interface{}{
	(*GetParticipantIdRequest)(nil),  // 0: com.daml.ledger.api.v1.admin.GetParticipantIdRequest
	(*GetParticipantIdResponse)(nil), // 1: com.daml.ledger.api.v1.admin.GetParticipantIdResponse
	(*GetPartiesRequest)(nil),        // 2: com.daml.ledger.api.v1.admin.GetPartiesRequest
	(*GetPartiesResponse)(nil),       // 3: com.daml.ledger.api.v1.admin.GetPartiesResponse
	(*ListKnownPartiesRequest)(nil),  // 4: com.daml.ledger.api.v1.admin.ListKnownPartiesRequest
	(*ListKnownPartiesResponse)(nil), // 5: com.daml.ledger.api.v1.admin.ListKnownPartiesResponse
	(*AllocatePartyRequest)(nil),     // 6: com.daml.ledger.api.v1.admin.AllocatePartyRequest
	(*AllocatePartyResponse)(nil),    // 7: com.daml.ledger.api.v1.admin.AllocatePartyResponse
	(*PartyDetails)(nil),             // 8: com.daml.ledger.api.v1.admin.PartyDetails
}
var file_com_daml_ledger_api_v1_admin_party_management_service_proto_depIdxs = []int32{
	8, // 0: com.daml.ledger.api.v1.admin.GetPartiesResponse.party_details:type_name -> com.daml.ledger.api.v1.admin.PartyDetails
	8, // 1: com.daml.ledger.api.v1.admin.ListKnownPartiesResponse.party_details:type_name -> com.daml.ledger.api.v1.admin.PartyDetails
	8, // 2: com.daml.ledger.api.v1.admin.AllocatePartyResponse.party_details:type_name -> com.daml.ledger.api.v1.admin.PartyDetails
	0, // 3: com.daml.ledger.api.v1.admin.PartyManagementService.GetParticipantId:input_type -> com.daml.ledger.api.v1.admin.GetParticipantIdRequest
	2, // 4: com.daml.ledger.api.v1.admin.PartyManagementService.GetParties:input_type -> com.daml.ledger.api.v1.admin.GetPartiesRequest
	4, // 5: com.daml.ledger.api.v1.admin.PartyManagementService.ListKnownParties:input_type -> com.daml.ledger.api.v1.admin.ListKnownPartiesRequest
	6, // 6: com.daml.ledger.api.v1.admin.PartyManagementService.AllocateParty:input_type -> com.daml.ledger.api.v1.admin.AllocatePartyRequest
	1, // 7: com.daml.ledger.api.v1.admin.PartyManagementService.GetParticipantId:output_type -> com.daml.ledger.api.v1.admin.GetParticipantIdResponse
	3, // 8: com.daml.ledger.api.v1.admin.PartyManagementService.GetParties:output_type -> com.daml.ledger.api.v1.admin.GetPartiesResponse
	5, // 9: com.daml.ledger.api.v1.admin.PartyManagementService.ListKnownParties:output_type -> com.daml.ledger.api.v1.admin.ListKnownPartiesResponse
	7, // 10: com.daml.ledger.api.v1.admin.PartyManagementService.AllocateParty:output_type -> com.daml.ledger.api.v1.admin.AllocatePartyResponse
	7, // [7:11] is the sub-list for method output_type
	3, // [3:7] is the sub-list for method input_type
	3, // [3:3] is the sub-list for extension type_name
	3, // [3:3] is the sub-list for extension extendee
	0, // [0:3] is the sub-list for field type_name
}

func init() { file_com_daml_ledger_api_v1_admin_party_management_service_proto_init() }
func file_com_daml_ledger_api_v1_admin_party_management_service_proto_init() {
	if File_com_daml_ledger_api_v1_admin_party_management_service_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetParticipantIdRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetParticipantIdResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetPartiesRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetPartiesResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ListKnownPartiesRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ListKnownPartiesResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*AllocatePartyRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[7].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*AllocatePartyResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes[8].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PartyDetails); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   9,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_com_daml_ledger_api_v1_admin_party_management_service_proto_goTypes,
		DependencyIndexes: file_com_daml_ledger_api_v1_admin_party_management_service_proto_depIdxs,
		MessageInfos:      file_com_daml_ledger_api_v1_admin_party_management_service_proto_msgTypes,
	}.Build()
	File_com_daml_ledger_api_v1_admin_party_management_service_proto = out.File
	file_com_daml_ledger_api_v1_admin_party_management_service_proto_rawDesc = nil
	file_com_daml_ledger_api_v1_admin_party_management_service_proto_goTypes = nil
	file_com_daml_ledger_api_v1_admin_party_management_service_proto_depIdxs = nil
}
