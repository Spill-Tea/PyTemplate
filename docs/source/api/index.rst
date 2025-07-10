PyTemplate API Documentation
============================

PyTemplate API documentation.

.. code-block:: python
   :caption: example.py

   from typing import ClassVar as ClassV

   CONSTANT_A: int = 0xFF
   CONSTANT_B: float = np.pi

   # NOTE: this is an example class
   class Example(object):
       """Example docstring.
       
       Args:
            arg1 (str): argument 1
            arg2 (int): argument 2
       
       Attributes:
            data (dict): data

       """
       arg1: str
       arg2: int
       data: dict
       other: ClassV[list[int]] = [1, 5, 7]

       def __init__(self, arg1: str, arg2: int) -> None:
           self.arg1 = arg1
           self.arg2 = arg2
           self.data = {
               "a": [(1, 2, (3, 4, 5)), (6, 7, (8, 9 , 10))],
               "b": {"c": (7, 4, 3), "d": {"e", "f", "g"}},
           }

       def __getattr__(self, value):
           return self.data[value]

       def method(self, value):
           return self[value]

       def write(self, text):
           print(f"{text:<5}\n")

       def do_something(self, value):
           if value > CONSTANT_A:
               return value - CONSTANT_B
           else:
               return value + 0b10011


.. toctree::
   :caption: Submodules


.. autosummary::
   :toctree: generated
   :recursive:
