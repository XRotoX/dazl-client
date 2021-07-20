// Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package admin

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// PartyManagementServiceClient is the client API for PartyManagementService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type PartyManagementServiceClient interface {
	// Return the identifier of the backing participant.
	// All horizontally scaled replicas should return the same id.
	// daml-on-sql: returns an identifier supplied on command line at launch time
	// daml-on-kv-ledger: as above
	// canton: returns globally unique identifier of the backing participant
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	GetParticipantId(ctx context.Context, in *GetParticipantIdRequest, opts ...grpc.CallOption) (*GetParticipantIdResponse, error)
	// Get the party details of the given parties. Only known parties will be
	// returned in the list.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	GetParties(ctx context.Context, in *GetPartiesRequest, opts ...grpc.CallOption) (*GetPartiesResponse, error)
	// List the parties known by the backing participant.
	// The list returned contains parties whose ledger access is facilitated by
	// backing participant and the ones maintained elsewhere.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	ListKnownParties(ctx context.Context, in *ListKnownPartiesRequest, opts ...grpc.CallOption) (*ListKnownPartiesResponse, error)
	// Adds a new party to the set managed by the backing participant.
	// Caller specifies a party identifier suggestion, the actual identifier
	// allocated might be different and is implementation specific.
	// This call may:
	// - Succeed, in which case the actual allocated identifier is visible in
	//   the response.
	// - Respond with a gRPC error
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	// - ``UNIMPLEMENTED``: if synchronous party allocation is not supported by the backing participant
	// - ``INVALID_ARGUMENT``: if the provided hint and/or display name is invalid on the given ledger (see below).
	// daml-on-sql: suggestion's uniqueness is checked and call rejected if the identifier is already present
	// daml-on-kv-ledger: suggestion's uniqueness is checked by the validators in
	// the consensus layer and call rejected if the identifier is already present.
	// canton: completely different globally unique identifier is allocated.
	// Behind the scenes calls to an internal protocol are made. As that protocol
	// is richer than the surface protocol, the arguments take implicit values
	// The party identifier suggestion must be a valid party name. Party names are required to be non-empty US-ASCII strings built from letters, digits, space,
	// colon, minus and underscore limited to 255 chars
	AllocateParty(ctx context.Context, in *AllocatePartyRequest, opts ...grpc.CallOption) (*AllocatePartyResponse, error)
}

type partyManagementServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewPartyManagementServiceClient(cc grpc.ClientConnInterface) PartyManagementServiceClient {
	return &partyManagementServiceClient{cc}
}

