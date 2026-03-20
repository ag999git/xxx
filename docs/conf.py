import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'My Python Book'
author = 'Your Name'
release = '1.0'

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

