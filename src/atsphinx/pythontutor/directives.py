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
        attrs = {
            "width": self.options.get("width", 800),
            "height": self.options.get("height", 500),
            "code": "\n".join(self.content),
        }
        node = nodes.pythontutor(**attrs)
        return [
            node,
        ]
