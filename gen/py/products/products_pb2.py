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
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17products/products.proto\x12\nproductspb\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd5\x02\n\x14\x43reateProductRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x61tegory_id\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12>\n\x13unit_of_measurement\x18\x04 \x01(\x0e\x32!.productspb.UnitOfMeasurementENUM\x12 \n\x03vat\x18\x05 \x01(\x0e\x32\x13.productspb.VATENUM\x12\x11\n\told_price\x18\x06 \x01(\x01\x12\x16\n\x0e\x64iscount_ratio\x18\x07 \x01(\x01\x12\x12\n\nis_visible\x18\x08 \x01(\x08\x12(\n\x06images\x18\x1f \x03(\x0b\x32\x18.productspb.ProductImage\x12:\n\x0f\x63haracteristics\x18  \x03(\x0b\x32!.productspb.ProductCharacteristic\"\x93\x08\n\x18UpdateProductByIDRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x37\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32).productspb.UpdateProductByIDRequest.Data\x1a\xb1\x07\n\x04\x44\x61ta\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x63\x61tegory_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x64\n\x13unit_of_measurement\x18\x04 \x01(\x0b\x32G.productspb.UpdateProductByIDRequest.Data.OptionalUnitOfMeasurementENUM\x12\x46\n\x03vat\x18\x05 \x01(\x0b\x32\x39.productspb.UpdateProductByIDRequest.Data.OptionalVATENUM\x12/\n\told_price\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x34\n\x0e\x64iscount_ratio\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12.\n\nis_visible\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12O\n\x06images\x18\x1f \x01(\x0b\x32?.productspb.UpdateProductByIDRequest.Data.OptionalProductImages\x12\x61\n\x0f\x63haracteristics\x18  \x01(\x0b\x32H.productspb.UpdateProductByIDRequest.Data.OptionalProductCharacteristics\x1aQ\n\x1dOptionalUnitOfMeasurementENUM\x12\x30\n\x05value\x18\x01 \x01(\x0e\x32!.productspb.UnitOfMeasurementENUM\x1a\x35\n\x0fOptionalVATENUM\x12\"\n\x05value\x18\x01 \x01(\x0e\x32\x13.productspb.VATENUM\x1a@\n\x15OptionalProductImages\x12\'\n\x05value\x18\x01 \x03(\x0b\x32\x18.productspb.ProductImage\x1aR\n\x1eOptionalProductCharacteristics\x12\x30\n\x05value\x18\x01 \x03(\x0b\x32!.productspb.ProductCharacteristic\"j\n\x15ProductCharacteristic\x12\x19\n\x11\x63haracteristic_id\x18\x01 \x01(\t\x12\x14\n\ntext_value\x18\x65 \x01(\tH\x00\x12\x17\n\rnumeric_value\x18\x66 \x01(\x01H\x00\x42\x07\n\x05value\"#\n\x15\x43reateProductResponse\x12\n\n\x02id\x18\x01 \x01(\t\"#\n\x15GetProductByIDRequest\x12\n\n\x02id\x18\x01 \x01(\t\";\n\x16GetProductByIDResponse\x12!\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x13.productspb.Product\"9\n\x14\x46indProductsResponse\x12!\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x13.productspb.Product\"j\n\x1b\x43reateCharacteristicRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12=\n\x0bvalues_type\x18\x02 \x01(\x0e\x32(.productspb.CharacteristicValuesTypeEnum\"*\n\x1c\x43reateCharacteristicResponse\x12\n\n\x02id\x18\x01 \x01(\t\"m\n\x1a\x46indCharacteristicsRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06search\x18\x02 \x01(\t\x12\x0b\n\x03ids\x18\x03 \x03(\t\x12\x0e\n\x06offset\x18\x04 \x01(\x04\x12\x13\n\x0b\x63\x61tegory_id\x18\x05 \x01(\t\"G\n\x1b\x46indCharacteristicsResponse\x12(\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1a.productspb.Characteristic\"\x99\x01\n\x1bUpdateCharacteristicRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12:\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32,.productspb.UpdateCharacteristicRequest.Data\x1a\x32\n\x04\x44\x61ta\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\")\n\x1b\x44\x65leteCharacteristicRequest\x12\n\n\x02id\x18\x01 \x01(\t\"/\n\x0cProductImage\x12\x11\n\timage_url\x18\x01 \x01(\t\x12\x0c\n\x04sort\x18\x02 \x01(\r\"i\n\x0e\x43haracteristic\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12=\n\x0bvalues_type\x18\x03 \x01(\x0e\x32(.productspb.CharacteristicValuesTypeEnum\"\xc9\x01\n%AddCharacteristicsToCategoriesRequest\x12V\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32H.productspb.AddCharacteristicsToCategoriesRequest.CategoryCharacteristic\x1aH\n\x16\x43\x61tegoryCharacteristic\x12\x13\n\x0b\x63\x61tegory_id\x18\x01 \x01(\t\x12\x19\n\x11\x63haracteristic_id\x18\x02 \x01(\t\"\xcf\x01\n(DropCharacteristicsFromCategoriesRequest\x12Y\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32K.productspb.DropCharacteristicsFromCategoriesRequest.CategoryCharacteristic\x1aH\n\x16\x43\x61tegoryCharacteristic\x12\x13\n\x0b\x63\x61tegory_id\x18\x01 \x01(\t\x12\x19\n\x11\x63haracteristic_id\x18\x02 \x01(\t\"!\n\x05Range\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x01\x12\n\n\x02to\x18\x02 \x01(\x01\"\x89\x02\n\x15\x43haracteristicsFilter\x12@\n\x0btext_values\x18\x01 \x03(\x0b\x32+.productspb.CharacteristicsFilter.TextValue\x12\x46\n\x0enumeric_values\x18\x02 \x03(\x0b\x32..productspb.CharacteristicsFilter.NumericValue\x1a\'\n\tTextValue\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\x1a=\n\x0cNumericValue\x12\n\n\x02id\x18\x01 \x01(\t\x12!\n\x06values\x18\x02 \x01(\x0b\x32\x11.productspb.Range\"\x87\x02\n\x15ProductsFilterRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0e\n\x06search\x18\x03 \x01(\t\x12 \n\x05price\x18\x04 \x01(\x0b\x32\x11.productspb.Range\x12\x31\n\x0b\x63\x61tegory_id\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x0f\x63haracteristics\x18\x06 \x01(\x0b\x32!.productspb.CharacteristicsFilter\x12.\n\nis_visible\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"p\n\x10\x41vailableFilters\x12 \n\x05price\x18\x01 \x01(\x0b\x32\x11.productspb.Range\x12:\n\x0f\x63haracteristics\x18\x02 \x01(\x0b\x32!.productspb.CharacteristicsFilter\"\xcb\x03\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x61tegory_id\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12>\n\x13unit_of_measurement\x18\x05 \x01(\x0e\x32!.productspb.UnitOfMeasurementENUM\x12 \n\x03vat\x18\x06 \x01(\x0e\x32\x13.productspb.VATENUM\x12\x11\n\told_price\x18\x07 \x01(\x01\x12\x16\n\x0e\x64iscount_ratio\x18\x08 \x01(\x01\x12\r\n\x05price\x18\t \x01(\x01\x12\x12\n\nis_visible\x18\n \x01(\x08\x12.\n\nupdated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x06images\x18\x0c \x03(\x0b\x32\x18.productspb.ProductImage\x12.\n\ncreated_at\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x42\n\x17product_characteristics\x18\x0e \x03(\x0b\x32!.productspb.ProductCharacteristic*\x98\x01\n\x15UnitOfMeasurementENUM\x12\t\n\x05PIECE\x10\x00\x12\x08\n\x04PAIR\x10\x01\x12\t\n\x05LITER\x10\x02\x12\x08\n\x04ROLL\x10\x03\x12\t\n\x05SHEET\x10\x04\x12\x0e\n\nCENTIMETRE\x10\x05\x12\t\n\x05METRE\x10\x06\x12\x0c\n\x08KILOGRAM\x10\x07\x12\x10\n\x0cSQUARE_METER\x10\x08\x12\x0f\n\x0b\x43UBIC_METER\x10\t*)\n\x07VATENUM\x12\t\n\x05NDS20\x10\x00\x12\t\n\x05NDS10\x10\x01\x12\x08\n\x04NDS0\x10\x02*5\n\x1c\x43haracteristicValuesTypeEnum\x12\x08\n\x04TEXT\x10\x00\x12\x0b\n\x07NUMERIC\x10\x01\x32\x97\x08\n\x08Products\x12T\n\rCreateProduct\x12 .productspb.CreateProductRequest\x1a!.productspb.CreateProductResponse\x12W\n\x0eGetProductByID\x12!.productspb.GetProductByIDRequest\x1a\".productspb.GetProductByIDResponse\x12S\n\x0c\x46indProducts\x12!.productspb.ProductsFilterRequest\x1a .productspb.FindProductsResponse\x12Q\n\x11UpdateProductByID\x12$.productspb.UpdateProductByIDRequest\x1a\x16.google.protobuf.Empty\x12i\n\x14\x43reateCharacteristic\x12\'.productspb.CreateCharacteristicRequest\x1a(.productspb.CreateCharacteristicResponse\x12\x66\n\x13\x46indCharacteristics\x12&.productspb.FindCharacteristicsRequest\x1a\'.productspb.FindCharacteristicsResponse\x12W\n\x14UpdateCharacteristic\x12\'.productspb.UpdateCharacteristicRequest\x1a\x16.google.protobuf.Empty\x12W\n\x14\x44\x65leteCharacteristic\x12\'.productspb.DeleteCharacteristicRequest\x1a\x16.google.protobuf.Empty\x12k\n\x1e\x41\x64\x64\x43haracteristicsToCategories\x12\x31.productspb.AddCharacteristicsToCategoriesRequest\x1a\x16.google.protobuf.Empty\x12q\n!DropCharacteristicsFromCategories\x12\x34.productspb.DropCharacteristicsFromCategoriesRequest\x1a\x16.google.protobuf.Empty\x12O\n\x0c\x41pplyFilters\x12!.productspb.ProductsFilterRequest\x1a\x1c.productspb.AvailableFiltersB=Z;github.com/electro-mpo-it/protos/gen/go/products;productspbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'products.products_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z;github.com/electro-mpo-it/protos/gen/go/products;productspb'
  _globals['_UNITOFMEASUREMENTENUM']._serialized_start=4076
  _globals['_UNITOFMEASUREMENTENUM']._serialized_end=4228
  _globals['_VATENUM']._serialized_start=4230
  _globals['_VATENUM']._serialized_end=4271
  _globals['_CHARACTERISTICVALUESTYPEENUM']._serialized_start=4273
  _globals['_CHARACTERISTICVALUESTYPEENUM']._serialized_end=4326
  _globals['_CREATEPRODUCTREQUEST']._serialized_start=134
  _globals['_CREATEPRODUCTREQUEST']._serialized_end=475
  _globals['_UPDATEPRODUCTBYIDREQUEST']._serialized_start=478
  _globals['_UPDATEPRODUCTBYIDREQUEST']._serialized_end=1521
  _globals['_UPDATEPRODUCTBYIDREQUEST_DATA']._serialized_start=576
  _globals['_UPDATEPRODUCTBYIDREQUEST_DATA']._serialized_end=1521
  _globals['_UPDATEPRODUCTBYIDREQUEST_DATA_OPTIONALUNITOFMEASUREMENTENUM']._serialized_start=1235
  _globals['_UPDATEPRODUCTBYIDREQUEST_DATA_OPTIONALUNITOFMEASUREMENTENUM']._serialized_end=1316
  _globals['_UPDATEPRODUCTBYIDREQUEST_DATA_OPTIONALVATENUM']._serialized_start=1318
  _globals['_UPDATEPRODUCTBYIDREQUEST_DATA_OPTIONALVATENUM']._serialized_end=1371
  _globals['_UPDATEPRODUCTBYIDREQUEST_DATA_OPTIONALPRODUCTIMAGES']._serialized_start=1373
  _globals['_UPDATEPRODUCTBYIDREQUEST_DATA_OPTIONALPRODUCTIMAGES']._serialized_end=1437
  _globals['_UPDATEPRODUCTBYIDREQUEST_DATA_OPTIONALPRODUCTCHARACTERISTICS']._serialized_start=1439
  _globals['_UPDATEPRODUCTBYIDREQUEST_DATA_OPTIONALPRODUCTCHARACTERISTICS']._serialized_end=1521
  _globals['_PRODUCTCHARACTERISTIC']._serialized_start=1523
  _globals['_PRODUCTCHARACTERISTIC']._serialized_end=1629
  _globals['_CREATEPRODUCTRESPONSE']._serialized_start=1631
  _globals['_CREATEPRODUCTRESPONSE']._serialized_end=1666
  _globals['_GETPRODUCTBYIDREQUEST']._serialized_start=1668
  _globals['_GETPRODUCTBYIDREQUEST']._serialized_end=1703
  _globals['_GETPRODUCTBYIDRESPONSE']._serialized_start=1705
  _globals['_GETPRODUCTBYIDRESPONSE']._serialized_end=1764
  _globals['_FINDPRODUCTSRESPONSE']._serialized_start=1766
  _globals['_FINDPRODUCTSRESPONSE']._serialized_end=1823
  _globals['_CREATECHARACTERISTICREQUEST']._serialized_start=1825
  _globals['_CREATECHARACTERISTICREQUEST']._serialized_end=1931
  _globals['_CREATECHARACTERISTICRESPONSE']._serialized_start=1933
  _globals['_CREATECHARACTERISTICRESPONSE']._serialized_end=1975
  _globals['_FINDCHARACTERISTICSREQUEST']._serialized_start=1977
  _globals['_FINDCHARACTERISTICSREQUEST']._serialized_end=2086
  _globals['_FINDCHARACTERISTICSRESPONSE']._serialized_start=2088
  _globals['_FINDCHARACTERISTICSRESPONSE']._serialized_end=2159
  _globals['_UPDATECHARACTERISTICREQUEST']._serialized_start=2162
  _globals['_UPDATECHARACTERISTICREQUEST']._serialized_end=2315
  _globals['_UPDATECHARACTERISTICREQUEST_DATA']._serialized_start=576
  _globals['_UPDATECHARACTERISTICREQUEST_DATA']._serialized_end=626
  _globals['_DELETECHARACTERISTICREQUEST']._serialized_start=2317
  _globals['_DELETECHARACTERISTICREQUEST']._serialized_end=2358
  _globals['_PRODUCTIMAGE']._serialized_start=2360
  _globals['_PRODUCTIMAGE']._serialized_end=2407
  _globals['_CHARACTERISTIC']._serialized_start=2409
  _globals['_CHARACTERISTIC']._serialized_end=2514
  _globals['_ADDCHARACTERISTICSTOCATEGORIESREQUEST']._serialized_start=2517
  _globals['_ADDCHARACTERISTICSTOCATEGORIESREQUEST']._serialized_end=2718
  _globals['_ADDCHARACTERISTICSTOCATEGORIESREQUEST_CATEGORYCHARACTERISTIC']._serialized_start=2646
  _globals['_ADDCHARACTERISTICSTOCATEGORIESREQUEST_CATEGORYCHARACTERISTIC']._serialized_end=2718
  _globals['_DROPCHARACTERISTICSFROMCATEGORIESREQUEST']._serialized_start=2721
  _globals['_DROPCHARACTERISTICSFROMCATEGORIESREQUEST']._serialized_end=2928
  _globals['_DROPCHARACTERISTICSFROMCATEGORIESREQUEST_CATEGORYCHARACTERISTIC']._serialized_start=2646
  _globals['_DROPCHARACTERISTICSFROMCATEGORIESREQUEST_CATEGORYCHARACTERISTIC']._serialized_end=2718
  _globals['_RANGE']._serialized_start=2930
  _globals['_RANGE']._serialized_end=2963
  _globals['_CHARACTERISTICSFILTER']._serialized_start=2966
  _globals['_CHARACTERISTICSFILTER']._serialized_end=3231
  _globals['_CHARACTERISTICSFILTER_TEXTVALUE']._serialized_start=3129
  _globals['_CHARACTERISTICSFILTER_TEXTVALUE']._serialized_end=3168
  _globals['_CHARACTERISTICSFILTER_NUMERICVALUE']._serialized_start=3170
  _globals['_CHARACTERISTICSFILTER_NUMERICVALUE']._serialized_end=3231
  _globals['_PRODUCTSFILTERREQUEST']._serialized_start=3234
  _globals['_PRODUCTSFILTERREQUEST']._serialized_end=3497
  _globals['_AVAILABLEFILTERS']._serialized_start=3499
  _globals['_AVAILABLEFILTERS']._serialized_end=3611
  _globals['_PRODUCT']._serialized_start=3614
  _globals['_PRODUCT']._serialized_end=4073
  _globals['_PRODUCTS']._serialized_start=4329
  _globals['_PRODUCTS']._serialized_end=5376
# @@protoc_insertion_point(module_scope)
