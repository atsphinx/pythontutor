"""Definition of directives."""

from docutils.parsers.rst import Directive, directives  # type:ignore

from . import nodes


class PythonTutor(Directive):  # noqa: D101
    has_content = True

    option_spec = {
        "width": directives.positive_int,
        "height": directives.positive_int,
    }

    def run(self):  # noqa: D102
        node = nodes.pythontutor()
        return [
            node,
        ]
