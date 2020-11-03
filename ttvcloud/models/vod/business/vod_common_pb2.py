# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vod/business/vod_common.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='vod/business/vod_common.proto',
  package='Vcloud.Models.Vod',
  syntax='proto3',
  serialized_options=b'\n#com.bytedanceapi.model.vod.businessB\tVodCommonP\001Z9github.com/TTvcloud/vcloud-sdk-golang/models/vod/business\240\001\001\330\001\001\302\002\000\312\002\032Vcloud\\Models\\Vod\\Business\342\002\031Vcloud\\Models\\GPBMetadata',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dvod/business/vod_common.proto\x12\x11Vcloud.Models.Vod\"\xf4\x01\n\rVodSourceInfo\x12\x0e\n\x06\x46ileId\x18\x01 \x01(\t\x12\x0b\n\x03Md5\x18\x02 \x01(\t\x12\x10\n\x08\x46ileType\x18\x03 \x01(\t\x12\r\n\x05\x43odec\x18\x04 \x01(\t\x12\x0e\n\x06Height\x18\x05 \x01(\x03\x12\r\n\x05Width\x18\x06 \x01(\x03\x12\x0e\n\x06\x46ormat\x18\x07 \x01(\t\x12\x10\n\x08\x44uration\x18\x08 \x01(\x02\x12\x0c\n\x04Size\x18\t \x01(\x03\x12\x10\n\x08StoreUri\x18\n \x01(\t\x12\x12\n\nDefinition\x18\x0b \x01(\t\x12\x0f\n\x07\x42itrate\x18\x0c \x01(\x03\x12\x0b\n\x03\x46ps\x18\r \x01(\x02\x12\x12\n\nCreateTime\x18\x0e \x01(\t\"S\n\x0fVodAdaptiveInfo\x12\x13\n\x0bMainPlayUrl\x18\x01 \x01(\t\x12\x15\n\rBackupPlayUrl\x18\x02 \x01(\t\x12\x14\n\x0c\x41\x64\x61ptiveType\x18\x03 \x01(\t\"\xd0\x03\n\x0bVodPlayInfo\x12\x0e\n\x06\x46ileId\x18\x01 \x01(\t\x12\x0b\n\x03Md5\x18\x02 \x01(\t\x12\x10\n\x08\x46ileType\x18\x03 \x01(\t\x12\x0e\n\x06\x46ormat\x18\x04 \x01(\t\x12\r\n\x05\x43odec\x18\x05 \x01(\t\x12\x12\n\nDefinition\x18\x06 \x01(\t\x12\x13\n\x0bMainPlayUrl\x18\x07 \x01(\t\x12\x15\n\rBackupPlayUrl\x18\x08 \x01(\t\x12\x0f\n\x07\x42itrate\x18\t \x01(\x02\x12\r\n\x05Width\x18\n \x01(\x03\x12\x0e\n\x06Height\x18\x0b \x01(\x03\x12\x0c\n\x04Size\x18\x0c \x01(\x03\x12\x11\n\tCheckInfo\x18\r \x01(\t\x12\x12\n\nIndexRange\x18\x0e \x01(\t\x12\x11\n\tInitRange\x18\x0f \x01(\t\x12\x13\n\x0bPreloadSize\x18\x10 \x01(\x03\x12\x16\n\x0ePreloadMinStep\x18\x11 \x01(\x03\x12\x16\n\x0ePreloadMaxStep\x18\x12 \x01(\x03\x12\x17\n\x0fPreloadInterval\x18\x13 \x01(\x03\x12\x14\n\x0cP2pVerifyUrl\x18\x14 \x01(\t\x12\x10\n\x08PlayAuth\x18\x15 \x01(\t\x12\x12\n\nPlayAuthId\x18\x16 \x01(\t\x12\x10\n\x08LogoType\x18\x17 \x01(\t\x12\x0f\n\x07Quality\x18\x18 \x01(\tB\xaf\x01\n#com.bytedanceapi.model.vod.businessB\tVodCommonP\x01Z9github.com/TTvcloud/vcloud-sdk-golang/models/vod/business\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02\x1aVcloud\\Models\\Vod\\Business\xe2\x02\x19Vcloud\\Models\\GPBMetadatab\x06proto3'
)




_VODSOURCEINFO = _descriptor.Descriptor(
  name='VodSourceInfo',
  full_name='Vcloud.Models.Vod.VodSourceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='FileId', full_name='Vcloud.Models.Vod.VodSourceInfo.FileId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Md5', full_name='Vcloud.Models.Vod.VodSourceInfo.Md5', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FileType', full_name='Vcloud.Models.Vod.VodSourceInfo.FileType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Codec', full_name='Vcloud.Models.Vod.VodSourceInfo.Codec', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Height', full_name='Vcloud.Models.Vod.VodSourceInfo.Height', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Width', full_name='Vcloud.Models.Vod.VodSourceInfo.Width', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Format', full_name='Vcloud.Models.Vod.VodSourceInfo.Format', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Duration', full_name='Vcloud.Models.Vod.VodSourceInfo.Duration', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Size', full_name='Vcloud.Models.Vod.VodSourceInfo.Size', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='StoreUri', full_name='Vcloud.Models.Vod.VodSourceInfo.StoreUri', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Definition', full_name='Vcloud.Models.Vod.VodSourceInfo.Definition', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Bitrate', full_name='Vcloud.Models.Vod.VodSourceInfo.Bitrate', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Fps', full_name='Vcloud.Models.Vod.VodSourceInfo.Fps', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CreateTime', full_name='Vcloud.Models.Vod.VodSourceInfo.CreateTime', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=297,
)


