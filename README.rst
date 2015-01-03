napoleon2html
===============================

.. image:: https://badge.fury.io/py/napoleon2html.png
    :target: http://badge.fury.io/py/napoleon2html

.. image:: https://pypip.in/d/napoleon2html/badge.png
        :target: https://pypi.python.org/pypi/napoleon2html


This project contains functions that encapsulate tranlation of Sphinx or
`Napoleon <http://sphinxcontrib-napoleon.readthedocs.org>`_  docstrings to HTML.

Documentation
-------------

There are three function, that can be used: ``napoleon_to_sphinx()``, ``sphinx_to_html()`` and ``napoleon_to_html()``.

napoleon_to_sphinx()
++++++++++++++++++++

This function can take documentation in `Napoleon <http://sphinxcontrib-napoleon.readthedocs.org>`_ format and translate it to Sphinx.    

Usage::

    napoleon2html.napoleon_to_sphinx("""
        Description of function
    
        Args:
            argument (str): Description of argument.
    
        Returns:
            int: Description of return.
    """)
    

Output::

  Description of function
  
  :Parameters: **argument** (*str*) --
               Description of argument.
  
  :returns: *int* --
            Description of return.


sphinx_to_html()
++++++++++++++++
Then there is the ``sphinx_to_html()``, which converts string in Sphinx format to HTML::

    napoleon2html.sphinx_to_html("""
        Description of function
      
        :Parameters: **argument** (*str*) --
                     Description of argument.
      
        :returns: *int* --
                  Description of return.
    """)

Output::

    <blockquote>
    <p>Description of function</p>
    <table class="docutils field-list" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
    <tr class="field"><th class="field-name">Parameters:</th><td class="field-body"><strong>argument</strong> (<em>str</em>) --
    Description of argument.</td>
    </tr>
    <tr class="field"><th class="field-name">returns:</th><td class="field-body"><em>int</em> --
    Description of return.</td>
    </tr>
    </tbody>
    </table>
    </blockquote>

napoleon_to_html()
++++++++++++++++++
Last function is ``napoleon_to_html()``, which wraps the previous two.