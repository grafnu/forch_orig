# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/dataplane_state.proto

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
  name='forch/proto/dataplane_state.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n!forch/proto/dataplane_state.proto\"\xc3\x07\n\x0e\x44\x61taplaneState\x12&\n\x06switch\x18\x01 \x01(\x0b\x32\x16.DataplaneState.Switch\x12$\n\x05stack\x18\x02 \x01(\x0b\x32\x15.DataplaneState.Stack\x12&\n\x06\x65gress\x18\x03 \x01(\x0b\x32\x16.DataplaneState.Egress\x12\x17\n\x0f\x64\x61taplane_state\x18\x04 \x01(\t\x12\x1e\n\x16\x64\x61taplane_state_detail\x18\x05 \x01(\t\x12$\n\x1c\x64\x61taplane_state_change_count\x18\x06 \x01(\x05\x12#\n\x1b\x64\x61taplane_state_last_change\x18\x07 \x01(\t\x12\x18\n\x10system_state_url\x18\x08 \x01(\t\x1a\xd4\x01\n\x06Switch\x12\x36\n\x08switches\x18\x01 \x03(\x0b\x32$.DataplaneState.Switch.SwitchesEntry\x12!\n\x19switch_state_change_count\x18\x02 \x01(\x05\x12 \n\x18switch_state_last_change\x18\x03 \x01(\t\x1aM\n\rSwitchesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.DataplaneState.SwitchStatus:\x02\x38\x01\x1a\xbe\x01\n\x05Stack\x12/\n\x05links\x18\x01 \x03(\x0b\x32 .DataplaneState.Stack.LinksEntry\x12\x1a\n\x12links_change_count\x18\x02 \x01(\x05\x12\x19\n\x11links_last_change\x18\x03 \x01(\t\x1aM\n\nLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.DataplaneState.StackLinkStatus:\x02\x38\x01\x1a\xb7\x01\n\x06\x45gress\x12\x14\n\x0c\x65gress_state\x18\x01 \x01(\t\x12\x1b\n\x13\x65gress_state_detail\x18\x02 \x01(\t\x12!\n\x19\x65gress_state_change_count\x18\x03 \x01(\x05\x12 \n\x18\x65gress_state_last_change\x18\x04 \x01(\t\x12 \n\x18\x65gress_state_last_update\x18\x05 \x01(\t\x12\x13\n\x0b\x61\x63tive_root\x18\x06 \x01(\t\x1a$\n\x0cSwitchStatus\x12\x14\n\x0cswitch_state\x18\x01 \x01(\t\x1a%\n\x0fStackLinkStatus\x12\x12\n\nlink_state\x18\x02 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DATAPLANESTATE_SWITCH_SWITCHESENTRY = _descriptor.Descriptor(
  name='SwitchesEntry',
  full_name='DataplaneState.Switch.SwitchesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DataplaneState.Switch.SwitchesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='DataplaneState.Switch.SwitchesEntry.value', index=1,
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
  serialized_start=468,
  serialized_end=545,
)

_DATAPLANESTATE_SWITCH = _descriptor.Descriptor(
  name='Switch',
  full_name='DataplaneState.Switch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='switches', full_name='DataplaneState.Switch.switches', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='switch_state_change_count', full_name='DataplaneState.Switch.switch_state_change_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='switch_state_last_change', full_name='DataplaneState.Switch.switch_state_last_change', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DATAPLANESTATE_SWITCH_SWITCHESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=545,
)

_DATAPLANESTATE_STACK_LINKSENTRY = _descriptor.Descriptor(
  name='LinksEntry',
  full_name='DataplaneState.Stack.LinksEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DataplaneState.Stack.LinksEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='DataplaneState.Stack.LinksEntry.value', index=1,
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
  serialized_start=661,
  serialized_end=738,
)

