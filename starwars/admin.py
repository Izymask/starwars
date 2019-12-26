from common.admin import create_admin

from starwars.models import ALL_MODELS

for model in ALL_MODELS:
    create_admin(model)