func (c *partyManagementServiceClient) GetParticipantId(ctx context.Context, in *GetParticipantIdRequest, opts ...grpc.CallOption) (*GetParticipantIdResponse, error) {
	out := new(GetParticipantIdResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.admin.PartyManagementService/GetParticipantId", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *partyManagementServiceClient) GetParties(ctx context.Context, in *GetPartiesRequest, opts ...grpc.CallOption) (*GetPartiesResponse, error) {
	out := new(GetPartiesResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.admin.PartyManagementService/GetParties", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *partyManagementServiceClient) ListKnownParties(ctx context.Context, in *ListKnownPartiesRequest, opts ...grpc.CallOption) (*ListKnownPartiesResponse, error) {
	out := new(ListKnownPartiesResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.admin.PartyManagementService/ListKnownParties", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *partyManagementServiceClient) AllocateParty(ctx context.Context, in *AllocatePartyRequest, opts ...grpc.CallOption) (*AllocatePartyResponse, error) {
	out := new(AllocatePartyResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.admin.PartyManagementService/AllocateParty", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// PartyManagementServiceServer is the server API for PartyManagementService service.
// All implementations must embed UnimplementedPartyManagementServiceServer
// for forward compatibility
type PartyManagementServiceServer interface {
	// Return the identifier of the backing participant.
	// All horizontally scaled replicas should return the same id.
	// daml-on-sql: returns an identifier supplied on command line at launch time
	// daml-on-kv-ledger: as above
	// canton: returns globally unique identifier of the backing participant
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	GetParticipantId(context.Context, *GetParticipantIdRequest) (*GetParticipantIdResponse, error)
	// Get the party details of the given parties. Only known parties will be
	// returned in the list.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	GetParties(context.Context, *GetPartiesRequest) (*GetPartiesResponse, error)
	// List the parties known by the backing participant.
	// The list returned contains parties whose ledger access is facilitated by
	// backing participant and the ones maintained elsewhere.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	ListKnownParties(context.Context, *ListKnownPartiesRequest) (*ListKnownPartiesResponse, error)
	// Adds a new party to the set managed by the backing participant.
	// Caller specifies a party identifier suggestion, the actual identifier
	// allocated might be different and is implementation specific.
	// This call may:
	// - Succeed, in which case the actual allocated identifier is visible in
	//   the response.
	// - Respond with a gRPC error
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	// - ``UNIMPLEMENTED``: if synchronous party allocation is not supported by the backing participant
	// - ``INVALID_ARGUMENT``: if the provided hint and/or display name is invalid on the given ledger (see below).
	// daml-on-sql: suggestion's uniqueness is checked and call rejected if the identifier is already present
	// daml-on-kv-ledger: suggestion's uniqueness is checked by the validators in
	// the consensus layer and call rejected if the identifier is already present.
	// canton: completely different globally unique identifier is allocated.
	// Behind the scenes calls to an internal protocol are made. As that protocol
	// is richer than the surface protocol, the arguments take implicit values
	// The party identifier suggestion must be a valid party name. Party names are required to be non-empty US-ASCII strings built from letters, digits, space,
	// colon, minus and underscore limited to 255 chars
	AllocateParty(context.Context, *AllocatePartyRequest) (*AllocatePartyResponse, error)
	mustEmbedUnimplementedPartyManagementServiceServer()
}

// UnimplementedPartyManagementServiceServer must be embedded to have forward compatible implementations.
type UnimplementedPartyManagementServiceServer struct {
}

func (UnimplementedPartyManagementServiceServer) GetParticipantId(context.Context, *GetParticipantIdRequest) (*GetParticipantIdResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetParticipantId not implemented")
}
func (UnimplementedPartyManagementServiceServer) GetParties(context.Context, *GetPartiesRequest) (*GetPartiesResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetParties not implemented")
}
func (UnimplementedPartyManagementServiceServer) ListKnownParties(context.Context, *ListKnownPartiesRequest) (*ListKnownPartiesResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListKnownParties not implemented")
}
func (UnimplementedPartyManagementServiceServer) AllocateParty(context.Context, *AllocatePartyRequest) (*AllocatePartyResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AllocateParty not implemented")
}
func (UnimplementedPartyManagementServiceServer) mustEmbedUnimplementedPartyManagementServiceServer() {
}

// UnsafePartyManagementServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to PartyManagementServiceServer will
// result in compilation errors.
type UnsafePartyManagementServiceServer interface {
	mustEmbedUnimplementedPartyManagementServiceServer()
}

func RegisterPartyManagementServiceServer(s grpc.ServiceRegistrar, srv PartyManagementServiceServer) {
	s.RegisterService(&PartyManagementService_ServiceDesc, srv)
}

func _PartyManagementService_GetParticipantId_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetParticipantIdRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PartyManagementServiceServer).GetParticipantId(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.admin.PartyManagementService/GetParticipantId",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PartyManagementServiceServer).GetParticipantId(ctx, req.(*GetParticipantIdRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PartyManagementService_GetParties_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetPartiesRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PartyManagementServiceServer).GetParties(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.admin.PartyManagementService/GetParties",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PartyManagementServiceServer).GetParties(ctx, req.(*GetPartiesRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PartyManagementService_ListKnownParties_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListKnownPartiesRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PartyManagementServiceServer).ListKnownParties(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.admin.PartyManagementService/ListKnownParties",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PartyManagementServiceServer).ListKnownParties(ctx, req.(*ListKnownPartiesRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PartyManagementService_AllocateParty_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AllocatePartyRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PartyManagementServiceServer).AllocateParty(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.admin.PartyManagementService/AllocateParty",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PartyManagementServiceServer).AllocateParty(ctx, req.(*AllocatePartyRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// PartyManagementService_ServiceDesc is the grpc.ServiceDesc for PartyManagementService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var PartyManagementService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v1.admin.PartyManagementService",
	HandlerType: (*PartyManagementServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetParticipantId",
			Handler:    _PartyManagementService_GetParticipantId_Handler,
		},
		{
			MethodName: "GetParties",
			Handler:    _PartyManagementService_GetParties_Handler,
		},
		{
			MethodName: "ListKnownParties",
			Handler:    _PartyManagementService_ListKnownParties_Handler,
		},
		{
			MethodName: "AllocateParty",
			Handler:    _PartyManagementService_AllocateParty_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/daml/ledger/api/v1/admin/party_management_service.proto",
}
