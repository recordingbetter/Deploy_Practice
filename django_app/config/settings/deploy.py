from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

DEBUG = False
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

print('@@@@@@@ DEBUG:', DEBUG)
print('@@@@@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)
