"""Embedding iframe from https://pythontutor.com."""

from sphinx.application import Sphinx

from . import directives, nodes, writers

__version__ = "0.2.0"


def setup(app: Sphinx):  # noqa: D103
    app.add_node(
        nodes.pythontutor,
        html=(writers.visit_pythontutor, writers.depart_pythontutor),
    )
    app.add_directive("pythontutor", directives.PythonTutor)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
