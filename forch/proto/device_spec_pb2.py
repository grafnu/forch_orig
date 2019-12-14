# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/device_spec.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='forch/proto/device_spec.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1d\x66orch/proto/device_spec.proto\"\xef\x04\n\nDeviceSpec\x12,\n\tmac_addrs\x18\x01 \x03(\x0b\x32\x19.DeviceSpec.MacAddrsEntry\x1aG\n\rMacAddrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.DeviceSpec.DeviceInfo:\x02\x38\x01\x1a\xb3\x01\n\nDeviceInfo\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05group\x18\x02 \x01(\t\x12<\n\x0b\x63ontrollers\x18\x03 \x03(\x0b\x32\'.DeviceSpec.DeviceInfo.ControllersEntry\x1aJ\n\x10\x43ontrollersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.DeviceSpec.Controller:\x02\x38\x01\x1a\x92\x01\n\nController\x12:\n\ncontrolees\x18\x01 \x03(\x0b\x32&.DeviceSpec.Controller.ControleesEntry\x1aH\n\x0f\x43ontroleesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.DeviceSpec.Controlee:\x02\x38\x01\x1a\x8e\x01\n\tControlee\x12\x36\n\tmac_addrs\x18\x01 \x03(\x0b\x32#.DeviceSpec.Controlee.MacAddrsEntry\x1aI\n\rMacAddrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.DeviceSpec.DeviceTarget:\x02\x38\x01\x1a\x0e\n\x0c\x44\x65viceTargetb\x06proto3')
)




_DEVICESPEC_MACADDRSENTRY = _descriptor.Descriptor(
  name='MacAddrsEntry',
  full_name='DeviceSpec.MacAddrsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DeviceSpec.MacAddrsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='DeviceSpec.MacAddrsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=165,
)

_DEVICESPEC_DEVICEINFO_CONTROLLERSENTRY = _descriptor.Descriptor(
  name='ControllersEntry',
  full_name='DeviceSpec.DeviceInfo.ControllersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DeviceSpec.DeviceInfo.ControllersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='DeviceSpec.DeviceInfo.ControllersEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=347,
)

_DEVICESPEC_DEVICEINFO = _descriptor.Descriptor(
  name='DeviceInfo',
  full_name='DeviceSpec.DeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='DeviceSpec.DeviceInfo.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='DeviceSpec.DeviceInfo.group', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controllers', full_name='DeviceSpec.DeviceInfo.controllers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEVICESPEC_DEVICEINFO_CONTROLLERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=347,
)

_DEVICESPEC_CONTROLLER_CONTROLEESENTRY = _descriptor.Descriptor(
  name='ControleesEntry',
  full_name='DeviceSpec.Controller.ControleesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DeviceSpec.Controller.ControleesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='DeviceSpec.Controller.ControleesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=424,
  serialized_end=496,
)

_DEVICESPEC_CONTROLLER = _descriptor.Descriptor(
  name='Controller',
  full_name='DeviceSpec.Controller',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='controlees', full_name='DeviceSpec.Controller.controlees', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEVICESPEC_CONTROLLER_CONTROLEESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=496,
)

_DEVICESPEC_CONTROLEE_MACADDRSENTRY = _descriptor.Descriptor(
  name='MacAddrsEntry',
  full_name='DeviceSpec.Controlee.MacAddrsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DeviceSpec.Controlee.MacAddrsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='DeviceSpec.Controlee.MacAddrsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=568,
  serialized_end=641,
)

_DEVICESPEC_CONTROLEE = _descriptor.Descriptor(
  name='Controlee',
  full_name='DeviceSpec.Controlee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac_addrs', full_name='DeviceSpec.Controlee.mac_addrs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEVICESPEC_CONTROLEE_MACADDRSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=499,
  serialized_end=641,
)

_DEVICESPEC_DEVICETARGET = _descriptor.Descriptor(
  name='DeviceTarget',
  full_name='DeviceSpec.DeviceTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=643,
  serialized_end=657,
)

_DEVICESPEC = _descriptor.Descriptor(
  name='DeviceSpec',
  full_name='DeviceSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac_addrs', full_name='DeviceSpec.mac_addrs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEVICESPEC_MACADDRSENTRY, _DEVICESPEC_DEVICEINFO, _DEVICESPEC_CONTROLLER, _DEVICESPEC_CONTROLEE, _DEVICESPEC_DEVICETARGET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=657,
)

