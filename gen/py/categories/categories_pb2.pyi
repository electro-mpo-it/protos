from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Category(_message.Message):
    __slots__ = ("id", "name", "parent_id", "image_url", "is_visible", "has_childs", "sort", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    IS_VISIBLE_FIELD_NUMBER: _ClassVar[int]
    HAS_CHILDS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    parent_id: _wrappers_pb2.StringValue
    image_url: str
    is_visible: bool
    has_childs: bool
    sort: int
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., parent_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., image_url: _Optional[str] = ..., is_visible: bool = ..., has_childs: bool = ..., sort: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("name", "parent_id", "image_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent_id: _wrappers_pb2.StringValue
    image_url: str
    def __init__(self, name: _Optional[str] = ..., parent_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., image_url: _Optional[str] = ...) -> None: ...

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
    data: Category
    def __init__(self, data: _Optional[_Union[Category, _Mapping]] = ...) -> None: ...

class FindRequest(_message.Message):
    __slots__ = ("search", "parent_id", "is_visible")
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_VISIBLE_FIELD_NUMBER: _ClassVar[int]
    search: _wrappers_pb2.StringValue
    parent_id: _wrappers_pb2.StringValue
    is_visible: _wrappers_pb2.BoolValue
    def __init__(self, search: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., parent_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., is_visible: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class FindResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[Category]
    def __init__(self, data: _Optional[_Iterable[_Union[Category, _Mapping]]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "data")
    class Data(_message.Message):
        __slots__ = ("name", "parent_id", "image_url")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PARENT_ID_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        name: NullNullString
        parent_id: NullNullString
        image_url: NullNullString
        def __init__(self, name: _Optional[_Union[NullNullString, _Mapping]] = ..., parent_id: _Optional[_Union[NullNullString, _Mapping]] = ..., image_url: _Optional[_Union[NullNullString, _Mapping]] = ...) -> None: ...
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

class DeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class SetSortRequest(_message.Message):
    __slots__ = ("parent_id", "data")
    class Sort(_message.Message):
        __slots__ = ("id", "sort")
        ID_FIELD_NUMBER: _ClassVar[int]
        SORT_FIELD_NUMBER: _ClassVar[int]
        id: str
        sort: int
        def __init__(self, id: _Optional[str] = ..., sort: _Optional[int] = ...) -> None: ...
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    parent_id: _wrappers_pb2.StringValue
    data: _containers.RepeatedCompositeFieldContainer[SetSortRequest.Sort]
    def __init__(self, parent_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., data: _Optional[_Iterable[_Union[SetSortRequest.Sort, _Mapping]]] = ...) -> None: ...

class NullNullString(_message.Message):
    __slots__ = ("null_value", "value")
    NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    null_value: _struct_pb2.NullValue
    value: str
    def __init__(self, null_value: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., value: _Optional[str] = ...) -> None: ...
