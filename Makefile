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


gen-all-go:
	protoc \
		--proto_path=./proto proto/*/*.proto \
		--go_out=./gen/go \
		--go_opt=paths=source_relative \
		--go-grpc_out=./gen/go/ \
		--go-grpc_opt=paths=source_relative


gen-all-py:
	python -m grpc_tools.protoc \
		--proto_path=./proto proto/*/*.proto \
		--pyi_out=./gen/py \
		--python_out=./gen/py \
		--grpc_python_out=./gen/py \


gen-all: gen-all-go gen-all-py