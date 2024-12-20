from project import app

from project.container import Container
from project.ui.routes.answer import get_answer_route, create_answer_route, update_answer_text_route
from project.ui.routes.question import get_question_route


def setup_project():
    app.register_blueprint(get_answer_route.blueprint, url_prefix="/answers")
    app.register_blueprint(create_answer_route.blueprint, url_prefix="/answers")
    app.register_blueprint(update_answer_text_route.blueprint, url_prefix="/answers")
    app.register_blueprint(get_question_route.blueprint, url_prefix="/questions")

    container = Container()

    app.container = container

    container.wire(modules=[
        __name__,
        get_answer_route,
        create_answer_route,
        update_answer_text_route,
        get_question_route,
    ])