_DEVICESPEC_MACADDRSENTRY.fields_by_name['value'].message_type = _DEVICESPEC_DEVICEINFO
_DEVICESPEC_MACADDRSENTRY.containing_type = _DEVICESPEC
_DEVICESPEC_DEVICEINFO_CONTROLLERSENTRY.fields_by_name['value'].message_type = _DEVICESPEC_CONTROLLER
_DEVICESPEC_DEVICEINFO_CONTROLLERSENTRY.containing_type = _DEVICESPEC_DEVICEINFO
_DEVICESPEC_DEVICEINFO.fields_by_name['controllers'].message_type = _DEVICESPEC_DEVICEINFO_CONTROLLERSENTRY
_DEVICESPEC_DEVICEINFO.containing_type = _DEVICESPEC
_DEVICESPEC_CONTROLLER_CONTROLEESENTRY.fields_by_name['value'].message_type = _DEVICESPEC_CONTROLEE
_DEVICESPEC_CONTROLLER_CONTROLEESENTRY.containing_type = _DEVICESPEC_CONTROLLER
_DEVICESPEC_CONTROLLER.fields_by_name['controlees'].message_type = _DEVICESPEC_CONTROLLER_CONTROLEESENTRY
_DEVICESPEC_CONTROLLER.containing_type = _DEVICESPEC
_DEVICESPEC_CONTROLEE_MACADDRSENTRY.fields_by_name['value'].message_type = _DEVICESPEC_DEVICETARGET
_DEVICESPEC_CONTROLEE_MACADDRSENTRY.containing_type = _DEVICESPEC_CONTROLEE
_DEVICESPEC_CONTROLEE.fields_by_name['mac_addrs'].message_type = _DEVICESPEC_CONTROLEE_MACADDRSENTRY
_DEVICESPEC_CONTROLEE.containing_type = _DEVICESPEC
_DEVICESPEC_DEVICETARGET.containing_type = _DEVICESPEC
_DEVICESPEC.fields_by_name['mac_addrs'].message_type = _DEVICESPEC_MACADDRSENTRY
DESCRIPTOR.message_types_by_name['DeviceSpec'] = _DEVICESPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceSpec = _reflection.GeneratedProtocolMessageType('DeviceSpec', (_message.Message,), dict(

  MacAddrsEntry = _reflection.GeneratedProtocolMessageType('MacAddrsEntry', (_message.Message,), dict(
    DESCRIPTOR = _DEVICESPEC_MACADDRSENTRY,
    __module__ = 'forch.proto.device_spec_pb2'
    # @@protoc_insertion_point(class_scope:DeviceSpec.MacAddrsEntry)
    ))
  ,

  DeviceInfo = _reflection.GeneratedProtocolMessageType('DeviceInfo', (_message.Message,), dict(

    ControllersEntry = _reflection.GeneratedProtocolMessageType('ControllersEntry', (_message.Message,), dict(
      DESCRIPTOR = _DEVICESPEC_DEVICEINFO_CONTROLLERSENTRY,
      __module__ = 'forch.proto.device_spec_pb2'
      # @@protoc_insertion_point(class_scope:DeviceSpec.DeviceInfo.ControllersEntry)
      ))
    ,
    DESCRIPTOR = _DEVICESPEC_DEVICEINFO,
    __module__ = 'forch.proto.device_spec_pb2'
    # @@protoc_insertion_point(class_scope:DeviceSpec.DeviceInfo)
    ))
  ,

  Controller = _reflection.GeneratedProtocolMessageType('Controller', (_message.Message,), dict(

    ControleesEntry = _reflection.GeneratedProtocolMessageType('ControleesEntry', (_message.Message,), dict(
      DESCRIPTOR = _DEVICESPEC_CONTROLLER_CONTROLEESENTRY,
      __module__ = 'forch.proto.device_spec_pb2'
      # @@protoc_insertion_point(class_scope:DeviceSpec.Controller.ControleesEntry)
      ))
    ,
    DESCRIPTOR = _DEVICESPEC_CONTROLLER,
    __module__ = 'forch.proto.device_spec_pb2'
    # @@protoc_insertion_point(class_scope:DeviceSpec.Controller)
    ))
  ,

  Controlee = _reflection.GeneratedProtocolMessageType('Controlee', (_message.Message,), dict(

    MacAddrsEntry = _reflection.GeneratedProtocolMessageType('MacAddrsEntry', (_message.Message,), dict(
      DESCRIPTOR = _DEVICESPEC_CONTROLEE_MACADDRSENTRY,
      __module__ = 'forch.proto.device_spec_pb2'
      # @@protoc_insertion_point(class_scope:DeviceSpec.Controlee.MacAddrsEntry)
      ))
    ,
    DESCRIPTOR = _DEVICESPEC_CONTROLEE,
    __module__ = 'forch.proto.device_spec_pb2'
    # @@protoc_insertion_point(class_scope:DeviceSpec.Controlee)
    ))
  ,

  DeviceTarget = _reflection.GeneratedProtocolMessageType('DeviceTarget', (_message.Message,), dict(
    DESCRIPTOR = _DEVICESPEC_DEVICETARGET,
    __module__ = 'forch.proto.device_spec_pb2'
    # @@protoc_insertion_point(class_scope:DeviceSpec.DeviceTarget)
    ))
  ,
  DESCRIPTOR = _DEVICESPEC,
  __module__ = 'forch.proto.device_spec_pb2'
  # @@protoc_insertion_point(class_scope:DeviceSpec)
  ))
_sym_db.RegisterMessage(DeviceSpec)
_sym_db.RegisterMessage(DeviceSpec.MacAddrsEntry)
_sym_db.RegisterMessage(DeviceSpec.DeviceInfo)
_sym_db.RegisterMessage(DeviceSpec.DeviceInfo.ControllersEntry)
_sym_db.RegisterMessage(DeviceSpec.Controller)
_sym_db.RegisterMessage(DeviceSpec.Controller.ControleesEntry)
_sym_db.RegisterMessage(DeviceSpec.Controlee)
_sym_db.RegisterMessage(DeviceSpec.Controlee.MacAddrsEntry)
_sym_db.RegisterMessage(DeviceSpec.DeviceTarget)


_DEVICESPEC_MACADDRSENTRY._options = None
_DEVICESPEC_DEVICEINFO_CONTROLLERSENTRY._options = None
_DEVICESPEC_CONTROLLER_CONTROLEESENTRY._options = None
_DEVICESPEC_CONTROLEE_MACADDRSENTRY._options = None
# @@protoc_insertion_point(module_scope)
