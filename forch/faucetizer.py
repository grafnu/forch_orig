"""Collect Faucet information and generate ACLs"""

import logging
import os
import sys
import yaml

from forch.forchestrator import configure_logging
from forch.utils import dict_proto
from forch.utils import proto_dict

from forch.proto.acl_rule_pb2 import AclRule
from forch.proto.match_rule_pb2 import MatchRule

LOGGER = logging.getLogger('topology')


class Faucetizer:
    """Collect Faucet information and generate ACLs"""
    def __init__(self):
        self._acl_rules = {}
        self._match_rules = {}

    def process_acl_rule(self, rule):
        """Process ACL rules inputs and generate concrete ACLs"""
        eth_src = rule.eth_src
        eth_dst = rule.eth_dst
        action_rules = rule.action_rules
        sys.stdout.write(f'{eth_src}, {eth_src}\n')
        sys.stdout.write(f'{action_rules}\n')

    def process_match_rule(self, rule_name, rule):
        """Process match rules inputs"""
        rule_dict = proto_dict(rule, True)
        self._match_rules[rule_name] = rule_dict
        sys.stdout.write(f'{rule_name}: {rule_dict.get("eth_type")}\n')


def load_acl_rules(base_dir_name):
    """Load acl rules file"""
    rules_file = os.path.join(base_dir_name, 'acl_rules.yaml')
    LOGGER.info('Loading acl rules file %s', rules_file)

    with open(rules_file) as file:
        rules = yaml.safe_load(file)

    LOGGER.info('Loaded %d acl rules', len(rules.get('rules', {})))
    return rules.get('rules', [])


def load_match_rules(base_dir_name):
    """Load match rules file"""
    rules_file = os.path.join(base_dir_name, 'match_rules.yaml')
    LOGGER.info('Loading match rules file %s', rules_file)

    with open(rules_file) as file:
        rules = yaml.safe_load(file)

    LOGGER.info('Loaded %d match rules', len(rules.get('rules', {})))
    return rules.get('rules', {})


if __name__ == '__main__':
    configure_logging()
    FAUCETIZER = Faucetizer()

    BASE_DIR = os.getenv('FORCH_CONFIG_DIR')

    ACL_RULE_SAMPLES = load_acl_rules(BASE_DIR)
    for rule in ACL_RULE_SAMPLES:
        FAUCETIZER.process_acl_rule(dict_proto(rule, AclRule))

    MATCH_RULE_SAMPLES = load_match_rules(BASE_DIR)
    for rule_name, rule in MATCH_RULE_SAMPLES:
        FAUCETIZER.process_match_rule(rule_name, dict_proto(rule, MatchRule))
