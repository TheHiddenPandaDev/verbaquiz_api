from flask.cli import FlaskGroup
from flask import jsonify

from project import app
from project import db
from project.domain.category.category import Category
from project.domain.question.question import Question
from project.domain.quizz.quizz import Quizz
from project.domain.quizz_questions.quizz_questions import QuizzQuestion
from project.domain.user.user import User
from project.domain.user_answer_quizz.user_answer_quizz import UserAnswers
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
    db.session.add(User(
        user_id=1,
        name="User",
        is_disabled=False,
    ))
    db.session.commit()

    db.session.add(Category(
        category_id=1,
        name="Test",
        is_disabled=None,
    ))
    db.session.commit()

    db.session.add(Quizz(
        quizz_id=1,
        category_id=1,
        user_id=1,
        status="Started",
        quizz_duration_in_seconds=1,
    ))
    db.session.commit()

    db.session.add(Question(
        question_id=1,
        category_id=1,
        text="Question",
    ))
    db.session.commit()

    db.session.add(QuizzQuestion(
        question_id=1,
        quizz_id=1,
    ))
    db.session.commit()

    db.session.add(Answer(
        answer_id=1,
        text="Answer",
        is_correct=True,
        question_id=1,
    ))
    db.session.add(Answer(
        answer_id=2,
        text="Answer",
        is_correct=False,
        question_id=1,
    ))
    db.session.add(Answer(
        answer_id=3,
        text="Answer",
        is_correct=False,
        question_id=1,
    ))
    db.session.add(Answer(
        answer_id=4,
        text="Answer",
        is_correct=False,
        question_id=1,
    ))
    db.session.commit()

    db.session.add(UserAnswers(
        quizz_id=1,
        user_id=1,
        question_id=1,
        selected_answer_id=4,
        correct_answer_id=1,
        status='Answered',
        started_at=None,
        finished_at=None,
    ))
    db.session.commit()


if __name__ == "__main__":
    cli()
