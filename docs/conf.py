import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "PopCatAPI-Wrapper"
copyright = "2022, Infernum1"
author = "Infernum1"

release = "0.0.1"

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "piccolo_theme"
