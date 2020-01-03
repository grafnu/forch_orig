# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/network_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='forch/proto/network_state.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1f\x66orch/proto/network_state.proto\"\xa2\x02\n\x0cNetworkState\x12=\n\x11named_match_rules\x18\x01 \x03(\x0b\x32\".NetworkState.NamedMatchRulesEntry\x12\x43\n\x14\x64\x65vice_mac_behaviors\x18\x02 \x03(\x0b\x32%.NetworkState.DeviceMacBehaviorsEntry\x1a\x42\n\x14NamedMatchRulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.MatchRule:\x02\x38\x01\x1aJ\n\x17\x44\x65viceMacBehaviorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.DeviceBehavior:\x02\x38\x01\"1\n\x0e\x44\x65viceBehavior\x12\x0b\n\x03vid\x18\x01 \x01(\x05\x12\x12\n\nrule_names\x18\x02 \x03(\t\"\xb6\x01\n\tMatchRule\x12\x10\n\x08\x65th_type\x18\x01 \x01(\x05\x12\x0f\n\x07\x65th_dst\x18\x03 \x01(\t\x12\x10\n\x08ip_proto\x18\x04 \x01(\x05\x12\x0e\n\x06ip_dst\x18\x06 \x01(\t\x12\x10\n\x08src_port\x18\x07 \x01(\x05\x12\x10\n\x08\x64st_port\x18\x08 \x01(\x05\x12!\n\x06\x61\x63tion\x18\t \x01(\x0e\x32\x11.MatchRule.Action\"\x1d\n\x06\x41\x63tion\x12\x08\n\x04\x44\x45NY\x10\x00\x12\t\n\x05\x41LLOW\x10\x01\x62\x06proto3')
)



_MATCHRULE_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='MatchRule.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DENY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALLOW', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=533,
  serialized_end=562,
)
_sym_db.RegisterEnumDescriptor(_MATCHRULE_ACTION)


_NETWORKSTATE_NAMEDMATCHRULESENTRY = _descriptor.Descriptor(
  name='NamedMatchRulesEntry',
  full_name='NetworkState.NamedMatchRulesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='NetworkState.NamedMatchRulesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='NetworkState.NamedMatchRulesEntry.value', index=1,
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
  serialized_start=184,
  serialized_end=250,
)

_NETWORKSTATE_DEVICEMACBEHAVIORSENTRY = _descriptor.Descriptor(
  name='DeviceMacBehaviorsEntry',
  full_name='NetworkState.DeviceMacBehaviorsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='NetworkState.DeviceMacBehaviorsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='NetworkState.DeviceMacBehaviorsEntry.value', index=1,
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
  serialized_start=252,
  serialized_end=326,
)

_NETWORKSTATE = _descriptor.Descriptor(
  name='NetworkState',
  full_name='NetworkState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='named_match_rules', full_name='NetworkState.named_match_rules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_mac_behaviors', full_name='NetworkState.device_mac_behaviors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NETWORKSTATE_NAMEDMATCHRULESENTRY, _NETWORKSTATE_DEVICEMACBEHAVIORSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=326,
)


_DEVICEBEHAVIOR = _descriptor.Descriptor(
  name='DeviceBehavior',
  full_name='DeviceBehavior',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vid', full_name='DeviceBehavior.vid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule_names', full_name='DeviceBehavior.rule_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=328,
  serialized_end=377,
)


_MATCHRULE = _descriptor.Descriptor(
  name='MatchRule',
  full_name='MatchRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='eth_type', full_name='MatchRule.eth_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eth_dst', full_name='MatchRule.eth_dst', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_proto', full_name='MatchRule.ip_proto', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_dst', full_name='MatchRule.ip_dst', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_port', full_name='MatchRule.src_port', index=4,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst_port', full_name='MatchRule.dst_port', index=5,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='MatchRule.action', index=6,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MATCHRULE_ACTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=562,
)

_NETWORKSTATE_NAMEDMATCHRULESENTRY.fields_by_name['value'].message_type = _MATCHRULE
_NETWORKSTATE_NAMEDMATCHRULESENTRY.containing_type = _NETWORKSTATE
_NETWORKSTATE_DEVICEMACBEHAVIORSENTRY.fields_by_name['value'].message_type = _DEVICEBEHAVIOR
_NETWORKSTATE_DEVICEMACBEHAVIORSENTRY.containing_type = _NETWORKSTATE
_NETWORKSTATE.fields_by_name['named_match_rules'].message_type = _NETWORKSTATE_NAMEDMATCHRULESENTRY
_NETWORKSTATE.fields_by_name['device_mac_behaviors'].message_type = _NETWORKSTATE_DEVICEMACBEHAVIORSENTRY
_MATCHRULE.fields_by_name['action'].enum_type = _MATCHRULE_ACTION
_MATCHRULE_ACTION.containing_type = _MATCHRULE
DESCRIPTOR.message_types_by_name['NetworkState'] = _NETWORKSTATE
DESCRIPTOR.message_types_by_name['DeviceBehavior'] = _DEVICEBEHAVIOR
DESCRIPTOR.message_types_by_name['MatchRule'] = _MATCHRULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NetworkState = _reflection.GeneratedProtocolMessageType('NetworkState', (_message.Message,), dict(

  NamedMatchRulesEntry = _reflection.GeneratedProtocolMessageType('NamedMatchRulesEntry', (_message.Message,), dict(
    DESCRIPTOR = _NETWORKSTATE_NAMEDMATCHRULESENTRY,
    __module__ = 'forch.proto.network_state_pb2'
    # @@protoc_insertion_point(class_scope:NetworkState.NamedMatchRulesEntry)
    ))
  ,

  DeviceMacBehaviorsEntry = _reflection.GeneratedProtocolMessageType('DeviceMacBehaviorsEntry', (_message.Message,), dict(
    DESCRIPTOR = _NETWORKSTATE_DEVICEMACBEHAVIORSENTRY,
    __module__ = 'forch.proto.network_state_pb2'
    # @@protoc_insertion_point(class_scope:NetworkState.DeviceMacBehaviorsEntry)
    ))
  ,
  DESCRIPTOR = _NETWORKSTATE,
  __module__ = 'forch.proto.network_state_pb2'
  # @@protoc_insertion_point(class_scope:NetworkState)
  ))
_sym_db.RegisterMessage(NetworkState)
_sym_db.RegisterMessage(NetworkState.NamedMatchRulesEntry)
_sym_db.RegisterMessage(NetworkState.DeviceMacBehaviorsEntry)

DeviceBehavior = _reflection.GeneratedProtocolMessageType('DeviceBehavior', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEBEHAVIOR,
  __module__ = 'forch.proto.network_state_pb2'
  # @@protoc_insertion_point(class_scope:DeviceBehavior)
  ))
_sym_db.RegisterMessage(DeviceBehavior)

MatchRule = _reflection.GeneratedProtocolMessageType('MatchRule', (_message.Message,), dict(
  DESCRIPTOR = _MATCHRULE,
  __module__ = 'forch.proto.network_state_pb2'
  # @@protoc_insertion_point(class_scope:MatchRule)
  ))
_sym_db.RegisterMessage(MatchRule)


_NETWORKSTATE_NAMEDMATCHRULESENTRY._options = None
_NETWORKSTATE_DEVICEMACBEHAVIORSENTRY._options = None
# @@protoc_insertion_point(module_scope)
