# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pactus/proto/utils.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 27, 2, "", "pactus/proto/utils.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x18pactus/proto/utils.proto\x12\x06pactus"H\n SignMessageWithPrivateKeyRequest\x12\x13\n\x0bprivate_key\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t"6\n!SignMessageWithPrivateKeyResponse\x12\x11\n\tsignature\x18\x01 \x01(\t"N\n\x14VerifyMessageRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\tsignature\x18\x02 \x01(\t\x12\x12\n\npublic_key\x18\x03 \x01(\t")\n\x15VerifyMessageResponse\x12\x10\n\x08is_valid\x18\x01 \x01(\x08\x32\xc7\x01\n\x05Utils\x12p\n\x19SignMessageWithPrivateKey\x12(.pactus.SignMessageWithPrivateKeyRequest\x1a).pactus.SignMessageWithPrivateKeyResponse\x12L\n\rVerifyMessage\x12\x1c.pactus.VerifyMessageRequest\x1a\x1d.pactus.VerifyMessageResponseB@\n\x0cpactus.utilsZ0github.com/pactus-project/pactus/www/grpc/pactusb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "pactus.proto.utils_pb2", _globals
)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = (
        b"\n\014pactus.utilsZ0github.com/pactus-project/pactus/www/grpc/pactus"
    )
    _globals["_SIGNMESSAGEWITHPRIVATEKEYREQUEST"]._serialized_start = 36
    _globals["_SIGNMESSAGEWITHPRIVATEKEYREQUEST"]._serialized_end = 108
    _globals["_SIGNMESSAGEWITHPRIVATEKEYRESPONSE"]._serialized_start = 110
    _globals["_SIGNMESSAGEWITHPRIVATEKEYRESPONSE"]._serialized_end = 164
    _globals["_VERIFYMESSAGEREQUEST"]._serialized_start = 166
    _globals["_VERIFYMESSAGEREQUEST"]._serialized_end = 244
    _globals["_VERIFYMESSAGERESPONSE"]._serialized_start = 246
    _globals["_VERIFYMESSAGERESPONSE"]._serialized_end = 287
    _globals["_UTILS"]._serialized_start = 290
    _globals["_UTILS"]._serialized_end = 489
# @@protoc_insertion_point(module_scope)