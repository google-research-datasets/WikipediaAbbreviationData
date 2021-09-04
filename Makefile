abbreviation_pb2.py: abbreviation.proto
	protoc --python_out=. $<
