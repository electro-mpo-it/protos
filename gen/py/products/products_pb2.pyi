from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnitOfMeasurementENUM(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PIECE: _ClassVar[UnitOfMeasurementENUM]
    PAIR: _ClassVar[UnitOfMeasurementENUM]
    LITER: _ClassVar[UnitOfMeasurementENUM]
    ROLL: _ClassVar[UnitOfMeasurementENUM]
    SHEET: _ClassVar[UnitOfMeasurementENUM]
    CENTIMETRE: _ClassVar[UnitOfMeasurementENUM]
    METRE: _ClassVar[UnitOfMeasurementENUM]
    KILOGRAM: _ClassVar[UnitOfMeasurementENUM]
    SQUARE_METER: _ClassVar[UnitOfMeasurementENUM]
    CUBIC_METER: _ClassVar[UnitOfMeasurementENUM]

class VATENUM(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NDS20: _ClassVar[VATENUM]
    NDS10: _ClassVar[VATENUM]
    NDS0: _ClassVar[VATENUM]

class CharacteristicValuesTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEXT: _ClassVar[CharacteristicValuesTypeEnum]
    NUMERIC: _ClassVar[CharacteristicValuesTypeEnum]
PIECE: UnitOfMeasurementENUM
PAIR: UnitOfMeasurementENUM
LITER: UnitOfMeasurementENUM
ROLL: UnitOfMeasurementENUM
SHEET: UnitOfMeasurementENUM
CENTIMETRE: UnitOfMeasurementENUM
METRE: UnitOfMeasurementENUM
KILOGRAM: UnitOfMeasurementENUM
SQUARE_METER: UnitOfMeasurementENUM
CUBIC_METER: UnitOfMeasurementENUM
NDS20: VATENUM
NDS10: VATENUM
NDS0: VATENUM
TEXT: CharacteristicValuesTypeEnum
NUMERIC: CharacteristicValuesTypeEnum

class OptionalUnitOfMeasurementENUM(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: UnitOfMeasurementENUM
    def __init__(self, value: _Optional[_Union[UnitOfMeasurementENUM, str]] = ...) -> None: ...

class OptionalVATENUM(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: VATENUM
    def __init__(self, value: _Optional[_Union[VATENUM, str]] = ...) -> None: ...

class ProductImage(_message.Message):
    __slots__ = ("image_url", "sort")
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    image_url: str
    sort: int
    def __init__(self, image_url: _Optional[str] = ..., sort: _Optional[int] = ...) -> None: ...

class Characteristic(_message.Message):
    __slots__ = ("id", "name", "values_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    values_type: CharacteristicValuesTypeEnum
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., values_type: _Optional[_Union[CharacteristicValuesTypeEnum, str]] = ...) -> None: ...

class ProductCharacteristic(_message.Message):
    __slots__ = ("characteristic", "text_value", "numeric_value")
    CHARACTERISTIC_FIELD_NUMBER: _ClassVar[int]
    TEXT_VALUE_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    characteristic: Characteristic
    text_value: str
    numeric_value: float
    def __init__(self, characteristic: _Optional[_Union[Characteristic, _Mapping]] = ..., text_value: _Optional[str] = ..., numeric_value: _Optional[float] = ...) -> None: ...

class Range(_message.Message):
    __slots__ = ("to",)
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    to: float
    def __init__(self, to: _Optional[float] = ..., **kwargs) -> None: ...

class CharacteristicsFilter(_message.Message):
    __slots__ = ("text_values", "numeric_values")
    class TextValue(_message.Message):
        __slots__ = ("id", "values")
        ID_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        id: str
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, id: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...
    class NumericValue(_message.Message):
        __slots__ = ("id", "values")
        ID_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        id: str
        values: Range
        def __init__(self, id: _Optional[str] = ..., values: _Optional[_Union[Range, _Mapping]] = ...) -> None: ...
    TEXT_VALUES_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    text_values: _containers.RepeatedCompositeFieldContainer[CharacteristicsFilter.TextValue]
    numeric_values: _containers.RepeatedCompositeFieldContainer[CharacteristicsFilter.NumericValue]
    def __init__(self, text_values: _Optional[_Iterable[_Union[CharacteristicsFilter.TextValue, _Mapping]]] = ..., numeric_values: _Optional[_Iterable[_Union[CharacteristicsFilter.NumericValue, _Mapping]]] = ...) -> None: ...

class ProductsFilter(_message.Message):
    __slots__ = ("limit", "offset", "search", "price", "category_id", "characteristics", "is_visible")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    CHARACTERISTICS_FIELD_NUMBER: _ClassVar[int]
    IS_VISIBLE_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    search: str
    price: Range
    category_id: _wrappers_pb2.StringValue
    characteristics: CharacteristicsFilter
    is_visible: _wrappers_pb2.BoolValue
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., search: _Optional[str] = ..., price: _Optional[_Union[Range, _Mapping]] = ..., category_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., characteristics: _Optional[_Union[CharacteristicsFilter, _Mapping]] = ..., is_visible: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class Product(_message.Message):
    __slots__ = ("id", "name", "category_id", "description", "unit_of_measurement", "vat", "old_price", "discount_ratio", "price", "is_visible", "updated_at", "images")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNIT_OF_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    VAT_FIELD_NUMBER: _ClassVar[int]
    OLD_PRICE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_RATIO_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    IS_VISIBLE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    category_id: str
    description: str
    unit_of_measurement: UnitOfMeasurementENUM
    vat: VATENUM
    old_price: float
    discount_ratio: float
    price: float
    is_visible: bool
    updated_at: _timestamp_pb2.Timestamp
    images: _containers.RepeatedCompositeFieldContainer[ProductImage]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., category_id: _Optional[str] = ..., description: _Optional[str] = ..., unit_of_measurement: _Optional[_Union[UnitOfMeasurementENUM, str]] = ..., vat: _Optional[_Union[VATENUM, str]] = ..., old_price: _Optional[float] = ..., discount_ratio: _Optional[float] = ..., price: _Optional[float] = ..., is_visible: bool = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., images: _Optional[_Iterable[_Union[ProductImage, _Mapping]]] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("name", "category_id", "description", "unit_of_measurement", "vat", "old_price", "discount_ratio")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNIT_OF_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    VAT_FIELD_NUMBER: _ClassVar[int]
    OLD_PRICE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_RATIO_FIELD_NUMBER: _ClassVar[int]
    name: str
    category_id: str
    description: str
    unit_of_measurement: UnitOfMeasurementENUM
    vat: VATENUM
    old_price: float
    discount_ratio: float
    def __init__(self, name: _Optional[str] = ..., category_id: _Optional[str] = ..., description: _Optional[str] = ..., unit_of_measurement: _Optional[_Union[UnitOfMeasurementENUM, str]] = ..., vat: _Optional[_Union[VATENUM, str]] = ..., old_price: _Optional[float] = ..., discount_ratio: _Optional[float] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetByIDResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: Product
    def __init__(self, data: _Optional[_Union[Product, _Mapping]] = ...) -> None: ...

class FindResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Product]
    def __init__(self, data: _Optional[_Iterable[_Union[Product, _Mapping]]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "data")
    class Data(_message.Message):
        __slots__ = ("name", "category_id", "description", "unit_of_measurement", "vat", "old_price", "discount_ratio")
        NAME_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        UNIT_OF_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
        VAT_FIELD_NUMBER: _ClassVar[int]
        OLD_PRICE_FIELD_NUMBER: _ClassVar[int]
        DISCOUNT_RATIO_FIELD_NUMBER: _ClassVar[int]
        name: _wrappers_pb2.StringValue
        category_id: _wrappers_pb2.StringValue
        description: _wrappers_pb2.StringValue
        unit_of_measurement: OptionalUnitOfMeasurementENUM
        vat: OptionalVATENUM
        old_price: _wrappers_pb2.DoubleValue
        discount_ratio: _wrappers_pb2.DoubleValue
        def __init__(self, name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., category_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., unit_of_measurement: _Optional[_Union[OptionalUnitOfMeasurementENUM, _Mapping]] = ..., vat: _Optional[_Union[OptionalVATENUM, _Mapping]] = ..., old_price: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., discount_ratio: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    data: UpdateRequest.Data
    def __init__(self, id: _Optional[str] = ..., data: _Optional[_Union[UpdateRequest.Data, _Mapping]] = ...) -> None: ...

class SetVisibleRequest(_message.Message):
    __slots__ = ("id", "data")
    class Data(_message.Message):
        __slots__ = ("is_visible",)
        IS_VISIBLE_FIELD_NUMBER: _ClassVar[int]
        is_visible: bool
        def __init__(self, is_visible: bool = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    data: SetVisibleRequest.Data
    def __init__(self, id: _Optional[str] = ..., data: _Optional[_Union[SetVisibleRequest.Data, _Mapping]] = ...) -> None: ...

class UpdateImagesRequest(_message.Message):
    __slots__ = ("id", "data")
    class Data(_message.Message):
        __slots__ = ("images",)
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        images: _containers.RepeatedCompositeFieldContainer[ProductImage]
        def __init__(self, images: _Optional[_Iterable[_Union[ProductImage, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    data: UpdateImagesRequest.Data
    def __init__(self, id: _Optional[str] = ..., data: _Optional[_Union[UpdateImagesRequest.Data, _Mapping]] = ...) -> None: ...

class CreateCharacteristicRequest(_message.Message):
    __slots__ = ("name", "values_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    values_type: CharacteristicValuesTypeEnum
    def __init__(self, name: _Optional[str] = ..., values_type: _Optional[_Union[CharacteristicValuesTypeEnum, str]] = ...) -> None: ...

class CreateCharacteristicResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FindCharacteristicsRequest(_message.Message):
    __slots__ = ("limit", "search")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    limit: int
    search: _wrappers_pb2.StringValue
    def __init__(self, limit: _Optional[int] = ..., search: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class FindCharacteristicsResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Characteristic]
    def __init__(self, data: _Optional[_Iterable[_Union[Characteristic, _Mapping]]] = ...) -> None: ...

class UpdateCharacteristicRequest(_message.Message):
    __slots__ = ("id", "data")
    class Data(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: _wrappers_pb2.StringValue
        def __init__(self, name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    data: UpdateCharacteristicRequest.Data
    def __init__(self, id: _Optional[str] = ..., data: _Optional[_Union[UpdateCharacteristicRequest.Data, _Mapping]] = ...) -> None: ...

class DeleteCharacteristicRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AddCharToProdRequest(_message.Message):
    __slots__ = ("product_id", "characteristic_id", "text_value", "numeric_value")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    CHARACTERISTIC_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_VALUE_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    characteristic_id: str
    text_value: str
    numeric_value: float
    def __init__(self, product_id: _Optional[str] = ..., characteristic_id: _Optional[str] = ..., text_value: _Optional[str] = ..., numeric_value: _Optional[float] = ...) -> None: ...

class RemoveCharFromProdRequest(_message.Message):
    __slots__ = ("product_id", "characteristic_id")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    CHARACTERISTIC_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    characteristic_id: str
    def __init__(self, product_id: _Optional[str] = ..., characteristic_id: _Optional[str] = ...) -> None: ...

class GetProdCharsRequest(_message.Message):
    __slots__ = ("product_id",)
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class GetProdCharsResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[ProductCharacteristic]
    def __init__(self, data: _Optional[_Iterable[_Union[ProductCharacteristic, _Mapping]]] = ...) -> None: ...
