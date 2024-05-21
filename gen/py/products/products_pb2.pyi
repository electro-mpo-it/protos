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

class CreateProductRequest(_message.Message):
    __slots__ = ("name", "category_id", "description", "unit_of_measurement", "vat", "old_price", "discount_ratio", "is_visible", "images", "characteristics")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNIT_OF_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    VAT_FIELD_NUMBER: _ClassVar[int]
    OLD_PRICE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_RATIO_FIELD_NUMBER: _ClassVar[int]
    IS_VISIBLE_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    CHARACTERISTICS_FIELD_NUMBER: _ClassVar[int]
    name: str
    category_id: str
    description: str
    unit_of_measurement: UnitOfMeasurementENUM
    vat: VATENUM
    old_price: float
    discount_ratio: float
    is_visible: bool
    images: _containers.RepeatedCompositeFieldContainer[ProductImage]
    characteristics: _containers.RepeatedCompositeFieldContainer[ProductCharacteristic]
    def __init__(self, name: _Optional[str] = ..., category_id: _Optional[str] = ..., description: _Optional[str] = ..., unit_of_measurement: _Optional[_Union[UnitOfMeasurementENUM, str]] = ..., vat: _Optional[_Union[VATENUM, str]] = ..., old_price: _Optional[float] = ..., discount_ratio: _Optional[float] = ..., is_visible: bool = ..., images: _Optional[_Iterable[_Union[ProductImage, _Mapping]]] = ..., characteristics: _Optional[_Iterable[_Union[ProductCharacteristic, _Mapping]]] = ...) -> None: ...

