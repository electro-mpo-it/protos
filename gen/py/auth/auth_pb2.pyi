from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUserAccessTokenRequest(_message.Message):
    __slots__ = ("email", "phone", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    phone: str
    password: str
    def __init__(self, email: _Optional[str] = ..., phone: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class GetUserAccessTokenResponse(_message.Message):
    __slots__ = ("access_token", "access_token_exp_at", "refresh_token", "refresh_token_exp_at")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_EXP_AT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_EXP_AT_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    access_token_exp_at: _timestamp_pb2.Timestamp
    refresh_token: str
    refresh_token_exp_at: _timestamp_pb2.Timestamp
    def __init__(self, access_token: _Optional[str] = ..., access_token_exp_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., refresh_token: _Optional[str] = ..., refresh_token_exp_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RefreshUserAccessTokenRequest(_message.Message):
    __slots__ = ("refresh_token",)
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    def __init__(self, refresh_token: _Optional[str] = ...) -> None: ...

class RefreshUserAccessTokenResponse(_message.Message):
    __slots__ = ("access_token", "access_token_exp_at", "refresh_token", "refresh_token_exp_at")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_EXP_AT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_EXP_AT_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    access_token_exp_at: _timestamp_pb2.Timestamp
    refresh_token: str
    refresh_token_exp_at: _timestamp_pb2.Timestamp
    def __init__(self, access_token: _Optional[str] = ..., access_token_exp_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., refresh_token: _Optional[str] = ..., refresh_token_exp_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
