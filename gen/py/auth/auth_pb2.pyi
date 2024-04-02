from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTokenRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class CreateTokenResponse(_message.Message):
    __slots__ = ("access_token", "refresh_token", "access_exp_at", "refresh_exp_at")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_EXP_AT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_EXP_AT_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    access_exp_at: _timestamp_pb2.Timestamp
    refresh_exp_at: _timestamp_pb2.Timestamp
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., access_exp_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., refresh_exp_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RefreshTokenRequest(_message.Message):
    __slots__ = ("refresh_token",)
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    def __init__(self, refresh_token: _Optional[str] = ...) -> None: ...

class RefreshTokenResponse(_message.Message):
    __slots__ = ("access_token", "refresh_token", "access_exp_at", "refresh_exp_at")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_EXP_AT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_EXP_AT_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    access_exp_at: _timestamp_pb2.Timestamp
    refresh_exp_at: _timestamp_pb2.Timestamp
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., access_exp_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., refresh_exp_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
