# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth/auth.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x61uth/auth.proto\x12\x06\x61uthpb\x1a\x1fgoogle/protobuf/timestamp.proto\"5\n\x12\x43reateTokenRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\xa9\x01\n\x13\x43reateTokenResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x31\n\raccess_exp_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0erefresh_exp_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\",\n\x13RefreshTokenRequest\x12\x15\n\rrefresh_token\x18\x01 \x01(\t\"\xaa\x01\n\x14RefreshTokenResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x31\n\raccess_exp_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0erefresh_exp_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\xa1\x01\n\x04\x41uth\x12J\n\x0f\x43reateUserToken\x12\x1a.authpb.CreateTokenRequest\x1a\x1b.authpb.CreateTokenResponse\x12M\n\x10RefreshUserToken\x12\x1b.authpb.RefreshTokenRequest\x1a\x1c.authpb.RefreshTokenResponseB5Z3github.com/electro-mpo-it/protos/gen/go/auth;authpbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth.auth_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/electro-mpo-it/protos/gen/go/auth;authpb'
  _globals['_CREATETOKENREQUEST']._serialized_start=60
  _globals['_CREATETOKENREQUEST']._serialized_end=113
  _globals['_CREATETOKENRESPONSE']._serialized_start=116
  _globals['_CREATETOKENRESPONSE']._serialized_end=285
  _globals['_REFRESHTOKENREQUEST']._serialized_start=287
  _globals['_REFRESHTOKENREQUEST']._serialized_end=331
  _globals['_REFRESHTOKENRESPONSE']._serialized_start=334
  _globals['_REFRESHTOKENRESPONSE']._serialized_end=504
  _globals['_AUTH']._serialized_start=507
  _globals['_AUTH']._serialized_end=668
# @@protoc_insertion_point(module_scope)
