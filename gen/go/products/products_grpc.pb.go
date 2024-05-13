// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             v4.25.3
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

const (
	Products_CreateProduct_FullMethodName        = "/productspb.Products/CreateProduct"
	Products_GetProductByID_FullMethodName       = "/productspb.Products/GetProductByID"
	Products_FindProducts_FullMethodName         = "/productspb.Products/FindProducts"
	Products_UpdateProductByID_FullMethodName    = "/productspb.Products/UpdateProductByID"
	Products_CreateCharacteristic_FullMethodName = "/productspb.Products/CreateCharacteristic"
	Products_FindCharacteristics_FullMethodName  = "/productspb.Products/FindCharacteristics"
	Products_UpdateCharacteristic_FullMethodName = "/productspb.Products/UpdateCharacteristic"
	Products_DeleteCharacteristic_FullMethodName = "/productspb.Products/DeleteCharacteristic"
	Products_ApplyFilters_FullMethodName         = "/productspb.Products/ApplyFilters"
)

// ProductsClient is the client API for Products service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ProductsClient interface {
	CreateProduct(ctx context.Context, in *CreateProductRequest, opts ...grpc.CallOption) (*CreateProductResponse, error)
	GetProductByID(ctx context.Context, in *GetProductByIDRequest, opts ...grpc.CallOption) (*GetProductByIDResponse, error)
	FindProducts(ctx context.Context, in *ProductsFilterRequest, opts ...grpc.CallOption) (*FindProductsResponse, error)
	UpdateProductByID(ctx context.Context, in *UpdateProductByIDRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	CreateCharacteristic(ctx context.Context, in *CreateCharacteristicRequest, opts ...grpc.CallOption) (*CreateCharacteristicResponse, error)
	FindCharacteristics(ctx context.Context, in *FindCharacteristicsRequest, opts ...grpc.CallOption) (*FindCharacteristicsResponse, error)
	UpdateCharacteristic(ctx context.Context, in *UpdateCharacteristicRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	DeleteCharacteristic(ctx context.Context, in *DeleteCharacteristicRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	ApplyFilters(ctx context.Context, in *ProductsFilterRequest, opts ...grpc.CallOption) (*AvailableFilters, error)
}

type productsClient struct {
	cc grpc.ClientConnInterface
}

func NewProductsClient(cc grpc.ClientConnInterface) ProductsClient {
	return &productsClient{cc}
}

func (c *productsClient) CreateProduct(ctx context.Context, in *CreateProductRequest, opts ...grpc.CallOption) (*CreateProductResponse, error) {
	out := new(CreateProductResponse)
	err := c.cc.Invoke(ctx, Products_CreateProduct_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) GetProductByID(ctx context.Context, in *GetProductByIDRequest, opts ...grpc.CallOption) (*GetProductByIDResponse, error) {
	out := new(GetProductByIDResponse)
	err := c.cc.Invoke(ctx, Products_GetProductByID_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) FindProducts(ctx context.Context, in *ProductsFilterRequest, opts ...grpc.CallOption) (*FindProductsResponse, error) {
	out := new(FindProductsResponse)
	err := c.cc.Invoke(ctx, Products_FindProducts_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) UpdateProductByID(ctx context.Context, in *UpdateProductByIDRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, Products_UpdateProductByID_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) CreateCharacteristic(ctx context.Context, in *CreateCharacteristicRequest, opts ...grpc.CallOption) (*CreateCharacteristicResponse, error) {
	out := new(CreateCharacteristicResponse)
	err := c.cc.Invoke(ctx, Products_CreateCharacteristic_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) FindCharacteristics(ctx context.Context, in *FindCharacteristicsRequest, opts ...grpc.CallOption) (*FindCharacteristicsResponse, error) {
	out := new(FindCharacteristicsResponse)
	err := c.cc.Invoke(ctx, Products_FindCharacteristics_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) UpdateCharacteristic(ctx context.Context, in *UpdateCharacteristicRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, Products_UpdateCharacteristic_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) DeleteCharacteristic(ctx context.Context, in *DeleteCharacteristicRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, Products_DeleteCharacteristic_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *productsClient) ApplyFilters(ctx context.Context, in *ProductsFilterRequest, opts ...grpc.CallOption) (*AvailableFilters, error) {
	out := new(AvailableFilters)
	err := c.cc.Invoke(ctx, Products_ApplyFilters_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ProductsServer is the server API for Products service.
// All implementations must embed UnimplementedProductsServer
// for forward compatibility
type ProductsServer interface {
	CreateProduct(context.Context, *CreateProductRequest) (*CreateProductResponse, error)
	GetProductByID(context.Context, *GetProductByIDRequest) (*GetProductByIDResponse, error)
	FindProducts(context.Context, *ProductsFilterRequest) (*FindProductsResponse, error)
	UpdateProductByID(context.Context, *UpdateProductByIDRequest) (*emptypb.Empty, error)
	CreateCharacteristic(context.Context, *CreateCharacteristicRequest) (*CreateCharacteristicResponse, error)
	FindCharacteristics(context.Context, *FindCharacteristicsRequest) (*FindCharacteristicsResponse, error)
	UpdateCharacteristic(context.Context, *UpdateCharacteristicRequest) (*emptypb.Empty, error)
	DeleteCharacteristic(context.Context, *DeleteCharacteristicRequest) (*emptypb.Empty, error)
	ApplyFilters(context.Context, *ProductsFilterRequest) (*AvailableFilters, error)
	mustEmbedUnimplementedProductsServer()
}

// UnimplementedProductsServer must be embedded to have forward compatible implementations.
type UnimplementedProductsServer struct {
}

func (UnimplementedProductsServer) CreateProduct(context.Context, *CreateProductRequest) (*CreateProductResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateProduct not implemented")
}
func (UnimplementedProductsServer) GetProductByID(context.Context, *GetProductByIDRequest) (*GetProductByIDResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetProductByID not implemented")
}
func (UnimplementedProductsServer) FindProducts(context.Context, *ProductsFilterRequest) (*FindProductsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method FindProducts not implemented")
}
func (UnimplementedProductsServer) UpdateProductByID(context.Context, *UpdateProductByIDRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateProductByID not implemented")
}
func (UnimplementedProductsServer) CreateCharacteristic(context.Context, *CreateCharacteristicRequest) (*CreateCharacteristicResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateCharacteristic not implemented")
}
func (UnimplementedProductsServer) FindCharacteristics(context.Context, *FindCharacteristicsRequest) (*FindCharacteristicsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method FindCharacteristics not implemented")
}
func (UnimplementedProductsServer) UpdateCharacteristic(context.Context, *UpdateCharacteristicRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateCharacteristic not implemented")
}
func (UnimplementedProductsServer) DeleteCharacteristic(context.Context, *DeleteCharacteristicRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteCharacteristic not implemented")
}
func (UnimplementedProductsServer) ApplyFilters(context.Context, *ProductsFilterRequest) (*AvailableFilters, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ApplyFilters not implemented")
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

func _Products_CreateProduct_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateProductRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).CreateProduct(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Products_CreateProduct_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).CreateProduct(ctx, req.(*CreateProductRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Products_GetProductByID_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetProductByIDRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).GetProductByID(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Products_GetProductByID_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).GetProductByID(ctx, req.(*GetProductByIDRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Products_FindProducts_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProductsFilterRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).FindProducts(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Products_FindProducts_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).FindProducts(ctx, req.(*ProductsFilterRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Products_UpdateProductByID_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateProductByIDRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).UpdateProductByID(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Products_UpdateProductByID_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).UpdateProductByID(ctx, req.(*UpdateProductByIDRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Products_CreateCharacteristic_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateCharacteristicRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).CreateCharacteristic(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Products_CreateCharacteristic_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).CreateCharacteristic(ctx, req.(*CreateCharacteristicRequest))
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
		FullMethod: Products_FindCharacteristics_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).FindCharacteristics(ctx, req.(*FindCharacteristicsRequest))
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
		FullMethod: Products_UpdateCharacteristic_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).UpdateCharacteristic(ctx, req.(*UpdateCharacteristicRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Products_DeleteCharacteristic_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DeleteCharacteristicRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).DeleteCharacteristic(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Products_DeleteCharacteristic_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).DeleteCharacteristic(ctx, req.(*DeleteCharacteristicRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Products_ApplyFilters_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProductsFilterRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProductsServer).ApplyFilters(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Products_ApplyFilters_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProductsServer).ApplyFilters(ctx, req.(*ProductsFilterRequest))
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
			MethodName: "CreateProduct",
			Handler:    _Products_CreateProduct_Handler,
		},
		{
			MethodName: "GetProductByID",
			Handler:    _Products_GetProductByID_Handler,
		},
		{
			MethodName: "FindProducts",
			Handler:    _Products_FindProducts_Handler,
		},
		{
			MethodName: "UpdateProductByID",
			Handler:    _Products_UpdateProductByID_Handler,
		},
		{
			MethodName: "CreateCharacteristic",
			Handler:    _Products_CreateCharacteristic_Handler,
		},
		{
			MethodName: "FindCharacteristics",
			Handler:    _Products_FindCharacteristics_Handler,
		},
		{
			MethodName: "UpdateCharacteristic",
			Handler:    _Products_UpdateCharacteristic_Handler,
		},
		{
			MethodName: "DeleteCharacteristic",
			Handler:    _Products_DeleteCharacteristic_Handler,
		},
		{
			MethodName: "ApplyFilters",
			Handler:    _Products_ApplyFilters_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "products/products.proto",
}
