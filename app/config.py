import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

SERVER_IP = os.getenv("SERVER_IP", "localhost")
USER = os.getenv("USER", "admin")
PASS = os.getenv("PASS", "@480U753c#")
CAMERA_USER = os.getenv("CAMERA_USER", "admin")
CAMERA_PASS = os.getenv("CAMERA_PASS", "480u753c")

ENDPOINTS = {
    "licenses": f"http://{SERVER_IP}:8601/Interface/Server/GetLicenses?ResponseFormat=json&AuthUser={USER}&AuthPass={PASS}",
    "cameras": f"http://{SERVER_IP}:8601/Interface/Cameras/GetCameras?ResponseFormat=json&AuthUser={CAMERA_USER}&AuthPass={CAMERA_PASS}",
    "cameraStatus": f"http://{SERVER_IP}:8601/Interface/Cameras/GetStatus?ResponseFormat=json&AuthUser={CAMERA_USER}&AuthPass={CAMERA_PASS}",
    "ioDevices": f"http://{SERVER_IP}:8601/Interface/IODevices/GetIODevices?ResponseFormat=json&AuthUser={USER}&AuthPass={PASS}",
    "ioStatus": f"http://{SERVER_IP}:8601/Interface/IODevices/GetStatus?ResponseFormat=json&AuthUser={USER}&AuthPass={PASS}",
}
