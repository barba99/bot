from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "808192"))
    API_HASH = getenv("API_HASH", "d2a1c1fe0d574f98068c63d4928aee8a")
    BOT_TOKEN = getenv("BOT_TOKEN", "1819174855:AAEEsMnG6vZnc1yJgVHvVVLshv1vya86rIQ")

config = Config()