_DATAPLANESTATE_STACK = _descriptor.Descriptor(
  name='Stack',
  full_name='DataplaneState.Stack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='links', full_name='DataplaneState.Stack.links', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='links_change_count', full_name='DataplaneState.Stack.links_change_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='links_last_change', full_name='DataplaneState.Stack.links_last_change', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DATAPLANESTATE_STACK_LINKSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=548,
  serialized_end=738,
)

_DATAPLANESTATE_EGRESS = _descriptor.Descriptor(
  name='Egress',
  full_name='DataplaneState.Egress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='egress_state', full_name='DataplaneState.Egress.egress_state', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egress_state_detail', full_name='DataplaneState.Egress.egress_state_detail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egress_state_change_count', full_name='DataplaneState.Egress.egress_state_change_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egress_state_last_change', full_name='DataplaneState.Egress.egress_state_last_change', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egress_state_last_update', full_name='DataplaneState.Egress.egress_state_last_update', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_root', full_name='DataplaneState.Egress.active_root', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=741,
  serialized_end=924,
)

_DATAPLANESTATE_SWITCHSTATUS = _descriptor.Descriptor(
  name='SwitchStatus',
  full_name='DataplaneState.SwitchStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='switch_state', full_name='DataplaneState.SwitchStatus.switch_state', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=926,
  serialized_end=962,
)

_DATAPLANESTATE_STACKLINKSTATUS = _descriptor.Descriptor(
  name='StackLinkStatus',
  full_name='DataplaneState.StackLinkStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='link_state', full_name='DataplaneState.StackLinkStatus.link_state', index=0,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=964,
  serialized_end=1001,
)

_DATAPLANESTATE = _descriptor.Descriptor(
  name='DataplaneState',
  full_name='DataplaneState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='switch', full_name='DataplaneState.switch', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stack', full_name='DataplaneState.stack', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egress', full_name='DataplaneState.egress', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataplane_state', full_name='DataplaneState.dataplane_state', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataplane_state_detail', full_name='DataplaneState.dataplane_state_detail', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataplane_state_change_count', full_name='DataplaneState.dataplane_state_change_count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataplane_state_last_change', full_name='DataplaneState.dataplane_state_last_change', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_state_url', full_name='DataplaneState.system_state_url', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DATAPLANESTATE_SWITCH, _DATAPLANESTATE_STACK, _DATAPLANESTATE_EGRESS, _DATAPLANESTATE_SWITCHSTATUS, _DATAPLANESTATE_STACKLINKSTATUS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=1001,
)

_DATAPLANESTATE_SWITCH_SWITCHESENTRY.fields_by_name['value'].message_type = _DATAPLANESTATE_SWITCHSTATUS
_DATAPLANESTATE_SWITCH_SWITCHESENTRY.containing_type = _DATAPLANESTATE_SWITCH
_DATAPLANESTATE_SWITCH.fields_by_name['switches'].message_type = _DATAPLANESTATE_SWITCH_SWITCHESENTRY
_DATAPLANESTATE_SWITCH.containing_type = _DATAPLANESTATE
_DATAPLANESTATE_STACK_LINKSENTRY.fields_by_name['value'].message_type = _DATAPLANESTATE_STACKLINKSTATUS
_DATAPLANESTATE_STACK_LINKSENTRY.containing_type = _DATAPLANESTATE_STACK
_DATAPLANESTATE_STACK.fields_by_name['links'].message_type = _DATAPLANESTATE_STACK_LINKSENTRY
_DATAPLANESTATE_STACK.containing_type = _DATAPLANESTATE
_DATAPLANESTATE_EGRESS.containing_type = _DATAPLANESTATE
_DATAPLANESTATE_SWITCHSTATUS.containing_type = _DATAPLANESTATE
_DATAPLANESTATE_STACKLINKSTATUS.containing_type = _DATAPLANESTATE
_DATAPLANESTATE.fields_by_name['switch'].message_type = _DATAPLANESTATE_SWITCH
_DATAPLANESTATE.fields_by_name['stack'].message_type = _DATAPLANESTATE_STACK
_DATAPLANESTATE.fields_by_name['egress'].message_type = _DATAPLANESTATE_EGRESS
DESCRIPTOR.message_types_by_name['DataplaneState'] = _DATAPLANESTATE

