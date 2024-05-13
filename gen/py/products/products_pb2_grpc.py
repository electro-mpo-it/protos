# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from products import products_pb2 as products_dot_products__pb2


class ProductsStub(object):
    """Сервис товаров
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateProduct = channel.unary_unary(
                '/productspb.Products/CreateProduct',
                request_serializer=products_dot_products__pb2.CreateProductRequest.SerializeToString,
                response_deserializer=products_dot_products__pb2.CreateProductResponse.FromString,
                )
        self.GetProductByID = channel.unary_unary(
                '/productspb.Products/GetProductByID',
                request_serializer=products_dot_products__pb2.GetProductByIDRequest.SerializeToString,
                response_deserializer=products_dot_products__pb2.GetProductByIDResponse.FromString,
                )
        self.FindProducts = channel.unary_unary(
                '/productspb.Products/FindProducts',
                request_serializer=products_dot_products__pb2.ProductsFilterRequest.SerializeToString,
                response_deserializer=products_dot_products__pb2.FindProductsResponse.FromString,
                )
        self.UpdateProductByID = channel.unary_unary(
                '/productspb.Products/UpdateProductByID',
                request_serializer=products_dot_products__pb2.UpdateProductByIDRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CreateCharacteristic = channel.unary_unary(
                '/productspb.Products/CreateCharacteristic',
                request_serializer=products_dot_products__pb2.CreateCharacteristicRequest.SerializeToString,
                response_deserializer=products_dot_products__pb2.CreateCharacteristicResponse.FromString,
                )
        self.FindCharacteristics = channel.unary_unary(
                '/productspb.Products/FindCharacteristics',
                request_serializer=products_dot_products__pb2.FindCharacteristicsRequest.SerializeToString,
                response_deserializer=products_dot_products__pb2.FindCharacteristicsResponse.FromString,
                )
        self.UpdateCharacteristic = channel.unary_unary(
                '/productspb.Products/UpdateCharacteristic',
                request_serializer=products_dot_products__pb2.UpdateCharacteristicRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DeleteCharacteristic = channel.unary_unary(
                '/productspb.Products/DeleteCharacteristic',
                request_serializer=products_dot_products__pb2.DeleteCharacteristicRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ApplyFilters = channel.unary_unary(
                '/productspb.Products/ApplyFilters',
                request_serializer=products_dot_products__pb2.ProductsFilterRequest.SerializeToString,
                response_deserializer=products_dot_products__pb2.AvailableFilters.FromString,
                )


class ProductsServicer(object):
    """Сервис товаров
    """

    def CreateProduct(self, request, context):
        """Создание товара
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProductByID(self, request, context):
        """Получение товара по его ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindProducts(self, request, context):
        """Поиск по товарам
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProductByID(self, request, context):
        """Частичное обновление товара
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCharacteristic(self, request, context):
        """Создать характеристику
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindCharacteristics(self, request, context):
        """Поиск по характеристикам
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCharacteristic(self, request, context):
        """Обновить данные о характеристике (Кроме типа данных!)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCharacteristic(self, request, context):
        """Удалить характеристику
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ApplyFilters(self, request, context):
        """<<Фасетная фильтрация товаров>> Выводит доступные для дальнейшей фильтрации цену и характеристики (Непосредственно товары метод не фильтрует.)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProduct,
                    request_deserializer=products_dot_products__pb2.CreateProductRequest.FromString,
                    response_serializer=products_dot_products__pb2.CreateProductResponse.SerializeToString,
            ),
            'GetProductByID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProductByID,
                    request_deserializer=products_dot_products__pb2.GetProductByIDRequest.FromString,
                    response_serializer=products_dot_products__pb2.GetProductByIDResponse.SerializeToString,
            ),
            'FindProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.FindProducts,
                    request_deserializer=products_dot_products__pb2.ProductsFilterRequest.FromString,
                    response_serializer=products_dot_products__pb2.FindProductsResponse.SerializeToString,
            ),
            'UpdateProductByID': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProductByID,
                    request_deserializer=products_dot_products__pb2.UpdateProductByIDRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CreateCharacteristic': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCharacteristic,
                    request_deserializer=products_dot_products__pb2.CreateCharacteristicRequest.FromString,
                    response_serializer=products_dot_products__pb2.CreateCharacteristicResponse.SerializeToString,
            ),
            'FindCharacteristics': grpc.unary_unary_rpc_method_handler(
                    servicer.FindCharacteristics,
                    request_deserializer=products_dot_products__pb2.FindCharacteristicsRequest.FromString,
                    response_serializer=products_dot_products__pb2.FindCharacteristicsResponse.SerializeToString,
            ),
            'UpdateCharacteristic': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCharacteristic,
                    request_deserializer=products_dot_products__pb2.UpdateCharacteristicRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeleteCharacteristic': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCharacteristic,
                    request_deserializer=products_dot_products__pb2.DeleteCharacteristicRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ApplyFilters': grpc.unary_unary_rpc_method_handler(
                    servicer.ApplyFilters,
                    request_deserializer=products_dot_products__pb2.ProductsFilterRequest.FromString,
                    response_serializer=products_dot_products__pb2.AvailableFilters.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'productspb.Products', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Products(object):
    """Сервис товаров
    """

    @staticmethod
    def CreateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/productspb.Products/CreateProduct',
            products_dot_products__pb2.CreateProductRequest.SerializeToString,
            products_dot_products__pb2.CreateProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProductByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/productspb.Products/GetProductByID',
            products_dot_products__pb2.GetProductByIDRequest.SerializeToString,
            products_dot_products__pb2.GetProductByIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/productspb.Products/FindProducts',
            products_dot_products__pb2.ProductsFilterRequest.SerializeToString,
            products_dot_products__pb2.FindProductsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProductByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/productspb.Products/UpdateProductByID',
            products_dot_products__pb2.UpdateProductByIDRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCharacteristic(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/productspb.Products/CreateCharacteristic',
            products_dot_products__pb2.CreateCharacteristicRequest.SerializeToString,
            products_dot_products__pb2.CreateCharacteristicResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindCharacteristics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/productspb.Products/FindCharacteristics',
            products_dot_products__pb2.FindCharacteristicsRequest.SerializeToString,
            products_dot_products__pb2.FindCharacteristicsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCharacteristic(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/productspb.Products/UpdateCharacteristic',
            products_dot_products__pb2.UpdateCharacteristicRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCharacteristic(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/productspb.Products/DeleteCharacteristic',
            products_dot_products__pb2.DeleteCharacteristicRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ApplyFilters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/productspb.Products/ApplyFilters',
            products_dot_products__pb2.ProductsFilterRequest.SerializeToString,
            products_dot_products__pb2.AvailableFilters.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
