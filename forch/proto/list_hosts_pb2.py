# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/list_hosts.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='forch/proto/list_hosts.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x1c\x66orch/proto/list_hosts.proto\"\xc8\x02\n\x08HostList\x12(\n\x08\x65th_srcs\x18\x01 \x03(\x0b\x32\x16.HostList.EthSrcsEntry\x12(\n\x08\x65th_dsts\x18\x02 \x03(\x0b\x32\x16.HostList.EthDstsEntry\x12\x18\n\x10system_state_url\x18\x03 \x01(\t\x1a\x42\n\x0c\x45thSrcsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.HostList.HostData:\x02\x38\x01\x1a\x42\n\x0c\x45thDstsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.HostList.HostData:\x02\x38\x01\x1a\x46\n\x08HostData\x12\x0e\n\x06switch\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x0f\n\x07host_ip\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HOSTLIST_ETHSRCSENTRY = _descriptor.Descriptor(
  name='EthSrcsEntry',
  full_name='HostList.EthSrcsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='HostList.EthSrcsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='HostList.EthSrcsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=221,
)

_HOSTLIST_ETHDSTSENTRY = _descriptor.Descriptor(
  name='EthDstsEntry',
  full_name='HostList.EthDstsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='HostList.EthDstsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='HostList.EthDstsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=289,
)

_HOSTLIST_HOSTDATA = _descriptor.Descriptor(
  name='HostData',
  full_name='HostList.HostData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='switch', full_name='HostList.HostData.switch', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='HostList.HostData.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host_ip', full_name='HostList.HostData.host_ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='HostList.HostData.url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=361,
)

_HOSTLIST = _descriptor.Descriptor(
  name='HostList',
  full_name='HostList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='eth_srcs', full_name='HostList.eth_srcs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eth_dsts', full_name='HostList.eth_dsts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_state_url', full_name='HostList.system_state_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_HOSTLIST_ETHSRCSENTRY, _HOSTLIST_ETHDSTSENTRY, _HOSTLIST_HOSTDATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=361,
)

_HOSTLIST_ETHSRCSENTRY.fields_by_name['value'].message_type = _HOSTLIST_HOSTDATA
_HOSTLIST_ETHSRCSENTRY.containing_type = _HOSTLIST
_HOSTLIST_ETHDSTSENTRY.fields_by_name['value'].message_type = _HOSTLIST_HOSTDATA
_HOSTLIST_ETHDSTSENTRY.containing_type = _HOSTLIST
_HOSTLIST_HOSTDATA.containing_type = _HOSTLIST
_HOSTLIST.fields_by_name['eth_srcs'].message_type = _HOSTLIST_ETHSRCSENTRY
_HOSTLIST.fields_by_name['eth_dsts'].message_type = _HOSTLIST_ETHDSTSENTRY
DESCRIPTOR.message_types_by_name['HostList'] = _HOSTLIST

HostList = _reflection.GeneratedProtocolMessageType('HostList', (_message.Message,), dict(

  EthSrcsEntry = _reflection.GeneratedProtocolMessageType('EthSrcsEntry', (_message.Message,), dict(
    DESCRIPTOR = _HOSTLIST_ETHSRCSENTRY,
    __module__ = 'forch.proto.list_hosts_pb2'
    # @@protoc_insertion_point(class_scope:HostList.EthSrcsEntry)
    ))
  ,

  EthDstsEntry = _reflection.GeneratedProtocolMessageType('EthDstsEntry', (_message.Message,), dict(
    DESCRIPTOR = _HOSTLIST_ETHDSTSENTRY,
    __module__ = 'forch.proto.list_hosts_pb2'
    # @@protoc_insertion_point(class_scope:HostList.EthDstsEntry)
    ))
  ,

  HostData = _reflection.GeneratedProtocolMessageType('HostData', (_message.Message,), dict(
    DESCRIPTOR = _HOSTLIST_HOSTDATA,
    __module__ = 'forch.proto.list_hosts_pb2'
    # @@protoc_insertion_point(class_scope:HostList.HostData)
    ))
  ,
  DESCRIPTOR = _HOSTLIST,
  __module__ = 'forch.proto.list_hosts_pb2'
  # @@protoc_insertion_point(class_scope:HostList)
  ))
_sym_db.RegisterMessage(HostList)
_sym_db.RegisterMessage(HostList.EthSrcsEntry)
_sym_db.RegisterMessage(HostList.EthDstsEntry)
_sym_db.RegisterMessage(HostList.HostData)


_HOSTLIST_ETHSRCSENTRY.has_options = True
_HOSTLIST_ETHSRCSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_HOSTLIST_ETHDSTSENTRY.has_options = True
_HOSTLIST_ETHDSTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
