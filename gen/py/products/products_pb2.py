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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17products/products.proto\x12\nproductspb\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd4\x01\n\rCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x61tegory_id\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12>\n\x13unit_of_measurement\x18\x04 \x01(\x0e\x32!.productspb.UnitOfMeasurementENUM\x12 \n\x03vat\x18\x05 \x01(\x0e\x32\x13.productspb.VATENUM\x12\x11\n\told_price\x18\x06 \x01(\x01\x12\x16\n\x0e\x64iscount_ratio\x18\x07 \x01(\x01\"\x1c\n\x0e\x43reateResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x1c\n\x0eGetByIDRequest\x12\n\n\x02id\x18\x01 \x01(\t\"4\n\x0fGetByIDResponse\x12!\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x13.productspb.Product\"1\n\x0c\x46indResponse\x12!\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x13.productspb.Product\"\xbd\x03\n\rUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12,\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1e.productspb.UpdateRequest.Data\x1a\xf1\x02\n\x04\x44\x61ta\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x63\x61tegory_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x46\n\x13unit_of_measurement\x18\x04 \x01(\x0b\x32).productspb.OptionalUnitOfMeasurementENUM\x12(\n\x03vat\x18\x05 \x01(\x0b\x32\x1b.productspb.OptionalVATENUM\x12/\n\told_price\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x34\n\x0e\x64iscount_ratio\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\"m\n\x11SetVisibleRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\".productspb.SetVisibleRequest.Data\x1a\x1a\n\x04\x44\x61ta\x12\x12\n\nis_visible\x18\x01 \x01(\x08\"K\n\x13UpdateImagesRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12(\n\x06images\x18\x02 \x03(\x0b\x32\x18.productspb.ProductImage\"j\n\x1b\x43reateCharacteristicRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12=\n\x0bvalues_type\x18\x02 \x01(\x0e\x32(.productspb.CharacteristicValuesTypeEnum\"*\n\x1c\x43reateCharacteristicResponse\x12\n\n\x02id\x18\x01 \x01(\t\"H\n\x1a\x46indCharacteristicsRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06search\x18\x02 \x01(\t\x12\x0b\n\x03ids\x18\x03 \x03(\t\"G\n\x1b\x46indCharacteristicsResponse\x12(\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1a.productspb.Characteristic\"\x99\x01\n\x1bUpdateCharacteristicRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12:\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32,.productspb.UpdateCharacteristicRequest.Data\x1a\x32\n\x04\x44\x61ta\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\")\n\x1b\x44\x65leteCharacteristicRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x88\x01\n\x1f\x41\x64\x64ProductCharacteristicRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x19\n\x11\x63haracteristic_id\x18\x02 \x01(\t\x12\x14\n\ntext_value\x18\x65 \x01(\tH\x00\x12\x17\n\rnumeric_value\x18\x66 \x01(\x01H\x00\x42\x07\n\x05value\".\n AddProductCharacteristicResponse\x12\n\n\x02id\x18\x01 \x01(\t\"0\n\"RemoveProductCharacteristicRequest\x12\n\n\x02id\x18\x01 \x01(\t\"6\n GetProductCharacteristicsRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\"T\n!GetProductCharacteristicsResponse\x12/\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32!.productspb.ProductCharacteristic\"Q\n\x1dOptionalUnitOfMeasurementENUM\x12\x30\n\x05value\x18\x01 \x01(\x0e\x32!.productspb.UnitOfMeasurementENUM\"5\n\x0fOptionalVATENUM\x12\"\n\x05value\x18\x01 \x01(\x0e\x32\x13.productspb.VATENUM\"/\n\x0cProductImage\x12\x11\n\timage_url\x18\x01 \x01(\t\x12\x0c\n\x04sort\x18\x02 \x01(\r\"i\n\x0e\x43haracteristic\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12=\n\x0bvalues_type\x18\x03 \x01(\x0e\x32(.productspb.CharacteristicValuesTypeEnum\"v\n\x15ProductCharacteristic\x12\n\n\x02id\x18\x01 \x01(\t\x12\x19\n\x11\x63haracteristic_id\x18\x02 \x01(\t\x12\x14\n\ntext_value\x18\x65 \x01(\tH\x00\x12\x17\n\rnumeric_value\x18\x66 \x01(\x01H\x00\x42\x07\n\x05value\"!\n\x05Range\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x01\x12\n\n\x02to\x18\x02 \x01(\x01\"\x89\x02\n\x15\x43haracteristicsFilter\x12@\n\x0btext_values\x18\x01 \x03(\x0b\x32+.productspb.CharacteristicsFilter.TextValue\x12\x46\n\x0enumeric_values\x18\x02 \x03(\x0b\x32..productspb.CharacteristicsFilter.NumericValue\x1a\'\n\tTextValue\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\x1a=\n\x0cNumericValue\x12\n\n\x02id\x18\x01 \x01(\t\x12!\n\x06values\x18\x02 \x01(\x0b\x32\x11.productspb.Range\"\x87\x02\n\x15ProductsFilterRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x0e\n\x06search\x18\x03 \x01(\t\x12 \n\x05price\x18\x04 \x01(\x0b\x32\x11.productspb.Range\x12\x31\n\x0b\x63\x61tegory_id\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x0f\x63haracteristics\x18\x06 \x01(\x0b\x32!.productspb.CharacteristicsFilter\x12.\n\nis_visible\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"p\n\x10\x41vailableFilters\x12 \n\x05price\x18\x01 \x01(\x0b\x32\x11.productspb.Range\x12:\n\x0f\x63haracteristics\x18\x02 \x01(\x0b\x32!.productspb.CharacteristicsFilter\"\x87\x03\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x61tegory_id\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12>\n\x13unit_of_measurement\x18\x05 \x01(\x0e\x32!.productspb.UnitOfMeasurementENUM\x12 \n\x03vat\x18\x06 \x01(\x0e\x32\x13.productspb.VATENUM\x12\x11\n\told_price\x18\x07 \x01(\x01\x12\x16\n\x0e\x64iscount_ratio\x18\x08 \x01(\x01\x12\r\n\x05price\x18\t \x01(\x01\x12\x12\n\nis_visible\x18\n \x01(\x08\x12.\n\nupdated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x06images\x18\x0c \x03(\x0b\x32\x18.productspb.ProductImage\x12.\n\ncreated_at\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp*\x98\x01\n\x15UnitOfMeasurementENUM\x12\t\n\x05PIECE\x10\x00\x12\x08\n\x04PAIR\x10\x01\x12\t\n\x05LITER\x10\x02\x12\x08\n\x04ROLL\x10\x03\x12\t\n\x05SHEET\x10\x04\x12\x0e\n\nCENTIMETRE\x10\x05\x12\t\n\x05METRE\x10\x06\x12\x0c\n\x08KILOGRAM\x10\x07\x12\x10\n\x0cSQUARE_METER\x10\x08\x12\x0f\n\x0b\x43UBIC_METER\x10\t*)\n\x07VATENUM\x12\t\n\x05NDS20\x10\x00\x12\t\n\x05NDS10\x10\x01\x12\x08\n\x04NDS0\x10\x02*5\n\x1c\x43haracteristicValuesTypeEnum\x12\x08\n\x04TEXT\x10\x00\x12\x0b\n\x07NUMERIC\x10\x01\x32\xcd\t\n\x08Products\x12?\n\x06\x43reate\x12\x19.productspb.CreateRequest\x1a\x1a.productspb.CreateResponse\x12\x42\n\x07GetByID\x12\x1a.productspb.GetByIDRequest\x1a\x1b.productspb.GetByIDResponse\x12\x43\n\x04\x46ind\x12!.productspb.ProductsFilterRequest\x1a\x18.productspb.FindResponse\x12;\n\x06Update\x12\x19.productspb.UpdateRequest\x1a\x16.google.protobuf.Empty\x12\x43\n\nSetVisible\x12\x1d.productspb.SetVisibleRequest\x1a\x16.google.protobuf.Empty\x12G\n\x0cUpdateImages\x12\x1f.productspb.UpdateImagesRequest\x1a\x16.google.protobuf.Empty\x12i\n\x14\x43reateCharacteristic\x12\'.productspb.CreateCharacteristicRequest\x1a(.productspb.CreateCharacteristicResponse\x12\x66\n\x13\x46indCharacteristics\x12&.productspb.FindCharacteristicsRequest\x1a\'.productspb.FindCharacteristicsResponse\x12W\n\x14UpdateCharacteristic\x12\'.productspb.UpdateCharacteristicRequest\x1a\x16.google.protobuf.Empty\x12W\n\x14\x44\x65leteCharacteristic\x12\'.productspb.DeleteCharacteristicRequest\x1a\x16.google.protobuf.Empty\x12u\n\x18\x41\x64\x64ProductCharacteristic\x12+.productspb.AddProductCharacteristicRequest\x1a,.productspb.AddProductCharacteristicResponse\x12\x65\n\x1bRemoveProductCharacteristic\x12..productspb.RemoveProductCharacteristicRequest\x1a\x16.google.protobuf.Empty\x12x\n\x19GetProductCharacteristics\x12,.productspb.GetProductCharacteristicsRequest\x1a-.productspb.GetProductCharacteristicsResponse\x12O\n\x0c\x41pplyFilters\x12!.productspb.ProductsFilterRequest\x1a\x1c.productspb.AvailableFiltersB=Z;github.com/electro-mpo-it/protos/gen/go/products;productspbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'products.products_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z;github.com/electro-mpo-it/protos/gen/go/products;productspb'
  _globals['_UNITOFMEASUREMENTENUM']._serialized_start=3518
  _globals['_UNITOFMEASUREMENTENUM']._serialized_end=3670
  _globals['_VATENUM']._serialized_start=3672
  _globals['_VATENUM']._serialized_end=3713
  _globals['_CHARACTERISTICVALUESTYPEENUM']._serialized_start=3715
  _globals['_CHARACTERISTICVALUESTYPEENUM']._serialized_end=3768
  _globals['_CREATEREQUEST']._serialized_start=134
  _globals['_CREATEREQUEST']._serialized_end=346
  _globals['_CREATERESPONSE']._serialized_start=348
  _globals['_CREATERESPONSE']._serialized_end=376
  _globals['_GETBYIDREQUEST']._serialized_start=378
  _globals['_GETBYIDREQUEST']._serialized_end=406
  _globals['_GETBYIDRESPONSE']._serialized_start=408
  _globals['_GETBYIDRESPONSE']._serialized_end=460
  _globals['_FINDRESPONSE']._serialized_start=462
  _globals['_FINDRESPONSE']._serialized_end=511
  _globals['_UPDATEREQUEST']._serialized_start=514
  _globals['_UPDATEREQUEST']._serialized_end=959
  _globals['_UPDATEREQUEST_DATA']._serialized_start=590
  _globals['_UPDATEREQUEST_DATA']._serialized_end=959
  _globals['_SETVISIBLEREQUEST']._serialized_start=961
  _globals['_SETVISIBLEREQUEST']._serialized_end=1070
  _globals['_SETVISIBLEREQUEST_DATA']._serialized_start=1044
  _globals['_SETVISIBLEREQUEST_DATA']._serialized_end=1070
  _globals['_UPDATEIMAGESREQUEST']._serialized_start=1072
  _globals['_UPDATEIMAGESREQUEST']._serialized_end=1147
  _globals['_CREATECHARACTERISTICREQUEST']._serialized_start=1149
  _globals['_CREATECHARACTERISTICREQUEST']._serialized_end=1255
  _globals['_CREATECHARACTERISTICRESPONSE']._serialized_start=1257
  _globals['_CREATECHARACTERISTICRESPONSE']._serialized_end=1299
  _globals['_FINDCHARACTERISTICSREQUEST']._serialized_start=1301
  _globals['_FINDCHARACTERISTICSREQUEST']._serialized_end=1373
  _globals['_FINDCHARACTERISTICSRESPONSE']._serialized_start=1375
  _globals['_FINDCHARACTERISTICSRESPONSE']._serialized_end=1446
  _globals['_UPDATECHARACTERISTICREQUEST']._serialized_start=1449
  _globals['_UPDATECHARACTERISTICREQUEST']._serialized_end=1602
  _globals['_UPDATECHARACTERISTICREQUEST_DATA']._serialized_start=590
  _globals['_UPDATECHARACTERISTICREQUEST_DATA']._serialized_end=640
  _globals['_DELETECHARACTERISTICREQUEST']._serialized_start=1604
  _globals['_DELETECHARACTERISTICREQUEST']._serialized_end=1645
  _globals['_ADDPRODUCTCHARACTERISTICREQUEST']._serialized_start=1648
  _globals['_ADDPRODUCTCHARACTERISTICREQUEST']._serialized_end=1784
  _globals['_ADDPRODUCTCHARACTERISTICRESPONSE']._serialized_start=1786
  _globals['_ADDPRODUCTCHARACTERISTICRESPONSE']._serialized_end=1832
  _globals['_REMOVEPRODUCTCHARACTERISTICREQUEST']._serialized_start=1834
  _globals['_REMOVEPRODUCTCHARACTERISTICREQUEST']._serialized_end=1882
  _globals['_GETPRODUCTCHARACTERISTICSREQUEST']._serialized_start=1884
  _globals['_GETPRODUCTCHARACTERISTICSREQUEST']._serialized_end=1938
  _globals['_GETPRODUCTCHARACTERISTICSRESPONSE']._serialized_start=1940
  _globals['_GETPRODUCTCHARACTERISTICSRESPONSE']._serialized_end=2024
  _globals['_OPTIONALUNITOFMEASUREMENTENUM']._serialized_start=2026
  _globals['_OPTIONALUNITOFMEASUREMENTENUM']._serialized_end=2107
  _globals['_OPTIONALVATENUM']._serialized_start=2109
  _globals['_OPTIONALVATENUM']._serialized_end=2162
  _globals['_PRODUCTIMAGE']._serialized_start=2164
  _globals['_PRODUCTIMAGE']._serialized_end=2211
  _globals['_CHARACTERISTIC']._serialized_start=2213
  _globals['_CHARACTERISTIC']._serialized_end=2318
  _globals['_PRODUCTCHARACTERISTIC']._serialized_start=2320
  _globals['_PRODUCTCHARACTERISTIC']._serialized_end=2438
  _globals['_RANGE']._serialized_start=2440
  _globals['_RANGE']._serialized_end=2473
  _globals['_CHARACTERISTICSFILTER']._serialized_start=2476
  _globals['_CHARACTERISTICSFILTER']._serialized_end=2741
  _globals['_CHARACTERISTICSFILTER_TEXTVALUE']._serialized_start=2639
  _globals['_CHARACTERISTICSFILTER_TEXTVALUE']._serialized_end=2678
  _globals['_CHARACTERISTICSFILTER_NUMERICVALUE']._serialized_start=2680
  _globals['_CHARACTERISTICSFILTER_NUMERICVALUE']._serialized_end=2741
  _globals['_PRODUCTSFILTERREQUEST']._serialized_start=2744
  _globals['_PRODUCTSFILTERREQUEST']._serialized_end=3007
  _globals['_AVAILABLEFILTERS']._serialized_start=3009
  _globals['_AVAILABLEFILTERS']._serialized_end=3121
  _globals['_PRODUCT']._serialized_start=3124
  _globals['_PRODUCT']._serialized_end=3515
  _globals['_PRODUCTS']._serialized_start=3771
  _globals['_PRODUCTS']._serialized_end=5000
# @@protoc_insertion_point(module_scope)
