from flask.cli import FlaskGroup
from flask import jsonify

from project import app
from project import db
from project.domain.question.question import Question
from project.setup.setup import setup_project

from project.domain.answer.answer import Answer

cli = FlaskGroup(True)

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

    db.session.add(Question(
        question_id=None,
        text="Question",
    ))
    db.session.commit()

    db.session.add(Answer(
        answer_id=None,
        text="Answer",
    ))
    db.session.commit()


if __name__ == "__main__":
    cli()
