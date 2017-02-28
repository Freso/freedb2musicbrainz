FreeDB2MusicBrainz.py
=====================

An aid to add information from FreeDB to MusicBrainz_.

.. _MusicBrainz: https://musicbrainz.org/

Motivation
----------

MusicBrainz has removed their previously integrated support for looking
through their indexed FreeDB data and using FreeDB data for seeding
tracklists.
This project/script intends to not only replace previous options, but
also improve on them.

Installation
------------

Using ``virtualenv3`` and ``pip``, you can run it like so [#]_::

  virtualenv3 ./path/to/virtualenvdir
  source ./path/to/virtualenvdir/bin/activate
  pip install -r requirements.txt
  ./freefreedb2musicbrainz.py

.. [#] If you're using a different shell than ``bash``, in particular
       one that doesn't follow POSIX, you may need to run slightly
       different commands. Look at the relevant documentation
       for virtualenv.

Testing
-------

There are currently no tests. :(

Contributing
------------

The project is still in its very early stages. Feel free to submit PRs,
but please adhere to code style and respect that not all the project
goals have been fully fleshed out yet, so your patch may not be in line
with the author's vision.

Code style
^^^^^^^^^^

The script will have a strict adherence to PEP8_, with the exception of
the line length. It is nice to stay under the 72/79 characters per line,
but not an absolute necessity.

.. _PEP8: https://www.python.org/dev/peps/pep-0008/

Contact
-------

The project is hosted on GitHub, and any bugs, feature requests, etc.
should go there: https://github.com/Freso/freedb2musicbrainz

The project lead can also be found as "Freso" on `Freenode IRC`_,
mainly in the #metabrainz and #musicbrainz channels. Feel free say hi.

.. _Freenode IRC: https://freenode.net/

License
-------

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
