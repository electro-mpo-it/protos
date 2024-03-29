# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: purchases/purchases.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19purchases/purchases.proto\x12\x0bpurchasespb\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\"d\n\x08Supplier\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x61lias\x18\x02 \x01(\t\x12\x12\n\nlegal_name\x18\x03 \x01(\t\x12\x0b\n\x03inn\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\r\n\x05phone\x18\x06 \x01(\t\"\xc1\x01\n\x0ePurchasingInfo\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\'\n\x08supplier\x18\x02 \x01(\x0b\x32\x15.purchasespb.Supplier\x12;\n\x15min_purchase_quantity\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x35\n\x12\x64\x65livery_timedelta\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\"\xa1\x01\n\x15\x43reateSupplierRequest\x12\r\n\x05\x61lias\x18\x01 \x01(\t\x12\x12\n\nlegal_name\x18\x02 \x01(\t\x12\x0b\n\x03inn\x18\x03 \x01(\t\x12+\n\x05\x65mail\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05phone\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"$\n\x16\x43reateSupplierResponse\x12\n\n\x02id\x18\x01 \x01(\t\" \n\x12GetSupplierRequest\x12\n\n\x02id\x18\x01 \x01(\t\":\n\x13GetSupplierResponse\x12#\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x15.purchasespb.Supplier\"\x9f\x01\n\x14\x46indSuppliersRequest\x12+\n\x05limit\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12,\n\x06offset\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12,\n\x06search\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"<\n\x15\x46indSuppliersResponse\x12#\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x15.purchasespb.Supplier\"\xc7\x02\n\x15UpdateSupplierRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x35\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\'.purchasespb.UpdateSupplierRequest.Data\x1a\xea\x01\n\x04\x44\x61ta\x12+\n\x05\x61lias\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nlegal_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x03inn\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05\x65mail\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05phone\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xba\x01\n\x1b\x43reatePurchasingInfoRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x13\n\x0bsupplier_id\x18\x02 \x01(\t\x12;\n\x15min_purchase_quantity\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x35\n\x12\x64\x65livery_timedelta\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\".\n\x18GetPurchasingInfoRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\"F\n\x19GetPurchasingInfoResponse\x12)\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1b.purchasespb.PurchasingInfo\"\x9e\x02\n\x1bUpdatePurchasingInfoRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12;\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32-.purchasespb.UpdatePurchasingInfoRequest.Data\x1a\xad\x01\n\x04\x44\x61ta\x12\x31\n\x0bsupplier_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x15min_purchase_quantity\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x35\n\x12\x64\x65livery_timedelta\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration2\xf6\x04\n\tPurchases\x12Y\n\x0e\x43reateSupplier\x12\".purchasespb.CreateSupplierRequest\x1a#.purchasespb.CreateSupplierResponse\x12P\n\x0bGetSupplier\x12\x1f.purchasespb.GetSupplierRequest\x1a .purchasespb.GetSupplierResponse\x12V\n\rFindSuppliers\x12!.purchasespb.FindSuppliersRequest\x1a\".purchasespb.FindSuppliersResponse\x12L\n\x0eUpdateSupplier\x12\".purchasespb.UpdateSupplierRequest\x1a\x16.google.protobuf.Empty\x12X\n\x14\x43reatePurchasingInfo\x12(.purchasespb.CreatePurchasingInfoRequest\x1a\x16.google.protobuf.Empty\x12\x62\n\x11GetPurchasingInfo\x12%.purchasespb.GetPurchasingInfoRequest\x1a&.purchasespb.GetPurchasingInfoResponse\x12X\n\x14UpdatePurchasingInfo\x12(.purchasespb.UpdatePurchasingInfoRequest\x1a\x16.google.protobuf.EmptyB?Z=github.com/electro-mpo-it/protos/gen/go/purchases;purchasespbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'purchases.purchases_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/electro-mpo-it/protos/gen/go/purchases;purchasespb'
  _globals['_SUPPLIER']._serialized_start=135
  _globals['_SUPPLIER']._serialized_end=235
  _globals['_PURCHASINGINFO']._serialized_start=238
  _globals['_PURCHASINGINFO']._serialized_end=431
  _globals['_CREATESUPPLIERREQUEST']._serialized_start=434
  _globals['_CREATESUPPLIERREQUEST']._serialized_end=595
  _globals['_CREATESUPPLIERRESPONSE']._serialized_start=597
  _globals['_CREATESUPPLIERRESPONSE']._serialized_end=633
  _globals['_GETSUPPLIERREQUEST']._serialized_start=635
  _globals['_GETSUPPLIERREQUEST']._serialized_end=667
  _globals['_GETSUPPLIERRESPONSE']._serialized_start=669
  _globals['_GETSUPPLIERRESPONSE']._serialized_end=727
  _globals['_FINDSUPPLIERSREQUEST']._serialized_start=730
  _globals['_FINDSUPPLIERSREQUEST']._serialized_end=889
  _globals['_FINDSUPPLIERSRESPONSE']._serialized_start=891
  _globals['_FINDSUPPLIERSRESPONSE']._serialized_end=951
  _globals['_UPDATESUPPLIERREQUEST']._serialized_start=954
  _globals['_UPDATESUPPLIERREQUEST']._serialized_end=1281
  _globals['_UPDATESUPPLIERREQUEST_DATA']._serialized_start=1047
  _globals['_UPDATESUPPLIERREQUEST_DATA']._serialized_end=1281
  _globals['_CREATEPURCHASINGINFOREQUEST']._serialized_start=1284
  _globals['_CREATEPURCHASINGINFOREQUEST']._serialized_end=1470
  _globals['_GETPURCHASINGINFOREQUEST']._serialized_start=1472
  _globals['_GETPURCHASINGINFOREQUEST']._serialized_end=1518
  _globals['_GETPURCHASINGINFORESPONSE']._serialized_start=1520
  _globals['_GETPURCHASINGINFORESPONSE']._serialized_end=1590
  _globals['_UPDATEPURCHASINGINFOREQUEST']._serialized_start=1593
  _globals['_UPDATEPURCHASINGINFOREQUEST']._serialized_end=1879
  _globals['_UPDATEPURCHASINGINFOREQUEST_DATA']._serialized_start=1706
  _globals['_UPDATEPURCHASINGINFOREQUEST_DATA']._serialized_end=1879
  _globals['_PURCHASES']._serialized_start=1882
  _globals['_PURCHASES']._serialized_end=2512
# @@protoc_insertion_point(module_scope)