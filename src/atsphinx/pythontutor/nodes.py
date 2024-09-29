"""Definition of nodes and writing behaviors."""

from docutils import nodes


class pythontutor(nodes.General, nodes.Element):  # noqa: D101
    pass


def visit_pythontutor(self, node: pythontutor):  # noqa: D103
    pass


def depart_pythontutor(self, node: pythontutor):  # noqa: D103
    pass
