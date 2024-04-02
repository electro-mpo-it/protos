from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("first_name", "last_name", "middle_name", "phone", "email", "password")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    middle_name: str
    phone: str
    email: str
    password: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., phone: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class GetCurrentUserRequest(_message.Message):
    __slots__ = ("access_token",)
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    def __init__(self, access_token: _Optional[str] = ...) -> None: ...

class GetCurrentUserResponse(_message.Message):
    __slots__ = ("id", "first_name", "last_name", "middle_name", "phone", "email", "is_email_confirmed", "is_superuser")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    IS_EMAIL_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    IS_SUPERUSER_FIELD_NUMBER: _ClassVar[int]
    id: int
    first_name: str
    last_name: str
    middle_name: str
    phone: str
    email: str
    is_email_confirmed: bool
    is_superuser: bool
    def __init__(self, id: _Optional[int] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., phone: _Optional[str] = ..., email: _Optional[str] = ..., is_email_confirmed: bool = ..., is_superuser: bool = ...) -> None: ...

class GetByIDRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class GetByIDResponse(_message.Message):
    __slots__ = ("id", "first_name", "last_name", "middle_name", "phone")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    id: int
    first_name: str
    last_name: str
    middle_name: str
    phone: str
    def __init__(self, id: _Optional[int] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., phone: _Optional[str] = ...) -> None: ...

class FindRequest(_message.Message):
    __slots__ = ("search", "user_ids", "order_by", "limit", "offset")
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    search: str
    user_ids: _containers.RepeatedScalarFieldContainer[int]
    order_by: str
    limit: int
    offset: int
    def __init__(self, search: _Optional[str] = ..., user_ids: _Optional[_Iterable[int]] = ..., order_by: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class FindResponse(_message.Message):
    __slots__ = ("data",)
    class User(_message.Message):
        __slots__ = ("id", "first_name", "last_name", "middle_name", "phone")
        ID_FIELD_NUMBER: _ClassVar[int]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
        PHONE_FIELD_NUMBER: _ClassVar[int]
        id: int
        first_name: str
        last_name: str
        middle_name: str
        phone: str
        def __init__(self, id: _Optional[int] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., phone: _Optional[str] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[FindResponse.User]
    def __init__(self, data: _Optional[_Iterable[_Union[FindResponse.User, _Mapping]]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("access_token", "user_id", "data")
    class UpdateUser(_message.Message):
        __slots__ = ("first_name", "last_name", "middle_name", "email", "phone")
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        PHONE_FIELD_NUMBER: _ClassVar[int]
        first_name: str
        last_name: str
        middle_name: str
        email: str
        phone: str
        def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ...) -> None: ...
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    user_id: int
    data: UpdateRequest.UpdateUser
    def __init__(self, access_token: _Optional[str] = ..., user_id: _Optional[int] = ..., data: _Optional[_Union[UpdateRequest.UpdateUser, _Mapping]] = ...) -> None: ...

class SetSuperuserStatusRequest(_message.Message):
    __slots__ = ("access_token", "user_id", "is_superuser")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SUPERUSER_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    user_id: int
    is_superuser: bool
    def __init__(self, access_token: _Optional[str] = ..., user_id: _Optional[int] = ..., is_superuser: bool = ...) -> None: ...
