# BSD 3-Clause License
#
# Copyright (c) 2025, Spill-Tea
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Sphinx configuration file."""

import os
import sys

from sphinx.application import Sphinx
from sphinx.highlighting import lexer_classes as _lexer_registry


sys.path.insert(0, os.path.abspath("../src/"))  # Required to see python package
sys.path.append(os.path.abspath("./_ext"))  # Required for custom extensions


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "PyTemplate"
copyright = "2025, Jason C Del Rio (Spill-Tea)"
author = "Jason C Del Rio (Spill-Tea)"
release = "v0.0.1"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
]

napoleon_google_docstring = True  # Use google docstring format (sphinx.ext.napoleon)
autosummary_generate = True  # Turn on sphinx.ext.autosummary

templates_path = ["_templates"]
exclude_patterns = []

pygments_style = "styles.VSCodeDarkPlus"  # Use custom syntax highlighting (style)


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
# html_logo = "_static/logo.png"
github_url = "https://github.com/Spill-Tea/PyTemplate"

# Theme options (specific to sphinx_rtd_theme)
# https://github.com/readthedocs/sphinx_rtd_theme/blob/master/docs/configuring.rst#id7
# html_theme_options = {}


def setup(app: Sphinx) -> None:
    """Custom sphinx application startup setup."""
    from lexers import CustomCythonLexer, CustomPythonLexer  # type: ignore

    # NOTE: overwrite default python lexer
    app.add_lexer("python", CustomPythonLexer)
    assert "python" in _lexer_registry, "python language not found in registry"
    assert _lexer_registry["python"] == CustomPythonLexer, (
        "custom Lexer not found in registry."
    )

    app.add_lexer("cython", CustomCythonLexer)
    assert "cython" in _lexer_registry, "python language not found in registry"
    assert _lexer_registry["cython"] == CustomCythonLexer, (
        "custom Lexer not found in registry."
    )
