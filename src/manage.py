import os

import click
from flask_migrate import Migrate
from main import create_app, db


app = create_app(os.getenv("APP_SETTINGS"))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


if __name__ == "__main__":
    app.cli()