DataplaneState = _reflection.GeneratedProtocolMessageType('DataplaneState', (_message.Message,), dict(

  Switch = _reflection.GeneratedProtocolMessageType('Switch', (_message.Message,), dict(

    SwitchesEntry = _reflection.GeneratedProtocolMessageType('SwitchesEntry', (_message.Message,), dict(
      DESCRIPTOR = _DATAPLANESTATE_SWITCH_SWITCHESENTRY,
      __module__ = 'forch.proto.dataplane_state_pb2'
      # @@protoc_insertion_point(class_scope:DataplaneState.Switch.SwitchesEntry)
      ))
    ,
    DESCRIPTOR = _DATAPLANESTATE_SWITCH,
    __module__ = 'forch.proto.dataplane_state_pb2'
    # @@protoc_insertion_point(class_scope:DataplaneState.Switch)
    ))
  ,

  Stack = _reflection.GeneratedProtocolMessageType('Stack', (_message.Message,), dict(

    LinksEntry = _reflection.GeneratedProtocolMessageType('LinksEntry', (_message.Message,), dict(
      DESCRIPTOR = _DATAPLANESTATE_STACK_LINKSENTRY,
      __module__ = 'forch.proto.dataplane_state_pb2'
      # @@protoc_insertion_point(class_scope:DataplaneState.Stack.LinksEntry)
      ))
    ,
    DESCRIPTOR = _DATAPLANESTATE_STACK,
    __module__ = 'forch.proto.dataplane_state_pb2'
    # @@protoc_insertion_point(class_scope:DataplaneState.Stack)
    ))
  ,

  Egress = _reflection.GeneratedProtocolMessageType('Egress', (_message.Message,), dict(
    DESCRIPTOR = _DATAPLANESTATE_EGRESS,
    __module__ = 'forch.proto.dataplane_state_pb2'
    # @@protoc_insertion_point(class_scope:DataplaneState.Egress)
    ))
  ,

  SwitchStatus = _reflection.GeneratedProtocolMessageType('SwitchStatus', (_message.Message,), dict(
    DESCRIPTOR = _DATAPLANESTATE_SWITCHSTATUS,
    __module__ = 'forch.proto.dataplane_state_pb2'
    # @@protoc_insertion_point(class_scope:DataplaneState.SwitchStatus)
    ))
  ,

  StackLinkStatus = _reflection.GeneratedProtocolMessageType('StackLinkStatus', (_message.Message,), dict(
    DESCRIPTOR = _DATAPLANESTATE_STACKLINKSTATUS,
    __module__ = 'forch.proto.dataplane_state_pb2'
    # @@protoc_insertion_point(class_scope:DataplaneState.StackLinkStatus)
    ))
  ,
  DESCRIPTOR = _DATAPLANESTATE,
  __module__ = 'forch.proto.dataplane_state_pb2'
  # @@protoc_insertion_point(class_scope:DataplaneState)
  ))
_sym_db.RegisterMessage(DataplaneState)
_sym_db.RegisterMessage(DataplaneState.Switch)
_sym_db.RegisterMessage(DataplaneState.Switch.SwitchesEntry)
_sym_db.RegisterMessage(DataplaneState.Stack)
_sym_db.RegisterMessage(DataplaneState.Stack.LinksEntry)
_sym_db.RegisterMessage(DataplaneState.Egress)
_sym_db.RegisterMessage(DataplaneState.SwitchStatus)
_sym_db.RegisterMessage(DataplaneState.StackLinkStatus)


_DATAPLANESTATE_SWITCH_SWITCHESENTRY.has_options = True
_DATAPLANESTATE_SWITCH_SWITCHESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_DATAPLANESTATE_STACK_LINKSENTRY.has_options = True
_DATAPLANESTATE_STACK_LINKSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
