Internal Structure
==================

Fire Search uses python, uv and Textual to create it's application.


- `Python <https://www.python.org>`_ - Programming language
- `uv <https://docs.astral.sh/uv/>`_ - Runtime
- `textual <https://textual.textualize.io/>`_ - UI library
- `readthedocs <https://about.readthedocs.com/>`_ + `restructuredtext <https://en.wikipedia.org/wiki/ReStructuredText>`_ + `sphinx <https://www.sphinx-doc.org/en/master/>`_ - This Documentation


The internal structer of Fire Search has all the panels communicate through the main application class.
Each widget communecates to other widgets by running functions in the application class. For example when the 
file viewer highlights a diffrent item it sets the selected item info varible on the main application and runs the refresh function for
the infomation panel.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   application