# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from users import users_pb2 as users_dot_users__pb2


class UsersStub(object):
    """Сервис пользователей
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/userspb.Users/CreateUser',
                request_serializer=users_dot_users__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=users_dot_users__pb2.CreateUserResponse.FromString,
                )
        self.GetUserByID = channel.unary_unary(
                '/userspb.Users/GetUserByID',
                request_serializer=users_dot_users__pb2.GetUserByIDRequest.SerializeToString,
                response_deserializer=users_dot_users__pb2.GetUserByIDResponse.FromString,
                )
        self.FindUsers = channel.unary_unary(
                '/userspb.Users/FindUsers',
                request_serializer=users_dot_users__pb2.FindUsersRequest.SerializeToString,
                response_deserializer=users_dot_users__pb2.FindUsersResponse.FromString,
                )


class UsersServicer(object):
    """Сервис пользователей
    """

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindUsers(self, request, context):
        """TODO: rpc DeleteUserByID (DeleteUserByIDRequest) returns (DeleteUserByIDResponse); // Удаляет всю информацию о пользователе, каскадно через брокер сообщений в других сервисах
        TODO: rpc SendUserEmailConfirmCode (SendUserEmailConfirmCodeRequest) returns (google.protobuf.Empty); // Отправляет код подтверждения на Email юзера. Код потребуется в методе обновления Email
        TODO: rpc ConfirmUserEmail (ConfirmUserEmailRequest) returns (google.protobuf.Empty);
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=users_dot_users__pb2.CreateUserRequest.FromString,
                    response_serializer=users_dot_users__pb2.CreateUserResponse.SerializeToString,
            ),
            'GetUserByID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByID,
                    request_deserializer=users_dot_users__pb2.GetUserByIDRequest.FromString,
                    response_serializer=users_dot_users__pb2.GetUserByIDResponse.SerializeToString,
            ),
            'FindUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.FindUsers,
                    request_deserializer=users_dot_users__pb2.FindUsersRequest.FromString,
                    response_serializer=users_dot_users__pb2.FindUsersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'userspb.Users', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Users(object):
    """Сервис пользователей
    """

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userspb.Users/CreateUser',
            users_dot_users__pb2.CreateUserRequest.SerializeToString,
            users_dot_users__pb2.CreateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userspb.Users/GetUserByID',
            users_dot_users__pb2.GetUserByIDRequest.SerializeToString,
            users_dot_users__pb2.GetUserByIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userspb.Users/FindUsers',
            users_dot_users__pb2.FindUsersRequest.SerializeToString,
            users_dot_users__pb2.FindUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
