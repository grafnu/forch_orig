# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/system_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from forch.proto import shared_constants_pb2 as forch_dot_proto_dot_shared__constants__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='forch/proto/system_state.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1e\x66orch/proto/system_state.proto\x1a\"forch/proto/shared_constants.proto\"\xff\x03\n\x0bSystemState\x12\x11\n\tsite_name\x18\x01 \x01(\t\x12\x17\n\x0f\x63ontroller_name\x18\x02 \x01(\t\x12\x1b\n\x13peer_controller_url\x18\x03 \x01(\t\x12\"\n\x0csystem_state\x18\x04 \x01(\x0e\x32\x0c.State.State\x12\x1b\n\x13system_state_detail\x18\x05 \x01(\t\x12!\n\x19system_state_change_count\x18\x06 \x01(\x05\x12 \n\x18system_state_last_change\x18\x07 \x01(\t\x12 \n\x18system_state_last_update\x18\x08 \x01(\t\x12\x34\n\x0fsummary_sources\x18\t \x01(\x0b\x32\x1b.SystemState.SummarySources\x1a\xc8\x01\n\x0eSummarySources\x12 \n\tcpn_state\x18\x01 \x01(\x0b\x32\r.StateSummary\x12$\n\rprocess_state\x18\x02 \x01(\x0b\x32\r.StateSummary\x12&\n\x0f\x64\x61taplane_state\x18\x03 \x01(\x0b\x32\r.StateSummary\x12#\n\x0cswitch_state\x18\x04 \x01(\x0b\x32\r.StateSummary\x12!\n\nlist_hosts\x18\x05 \x01(\x0b\x32\r.StateSummary\"\xa2\x01\n\x0cStateSummary\x12\x1b\n\x05state\x18\x01 \x01(\x0e\x32\x0c.State.State\x12\x0e\n\x06\x64\x65tail\x18\x02 \x01(\t\x12\x14\n\x0c\x63hange_count\x18\x03 \x01(\x05\x12\x13\n\x0blast_update\x18\x04 \x01(\t\x12\x13\n\x0blast_change\x18\x05 \x01(\t\x12\x0b\n\x03url\x18\x06 \x01(\t\x12\x18\n\x10system_state_url\x18\x07 \x01(\tb\x06proto3')
  ,
  dependencies=[forch_dot_proto_dot_shared__constants__pb2.DESCRIPTOR,])




_SYSTEMSTATE_SUMMARYSOURCES = _descriptor.Descriptor(
  name='SummarySources',
  full_name='SystemState.SummarySources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpn_state', full_name='SystemState.SummarySources.cpn_state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='process_state', full_name='SystemState.SummarySources.process_state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataplane_state', full_name='SystemState.SummarySources.dataplane_state', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='switch_state', full_name='SystemState.SummarySources.switch_state', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list_hosts', full_name='SystemState.SummarySources.list_hosts', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=582,
)

_SYSTEMSTATE = _descriptor.Descriptor(
  name='SystemState',
  full_name='SystemState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='site_name', full_name='SystemState.site_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controller_name', full_name='SystemState.controller_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peer_controller_url', full_name='SystemState.peer_controller_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_state', full_name='SystemState.system_state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_state_detail', full_name='SystemState.system_state_detail', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_state_change_count', full_name='SystemState.system_state_change_count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_state_last_change', full_name='SystemState.system_state_last_change', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_state_last_update', full_name='SystemState.system_state_last_update', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='summary_sources', full_name='SystemState.summary_sources', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SYSTEMSTATE_SUMMARYSOURCES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=582,
)


_STATESUMMARY = _descriptor.Descriptor(
  name='StateSummary',
  full_name='StateSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='StateSummary.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detail', full_name='StateSummary.detail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='change_count', full_name='StateSummary.change_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_update', full_name='StateSummary.last_update', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_change', full_name='StateSummary.last_change', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='StateSummary.url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_state_url', full_name='StateSummary.system_state_url', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=585,
  serialized_end=747,
)

_SYSTEMSTATE_SUMMARYSOURCES.fields_by_name['cpn_state'].message_type = _STATESUMMARY
_SYSTEMSTATE_SUMMARYSOURCES.fields_by_name['process_state'].message_type = _STATESUMMARY
_SYSTEMSTATE_SUMMARYSOURCES.fields_by_name['dataplane_state'].message_type = _STATESUMMARY
_SYSTEMSTATE_SUMMARYSOURCES.fields_by_name['switch_state'].message_type = _STATESUMMARY
_SYSTEMSTATE_SUMMARYSOURCES.fields_by_name['list_hosts'].message_type = _STATESUMMARY
_SYSTEMSTATE_SUMMARYSOURCES.containing_type = _SYSTEMSTATE
_SYSTEMSTATE.fields_by_name['system_state'].enum_type = forch_dot_proto_dot_shared__constants__pb2._STATE_STATE
_SYSTEMSTATE.fields_by_name['summary_sources'].message_type = _SYSTEMSTATE_SUMMARYSOURCES
_STATESUMMARY.fields_by_name['state'].enum_type = forch_dot_proto_dot_shared__constants__pb2._STATE_STATE
DESCRIPTOR.message_types_by_name['SystemState'] = _SYSTEMSTATE
DESCRIPTOR.message_types_by_name['StateSummary'] = _STATESUMMARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SystemState = _reflection.GeneratedProtocolMessageType('SystemState', (_message.Message,), dict(

  SummarySources = _reflection.GeneratedProtocolMessageType('SummarySources', (_message.Message,), dict(
    DESCRIPTOR = _SYSTEMSTATE_SUMMARYSOURCES,
    __module__ = 'forch.proto.system_state_pb2'
    # @@protoc_insertion_point(class_scope:SystemState.SummarySources)
    ))
  ,
  DESCRIPTOR = _SYSTEMSTATE,
  __module__ = 'forch.proto.system_state_pb2'
  # @@protoc_insertion_point(class_scope:SystemState)
  ))
_sym_db.RegisterMessage(SystemState)
_sym_db.RegisterMessage(SystemState.SummarySources)

StateSummary = _reflection.GeneratedProtocolMessageType('StateSummary', (_message.Message,), dict(
  DESCRIPTOR = _STATESUMMARY,
  __module__ = 'forch.proto.system_state_pb2'
  # @@protoc_insertion_point(class_scope:StateSummary)
  ))
_sym_db.RegisterMessage(StateSummary)


# @@protoc_insertion_point(module_scope)
