import os
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

DATABASE_URL = f'sqlite:///'