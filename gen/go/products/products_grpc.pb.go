// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.25.0
// source: products/products.proto

package productspb

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

// ProductsClient is the client API for Products service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ProductsClient interface {
	Create(ctx context.Context, in *CreateProductRequest, opts ...grpc.CallOption) (*CreateProductResponse, error)
	GetByID(ctx context.Context, in *GetProductRequest, opts ...grpc.CallOption) (*GetProductResponse, error)
	Find(ctx context.Context, in *FindProductsRequest, opts ...grpc.CallOption) (*FindProductsResponse, error)
	Update(ctx context.Context, in *UpdateProductRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	FindCharacteristics(ctx context.Context, in *FindCharacteristicsRequest, opts ...grpc.CallOption) (*FindCharacteristicsResponse, error)
	AddCharacteristic(ctx context.Context, in *AddCharacteristicRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	UpdateCharacteristic(ctx context.Context, in *UpdateCharacteristicRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	RemoveCharacteristic(ctx context.Context, in *RemoveCharacteristicRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
}

type productsClient struct {
	cc grpc.ClientConnInterface
}

func NewProductsClient(cc grpc.ClientConnInterface) ProductsClient {
	return &productsClient{cc}
}

func (c *productsClient) Create(ctx context.Context, in *CreateProductRequest, opts ...grpc.CallOption) (*CreateProductResponse, error) {
	out := new(CreateProductResponse)
	err := c.cc.Invoke(ctx, "/productspb.Products/Create", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) GetByID(ctx context.Context, in *GetProductRequest, opts ...grpc.CallOption) (*GetProductResponse, error) {
	out := new(GetProductResponse)
	err := c.cc.Invoke(ctx, "/productspb.Products/GetByID", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) Find(ctx context.Context, in *FindProductsRequest, opts ...grpc.CallOption) (*FindProductsResponse, error) {
	out := new(FindProductsResponse)
	err := c.cc.Invoke(ctx, "/productspb.Products/Find", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) Update(ctx context.Context, in *UpdateProductRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, "/productspb.Products/Update", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) FindCharacteristics(ctx context.Context, in *FindCharacteristicsRequest, opts ...grpc.CallOption) (*FindCharacteristicsResponse, error) {
	out := new(FindCharacteristicsResponse)
	err := c.cc.Invoke(ctx, "/productspb.Products/FindCharacteristics", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) AddCharacteristic(ctx context.Context, in *AddCharacteristicRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, "/productspb.Products/AddCharacteristic", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) UpdateCharacteristic(ctx context.Context, in *UpdateCharacteristicRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, "/productspb.Products/UpdateCharacteristic", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) RemoveCharacteristic(ctx context.Context, in *RemoveCharacteristicRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, "/productspb.Products/RemoveCharacteristic", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ProductsServer is the server API for Products service.
// All implementations must embed UnimplementedProductsServer
// for forward compatibility
type ProductsServer interface {
	Create(context.Context, *CreateProductRequest) (*CreateProductResponse, error)
	GetByID(context.Context, *GetProductRequest) (*GetProductResponse, error)
	Find(context.Context, *FindProductsRequest) (*FindProductsResponse, error)
	Update(context.Context, *UpdateProductRequest) (*emptypb.Empty, error)
	FindCharacteristics(context.Context, *FindCharacteristicsRequest) (*FindCharacteristicsResponse, error)
	AddCharacteristic(context.Context, *AddCharacteristicRequest) (*emptypb.Empty, error)
	UpdateCharacteristic(context.Context, *UpdateCharacteristicRequest) (*emptypb.Empty, error)
	RemoveCharacteristic(context.Context, *RemoveCharacteristicRequest) (*emptypb.Empty, error)
	mustEmbedUnimplementedProductsServer()
}

// UnimplementedProductsServer must be embedded to have forward compatible implementations.
type UnimplementedProductsServer struct {
}

func (UnimplementedProductsServer) Create(context.Context, *CreateProductRequest) (*CreateProductResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create not implemented")
}
func (UnimplementedProductsServer) GetByID(context.Context, *GetProductRequest) (*GetProductResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetByID not implemented")
}
func (UnimplementedProductsServer) Find(context.Context, *FindProductsRequest) (*FindProductsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Find not implemented")
}
func (UnimplementedProductsServer) Update(context.Context, *UpdateProductRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (UnimplementedProductsServer) FindCharacteristics(context.Context, *FindCharacteristicsRequest) (*FindCharacteristicsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method FindCharacteristics not implemented")
}
func (UnimplementedProductsServer) AddCharacteristic(context.Context, *AddCharacteristicRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AddCharacteristic not implemented")
}
func (UnimplementedProductsServer) UpdateCharacteristic(context.Context, *UpdateCharacteristicRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateCharacteristic not implemented")
}
func (UnimplementedProductsServer) RemoveCharacteristic(context.Context, *RemoveCharacteristicRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RemoveCharacteristic not implemented")
}
func (UnimplementedProductsServer) mustEmbedUnimplementedProductsServer() {}

// UnsafeProductsServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ProductsServer will
// result in compilation errors.
type UnsafeProductsServer interface {
	mustEmbedUnimplementedProductsServer()
}

func RegisterProductsServer(s grpc.ServiceRegistrar, srv ProductsServer) {
	s.RegisterService(&Products_ServiceDesc, srv)
}

func _Products_Create_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateProductRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).Create(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/productspb.Products/Create",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).Create(ctx, req.(*CreateProductRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Products_GetByID_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetProductRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).GetByID(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/productspb.Products/GetByID",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).GetByID(ctx, req.(*GetProductRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Products_Find_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(FindProductsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).Find(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/productspb.Products/Find",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).Find(ctx, req.(*FindProductsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Products_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateProductRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/productspb.Products/Update",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).Update(ctx, req.(*UpdateProductRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Products_FindCharacteristics_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(FindCharacteristicsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).FindCharacteristics(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/productspb.Products/FindCharacteristics",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).FindCharacteristics(ctx, req.(*FindCharacteristicsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Products_AddCharacteristic_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AddCharacteristicRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).AddCharacteristic(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/productspb.Products/AddCharacteristic",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).AddCharacteristic(ctx, req.(*AddCharacteristicRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Products_UpdateCharacteristic_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateCharacteristicRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).UpdateCharacteristic(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/productspb.Products/UpdateCharacteristic",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).UpdateCharacteristic(ctx, req.(*UpdateCharacteristicRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Products_RemoveCharacteristic_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(RemoveCharacteristicRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).RemoveCharacteristic(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/productspb.Products/RemoveCharacteristic",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).RemoveCharacteristic(ctx, req.(*RemoveCharacteristicRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Products_ServiceDesc is the grpc.ServiceDesc for Products service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Products_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "productspb.Products",
	HandlerType: (*ProductsServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Create",
			Handler:    _Products_Create_Handler,
		},
		{
			MethodName: "GetByID",
			Handler:    _Products_GetByID_Handler,
		},
		{
			MethodName: "Find",
			Handler:    _Products_Find_Handler,
		},
		{
			MethodName: "Update",
			Handler:    _Products_Update_Handler,
		},
		{
			MethodName: "FindCharacteristics",
			Handler:    _Products_FindCharacteristics_Handler,
		},
		{
			MethodName: "AddCharacteristic",
			Handler:    _Products_AddCharacteristic_Handler,
		},
		{
			MethodName: "UpdateCharacteristic",
			Handler:    _Products_UpdateCharacteristic_Handler,
		},
		{
			MethodName: "RemoveCharacteristic",
			Handler:    _Products_RemoveCharacteristic_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "products/products.proto",
}