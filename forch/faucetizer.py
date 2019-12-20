"""Collect Faucet information and generate ACLs"""

import logging
import os
import sys

from forch.forchestrator import configure_logging
from forch.utils import proto_dict
from forch.utils import yaml_proto

from forch.proto.acl_rules_pb2 import AclRules

LOGGER = logging.getLogger('topology')


class Faucetizer:
    def __init__(self):
        self._rules = []

    def process_rules(self, rules):
        rules_dict = proto_dict(rules, True)
        self._rules = rules_dict.get('rules')
        for rule in self._rules:
            sys.stdout.write(str(rule))


def load_rules():
    """Load rules file"""
    base_dir_name = os.getenv('FORCH_CONFIG_DIR')
    rules_file = os.path.join(base_dir_name, 'acl_rules.yaml')
    LOGGER.info('Loading rules file %s', rules_file)
    rules = yaml_proto(rules_file, AclRules)
    LOGGER.info('Loaded %d acl rules', len(rules.rules))
    return rules


if __name__ == '__main__':
    configure_logging()
    faucetizer = Faucetizer()

    rule_samples = load_rules()
    faucetizer.process_rules(rule_samples)
