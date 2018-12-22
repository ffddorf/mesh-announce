import providers
import socket

class Source(providers.DataSource):
    def required_args(self):
        return ['hostname']

    def call(self, hostname):
        return hostname
