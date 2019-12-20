"""Module for authenticating devices connecting to a faucet network"""

import logging
import sys
import os
import yaml

from forch.forchestrator import configure_logging
from forch.utils import proto_dict, dict_proto

from forch.proto.auth_result_pb2 import AuthResult

LOGGER = logging.getLogger('authenticator')
AUTH_FILE_NAME = 'auth.yaml'

class Authenticator:
    """Authenticate devices using MAB/dot1x"""
    def __init__(self):
        self.auth_map = self._get_auth_map()

    def _get_auth_map(self):
        base_dir = os.getenv('FORCH_CONFIG_DIR')
        auth_file = os.path.join(base_dir, AUTH_FILE_NAME)
        auth_map = None
        with open(auth_file, 'r') as stream:
            try:
                auth_map = yaml.safe_load(stream).get('auth_map')
            except yaml.YAMLError as exc:
                LOGGER.error("Error loading yaml file: %s", exc, exc_info=True)
        return auth_map

    def authenticate(self, auth_id):
        """Returns role and segment for given auth_id"""
        auth_result = {}
        if auth_id in self.auth_map:
            auth_result = self.auth_map.get(auth_id)
        else:
            auth_result = self.auth_map.get('default')
        auth_result['auth_id'] = auth_id
        return dict_proto(auth_result, AuthResult)

    def print_auth_result(self, auth_result):
        """Prints AuthResult object to out"""
        sys.stdout.write(str(proto_dict(auth_result)) + '\n')


if __name__=='__main__':
    configure_logging()
    AUTHENTICATOR = Authenticator()
    mac_list = ["9a:02:57:1e:8f:01", "9a:02:57:1e:8f:02", "9a:02:57:1e:8f:03"]
    for mac in mac_list:
        result = AUTHENTICATOR.authenticate(mac)
        AUTHENTICATOR.print_auth_result(result)
