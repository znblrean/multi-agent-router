import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    STACK_KEY = os.getenv("STACKEXCHANGE_KEY")  # کلید API از .env
    TIMEOUT = 30
    MAX_RESULTS = 3

config = Config()