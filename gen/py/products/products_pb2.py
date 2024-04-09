# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: products/products.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17products/products.proto\x12\nproductspb\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"Q\n\x1dOptionalUnitOfMeasurementENUM\x12\x30\n\x05value\x18\x01 \x01(\x0e\x32!.productspb.UnitOfMeasurementENUM\"5\n\x0fOptionalVATENUM\x12\"\n\x05value\x18\x01 \x01(\x0e\x32\x13.productspb.VATENUM\"/\n\x0cProductImage\x12\x11\n\timage_url\x18\x01 \x01(\t\x12\x0c\n\x04sort\x18\x02 \x01(\r\"\xd0\x02\n\x15\x43haracteristicsFilter\x12@\n\x0btext_values\x18\x01 \x03(\x0b\x32+.productspb.CharacteristicsFilter.TextValue\x12\x46\n\x0enumeric_values\x18\x02 \x03(\x0b\x32..productspb.CharacteristicsFilter.NumericValue\x1a\'\n\tTextValue\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\x1a\x83\x01\n\x0cNumericValue\x12\n\n\x02id\x18\x01 \x01(\t\x12\x44\n\x06values\x18\x02 \x01(\x0b\x32\x34.productspb.CharacteristicsFilter.NumericValue.Range\x1a!\n\x05Range\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x01\x12\n\n\x02to\x18\x02 \x01(\x01\"\xd7\x02\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x61tegory_id\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12>\n\x13unit_of_measurement\x18\x05 \x01(\x0e\x32!.productspb.UnitOfMeasurementENUM\x12 \n\x03vat\x18\x06 \x01(\x0e\x32\x13.productspb.VATENUM\x12\x11\n\told_price\x18\x07 \x01(\x01\x12\x16\n\x0e\x64iscount_ratio\x18\x08 \x01(\x01\x12\r\n\x05price\x18\t \x01(\x01\x12\x12\n\nis_visible\x18\n \x01(\x08\x12.\n\nupdated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x06images\x18\x0c \x03(\x0b\x32\x18.productspb.ProductImage\"\xd4\x01\n\rCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x61tegory_id\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12>\n\x13unit_of_measurement\x18\x04 \x01(\x0e\x32!.productspb.UnitOfMeasurementENUM\x12 \n\x03vat\x18\x05 \x01(\x0e\x32\x13.productspb.VATENUM\x12\x11\n\told_price\x18\x06 \x01(\x01\x12\x16\n\x0e\x64iscount_ratio\x18\x07 \x01(\x01\"\x1c\n\x0e\x43reateResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x1c\n\x0eGetByIDRequest\x12\n\n\x02id\x18\x01 \x01(\t\"4\n\x0fGetByIDResponse\x12!\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x13.productspb.Product\"\xf9\x01\n\x0b\x46indRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12,\n\x06search\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x63\x61tegory_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\nis_visible\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12:\n\x0f\x63haracteristics\x18\x06 \x01(\x0b\x32!.productspb.CharacteristicsFilter\"1\n\x0c\x46indResponse\x12!\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x13.productspb.Product\"\xbd\x03\n\rUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12,\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1e.productspb.UpdateRequest.Data\x1a\xf1\x02\n\x04\x44\x61ta\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x63\x61tegory_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x46\n\x13unit_of_measurement\x18\x04 \x01(\x0b\x32).productspb.OptionalUnitOfMeasurementENUM\x12(\n\x03vat\x18\x05 \x01(\x0b\x32\x1b.productspb.OptionalVATENUM\x12/\n\told_price\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x34\n\x0e\x64iscount_ratio\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\"m\n\x11SetVisibleRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\".productspb.SetVisibleRequest.Data\x1a\x1a\n\x04\x44\x61ta\x12\x12\n\nis_visible\x18\x01 \x01(\x08\"\x87\x01\n\x13UpdateImagesRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32$.productspb.UpdateImagesRequest.Data\x1a\x30\n\x04\x44\x61ta\x12(\n\x06images\x18\x01 \x03(\x0b\x32\x18.productspb.ProductImage*\x98\x01\n\x15UnitOfMeasurementENUM\x12\t\n\x05PIECE\x10\x00\x12\x08\n\x04PAIR\x10\x01\x12\t\n\x05LITER\x10\x02\x12\x08\n\x04ROLL\x10\x03\x12\t\n\x05SHEET\x10\x04\x12\x0e\n\nCENTIMETRE\x10\x05\x12\t\n\x05METRE\x10\x06\x12\x0c\n\x08KILOGRAM\x10\x07\x12\x10\n\x0cSQUARE_METER\x10\x08\x12\x0f\n\x0b\x43UBIC_METER\x10\t*)\n\x07VATENUM\x12\t\n\x05NDS20\x10\x00\x12\t\n\x05NDS10\x10\x01\x12\x08\n\x04NDS0\x10\x02\x32\x95\x03\n\x08Products\x12?\n\x06\x43reate\x12\x19.productspb.CreateRequest\x1a\x1a.productspb.CreateResponse\x12\x42\n\x07GetByID\x12\x1a.productspb.GetByIDRequest\x1a\x1b.productspb.GetByIDResponse\x12\x39\n\x04\x46ind\x12\x17.productspb.FindRequest\x1a\x18.productspb.FindResponse\x12;\n\x06Update\x12\x19.productspb.UpdateRequest\x1a\x16.google.protobuf.Empty\x12\x43\n\nSetVisible\x12\x1d.productspb.SetVisibleRequest\x1a\x16.google.protobuf.Empty\x12G\n\x0cUpdateImages\x12\x1f.productspb.UpdateImagesRequest\x1a\x16.google.protobuf.EmptyB=Z;github.com/electro-mpo-it/protos/gen/go/products;productspbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'products.products_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z;github.com/electro-mpo-it/protos/gen/go/products;productspb'
  _globals['_UNITOFMEASUREMENTENUM']._serialized_start=2335
  _globals['_UNITOFMEASUREMENTENUM']._serialized_end=2487
  _globals['_VATENUM']._serialized_start=2489
  _globals['_VATENUM']._serialized_end=2530
  _globals['_OPTIONALUNITOFMEASUREMENTENUM']._serialized_start=133
  _globals['_OPTIONALUNITOFMEASUREMENTENUM']._serialized_end=214
  _globals['_OPTIONALVATENUM']._serialized_start=216
  _globals['_OPTIONALVATENUM']._serialized_end=269
  _globals['_PRODUCTIMAGE']._serialized_start=271
  _globals['_PRODUCTIMAGE']._serialized_end=318
  _globals['_CHARACTERISTICSFILTER']._serialized_start=321
  _globals['_CHARACTERISTICSFILTER']._serialized_end=657
  _globals['_CHARACTERISTICSFILTER_TEXTVALUE']._serialized_start=484
  _globals['_CHARACTERISTICSFILTER_TEXTVALUE']._serialized_end=523
  _globals['_CHARACTERISTICSFILTER_NUMERICVALUE']._serialized_start=526
  _globals['_CHARACTERISTICSFILTER_NUMERICVALUE']._serialized_end=657
  _globals['_CHARACTERISTICSFILTER_NUMERICVALUE_RANGE']._serialized_start=624
  _globals['_CHARACTERISTICSFILTER_NUMERICVALUE_RANGE']._serialized_end=657
  _globals['_PRODUCT']._serialized_start=660
  _globals['_PRODUCT']._serialized_end=1003
  _globals['_CREATEREQUEST']._serialized_start=1006
  _globals['_CREATEREQUEST']._serialized_end=1218
  _globals['_CREATERESPONSE']._serialized_start=1220
  _globals['_CREATERESPONSE']._serialized_end=1248
  _globals['_GETBYIDREQUEST']._serialized_start=1250
  _globals['_GETBYIDREQUEST']._serialized_end=1278
  _globals['_GETBYIDRESPONSE']._serialized_start=1280
  _globals['_GETBYIDRESPONSE']._serialized_end=1332
  _globals['_FINDREQUEST']._serialized_start=1335
  _globals['_FINDREQUEST']._serialized_end=1584
  _globals['_FINDRESPONSE']._serialized_start=1586
  _globals['_FINDRESPONSE']._serialized_end=1635
  _globals['_UPDATEREQUEST']._serialized_start=1638
  _globals['_UPDATEREQUEST']._serialized_end=2083
  _globals['_UPDATEREQUEST_DATA']._serialized_start=1714
  _globals['_UPDATEREQUEST_DATA']._serialized_end=2083
  _globals['_SETVISIBLEREQUEST']._serialized_start=2085
  _globals['_SETVISIBLEREQUEST']._serialized_end=2194
  _globals['_SETVISIBLEREQUEST_DATA']._serialized_start=2168
  _globals['_SETVISIBLEREQUEST_DATA']._serialized_end=2194
  _globals['_UPDATEIMAGESREQUEST']._serialized_start=2197
  _globals['_UPDATEIMAGESREQUEST']._serialized_end=2332
  _globals['_UPDATEIMAGESREQUEST_DATA']._serialized_start=2284
  _globals['_UPDATEIMAGESREQUEST_DATA']._serialized_end=2332
  _globals['_PRODUCTS']._serialized_start=2533
  _globals['_PRODUCTS']._serialized_end=2938
# @@protoc_insertion_point(module_scope)
