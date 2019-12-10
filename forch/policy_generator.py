"""Core orchestrator"""

import logging

LOGGER = logging.getLogger('orchestrator')


class PolicyGenerator:
    """Class to handle AAA and generate corresponding polices"""
    def __init__(self):
        self._learned_macs = {}

    def process_port_learn(self, timestamp, switch, port, mac, src_ip):
        """Process MAC learning events"""
        LOGGER.debug('Learned MAC address %s on switch %s port %s with IP %s',
                     mac, switch, port, src_ip)
        mac_map = self._learned_macs.setdefault(mac)
        mac_map[switch] = port
        mac_map['ip'] = src_ip

    def _make_role_based_acl(self, mac, action):
        LOGGER.debug('Generating ACL for MAC %s with action %s', mac, action)
        self._learned_macs[mac]['action'] = action