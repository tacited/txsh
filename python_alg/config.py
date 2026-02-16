"""
Configuration for Python algorithm service: OSS credentials and model paths.
"""
import os
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent

# ----- OSS (Aliyun) -----
OSS_ACCESS_KEY_ID = os.getenv("OSS_ACCESS_KEY_ID")
OSS_ACCESS_KEY_SECRET = os.getenv("OSS_ACCESS_KEY_SECRET")
OSS_ENDPOINT = os.getenv("OSS_ENDPOINT", "oss-cn-chengdu.aliyuncs.com")
OSS_BUCKET_NAME = os.getenv("OSS_BUCKET_NAME", "tacited-waimai")

# ----- YOLO Model -----
# Canonical models directory (put all your *.pt here)
MODELS_DIR = Path(os.getenv("YOLO_MODELS_DIR", str(BASE_DIR / "models")))
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# Default model file path (can be overridden by env)
MODEL_PATH = os.getenv("YOLO_MODEL_PATH", str(MODELS_DIR / "yolo11n.pt"))
# Fallback: use Ultralytics built-in model name if local file missing
MODEL_FALLBACK = os.getenv("YOLO_MODEL_FALLBACK", "yolo11n.pt")

# ----- Detection thresholds (for head tilt / close distance) -----
# Distance estimation: Real width of object in cm and Focal length
REAL_FACE_WIDTH_CM = float(os.getenv("REAL_FACE_WIDTH_CM", "15"))
REAL_PERSON_WIDTH_CM = float(os.getenv("REAL_PERSON_WIDTH_CM", "45"))
FOCAL_LENGTH = float(os.getenv("FOCAL_LENGTH", "600"))

# Head tilt: ratio of box height to width; if aspect ratio suggests tilted head
HEAD_TILT_ASPECT_RATIO_MIN = float(os.getenv("HEAD_TILT_ASPECT_RATIO_MIN", "0.8"))
HEAD_TILT_ASPECT_RATIO_MAX = float(os.getenv("HEAD_TILT_ASPECT_RATIO_MAX", "1.4"))
# Close distance: face box area relative to image area (larger = closer)
CLOSE_DISTANCE_AREA_RATIO_THRESHOLD = float(os.getenv("CLOSE_DISTANCE_AREA_RATIO_THRESHOLD", "0.25"))

# ----- Temp dir for downloaded/processed files -----
TEMP_DIR = BASE_DIR / "tmp"
TEMP_DIR.mkdir(exist_ok=True)
