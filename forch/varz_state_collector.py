"""Scrape varz from Faucet"""
import logging
import time

import prometheus_client.parser
import requests

LOGGER = logging.getLogger('vstate')


class VarzStateCollector:
    def __init__(self, endpoint, target_metrics):
        self._endpoint = endpoint
        self._target_metrics = target_metrics

    def _get_metrics(self):
        metric_map = {}

        response = requests.get(self._endpoint)
        if response.status_code == requests.status_codes.codes.ok: # pylint: disable=no-member
            content = response.content.decode('utf-8', 'strict')
            metrics = prometheus_client.parser.text_string_to_metric_families(content)
            for metric in metrics:
                if metric.name not in self._target_metrics:
                    continue
                metric_map[metric.name] = metric

        return metric_map

    def get_metrics(self, retries=3):
        """Get a list of target metrics"""
        for retry in range(retries):
            try:
                return self._get_metrics()
            except Exception as e:
                LOGGER.error('Cannot retrieve prometheus metrics: %s, retry: %d', e, retry)
                time.sleep(1)
        return None
