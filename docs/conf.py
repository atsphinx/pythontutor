from atsphinx.pythontutor import __version__ as version

# -- Project information
project = "atsphinx-pythontutor"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = version

# -- General configuration
extensions = [
    "sphinx.ext.todo",
    "atsphinx.pythontutor",
    "atsphinx.mini18n",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "furo"
html_static_path = ["_static"]


# -- Extension configuration
# atsphinx.mini18n
mini18n_default_language = "en"
mini18n_support_languages = ["en", "ja"]
mini18n_select_lang_label = ""
mini18n_basepath = "/pythontutor/"
