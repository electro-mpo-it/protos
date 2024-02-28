// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.25.0
// source: suppliers/suppliers.proto

package supplpb

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// SuppliersClient is the client API for Suppliers service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type SuppliersClient interface {
	Create(ctx context.Context, in *CreateRequest, opts ...grpc.CallOption) (*CreateResponse, error)
	GetByID(ctx context.Context, in *GetByIDRequest, opts ...grpc.CallOption) (*GetByIDResponse, error)
	Find(ctx context.Context, in *FindRequest, opts ...grpc.CallOption) (*FindResponse, error)
	Update(ctx context.Context, in *UpdateRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
}

type suppliersClient struct {
	cc grpc.ClientConnInterface
}

func NewSuppliersClient(cc grpc.ClientConnInterface) SuppliersClient {
	return &suppliersClient{cc}
}

func (c *suppliersClient) Create(ctx context.Context, in *CreateRequest, opts ...grpc.CallOption) (*CreateResponse, error) {
	out := new(CreateResponse)
	err := c.cc.Invoke(ctx, "/supplpb.Suppliers/Create", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *suppliersClient) GetByID(ctx context.Context, in *GetByIDRequest, opts ...grpc.CallOption) (*GetByIDResponse, error) {
	out := new(GetByIDResponse)
	err := c.cc.Invoke(ctx, "/supplpb.Suppliers/GetByID", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *suppliersClient) Find(ctx context.Context, in *FindRequest, opts ...grpc.CallOption) (*FindResponse, error) {
	out := new(FindResponse)
	err := c.cc.Invoke(ctx, "/supplpb.Suppliers/Find", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *suppliersClient) Update(ctx context.Context, in *UpdateRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, "/supplpb.Suppliers/Update", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SuppliersServer is the server API for Suppliers service.
// All implementations must embed UnimplementedSuppliersServer
// for forward compatibility
type SuppliersServer interface {
	Create(context.Context, *CreateRequest) (*CreateResponse, error)
	GetByID(context.Context, *GetByIDRequest) (*GetByIDResponse, error)
	Find(context.Context, *FindRequest) (*FindResponse, error)
	Update(context.Context, *UpdateRequest) (*emptypb.Empty, error)
	mustEmbedUnimplementedSuppliersServer()
}

// UnimplementedSuppliersServer must be embedded to have forward compatible implementations.
type UnimplementedSuppliersServer struct {
}

func (UnimplementedSuppliersServer) Create(context.Context, *CreateRequest) (*CreateResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create not implemented")
}
func (UnimplementedSuppliersServer) GetByID(context.Context, *GetByIDRequest) (*GetByIDResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetByID not implemented")
}
func (UnimplementedSuppliersServer) Find(context.Context, *FindRequest) (*FindResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Find not implemented")
}
func (UnimplementedSuppliersServer) Update(context.Context, *UpdateRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (UnimplementedSuppliersServer) mustEmbedUnimplementedSuppliersServer() {}

// UnsafeSuppliersServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to SuppliersServer will
// result in compilation errors.
type UnsafeSuppliersServer interface {
	mustEmbedUnimplementedSuppliersServer()
}

func RegisterSuppliersServer(s grpc.ServiceRegistrar, srv SuppliersServer) {
	s.RegisterService(&Suppliers_ServiceDesc, srv)
}

func _Suppliers_Create_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SuppliersServer).Create(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/supplpb.Suppliers/Create",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SuppliersServer).Create(ctx, req.(*CreateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Suppliers_GetByID_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetByIDRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SuppliersServer).GetByID(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/supplpb.Suppliers/GetByID",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SuppliersServer).GetByID(ctx, req.(*GetByIDRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Suppliers_Find_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(FindRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SuppliersServer).Find(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/supplpb.Suppliers/Find",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SuppliersServer).Find(ctx, req.(*FindRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Suppliers_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SuppliersServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/supplpb.Suppliers/Update",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SuppliersServer).Update(ctx, req.(*UpdateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Suppliers_ServiceDesc is the grpc.ServiceDesc for Suppliers service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Suppliers_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "supplpb.Suppliers",
	HandlerType: (*SuppliersServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Create",
			Handler:    _Suppliers_Create_Handler,
		},
		{
			MethodName: "GetByID",
			Handler:    _Suppliers_GetByID_Handler,
		},
		{
			MethodName: "Find",
			Handler:    _Suppliers_Find_Handler,
		},
		{
			MethodName: "Update",
			Handler:    _Suppliers_Update_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "suppliers/suppliers.proto",
}