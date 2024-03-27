# gen-auth:
# 	protoc -I proto proto/auth/*.proto --go_out=./gen/go --go_opt=paths=source_relative --go-grpc_out=./gen/go/ --go-grpc_opt=paths=source_relative

# gen-categories:
# 	protoc --proto_path=./proto proto/categories/*.proto --go_out=./gen/go --go_opt=paths=source_relative --go-grpc_out=./gen/go/ --go-grpc_opt=paths=source_relative

# gen-products:
# 	protoc -I proto proto/products/*.proto --go_out=./gen/go --go_opt=paths=source_relative --go-grpc_out=./gen/go/ --go-grpc_opt=paths=source_relative

# gen-users:
# 	protoc -I proto proto/users/*.proto --go_out=./gen/go --go_opt=paths=source_relative --go-grpc_out=./gen/go/ --go-grpc_opt=paths=source_relative

# gen-purchases:
# 	protoc -I proto proto/purchases/*.proto --go_out=./gen/go --go_opt=paths=source_relative --go-grpc_out=./gen/go/ --go-grpc_opt=paths=source_relative


gen-all:
	protoc --proto_path=./proto proto/*/*.proto --go_out=./gen/go --go_opt=paths=source_relative --go-grpc_out=./gen/go/ --go-grpc_opt=paths=source_relative
