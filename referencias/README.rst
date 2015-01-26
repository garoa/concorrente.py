=========================================
Referências sobre programação concorrente
=========================================

Frases
======

Rob Pike (co-inventor da linguagem Go), slide #5 de `Concurrency is not Parallelism (it's better)`__ 

    Concurrency is about dealing with lots of things at once.<br>
    Parallelism is about doing lots of things at once.

__ http://concur.rspace.googlecode.com/hg/talk/concur.html#slide-5

David Beazley (professor e autor de livros sobre Python), slide #9 de "A Curious Course on Coroutines and Concurrency" (PyCon 2009 tutorial):

    Concurrency: one of the most dificult topics in computer science (usually best avoided).

Michele Simionato, em `Threads, processes and concurrency in Python: some thoughts`__.

__ http://www.artima.com/weblogs/viewpost.jsp?thread=299551

    The people bashing threads are typically system programmers which have in mind use cases that the typical application programmer will never encounter in her life. [...] In 99% of the use cases an application programmer is likely to run into, the simple pattern of spawning a bunch of independent threads and collecting the results in a queue is everything one needs to know.



Apresentações
=============

Brian K. Quinlan, `The future is soon!`__ -- This talk introduces PEP 3148, a proposed library that makes it easier to build concurrent applications or modify existing application to exploit opportunities for parallelism.

.. __: http://www.pyvideo.org/video/480/pyconau-2010--the-future-is-soon

Guido van Rossum `Tulip: Async I/O for Python 3`__  (Twitter University)

.. __: https://www.youtube.com/watch?v=1coLC-MUCJc

Guido van Rossum `Tulip`__ (January 2014) (Linked.in)

.. __: https://www.youtube.com/watch?v=aurOB4qYuFM

Dino Viehland `Using futures for async GUI programming in Python 3.3`__ (PyCon US 2013)

__ http://lanyrd.com/2013/pycon/scdywd/


Posts
=====

- Guido van Rossum, `It isn't Easy to Remove the GIL.`__

__ http://www.artima.com/weblogs/viewpost.jsp?thread=214235

- Shannon Behrens, `Concurrency and Python`__ (Dr. Dobb's Journal, February 3, 2008)

__ http://www.drdobbs.com/open-source/concurrency-and-python/206103078?pgno=1

- Doug Hellmann, `Communication Between Processes`__ -- multiprocessing queues

__ http://pymotw.com/2/multiprocessing/communication.html#multiprocessing-queues

- Jesse Noller (autor do pacote `multiprocessing`) -- `Python Threads and the Global Interpreter Lock`__ 

http://jessenoller.com/2009/02/01/python-threads-and-the-global-interpreter-lock/

- Fredrik Lundh (autor de muitas libs), `Some Notes on Tim Bray's Wide Finder Benchmark`__

__ http://effbot.org/zone/wide-finder.htm

- Bruce Eckcel (autor de *Thinking in Java*), `Coroutines, Concurrency & Distributed Systems`__

__ http://python-3-patterns-idioms-test.readthedocs.org/en/latest/CoroutinesAndConcurrency.html


Documentação oficial
====================

- `PEP 371`__ -- Addition of the multiprocessing package to the standard library`

__ https://www.python.org/dev/peps/pep-0371/

- `PEP 3156`__ -- Asynchronous IO Support Rebooted: the "asyncio" Module

__ https://www.python.org/dev/peps/pep-3156/


- `FAQ`__ -- Can’t we get rid of the Global Interpreter Lock?

__ https://docs.python.org/2/faq/library.html#can-t-we-get-rid-of-the-global-interpreter-lock


=== Further reading



asyncio examples gist
https://gist.github.com/keis/10627651

Fetching data with Python's asyncio in a sequential order
http://stackoverflow.com/questions/24246734/fetching-data-with-pythons-asyncio-in-a-sequential-order

Nick Coghlan's Some Thoughts on Asynchronous Programming
http://python-notes.curiousefficiency.org/en/latest/pep_ideas/async_programming.html

Python Async IO Horizon (slides)
http://www.slideshare.net/ssspiochld/python-async-io-horizon

Nullege Python code search: asyncio.gather
http://nullege.com/codes/search/asyncio.gather

Concurrent HTTP Requests with Python3 and asyncio
http://geekgirl.io/concurrent-http-requests-with-python3-and-asyncio/

asyncio.wait(*futures) trap (GvR answers)
http://comments.gmane.org/gmane.comp.python.tulip/1737

Playing with asyncio
http://www.getoffmalawn.com/blog/playing-with-asyncio


