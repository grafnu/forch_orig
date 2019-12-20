"""Collect Faucet information and generate ACLs"""

import logging
import os
import sys

from forch.forchestrator import configure_logging
from forch.utils import proto_dict
from forch.utils import yaml_proto

from forch.proto.acl_rules_pb2 import AclRules
from forch.proto.match_rules_pb2 import MatchRules

LOGGER = logging.getLogger('topology')


class Faucetizer:
    """Collect Faucet information and generate ACLs"""
    def __init__(self):
        self._acl_rules = []
        self._match_rules = {}

    def process_acl_rules(self, rules):
        """Process ACL rules inputs and generate concrete ACLs"""
        rules_dict = proto_dict(rules, True)
        self._acl_rules = rules_dict.get('rules')
        for rule in self._acl_rules:
            sys.stdout.write(f'{rule}\n')

    def process_match_rules(self, rules):
        """Process match rules inputs"""
        rules_dict = proto_dict(rules, True)
        self._match_rules = rules_dict.get('rules')
        for rule_name, rule in sorted(self._match_rules.items()):
            eth_types = [m.get('eth_type') for m in rule.get('matches', [])]
            sys.stdout.write(f'{rule_name}: {eth_types}\n')


def load_acl_rules(base_dir_name):
    """Load acl rules file"""
    rules_file = os.path.join(base_dir_name, 'acl_rules.yaml')
    LOGGER.info('Loading acl rules file %s', rules_file)
    rules = yaml_proto(rules_file, AclRules)
    LOGGER.info('Loaded %d acl rules', len(rules.rules))
    return rules


def load_match_rules(base_dir_name):
    """Load match rules file"""
    rules_file = os.path.join(base_dir_name, 'match_rules.yaml')
    LOGGER.info('Loading match rules file %s', rules_file)
    rules = yaml_proto(rules_file, MatchRules)
    LOGGER.info('Loaded %d match rules', len(rules.rules))
    return rules


if __name__ == '__main__':
    configure_logging()
    FAUCETIZER = Faucetizer()

    BASE_DIR = os.getenv('FORCH_CONFIG_DIR')

    ACL_RULE_SAMPLES = load_acl_rules(BASE_DIR)
    FAUCETIZER.process_acl_rules(ACL_RULE_SAMPLES)

    MATCH_RULE_SAMPLES = load_match_rules(BASE_DIR)
    FAUCETIZER.process_match_rules(MATCH_RULE_SAMPLES)
