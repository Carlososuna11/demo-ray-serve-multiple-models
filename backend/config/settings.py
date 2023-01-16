import os
from pathlib import Path
from backend_base.utils.environment import get_env
from backend_base.utils.string import bool_from_str

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = bool_from_str(get_env('DEBUG', 't'))

PROJECT_NAME = get_env('PROJECT_NAME', 'DEMO MULTIPLE MODEL SERVING')
PROJECT_DESCRIPTION = get_env('PROJECT_DESCRIPTION', '')
PROJECT_VERSION = get_env('PROJECT_VERSION', '0.1.0')

RAY_ADDRESS = get_env(
    'RAY_ADDRESS',
    'auto'
)

# Path to the model
SUMMARIZATION_MODEL_PATH = os.path.join(
    BASE_DIR,
    'models',
    'summarization'
)

GPT_MODEL_PATH = os.path.join(
    BASE_DIR,
    'models',
    'gpt2'
)
