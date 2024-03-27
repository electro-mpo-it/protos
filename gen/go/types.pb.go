// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.33.0
// 	protoc        v4.25.3
// source: types.proto

package typespb

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	structpb "google.golang.org/protobuf/types/known/structpb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// Используется в случаях, когда значение поля может быть (строкой или NULL) или значение поля игнорируется
type NullNullString struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Kind:
	//
	//	*NullNullString_N
	//	*NullNullString_Value
	Kind isNullNullString_Kind `protobuf_oneof:"kind"`
}

func (x *NullNullString) Reset() {
	*x = NullNullString{}
	if protoimpl.UnsafeEnabled {
		mi := &file_types_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *NullNullString) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*NullNullString) ProtoMessage() {}

func (x *NullNullString) ProtoReflect() protoreflect.Message {
	mi := &file_types_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use NullNullString.ProtoReflect.Descriptor instead.
func (*NullNullString) Descriptor() ([]byte, []int) {
	return file_types_proto_rawDescGZIP(), []int{0}
}

func (m *NullNullString) GetKind() isNullNullString_Kind {
	if m != nil {
		return m.Kind
	}
	return nil
}

func (x *NullNullString) GetN() structpb.NullValue {
	if x, ok := x.GetKind().(*NullNullString_N); ok {
		return x.N
	}
	return structpb.NullValue(0)
}

func (x *NullNullString) GetValue() string {
	if x, ok := x.GetKind().(*NullNullString_Value); ok {
		return x.Value
	}
	return ""
}

type isNullNullString_Kind interface {
	isNullNullString_Kind()
}

type NullNullString_N struct {
	N structpb.NullValue `protobuf:"varint,1,opt,name=n,proto3,enum=google.protobuf.NullValue,oneof"`
}

type NullNullString_Value struct {
	Value string `protobuf:"bytes,2,opt,name=value,proto3,oneof"`
}

func (*NullNullString_N) isNullNullString_Kind() {}

func (*NullNullString_Value) isNullNullString_Kind() {}

var File_types_proto protoreflect.FileDescriptor

var file_types_proto_rawDesc = []byte{
	0x0a, 0x0b, 0x74, 0x79, 0x70, 0x65, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x07, 0x74,
	0x79, 0x70, 0x65, 0x73, 0x70, 0x62, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x73, 0x74, 0x72, 0x75, 0x63, 0x74, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x22, 0x5c, 0x0a, 0x0e, 0x4e, 0x75, 0x6c, 0x6c, 0x4e, 0x75, 0x6c, 0x6c,
	0x53, 0x74, 0x72, 0x69, 0x6e, 0x67, 0x12, 0x2a, 0x0a, 0x01, 0x6e, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x0e, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2e, 0x4e, 0x75, 0x6c, 0x6c, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x48, 0x00, 0x52,
	0x01, 0x6e, 0x12, 0x16, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x09, 0x48, 0x00, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x42, 0x06, 0x0a, 0x04, 0x6b, 0x69,
	0x6e, 0x64, 0x42, 0x31, 0x5a, 0x2f, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d,
	0x2f, 0x65, 0x6c, 0x65, 0x63, 0x74, 0x72, 0x6f, 0x2d, 0x6d, 0x70, 0x6f, 0x2d, 0x69, 0x74, 0x2f,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x67, 0x65, 0x6e, 0x2f, 0x67, 0x6f, 0x3b, 0x74, 0x79,
	0x70, 0x65, 0x73, 0x70, 0x62, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_types_proto_rawDescOnce sync.Once
	file_types_proto_rawDescData = file_types_proto_rawDesc
)

func file_types_proto_rawDescGZIP() []byte {
	file_types_proto_rawDescOnce.Do(func() {
		file_types_proto_rawDescData = protoimpl.X.CompressGZIP(file_types_proto_rawDescData)
	})
	return file_types_proto_rawDescData
}

var file_types_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_types_proto_goTypes = []interface{}{
	(*NullNullString)(nil),  // 0: typespb.NullNullString
	(structpb.NullValue)(0), // 1: google.protobuf.NullValue
}
var file_types_proto_depIdxs = []int32{
	1, // 0: typespb.NullNullString.n:type_name -> google.protobuf.NullValue
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_types_proto_init() }
func file_types_proto_init() {
	if File_types_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_types_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*NullNullString); i {
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
	file_types_proto_msgTypes[0].OneofWrappers = []interface{}{
		(*NullNullString_N)(nil),
		(*NullNullString_Value)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_types_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_types_proto_goTypes,
		DependencyIndexes: file_types_proto_depIdxs,
		MessageInfos:      file_types_proto_msgTypes,
	}.Build()
	File_types_proto = out.File
	file_types_proto_rawDesc = nil
	file_types_proto_goTypes = nil
	file_types_proto_depIdxs = nil
}
