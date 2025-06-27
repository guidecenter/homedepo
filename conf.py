# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Home Depot Credit Card Help'
copyright = '2025, Home Depot Credit Card Help'
author = 'Home Depot Credit Card Help Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "How to Activate and Manage Your Home Depot Credit Card"

# Optional short title (e.g., for navbar)
html_short_title = "Activate & Manage Home Depot Card"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Choose a theme
# Uncomment one of the following if needed
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML in RST files (for buttons, embeds, etc.)
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
    # Add other options based on the theme you choose
}

# Enable raw directive
raw_enabled = True

# Paths to templates and static files
# Uncomment these if you have custom templates or styles
# templates_path = ['_templates']
# html_static_path = ['_static']

# Patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
