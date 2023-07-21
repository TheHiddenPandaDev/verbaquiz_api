from project import app

from project.container import Container
from project.ui.routes.answer import get_answer_route


def setup_project():
    app.register_blueprint(get_answer_route.blueprint, url_prefix="/answer")

    container = Container()

    app.container = container

    container.wire(modules=[
        __name__,
        get_answer_route,
    ])
