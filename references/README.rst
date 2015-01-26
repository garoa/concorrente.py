=========================================
Referências sobre programação concorrente
=========================================

Frases
======

Rob Pike (co-inventor da linguagem Go), slide #5 de `Concurrency is not Parallelism (it's better) <http://concur.rspace.googlecode.com/hg/talk/concur.html#slide-5>`_ 

    Concurrency is about dealing with lots of things at once.

    Parallelism is about doing lots of things at once.

    Not the same, but related.

    One is about structure, one is about execution.

    Concurrency provides a way to structure a solution to solve a problem that may (but not necessarily) be parallelizable.

David Beazley (professor e autor de livros sobre Python), slide #9 de "A Curious Course on Coroutines and Concurrency" (PyCon 2009 tutorial):

    Concurrency: one of the most dificult topics in computer science (usually best avoided).

Michele Simionato, em `Threads, processes and concurrency in Python: some thoughts <http://www.artima.com/weblogs/viewpost.jsp?thread=299551>`_

    The people bashing threads are typically system programmers which have in mind use cases that the typical application programmer will never encounter in her life. [...] In 99% of the use cases an application programmer is likely to run into, the simple pattern of spawning a bunch of independent threads and collecting the results in a queue is everything one needs to know.



Apresentações
=============

Brian K. Quinlan, `The future is soon! <http://www.pyvideo.org/video/480/pyconau-2010--the-future-is-soon>`_ -- This talk introduces PEP 3148, a proposed library that makes it easier to build concurrent applications or modify existing application to exploit opportunities for parallelism.



Guido van Rossum `Tulip: Async I/O for Python 3 <https://www.youtube.com/watch?v=1coLC-MUCJc>`_  (Twitter University)

Guido van Rossum `Tulip <https://www.youtube.com/watch?v=aurOB4qYuFM>`_ (January 2014) (Linked.in)

Dino Viehland `Using futures for async GUI programming in Python 3.3 <http://lanyrd.com/2013/pycon/scdywd/>`_ (PyCon US 2013)

Posts
=====

- Guido van Rossum, `It isn't Easy to Remove the GIL. <http://www.artima.com/weblogs/viewpost.jsp?thread=214235>`_

- Shannon Behrens, `Concurrency and Python <http://www.drdobbs.com/open-source/concurrency-and-python/206103078?pgno=1>`_ (Dr. Dobb's Journal, February 3, 2008)

- Doug Hellmann, `Communication Between Processes <http://pymotw.com/2/multiprocessing/communication.html#multiprocessing-queues>`_ -- multiprocessing queues

- Jesse Noller (autor do pacote `multiprocessing`) -- `Python Threads and the Global Interpreter Lock <http://jessenoller.com/2009/02/01/python-threads-and-the-global-interpreter-lock/>`_ 

- Nick Coghlan, `Some Thoughts on Asynchronous Programming <http://python-notes.curiousefficiency.org/en/latest/pep_ideas/async_programming.html>`_

- Nathan Hoad, `Playing with asyncio <http://www.getoffmalawn.com/blog/playing-with-asyncio>`_

- Fredrik Lundh (autor de muitas libs), `Some Notes on Tim Bray's Wide Finder Benchmark <http://effbot.org/zone/wide-finder.htm>`_

- Bruce Eckcel (autor de *Thinking in Java*), `Coroutines, Concurrency & Distributed Systems <http://python-3-patterns-idioms-test.readthedocs.org/en/latest/CoroutinesAndConcurrency.html>`_

Documentação oficial
====================

- `PEP 371 <https://www.python.org/dev/peps/pep-0371/>`_ -- Addition of the multiprocessing package to the standard library`

- `PEP 3156 <https://www.python.org/dev/peps/pep-3156/>`_ -- Asynchronous IO Support Rebooted: the "asyncio" Module

- `FAQ <https://docs.python.org/2/faq/library.html#can-t-we-get-rid-of-the-global-interpreter-lock>`_ -- Can’t we get rid of the Global Interpreter Lock?


Examples
========

- `asyncio examples gist <https://gist.github.com/keis/10627651>`_

- `Fetching data with Python's asyncio in a sequential order <http://stackoverflow.com/questions/24246734/fetching-data-with-pythons-asyncio-in-a-sequential-order>`_

- `Python Async IO Horizon <http://www.slideshare.net/ssspiochld/python-async-io-horizon>`_ (slides)

- Nullege Python code search: `asyncio.gather <http://nullege.com/codes/search/asyncio.gather>`_

- `Concurrent HTTP Requests with Python3 and asyncio <http://geekgirl.io/concurrent-http-requests-with-python3-and-asyncio/>`_

- GvR answers: `asyncio.wait(*futures) trap <http://comments.gmane.org/gmane.comp.python.tulip/1737>`_



