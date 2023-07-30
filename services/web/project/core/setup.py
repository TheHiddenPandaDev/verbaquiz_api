from project import app

from project.core.container_config import Container
from project.ui.routes.answer import get_answer_route


def setup_project():

    container = Container()

    app.container = container

    container.wire(modules=[
        __name__,
        get_answer_route,
    ])
