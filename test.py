from environs import Env
import os

env = Env()
env.read_env()

print(os.environ.get("SECRET_KEY"))