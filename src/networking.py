import netifaces

def get_default_gateway():
    gws = netifaces.gateways()
    gateway_ip = gws['default'][netifaces.AF_INET][0]
    return gateway_ip
