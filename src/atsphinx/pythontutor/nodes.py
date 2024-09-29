"""Definition of nodes and writing behaviors."""

from urllib.parse import quote

from docutils import nodes
from sphinx.writers.html5 import HTML5Translator


class pythontutor(nodes.General, nodes.Element):  # noqa: D101
    pass


def visit_pythontutor(self: HTML5Translator, node: pythontutor):  # noqa: D103
    code = quote(node["code"], safe="/',")
    url = f"https://pythontutor.com/iframe-embed.html#code={code}&py=3"
    attrs = {
        "width": node["width"],
        "height": node["height"],
        "src": url,
    }
    self.body.append(self.starttag(node, "iframe", **attrs))


def depart_pythontutor(self: HTML5Translator, node: pythontutor):  # noqa: D103
    self.body.append("</iframe>")
