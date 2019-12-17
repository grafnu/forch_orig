# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/switch_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from forch.proto import shared_constants_pb2 as forch_dot_proto_dot_shared__constants__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='forch/proto/switch_state.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x1e\x66orch/proto/switch_state.proto\x1a\"forch/proto/shared_constants.proto\"\xfe\x0c\n\x0bSwitchState\x12\"\n\x0cswitch_state\x18\x01 \x01(\x0e\x32\x0c.State.State\x12\x1b\n\x13switch_state_detail\x18\x02 \x01(\t\x12!\n\x19switch_state_change_count\x18\x03 \x01(\x05\x12 \n\x18switch_state_last_change\x18\x04 \x01(\t\x12\x18\n\x10system_state_url\x18\x05 \x01(\t\x12,\n\x08switches\x18\x06 \x03(\x0b\x32\x1a.SwitchState.SwitchesEntry\x12\x19\n\x11switches_restrict\x18\x07 \x01(\t\x1aH\n\rSwitchesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.SwitchState.SwitchNode:\x02\x38\x01\x1a\xef\x07\n\nSwitchNode\x12\x36\n\nattributes\x18\x01 \x01(\x0b\x32\".SwitchState.SwitchNode.Attributes\x12\"\n\x0cswitch_state\x18\x02 \x01(\x0e\x32\x0c.State.State\x12 \n\x18restart_type_event_count\x18\x03 \x01(\x05\x12\x14\n\x0crestart_type\x18\x04 \x01(\t\x12 \n\x18restart_type_last_change\x18\x05 \x01(\t\x12!\n\x19switch_state_change_count\x18\x06 \x01(\x05\x12 \n\x18switch_state_last_change\x18\x07 \x01(\t\x12\x31\n\x05ports\x18\x08 \x03(\x0b\x32\".SwitchState.SwitchNode.PortsEntry\x12\x16\n\x0eports_restrict\x18\t \x01(\x05\x12\x33\n\troot_path\x18\n \x03(\x0b\x32 .SwitchState.SwitchNode.NodePath\x12\x45\n\x10\x61\x63\x63\x65ss_port_macs\x18\x0b \x03(\x0b\x32+.SwitchState.SwitchNode.AccessPortMacsEntry\x12I\n\x12stacking_port_macs\x18\x0c \x03(\x0b\x32-.SwitchState.SwitchNode.StackingPortMacsEntry\x12\x45\n\x10\x65gress_port_macs\x18\r \x03(\x0b\x32+.SwitchState.SwitchNode.EgressPortMacsEntry\x1a?\n\nPortsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.SwitchState.Port:\x02\x38\x01\x1aL\n\x13\x41\x63\x63\x65ssPortMacsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.SwitchState.PortInfo:\x02\x38\x01\x1aN\n\x15StackingPortMacsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.SwitchState.PortInfo:\x02\x38\x01\x1aL\n\x13\x45gressPortMacsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.SwitchState.PortInfo:\x02\x38\x01\x1a\x1b\n\nAttributes\x12\r\n\x05\x64p_id\x18\x01 \x01(\x03\x1a\x43\n\x08NodePath\x12\x0e\n\x06switch\x18\x01 \x01(\t\x12\n\n\x02in\x18\x02 \x01(\x05\x12\x0b\n\x03out\x18\x03 \x01(\x05\x12\x0e\n\x06\x65gress\x18\x04 \x01(\x05\x1a\xfb\x01\n\x04Port\x12\x30\n\nattributes\x18\x01 \x01(\x0b\x32\x1c.SwitchState.Port.Attributes\x12 \n\nport_state\x18\x02 \x01(\x0e\x32\x0c.State.State\x12\x19\n\x11state_last_change\x18\x03 \x01(\t\x12\x1a\n\x12state_change_count\x18\x04 \x01(\x05\x1ah\n\nAttributes\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x11\n\tport_type\x18\x02 \x01(\t\x12\x19\n\x11stack_peer_switch\x18\x03 \x01(\t\x12\x17\n\x0fstack_peer_port\x18\x04 \x01(\x05\x1aL\n\x08PortInfo\x12\x0c\n\x04port\x18\x01 \x01(\x05\x12\x12\n\nip_address\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\tb\x06proto3')
  ,
  dependencies=[forch_dot_proto_dot_shared__constants__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SWITCHSTATE_SWITCHESENTRY = _descriptor.Descriptor(
  name='SwitchesEntry',
  full_name='SwitchState.SwitchesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SwitchState.SwitchesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='SwitchState.SwitchesEntry.value', index=1,
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
  serialized_start=319,
  serialized_end=391,
)

_SWITCHSTATE_SWITCHNODE_PORTSENTRY = _descriptor.Descriptor(
  name='PortsEntry',
  full_name='SwitchState.SwitchNode.PortsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SwitchState.SwitchNode.PortsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='SwitchState.SwitchNode.PortsEntry.value', index=1,
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
  serialized_start=1004,
  serialized_end=1067,
)

_SWITCHSTATE_SWITCHNODE_ACCESSPORTMACSENTRY = _descriptor.Descriptor(
  name='AccessPortMacsEntry',
  full_name='SwitchState.SwitchNode.AccessPortMacsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SwitchState.SwitchNode.AccessPortMacsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='SwitchState.SwitchNode.AccessPortMacsEntry.value', index=1,
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
  serialized_start=1069,
  serialized_end=1145,
)

_SWITCHSTATE_SWITCHNODE_STACKINGPORTMACSENTRY = _descriptor.Descriptor(
  name='StackingPortMacsEntry',
  full_name='SwitchState.SwitchNode.StackingPortMacsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SwitchState.SwitchNode.StackingPortMacsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='SwitchState.SwitchNode.StackingPortMacsEntry.value', index=1,
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
  serialized_start=1147,
  serialized_end=1225,
)

_SWITCHSTATE_SWITCHNODE_EGRESSPORTMACSENTRY = _descriptor.Descriptor(
  name='EgressPortMacsEntry',
  full_name='SwitchState.SwitchNode.EgressPortMacsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SwitchState.SwitchNode.EgressPortMacsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='SwitchState.SwitchNode.EgressPortMacsEntry.value', index=1,
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
  serialized_start=1227,
  serialized_end=1303,
)

_SWITCHSTATE_SWITCHNODE_ATTRIBUTES = _descriptor.Descriptor(
  name='Attributes',
  full_name='SwitchState.SwitchNode.Attributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dp_id', full_name='SwitchState.SwitchNode.Attributes.dp_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1305,
  serialized_end=1332,
)

_SWITCHSTATE_SWITCHNODE_NODEPATH = _descriptor.Descriptor(
  name='NodePath',
  full_name='SwitchState.SwitchNode.NodePath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='switch', full_name='SwitchState.SwitchNode.NodePath.switch', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in', full_name='SwitchState.SwitchNode.NodePath.in', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out', full_name='SwitchState.SwitchNode.NodePath.out', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egress', full_name='SwitchState.SwitchNode.NodePath.egress', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1334,
  serialized_end=1401,
)

_SWITCHSTATE_SWITCHNODE = _descriptor.Descriptor(
  name='SwitchNode',
  full_name='SwitchState.SwitchNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attributes', full_name='SwitchState.SwitchNode.attributes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='switch_state', full_name='SwitchState.SwitchNode.switch_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='restart_type_event_count', full_name='SwitchState.SwitchNode.restart_type_event_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='restart_type', full_name='SwitchState.SwitchNode.restart_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='restart_type_last_change', full_name='SwitchState.SwitchNode.restart_type_last_change', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='switch_state_change_count', full_name='SwitchState.SwitchNode.switch_state_change_count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='switch_state_last_change', full_name='SwitchState.SwitchNode.switch_state_last_change', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ports', full_name='SwitchState.SwitchNode.ports', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ports_restrict', full_name='SwitchState.SwitchNode.ports_restrict', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='root_path', full_name='SwitchState.SwitchNode.root_path', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='access_port_macs', full_name='SwitchState.SwitchNode.access_port_macs', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stacking_port_macs', full_name='SwitchState.SwitchNode.stacking_port_macs', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egress_port_macs', full_name='SwitchState.SwitchNode.egress_port_macs', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SWITCHSTATE_SWITCHNODE_PORTSENTRY, _SWITCHSTATE_SWITCHNODE_ACCESSPORTMACSENTRY, _SWITCHSTATE_SWITCHNODE_STACKINGPORTMACSENTRY, _SWITCHSTATE_SWITCHNODE_EGRESSPORTMACSENTRY, _SWITCHSTATE_SWITCHNODE_ATTRIBUTES, _SWITCHSTATE_SWITCHNODE_NODEPATH, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=1401,
)

_SWITCHSTATE_PORT_ATTRIBUTES = _descriptor.Descriptor(
  name='Attributes',
  full_name='SwitchState.Port.Attributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='SwitchState.Port.Attributes.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port_type', full_name='SwitchState.Port.Attributes.port_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stack_peer_switch', full_name='SwitchState.Port.Attributes.stack_peer_switch', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stack_peer_port', full_name='SwitchState.Port.Attributes.stack_peer_port', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1551,
  serialized_end=1655,
)

_SWITCHSTATE_PORT = _descriptor.Descriptor(
  name='Port',
  full_name='SwitchState.Port',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attributes', full_name='SwitchState.Port.attributes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port_state', full_name='SwitchState.Port.port_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state_last_change', full_name='SwitchState.Port.state_last_change', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state_change_count', full_name='SwitchState.Port.state_change_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SWITCHSTATE_PORT_ATTRIBUTES, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1404,
  serialized_end=1655,
)

_SWITCHSTATE_PORTINFO = _descriptor.Descriptor(
  name='PortInfo',
  full_name='SwitchState.PortInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='SwitchState.PortInfo.port', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip_address', full_name='SwitchState.PortInfo.ip_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='SwitchState.PortInfo.timestamp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='SwitchState.PortInfo.url', index=3,
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
  serialized_start=1657,
  serialized_end=1733,
)

_SWITCHSTATE = _descriptor.Descriptor(
  name='SwitchState',
  full_name='SwitchState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='switch_state', full_name='SwitchState.switch_state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='switch_state_detail', full_name='SwitchState.switch_state_detail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='switch_state_change_count', full_name='SwitchState.switch_state_change_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='switch_state_last_change', full_name='SwitchState.switch_state_last_change', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_state_url', full_name='SwitchState.system_state_url', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='switches', full_name='SwitchState.switches', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='switches_restrict', full_name='SwitchState.switches_restrict', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SWITCHSTATE_SWITCHESENTRY, _SWITCHSTATE_SWITCHNODE, _SWITCHSTATE_PORT, _SWITCHSTATE_PORTINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=1733,
)

_SWITCHSTATE_SWITCHESENTRY.fields_by_name['value'].message_type = _SWITCHSTATE_SWITCHNODE
_SWITCHSTATE_SWITCHESENTRY.containing_type = _SWITCHSTATE
_SWITCHSTATE_SWITCHNODE_PORTSENTRY.fields_by_name['value'].message_type = _SWITCHSTATE_PORT
_SWITCHSTATE_SWITCHNODE_PORTSENTRY.containing_type = _SWITCHSTATE_SWITCHNODE
_SWITCHSTATE_SWITCHNODE_ACCESSPORTMACSENTRY.fields_by_name['value'].message_type = _SWITCHSTATE_PORTINFO
_SWITCHSTATE_SWITCHNODE_ACCESSPORTMACSENTRY.containing_type = _SWITCHSTATE_SWITCHNODE
_SWITCHSTATE_SWITCHNODE_STACKINGPORTMACSENTRY.fields_by_name['value'].message_type = _SWITCHSTATE_PORTINFO
_SWITCHSTATE_SWITCHNODE_STACKINGPORTMACSENTRY.containing_type = _SWITCHSTATE_SWITCHNODE
_SWITCHSTATE_SWITCHNODE_EGRESSPORTMACSENTRY.fields_by_name['value'].message_type = _SWITCHSTATE_PORTINFO
_SWITCHSTATE_SWITCHNODE_EGRESSPORTMACSENTRY.containing_type = _SWITCHSTATE_SWITCHNODE
_SWITCHSTATE_SWITCHNODE_ATTRIBUTES.containing_type = _SWITCHSTATE_SWITCHNODE
_SWITCHSTATE_SWITCHNODE_NODEPATH.containing_type = _SWITCHSTATE_SWITCHNODE
_SWITCHSTATE_SWITCHNODE.fields_by_name['attributes'].message_type = _SWITCHSTATE_SWITCHNODE_ATTRIBUTES
_SWITCHSTATE_SWITCHNODE.fields_by_name['switch_state'].enum_type = forch_dot_proto_dot_shared__constants__pb2._STATE_STATE
_SWITCHSTATE_SWITCHNODE.fields_by_name['ports'].message_type = _SWITCHSTATE_SWITCHNODE_PORTSENTRY
_SWITCHSTATE_SWITCHNODE.fields_by_name['root_path'].message_type = _SWITCHSTATE_SWITCHNODE_NODEPATH
_SWITCHSTATE_SWITCHNODE.fields_by_name['access_port_macs'].message_type = _SWITCHSTATE_SWITCHNODE_ACCESSPORTMACSENTRY
_SWITCHSTATE_SWITCHNODE.fields_by_name['stacking_port_macs'].message_type = _SWITCHSTATE_SWITCHNODE_STACKINGPORTMACSENTRY
_SWITCHSTATE_SWITCHNODE.fields_by_name['egress_port_macs'].message_type = _SWITCHSTATE_SWITCHNODE_EGRESSPORTMACSENTRY
_SWITCHSTATE_SWITCHNODE.containing_type = _SWITCHSTATE
_SWITCHSTATE_PORT_ATTRIBUTES.containing_type = _SWITCHSTATE_PORT
_SWITCHSTATE_PORT.fields_by_name['attributes'].message_type = _SWITCHSTATE_PORT_ATTRIBUTES
_SWITCHSTATE_PORT.fields_by_name['port_state'].enum_type = forch_dot_proto_dot_shared__constants__pb2._STATE_STATE
_SWITCHSTATE_PORT.containing_type = _SWITCHSTATE
_SWITCHSTATE_PORTINFO.containing_type = _SWITCHSTATE
_SWITCHSTATE.fields_by_name['switch_state'].enum_type = forch_dot_proto_dot_shared__constants__pb2._STATE_STATE
_SWITCHSTATE.fields_by_name['switches'].message_type = _SWITCHSTATE_SWITCHESENTRY
DESCRIPTOR.message_types_by_name['SwitchState'] = _SWITCHSTATE

SwitchState = _reflection.GeneratedProtocolMessageType('SwitchState', (_message.Message,), dict(

  SwitchesEntry = _reflection.GeneratedProtocolMessageType('SwitchesEntry', (_message.Message,), dict(
    DESCRIPTOR = _SWITCHSTATE_SWITCHESENTRY,
    __module__ = 'forch.proto.switch_state_pb2'
    # @@protoc_insertion_point(class_scope:SwitchState.SwitchesEntry)
    ))
  ,

  SwitchNode = _reflection.GeneratedProtocolMessageType('SwitchNode', (_message.Message,), dict(

    PortsEntry = _reflection.GeneratedProtocolMessageType('PortsEntry', (_message.Message,), dict(
      DESCRIPTOR = _SWITCHSTATE_SWITCHNODE_PORTSENTRY,
      __module__ = 'forch.proto.switch_state_pb2'
      # @@protoc_insertion_point(class_scope:SwitchState.SwitchNode.PortsEntry)
      ))
    ,

    AccessPortMacsEntry = _reflection.GeneratedProtocolMessageType('AccessPortMacsEntry', (_message.Message,), dict(
      DESCRIPTOR = _SWITCHSTATE_SWITCHNODE_ACCESSPORTMACSENTRY,
      __module__ = 'forch.proto.switch_state_pb2'
      # @@protoc_insertion_point(class_scope:SwitchState.SwitchNode.AccessPortMacsEntry)
      ))
    ,

    StackingPortMacsEntry = _reflection.GeneratedProtocolMessageType('StackingPortMacsEntry', (_message.Message,), dict(
      DESCRIPTOR = _SWITCHSTATE_SWITCHNODE_STACKINGPORTMACSENTRY,
      __module__ = 'forch.proto.switch_state_pb2'
      # @@protoc_insertion_point(class_scope:SwitchState.SwitchNode.StackingPortMacsEntry)
      ))
    ,

    EgressPortMacsEntry = _reflection.GeneratedProtocolMessageType('EgressPortMacsEntry', (_message.Message,), dict(
      DESCRIPTOR = _SWITCHSTATE_SWITCHNODE_EGRESSPORTMACSENTRY,
      __module__ = 'forch.proto.switch_state_pb2'
      # @@protoc_insertion_point(class_scope:SwitchState.SwitchNode.EgressPortMacsEntry)
      ))
    ,

    Attributes = _reflection.GeneratedProtocolMessageType('Attributes', (_message.Message,), dict(
      DESCRIPTOR = _SWITCHSTATE_SWITCHNODE_ATTRIBUTES,
      __module__ = 'forch.proto.switch_state_pb2'
      # @@protoc_insertion_point(class_scope:SwitchState.SwitchNode.Attributes)
      ))
    ,

    NodePath = _reflection.GeneratedProtocolMessageType('NodePath', (_message.Message,), dict(
      DESCRIPTOR = _SWITCHSTATE_SWITCHNODE_NODEPATH,
      __module__ = 'forch.proto.switch_state_pb2'
      # @@protoc_insertion_point(class_scope:SwitchState.SwitchNode.NodePath)
      ))
    ,
    DESCRIPTOR = _SWITCHSTATE_SWITCHNODE,
    __module__ = 'forch.proto.switch_state_pb2'
    # @@protoc_insertion_point(class_scope:SwitchState.SwitchNode)
    ))
  ,

  Port = _reflection.GeneratedProtocolMessageType('Port', (_message.Message,), dict(

    Attributes = _reflection.GeneratedProtocolMessageType('Attributes', (_message.Message,), dict(
      DESCRIPTOR = _SWITCHSTATE_PORT_ATTRIBUTES,
      __module__ = 'forch.proto.switch_state_pb2'
      # @@protoc_insertion_point(class_scope:SwitchState.Port.Attributes)
      ))
    ,
    DESCRIPTOR = _SWITCHSTATE_PORT,
    __module__ = 'forch.proto.switch_state_pb2'
    # @@protoc_insertion_point(class_scope:SwitchState.Port)
    ))
  ,

  PortInfo = _reflection.GeneratedProtocolMessageType('PortInfo', (_message.Message,), dict(
    DESCRIPTOR = _SWITCHSTATE_PORTINFO,
    __module__ = 'forch.proto.switch_state_pb2'
    # @@protoc_insertion_point(class_scope:SwitchState.PortInfo)
    ))
  ,
  DESCRIPTOR = _SWITCHSTATE,
  __module__ = 'forch.proto.switch_state_pb2'
  # @@protoc_insertion_point(class_scope:SwitchState)
  ))
_sym_db.RegisterMessage(SwitchState)
_sym_db.RegisterMessage(SwitchState.SwitchesEntry)
_sym_db.RegisterMessage(SwitchState.SwitchNode)
_sym_db.RegisterMessage(SwitchState.SwitchNode.PortsEntry)
_sym_db.RegisterMessage(SwitchState.SwitchNode.AccessPortMacsEntry)
_sym_db.RegisterMessage(SwitchState.SwitchNode.StackingPortMacsEntry)
_sym_db.RegisterMessage(SwitchState.SwitchNode.EgressPortMacsEntry)
_sym_db.RegisterMessage(SwitchState.SwitchNode.Attributes)
_sym_db.RegisterMessage(SwitchState.SwitchNode.NodePath)
_sym_db.RegisterMessage(SwitchState.Port)
_sym_db.RegisterMessage(SwitchState.Port.Attributes)
_sym_db.RegisterMessage(SwitchState.PortInfo)


_SWITCHSTATE_SWITCHESENTRY.has_options = True
_SWITCHSTATE_SWITCHESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_SWITCHSTATE_SWITCHNODE_PORTSENTRY.has_options = True
_SWITCHSTATE_SWITCHNODE_PORTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_SWITCHSTATE_SWITCHNODE_ACCESSPORTMACSENTRY.has_options = True
_SWITCHSTATE_SWITCHNODE_ACCESSPORTMACSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_SWITCHSTATE_SWITCHNODE_STACKINGPORTMACSENTRY.has_options = True
_SWITCHSTATE_SWITCHNODE_STACKINGPORTMACSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_SWITCHSTATE_SWITCHNODE_EGRESSPORTMACSENTRY.has_options = True
_SWITCHSTATE_SWITCHNODE_EGRESSPORTMACSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
