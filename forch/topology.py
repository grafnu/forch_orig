"""Module for managing orchestrator device topologies"""

import logging
import os

from forch.forchestrator import configure_logging

from forch.utils import yaml_proto

from forch.proto.device_spec_pb2 import DeviceSpec

LOGGER = logging.getLogger('topology')

def load_devices():
    """Load a device specification file"""
    base_dir_name = os.getenv('FORCH_CONFIG_DIR')
    device_spec_file_name = os.path.join(base_dir_name, 'device_spec.yaml')
    LOGGER.info('Loading device spec file %s', device_spec_file_name)
    device_spec = yaml_proto(device_spec_file_name, DeviceSpec)
    loaded_macs = list(device_spec.mac_addrs.keys())
    loaded_macs.sort()
    LOGGER.info('Loaded device spec for devices: %s', loaded_macs)
    print(loaded_macs)

if __name__ == '__main__':
    configure_logging()
    load_devices()
