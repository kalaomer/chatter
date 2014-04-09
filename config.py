# Ayarlar

_config = {
    'HOST': '',
    'PORT': 8000,
    'LISTEN': 4,
    'MAX_PACKAGE_SIZE': 1024
}

def config(index = None):
    if index == None:
        return _config
    return _config[index]