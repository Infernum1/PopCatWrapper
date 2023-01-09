Introduction
============

.. important::

   Project development has been paused till April, 2023

.. toctree::
   :maxdepth: 2

   modules
   self

Installation
============

To use `PopCatWrapper <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html>`_, install it using `pip <https://pypi.org/project/pip/>`_

.. code-block::
   :linenos:

   (.venv) $ pip install popcatapiwrapper

or install it from the `github repo <https://github.com/Infernum1/PopCatWrapper>`_ using `git <https://git-scm.com>`_ with the following command

.. code-block::
   :linenos:

   (.venv) $ pip install -U git+https://github.com/Infernum1/PopCatWrapper


Examples
========
An example of the `get_element_info <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.client.PopCatAPI.get_element_info>`_ feature

.. code-block::
   :linenos:

   import PopCatAPIWrapper
   import asyncio

   client = PopCatAPIWrapper.client.PopCatAPI()

   async def el(element: str):
      element = await client.get_element_info(element=element)
      print(element.summary)

   if __name__ == "__main__":
      asyncio.run(el("Oxygen"))


or the `get_color_info <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.client.PopCatAPI.get_color_info>`_ feature

.. code-block::
   :linenos:

   import PopCatAPIWrapper
   import asyncio

   client = PopCatAPIWrapper.client.PopCatAPI()

   async def color(color: str):
      color_obj = await client.get_color_info(color=color)
      print(color_obj.name)

   if __name__ == "__main__":
      asyncio.run(color("547df0"))

Take a look at all the methods `here <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html>`_
