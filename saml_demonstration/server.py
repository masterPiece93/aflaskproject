# server
from collections import namedtuple
from typing import Iterable
from app import create_app

def get_server_config_map(keys: Iterable):
    ConfigMap: dict = dict.fromkeys(keys)
    entry = namedtuple('entries', 'config_name, served_on')
    ConfigMap['local'] = entry('LocalConfig', ('localhost',5000))
    ConfigMap['dev'] = entry('DevelopmentConfig', ('some.ip.address.value',5000)),
    ConfigMap['prod'] = entry('ProductionConfig', ('some.ip.address.value',5000)),
    ConfigMap['test'] = entry('TestingConfig', ('some.ip.address.value',5000))
    return ConfigMap
def run_server():
    from commandline import parser, __env_choices__
    ConfigMap: dict = get_server_config_map(__env_choices__)
    args = parser.parse_args()
    server = ConfigMap[args.environment]
    app = create_app(f'config.{server.config_name}')
    app.run(*server.served_on)
if __name__ == '__main__':
    run_server()