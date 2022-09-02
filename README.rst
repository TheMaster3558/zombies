brains.py
==========
Run brainfuck files.


License
--------
MIT


Installation
-------------
.. code-block:: sh

    $ pip install brains.py


Python Usage
-------------
.. code-block:: py

    import brains

    interpreter = brains.BF()
    code = '''
    >+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]
    >++++++++[<++++>-] <.>+++++++++++[<++++++++>-]<-.--------.+++
    .------.--------.[-]>++++++++[<++++>- ]<+.[-]++++++++++.
    '''
    interpreter.run(code)  # Hello World!

    # you can also run a .bf file
    interpreter.run('helloworld.bf')


Command Line Usage
-------------------
Run a `.bf` file

.. code-block:: sh

    $ brains helloworld.bf


Use the REPL

.. code-block:: sh

    $ brains
    Running Brainfuck REPL made in Python...
    brains.py 0.1.0a by Kaushal Dabbiru
    Type "stop" to exit
    \\\ >>++<<+-


Code Formatting
----------------
All code should mostly follow PEP8.