class UpdateProductByIDRequest(_message.Message):
    __slots__ = ("id", "data")
    class Data(_message.Message):
        __slots__ = ("name", "category_id", "description", "unit_of_measurement", "vat", "old_price", "discount_ratio", "is_visible", "images", "characteristics")
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
        class OptionalProductImages(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: _containers.RepeatedCompositeFieldContainer[ProductImage]
            def __init__(self, value: _Optional[_Iterable[_Union[ProductImage, _Mapping]]] = ...) -> None: ...
        class OptionalProductCharacteristics(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: _containers.RepeatedCompositeFieldContainer[ProductCharacteristic]
            def __init__(self, value: _Optional[_Iterable[_Union[ProductCharacteristic, _Mapping]]] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        UNIT_OF_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
        VAT_FIELD_NUMBER: _ClassVar[int]
        OLD_PRICE_FIELD_NUMBER: _ClassVar[int]
        DISCOUNT_RATIO_FIELD_NUMBER: _ClassVar[int]
        IS_VISIBLE_FIELD_NUMBER: _ClassVar[int]
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        CHARACTERISTICS_FIELD_NUMBER: _ClassVar[int]
        name: _wrappers_pb2.StringValue
        category_id: _wrappers_pb2.StringValue
        description: _wrappers_pb2.StringValue
        unit_of_measurement: UpdateProductByIDRequest.Data.OptionalUnitOfMeasurementENUM
        vat: UpdateProductByIDRequest.Data.OptionalVATENUM
        old_price: _wrappers_pb2.DoubleValue
        discount_ratio: _wrappers_pb2.DoubleValue
        is_visible: _wrappers_pb2.BoolValue
        images: UpdateProductByIDRequest.Data.OptionalProductImages
        characteristics: UpdateProductByIDRequest.Data.OptionalProductCharacteristics
        def __init__(self, name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., category_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., unit_of_measurement: _Optional[_Union[UpdateProductByIDRequest.Data.OptionalUnitOfMeasurementENUM, _Mapping]] = ..., vat: _Optional[_Union[UpdateProductByIDRequest.Data.OptionalVATENUM, _Mapping]] = ..., old_price: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., discount_ratio: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., is_visible: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., images: _Optional[_Union[UpdateProductByIDRequest.Data.OptionalProductImages, _Mapping]] = ..., characteristics: _Optional[_Union[UpdateProductByIDRequest.Data.OptionalProductCharacteristics, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    data: UpdateProductByIDRequest.Data
    def __init__(self, id: _Optional[str] = ..., data: _Optional[_Union[UpdateProductByIDRequest.Data, _Mapping]] = ...) -> None: ...

class ProductCharacteristic(_message.Message):
    __slots__ = ("characteristic_id", "text_value", "numeric_value")
    CHARACTERISTIC_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_VALUE_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    characteristic_id: str
    text_value: str
    numeric_value: float
    def __init__(self, characteristic_id: _Optional[str] = ..., text_value: _Optional[str] = ..., numeric_value: _Optional[float] = ...) -> None: ...

class CreateProductResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetProductByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetProductByIDResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: Product
    def __init__(self, data: _Optional[_Union[Product, _Mapping]] = ...) -> None: ...

class FindProductsResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Product]
    def __init__(self, data: _Optional[_Iterable[_Union[Product, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ("limit", "search", "ids", "offset")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    search: str
    ids: _containers.RepeatedScalarFieldContainer[str]
    offset: int
    def __init__(self, limit: _Optional[int] = ..., search: _Optional[str] = ..., ids: _Optional[_Iterable[str]] = ..., offset: _Optional[int] = ...) -> None: ...

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

class AddCharacteristicsToCategoriesRequest(_message.Message):
    __slots__ = ("data",)
    class CategoryCharacteristic(_message.Message):
        __slots__ = ("category_id", "characteristic_id")
        CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
        CHARACTERISTIC_ID_FIELD_NUMBER: _ClassVar[int]
        category_id: str
        characteristic_id: str
        def __init__(self, category_id: _Optional[str] = ..., characteristic_id: _Optional[str] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[AddCharacteristicsToCategoriesRequest.CategoryCharacteristic]
    def __init__(self, data: _Optional[_Iterable[_Union[AddCharacteristicsToCategoriesRequest.CategoryCharacteristic, _Mapping]]] = ...) -> None: ...

class DropCharacteristicsFromCategoriesRequest(_message.Message):
    __slots__ = ("data",)
    class CategoryCharacteristic(_message.Message):
        __slots__ = ("category_id", "characteristic_id")
        CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
        CHARACTERISTIC_ID_FIELD_NUMBER: _ClassVar[int]
        category_id: str
        characteristic_id: str
        def __init__(self, category_id: _Optional[str] = ..., characteristic_id: _Optional[str] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[DropCharacteristicsFromCategoriesRequest.CategoryCharacteristic]
    def __init__(self, data: _Optional[_Iterable[_Union[DropCharacteristicsFromCategoriesRequest.CategoryCharacteristic, _Mapping]]] = ...) -> None: ...

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

class ProductsFilterRequest(_message.Message):
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

class AvailableFilters(_message.Message):
    __slots__ = ("price", "characteristics")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CHARACTERISTICS_FIELD_NUMBER: _ClassVar[int]
    price: Range
    characteristics: CharacteristicsFilter
    def __init__(self, price: _Optional[_Union[Range, _Mapping]] = ..., characteristics: _Optional[_Union[CharacteristicsFilter, _Mapping]] = ...) -> None: ...

class Product(_message.Message):
    __slots__ = ("id", "name", "category_id", "description", "unit_of_measurement", "vat", "old_price", "discount_ratio", "price", "is_visible", "updated_at", "images", "created_at", "product_characteristics")
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
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CHARACTERISTICS_FIELD_NUMBER: _ClassVar[int]
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
    created_at: _timestamp_pb2.Timestamp
    product_characteristics: _containers.RepeatedCompositeFieldContainer[ProductCharacteristic]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., category_id: _Optional[str] = ..., description: _Optional[str] = ..., unit_of_measurement: _Optional[_Union[UnitOfMeasurementENUM, str]] = ..., vat: _Optional[_Union[VATENUM, str]] = ..., old_price: _Optional[float] = ..., discount_ratio: _Optional[float] = ..., price: _Optional[float] = ..., is_visible: bool = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., images: _Optional[_Iterable[_Union[ProductImage, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., product_characteristics: _Optional[_Iterable[_Union[ProductCharacteristic, _Mapping]]] = ...) -> None: ...
