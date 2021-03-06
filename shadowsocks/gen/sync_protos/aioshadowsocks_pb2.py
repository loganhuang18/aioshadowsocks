# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aioshadowsocks.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="aioshadowsocks.proto",
    package="aioshadowsocks",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x14\x61ioshadowsocks.proto\x12\x0e\x61ioshadowsocks"\x1c\n\tUserIdReq\x12\x0f\n\x07user_id\x18\x01 \x01(\x05"\x17\n\x07PortReq\x12\x0c\n\x04port\x18\x01 \x01(\x05"p\n\x07UserReq\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x0e\n\x06method\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x0e\n\x06\x65nable\x18\x05 \x01(\x08\x12\x14\n\x0ctcp_conn_num\x18\x06 \x01(\x05"\x1d\n\x0eHealthCheckReq\x12\x0b\n\x03url\x18\x01 \x01(\t"7\n\x0eHealthCheckRes\x12\x13\n\x0bstatus_code\x18\x01 \x01(\t\x12\x10\n\x08\x64uration\x18\x02 \x01(\x05"\x07\n\x05\x45mpty"\xee\x01\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x0e\n\x06method\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x0e\n\x06\x65nable\x18\x05 \x01(\x08\x12\x13\n\x0bspeed_limit\x18\x06 \x01(\x05\x12\x14\n\x0c\x61\x63\x63\x65ss_order\x18\x07 \x01(\x05\x12\x11\n\tneed_sync\x18\x08 \x01(\x08\x12\x0f\n\x07ip_list\x18\t \x03(\t\x12\x14\n\x0ctcp_conn_num\x18\n \x01(\x05\x12\x16\n\x0eupload_traffic\x18\x0b \x01(\x03\x12\x18\n\x10\x64ownload_traffic\x18\x0c \x01(\x03".\n\x08UserList\x12"\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x14.aioshadowsocks.User"T\n\x11\x46indAccessUserReq\x12\x0c\n\x04port\x18\x01 \x01(\x05\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x13\n\x0bts_protocol\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c"_\n\x0e\x44\x65\x63ryptDataReq\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x0e\n\x06method\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c"\x1e\n\x0e\x44\x65\x63ryptDataRes\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x32\xb4\x04\n\x02ss\x12=\n\nCreateUser\x12\x17.aioshadowsocks.UserReq\x1a\x14.aioshadowsocks.User"\x00\x12=\n\nUpdateUser\x12\x17.aioshadowsocks.UserReq\x1a\x14.aioshadowsocks.User"\x00\x12<\n\x07GetUser\x12\x19.aioshadowsocks.UserIdReq\x1a\x14.aioshadowsocks.User"\x00\x12@\n\nDeleteUser\x12\x19.aioshadowsocks.UserIdReq\x1a\x15.aioshadowsocks.Empty"\x00\x12?\n\x08ListUser\x12\x17.aioshadowsocks.UserReq\x1a\x18.aioshadowsocks.UserList"\x00\x12Q\n\x0bHealthCheck\x12\x1e.aioshadowsocks.HealthCheckReq\x1a\x1e.aioshadowsocks.HealthCheckRes"\x00\x30\x01\x12K\n\x0e\x46indAccessUser\x12!.aioshadowsocks.FindAccessUserReq\x1a\x14.aioshadowsocks.User"\x00\x12O\n\x0b\x44\x65\x63ryptData\x12\x1e.aioshadowsocks.DecryptDataReq\x1a\x1e.aioshadowsocks.DecryptDataRes"\x00\x62\x06proto3',
)


_USERIDREQ = _descriptor.Descriptor(
    name="UserIdReq",
    full_name="aioshadowsocks.UserIdReq",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="user_id",
            full_name="aioshadowsocks.UserIdReq.user_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=40,
    serialized_end=68,
)


_PORTREQ = _descriptor.Descriptor(
    name="PortReq",
    full_name="aioshadowsocks.PortReq",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="port",
            full_name="aioshadowsocks.PortReq.port",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=70,
    serialized_end=93,
)


_USERREQ = _descriptor.Descriptor(
    name="UserReq",
    full_name="aioshadowsocks.UserReq",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="user_id",
            full_name="aioshadowsocks.UserReq.user_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="port",
            full_name="aioshadowsocks.UserReq.port",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="method",
            full_name="aioshadowsocks.UserReq.method",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="password",
            full_name="aioshadowsocks.UserReq.password",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="enable",
            full_name="aioshadowsocks.UserReq.enable",
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="tcp_conn_num",
            full_name="aioshadowsocks.UserReq.tcp_conn_num",
            index=5,
            number=6,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=95,
    serialized_end=207,
)


_HEALTHCHECKREQ = _descriptor.Descriptor(
    name="HealthCheckReq",
    full_name="aioshadowsocks.HealthCheckReq",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="url",
            full_name="aioshadowsocks.HealthCheckReq.url",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=209,
    serialized_end=238,
)


_HEALTHCHECKRES = _descriptor.Descriptor(
    name="HealthCheckRes",
    full_name="aioshadowsocks.HealthCheckRes",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="status_code",
            full_name="aioshadowsocks.HealthCheckRes.status_code",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="duration",
            full_name="aioshadowsocks.HealthCheckRes.duration",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=240,
    serialized_end=295,
)


_EMPTY = _descriptor.Descriptor(
    name="Empty",
    full_name="aioshadowsocks.Empty",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=297,
    serialized_end=304,
)


_USER = _descriptor.Descriptor(
    name="User",
    full_name="aioshadowsocks.User",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="user_id",
            full_name="aioshadowsocks.User.user_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="port",
            full_name="aioshadowsocks.User.port",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="method",
            full_name="aioshadowsocks.User.method",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="password",
            full_name="aioshadowsocks.User.password",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="enable",
            full_name="aioshadowsocks.User.enable",
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="speed_limit",
            full_name="aioshadowsocks.User.speed_limit",
            index=5,
            number=6,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="access_order",
            full_name="aioshadowsocks.User.access_order",
            index=6,
            number=7,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="need_sync",
            full_name="aioshadowsocks.User.need_sync",
            index=7,
            number=8,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="ip_list",
            full_name="aioshadowsocks.User.ip_list",
            index=8,
            number=9,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="tcp_conn_num",
            full_name="aioshadowsocks.User.tcp_conn_num",
            index=9,
            number=10,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="upload_traffic",
            full_name="aioshadowsocks.User.upload_traffic",
            index=10,
            number=11,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="download_traffic",
            full_name="aioshadowsocks.User.download_traffic",
            index=11,
            number=12,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=307,
    serialized_end=545,
)


_USERLIST = _descriptor.Descriptor(
    name="UserList",
    full_name="aioshadowsocks.UserList",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="data",
            full_name="aioshadowsocks.UserList.data",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=547,
    serialized_end=593,
)


_FINDACCESSUSERREQ = _descriptor.Descriptor(
    name="FindAccessUserReq",
    full_name="aioshadowsocks.FindAccessUserReq",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="port",
            full_name="aioshadowsocks.FindAccessUserReq.port",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="method",
            full_name="aioshadowsocks.FindAccessUserReq.method",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="ts_protocol",
            full_name="aioshadowsocks.FindAccessUserReq.ts_protocol",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="aioshadowsocks.FindAccessUserReq.data",
            index=3,
            number=4,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=595,
    serialized_end=679,
)


_DECRYPTDATAREQ = _descriptor.Descriptor(
    name="DecryptDataReq",
    full_name="aioshadowsocks.DecryptDataReq",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="user_id",
            full_name="aioshadowsocks.DecryptDataReq.user_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="uuid",
            full_name="aioshadowsocks.DecryptDataReq.uuid",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="password",
            full_name="aioshadowsocks.DecryptDataReq.password",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="method",
            full_name="aioshadowsocks.DecryptDataReq.method",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="aioshadowsocks.DecryptDataReq.data",
            index=4,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=681,
    serialized_end=776,
)


_DECRYPTDATARES = _descriptor.Descriptor(
    name="DecryptDataRes",
    full_name="aioshadowsocks.DecryptDataRes",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="data",
            full_name="aioshadowsocks.DecryptDataRes.data",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=778,
    serialized_end=808,
)

_USERLIST.fields_by_name["data"].message_type = _USER
DESCRIPTOR.message_types_by_name["UserIdReq"] = _USERIDREQ
DESCRIPTOR.message_types_by_name["PortReq"] = _PORTREQ
DESCRIPTOR.message_types_by_name["UserReq"] = _USERREQ
DESCRIPTOR.message_types_by_name["HealthCheckReq"] = _HEALTHCHECKREQ
DESCRIPTOR.message_types_by_name["HealthCheckRes"] = _HEALTHCHECKRES
DESCRIPTOR.message_types_by_name["Empty"] = _EMPTY
DESCRIPTOR.message_types_by_name["User"] = _USER
DESCRIPTOR.message_types_by_name["UserList"] = _USERLIST
DESCRIPTOR.message_types_by_name["FindAccessUserReq"] = _FINDACCESSUSERREQ
DESCRIPTOR.message_types_by_name["DecryptDataReq"] = _DECRYPTDATAREQ
DESCRIPTOR.message_types_by_name["DecryptDataRes"] = _DECRYPTDATARES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserIdReq = _reflection.GeneratedProtocolMessageType(
    "UserIdReq",
    (_message.Message,),
    {
        "DESCRIPTOR": _USERIDREQ,
        "__module__": "aioshadowsocks_pb2"
        # @@protoc_insertion_point(class_scope:aioshadowsocks.UserIdReq)
    },
)
_sym_db.RegisterMessage(UserIdReq)

PortReq = _reflection.GeneratedProtocolMessageType(
    "PortReq",
    (_message.Message,),
    {
        "DESCRIPTOR": _PORTREQ,
        "__module__": "aioshadowsocks_pb2"
        # @@protoc_insertion_point(class_scope:aioshadowsocks.PortReq)
    },
)
_sym_db.RegisterMessage(PortReq)

UserReq = _reflection.GeneratedProtocolMessageType(
    "UserReq",
    (_message.Message,),
    {
        "DESCRIPTOR": _USERREQ,
        "__module__": "aioshadowsocks_pb2"
        # @@protoc_insertion_point(class_scope:aioshadowsocks.UserReq)
    },
)
_sym_db.RegisterMessage(UserReq)

HealthCheckReq = _reflection.GeneratedProtocolMessageType(
    "HealthCheckReq",
    (_message.Message,),
    {
        "DESCRIPTOR": _HEALTHCHECKREQ,
        "__module__": "aioshadowsocks_pb2"
        # @@protoc_insertion_point(class_scope:aioshadowsocks.HealthCheckReq)
    },
)
_sym_db.RegisterMessage(HealthCheckReq)

HealthCheckRes = _reflection.GeneratedProtocolMessageType(
    "HealthCheckRes",
    (_message.Message,),
    {
        "DESCRIPTOR": _HEALTHCHECKRES,
        "__module__": "aioshadowsocks_pb2"
        # @@protoc_insertion_point(class_scope:aioshadowsocks.HealthCheckRes)
    },
)
_sym_db.RegisterMessage(HealthCheckRes)

Empty = _reflection.GeneratedProtocolMessageType(
    "Empty",
    (_message.Message,),
    {
        "DESCRIPTOR": _EMPTY,
        "__module__": "aioshadowsocks_pb2"
        # @@protoc_insertion_point(class_scope:aioshadowsocks.Empty)
    },
)
_sym_db.RegisterMessage(Empty)

User = _reflection.GeneratedProtocolMessageType(
    "User",
    (_message.Message,),
    {
        "DESCRIPTOR": _USER,
        "__module__": "aioshadowsocks_pb2"
        # @@protoc_insertion_point(class_scope:aioshadowsocks.User)
    },
)
_sym_db.RegisterMessage(User)

UserList = _reflection.GeneratedProtocolMessageType(
    "UserList",
    (_message.Message,),
    {
        "DESCRIPTOR": _USERLIST,
        "__module__": "aioshadowsocks_pb2"
        # @@protoc_insertion_point(class_scope:aioshadowsocks.UserList)
    },
)
_sym_db.RegisterMessage(UserList)

FindAccessUserReq = _reflection.GeneratedProtocolMessageType(
    "FindAccessUserReq",
    (_message.Message,),
    {
        "DESCRIPTOR": _FINDACCESSUSERREQ,
        "__module__": "aioshadowsocks_pb2"
        # @@protoc_insertion_point(class_scope:aioshadowsocks.FindAccessUserReq)
    },
)
_sym_db.RegisterMessage(FindAccessUserReq)

DecryptDataReq = _reflection.GeneratedProtocolMessageType(
    "DecryptDataReq",
    (_message.Message,),
    {
        "DESCRIPTOR": _DECRYPTDATAREQ,
        "__module__": "aioshadowsocks_pb2"
        # @@protoc_insertion_point(class_scope:aioshadowsocks.DecryptDataReq)
    },
)
_sym_db.RegisterMessage(DecryptDataReq)

DecryptDataRes = _reflection.GeneratedProtocolMessageType(
    "DecryptDataRes",
    (_message.Message,),
    {
        "DESCRIPTOR": _DECRYPTDATARES,
        "__module__": "aioshadowsocks_pb2"
        # @@protoc_insertion_point(class_scope:aioshadowsocks.DecryptDataRes)
    },
)
_sym_db.RegisterMessage(DecryptDataRes)


_SS = _descriptor.ServiceDescriptor(
    name="ss",
    full_name="aioshadowsocks.ss",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=811,
    serialized_end=1375,
    methods=[
        _descriptor.MethodDescriptor(
            name="CreateUser",
            full_name="aioshadowsocks.ss.CreateUser",
            index=0,
            containing_service=None,
            input_type=_USERREQ,
            output_type=_USER,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="UpdateUser",
            full_name="aioshadowsocks.ss.UpdateUser",
            index=1,
            containing_service=None,
            input_type=_USERREQ,
            output_type=_USER,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetUser",
            full_name="aioshadowsocks.ss.GetUser",
            index=2,
            containing_service=None,
            input_type=_USERIDREQ,
            output_type=_USER,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="DeleteUser",
            full_name="aioshadowsocks.ss.DeleteUser",
            index=3,
            containing_service=None,
            input_type=_USERIDREQ,
            output_type=_EMPTY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ListUser",
            full_name="aioshadowsocks.ss.ListUser",
            index=4,
            containing_service=None,
            input_type=_USERREQ,
            output_type=_USERLIST,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="HealthCheck",
            full_name="aioshadowsocks.ss.HealthCheck",
            index=5,
            containing_service=None,
            input_type=_HEALTHCHECKREQ,
            output_type=_HEALTHCHECKRES,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="FindAccessUser",
            full_name="aioshadowsocks.ss.FindAccessUser",
            index=6,
            containing_service=None,
            input_type=_FINDACCESSUSERREQ,
            output_type=_USER,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="DecryptData",
            full_name="aioshadowsocks.ss.DecryptData",
            index=7,
            containing_service=None,
            input_type=_DECRYPTDATAREQ,
            output_type=_DECRYPTDATARES,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_SS)

DESCRIPTOR.services_by_name["ss"] = _SS

# @@protoc_insertion_point(module_scope)
