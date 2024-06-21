from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUserRequest(_message.Message):
    __slots__ = ("first_name", "last_name", "image_url", "email", "phone", "password")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    first_name: _wrappers_pb2.StringValue
    last_name: _wrappers_pb2.StringValue
    image_url: _wrappers_pb2.StringValue
    email: _wrappers_pb2.StringValue
    phone: _wrappers_pb2.StringValue
    password: str
    def __init__(self, first_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., last_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., image_url: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., email: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., phone: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., password: _Optional[str] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetUserByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetUserByIDResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: User
    def __init__(self, data: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class FindUsersRequest(_message.Message):
    __slots__ = ("ids", "email", "phone", "is_blocked")
    IDS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    email: str
    phone: str
    is_blocked: _wrappers_pb2.BoolValue
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., is_blocked: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class FindUsersResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, data: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("id", "first_name", "last_name", "image_url", "email", "phone", "is_blocked", "is_email_verified", "is_phone_verified", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    IS_EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    first_name: _wrappers_pb2.StringValue
    last_name: _wrappers_pb2.StringValue
    image_url: _wrappers_pb2.StringValue
    email: _wrappers_pb2.StringValue
    phone: _wrappers_pb2.StringValue
    is_blocked: bool
    is_email_verified: bool
    is_phone_verified: bool
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., first_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., last_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., image_url: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., email: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., phone: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., is_blocked: bool = ..., is_email_verified: bool = ..., is_phone_verified: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