_VODADAPTIVEINFO = _descriptor.Descriptor(
  name='VodAdaptiveInfo',
  full_name='Vcloud.Models.Vod.VodAdaptiveInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='MainPlayUrl', full_name='Vcloud.Models.Vod.VodAdaptiveInfo.MainPlayUrl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BackupPlayUrl', full_name='Vcloud.Models.Vod.VodAdaptiveInfo.BackupPlayUrl', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='AdaptiveType', full_name='Vcloud.Models.Vod.VodAdaptiveInfo.AdaptiveType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=382,
)


_VODPLAYINFO = _descriptor.Descriptor(
  name='VodPlayInfo',
  full_name='Vcloud.Models.Vod.VodPlayInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='FileId', full_name='Vcloud.Models.Vod.VodPlayInfo.FileId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Md5', full_name='Vcloud.Models.Vod.VodPlayInfo.Md5', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FileType', full_name='Vcloud.Models.Vod.VodPlayInfo.FileType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Format', full_name='Vcloud.Models.Vod.VodPlayInfo.Format', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Codec', full_name='Vcloud.Models.Vod.VodPlayInfo.Codec', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Definition', full_name='Vcloud.Models.Vod.VodPlayInfo.Definition', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MainPlayUrl', full_name='Vcloud.Models.Vod.VodPlayInfo.MainPlayUrl', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BackupPlayUrl', full_name='Vcloud.Models.Vod.VodPlayInfo.BackupPlayUrl', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Bitrate', full_name='Vcloud.Models.Vod.VodPlayInfo.Bitrate', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Width', full_name='Vcloud.Models.Vod.VodPlayInfo.Width', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Height', full_name='Vcloud.Models.Vod.VodPlayInfo.Height', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Size', full_name='Vcloud.Models.Vod.VodPlayInfo.Size', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CheckInfo', full_name='Vcloud.Models.Vod.VodPlayInfo.CheckInfo', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='IndexRange', full_name='Vcloud.Models.Vod.VodPlayInfo.IndexRange', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='InitRange', full_name='Vcloud.Models.Vod.VodPlayInfo.InitRange', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PreloadSize', full_name='Vcloud.Models.Vod.VodPlayInfo.PreloadSize', index=15,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PreloadMinStep', full_name='Vcloud.Models.Vod.VodPlayInfo.PreloadMinStep', index=16,
      number=17, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PreloadMaxStep', full_name='Vcloud.Models.Vod.VodPlayInfo.PreloadMaxStep', index=17,
      number=18, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PreloadInterval', full_name='Vcloud.Models.Vod.VodPlayInfo.PreloadInterval', index=18,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='P2pVerifyUrl', full_name='Vcloud.Models.Vod.VodPlayInfo.P2pVerifyUrl', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PlayAuth', full_name='Vcloud.Models.Vod.VodPlayInfo.PlayAuth', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PlayAuthId', full_name='Vcloud.Models.Vod.VodPlayInfo.PlayAuthId', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LogoType', full_name='Vcloud.Models.Vod.VodPlayInfo.LogoType', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Quality', full_name='Vcloud.Models.Vod.VodPlayInfo.Quality', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=849,
)

DESCRIPTOR.message_types_by_name['VodSourceInfo'] = _VODSOURCEINFO
DESCRIPTOR.message_types_by_name['VodAdaptiveInfo'] = _VODADAPTIVEINFO
DESCRIPTOR.message_types_by_name['VodPlayInfo'] = _VODPLAYINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VodSourceInfo = _reflection.GeneratedProtocolMessageType('VodSourceInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODSOURCEINFO,
  '__module__' : 'vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Vcloud.Models.Vod.VodSourceInfo)
  })
_sym_db.RegisterMessage(VodSourceInfo)

VodAdaptiveInfo = _reflection.GeneratedProtocolMessageType('VodAdaptiveInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODADAPTIVEINFO,
  '__module__' : 'vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Vcloud.Models.Vod.VodAdaptiveInfo)
  })
_sym_db.RegisterMessage(VodAdaptiveInfo)

VodPlayInfo = _reflection.GeneratedProtocolMessageType('VodPlayInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODPLAYINFO,
  '__module__' : 'vod.business.vod_common_pb2'
  # @@protoc_insertion_point(class_scope:Vcloud.Models.Vod.VodPlayInfo)
  })
_sym_db.RegisterMessage(VodPlayInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
