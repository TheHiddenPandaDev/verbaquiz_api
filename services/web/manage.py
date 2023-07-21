from flask.cli import FlaskGroup
from flask import jsonify

from project import app
from project import db
from project.setup.setup import setup_project

from project.domain.answer.answer import Answer

cli = FlaskGroup(app)

setup_project()
@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if hasattr(e, 'get_response') and hasattr(e, 'code'):
        return e.get_response(), e.code
    return jsonify(error=str(e)), code

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

    # Seed DB
    db.session.add(Answer(
        answer_id=1,
        text="Test",
    ))
    db.session.commit()


if __name__ == "__main__":
    cli()
