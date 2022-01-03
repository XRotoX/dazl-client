// Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0
// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package v1

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

// PackageServiceClient is the client API for PackageService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type PackageServiceClient interface {
	// Returns the identifiers of all supported packages.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	// - ``NOT_FOUND``: if the request does not include a valid ledger id
	ListPackages(ctx context.Context, in *ListPackagesRequest, opts ...grpc.CallOption) (*ListPackagesResponse, error)
	// Returns the contents of a single package.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	// - ``NOT_FOUND``: if the requested package is unknown
	GetPackage(ctx context.Context, in *GetPackageRequest, opts ...grpc.CallOption) (*GetPackageResponse, error)
	// Returns the status of a single package.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	// - ``NOT_FOUND``: if the requested package is unknown
	GetPackageStatus(ctx context.Context, in *GetPackageStatusRequest, opts ...grpc.CallOption) (*GetPackageStatusResponse, error)
}

type packageServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewPackageServiceClient(cc grpc.ClientConnInterface) PackageServiceClient {
	return &packageServiceClient{cc}
}

func (c *packageServiceClient) ListPackages(ctx context.Context, in *ListPackagesRequest, opts ...grpc.CallOption) (*ListPackagesResponse, error) {
	out := new(ListPackagesResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.PackageService/ListPackages", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *packageServiceClient) GetPackage(ctx context.Context, in *GetPackageRequest, opts ...grpc.CallOption) (*GetPackageResponse, error) {
	out := new(GetPackageResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.PackageService/GetPackage", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *packageServiceClient) GetPackageStatus(ctx context.Context, in *GetPackageStatusRequest, opts ...grpc.CallOption) (*GetPackageStatusResponse, error) {
	out := new(GetPackageStatusResponse)
	err := c.cc.Invoke(ctx, "/com.daml.ledger.api.v1.PackageService/GetPackageStatus", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// PackageServiceServer is the server API for PackageService service.
// All implementations must embed UnimplementedPackageServiceServer
// for forward compatibility
type PackageServiceServer interface {
	// Returns the identifiers of all supported packages.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	// - ``NOT_FOUND``: if the request does not include a valid ledger id
	ListPackages(context.Context, *ListPackagesRequest) (*ListPackagesResponse, error)
	// Returns the contents of a single package.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	// - ``NOT_FOUND``: if the requested package is unknown
	GetPackage(context.Context, *GetPackageRequest) (*GetPackageResponse, error)
	// Returns the status of a single package.
	// Errors:
	// - ``UNAUTHENTICATED``: if the request does not include a valid access token
	// - ``PERMISSION_DENIED``: if the claims in the token are insufficient to perform a given operation
	// - ``NOT_FOUND``: if the requested package is unknown
	GetPackageStatus(context.Context, *GetPackageStatusRequest) (*GetPackageStatusResponse, error)
	mustEmbedUnimplementedPackageServiceServer()
}

// UnimplementedPackageServiceServer must be embedded to have forward compatible implementations.
type UnimplementedPackageServiceServer struct {
}

func (UnimplementedPackageServiceServer) ListPackages(context.Context, *ListPackagesRequest) (*ListPackagesResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListPackages not implemented")
}
func (UnimplementedPackageServiceServer) GetPackage(context.Context, *GetPackageRequest) (*GetPackageResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetPackage not implemented")
}
func (UnimplementedPackageServiceServer) GetPackageStatus(context.Context, *GetPackageStatusRequest) (*GetPackageStatusResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetPackageStatus not implemented")
}
func (UnimplementedPackageServiceServer) mustEmbedUnimplementedPackageServiceServer() {}

// UnsafePackageServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to PackageServiceServer will
// result in compilation errors.
type UnsafePackageServiceServer interface {
	mustEmbedUnimplementedPackageServiceServer()
}

func RegisterPackageServiceServer(s grpc.ServiceRegistrar, srv PackageServiceServer) {
	s.RegisterService(&PackageService_ServiceDesc, srv)
}

func _PackageService_ListPackages_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListPackagesRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PackageServiceServer).ListPackages(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.PackageService/ListPackages",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PackageServiceServer).ListPackages(ctx, req.(*ListPackagesRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PackageService_GetPackage_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetPackageRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PackageServiceServer).GetPackage(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.PackageService/GetPackage",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PackageServiceServer).GetPackage(ctx, req.(*GetPackageRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PackageService_GetPackageStatus_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetPackageStatusRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PackageServiceServer).GetPackageStatus(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/com.daml.ledger.api.v1.PackageService/GetPackageStatus",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PackageServiceServer).GetPackageStatus(ctx, req.(*GetPackageStatusRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// PackageService_ServiceDesc is the grpc.ServiceDesc for PackageService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var PackageService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "com.daml.ledger.api.v1.PackageService",
	HandlerType: (*PackageServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ListPackages",
			Handler:    _PackageService_ListPackages_Handler,
		},
		{
			MethodName: "GetPackage",
			Handler:    _PackageService_GetPackage_Handler,
		},
		{
			MethodName: "GetPackageStatus",
			Handler:    _PackageService_GetPackageStatus_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "com/daml/ledger/api/v1/package_service.proto",
}
