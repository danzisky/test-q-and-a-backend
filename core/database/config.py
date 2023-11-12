# Python imports
import os

db_directory = "core/database"
db_filename = "quiz-app.db"

# Internal imports
config = {
    "default": {
        "engine": "tortoise.backends.sqlite",
        "credentials": {
            "file_path": os.path.join(os.getcwd(), db_directory, db_filename),
        },
    }
}

print(config)

TORTOISE_ORM = {
    "connections": config,
    "apps": {
        "models": {
            "models": ["core.database.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
