"""Collect Faucet information and generate ACLs"""

import logging
import os
import sys

from forch.forchestrator import configure_logging
from forch.utils import proto_dict
from forch.utils import yaml_proto

from forch.proto.network_state_pb2 import NetworkState

LOGGER = logging.getLogger('topology')


class Faucetizer:
    """Collect Faucet information and generate ACLs"""
    def __init__(self):
        self._network_state = {}

    def process_network_state(self, network_state):
        """Process network state inputs"""
        self._network_state = proto_dict(network_state, True)
        for eth_src, behavior in self._network_state.get('device_behaviors', {}).items():
            sys.stdout.write(f'{eth_src}: {behavior["vid"]}\n')
            sys.stdout.write(f'{behavior["matches"]}\n')


def load_network_state(base_dir_name):
    """Load network state file"""
    file = os.path.join(base_dir_name, 'network_state.yaml')
    LOGGER.info('Loading network state file %s', file)
    network_state = yaml_proto(file, NetworkState)
    LOGGER.info('Loaded %d devices', len(network_state.device_behaviors))
    return network_state


if __name__ == '__main__':
    configure_logging()
    FAUCETIZER = Faucetizer()

    BASE_DIR = os.getenv('FORCH_CONFIG_DIR')
    NETWORK_STATE_SAMPLES = load_network_state(BASE_DIR)
    FAUCETIZER.process_network_state(NETWORK_STATE_SAMPLES)
