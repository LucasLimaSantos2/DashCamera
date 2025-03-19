from app.config import ENDPOINTS
from app.utils import fetch_data

# Função para obter dados das licenças
def get_licenses():
    return fetch_data(ENDPOINTS["licenses"])

# Função para obter dados das câmeras
def get_cameras():
    return fetch_data(ENDPOINTS["cameras"])

# Função para obter status das câmeras
def get_camera_status():
    return fetch_data(ENDPOINTS["cameraStatus"])

# Função para obter dispositivos de I/O
def get_io_devices():
    return fetch_data(ENDPOINTS["ioDevices"])

# Função para obter status de dispositivos de I/O
def get_io_status():
    return fetch_data(ENDPOINTS["ioStatus"])

# Função para consolidar todos os dados
def get_all_data():
    return {
        "licenses": get_licenses(),
        "cameras": get_cameras(),
        "cameraStatus": get_camera_status(),
        "ioDevices": get_io_devices(),
        "ioStatus": get_io_status(),
    }
