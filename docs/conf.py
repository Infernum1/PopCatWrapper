import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "PopCatAPIWrapper"
copyright = "2022, Infernum1"
author = "Infernum1"
release = "0.0.8"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "furo"
html_favicon = "favicon.ico"
