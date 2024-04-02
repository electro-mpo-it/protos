from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Supplier(_message.Message):
    __slots__ = ("id", "alias", "legal_name", "inn", "email", "phone")
    ID_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    LEGAL_NAME_FIELD_NUMBER: _ClassVar[int]
    INN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    id: str
    alias: str
    legal_name: str
    inn: str
    email: str
    phone: str
    def __init__(self, id: _Optional[str] = ..., alias: _Optional[str] = ..., legal_name: _Optional[str] = ..., inn: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ...) -> None: ...

class PurchasingInfo(_message.Message):
    __slots__ = ("product_id", "supplier", "min_purchase_quantity", "delivery_timedelta")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLIER_FIELD_NUMBER: _ClassVar[int]
    MIN_PURCHASE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TIMEDELTA_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    supplier: Supplier
    min_purchase_quantity: _wrappers_pb2.DoubleValue
    delivery_timedelta: _duration_pb2.Duration
    def __init__(self, product_id: _Optional[str] = ..., supplier: _Optional[_Union[Supplier, _Mapping]] = ..., min_purchase_quantity: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., delivery_timedelta: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class CreateSupplierRequest(_message.Message):
    __slots__ = ("alias", "legal_name", "inn", "email", "phone")
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    LEGAL_NAME_FIELD_NUMBER: _ClassVar[int]
    INN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    alias: str
    legal_name: str
    inn: str
    email: _wrappers_pb2.StringValue
    phone: _wrappers_pb2.StringValue
    def __init__(self, alias: _Optional[str] = ..., legal_name: _Optional[str] = ..., inn: _Optional[str] = ..., email: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., phone: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class CreateSupplierResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetSupplierRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetSupplierResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: Supplier
    def __init__(self, data: _Optional[_Union[Supplier, _Mapping]] = ...) -> None: ...

class FindSuppliersRequest(_message.Message):
    __slots__ = ("limit", "offset", "search")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    limit: _wrappers_pb2.UInt32Value
    offset: _wrappers_pb2.UInt64Value
    search: _wrappers_pb2.StringValue
    def __init__(self, limit: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., offset: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., search: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class FindSuppliersResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Supplier]
    def __init__(self, data: _Optional[_Iterable[_Union[Supplier, _Mapping]]] = ...) -> None: ...

class UpdateSupplierRequest(_message.Message):
    __slots__ = ("id", "data")
    class Data(_message.Message):
        __slots__ = ("alias", "legal_name", "inn", "email", "phone")
        ALIAS_FIELD_NUMBER: _ClassVar[int]
        LEGAL_NAME_FIELD_NUMBER: _ClassVar[int]
        INN_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        PHONE_FIELD_NUMBER: _ClassVar[int]
        alias: _wrappers_pb2.StringValue
        legal_name: _wrappers_pb2.StringValue
        inn: _wrappers_pb2.StringValue
        email: _wrappers_pb2.StringValue
        phone: _wrappers_pb2.StringValue
        def __init__(self, alias: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., legal_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., inn: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., email: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., phone: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    data: UpdateSupplierRequest.Data
    def __init__(self, id: _Optional[str] = ..., data: _Optional[_Union[UpdateSupplierRequest.Data, _Mapping]] = ...) -> None: ...

class CreatePurchasingInfoRequest(_message.Message):
    __slots__ = ("product_id", "supplier_id", "min_purchase_quantity", "delivery_timedelta")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLIER_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_PURCHASE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TIMEDELTA_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    supplier_id: str
    min_purchase_quantity: _wrappers_pb2.DoubleValue
    delivery_timedelta: _duration_pb2.Duration
    def __init__(self, product_id: _Optional[str] = ..., supplier_id: _Optional[str] = ..., min_purchase_quantity: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., delivery_timedelta: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class GetPurchasingInfoRequest(_message.Message):
    __slots__ = ("product_id",)
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class GetPurchasingInfoResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: PurchasingInfo
    def __init__(self, data: _Optional[_Union[PurchasingInfo, _Mapping]] = ...) -> None: ...

class UpdatePurchasingInfoRequest(_message.Message):
    __slots__ = ("product_id", "data")
    class Data(_message.Message):
        __slots__ = ("supplier_id", "min_purchase_quantity", "delivery_timedelta")
        SUPPLIER_ID_FIELD_NUMBER: _ClassVar[int]
        MIN_PURCHASE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
        DELIVERY_TIMEDELTA_FIELD_NUMBER: _ClassVar[int]
        supplier_id: _wrappers_pb2.StringValue
        min_purchase_quantity: _wrappers_pb2.DoubleValue
        delivery_timedelta: _duration_pb2.Duration
        def __init__(self, supplier_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., min_purchase_quantity: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., delivery_timedelta: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    data: UpdatePurchasingInfoRequest.Data
    def __init__(self, product_id: _Optional[str] = ..., data: _Optional[_Union[UpdatePurchasingInfoRequest.Data, _Mapping]] = ...) -> None: ...
