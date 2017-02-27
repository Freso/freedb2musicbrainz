#!/usr/bin/python3
# vim:fileencoding=utf-8
#
# FreeDB2MusicBrainz.py: Submit data from FreeDB to MusicBrainz
# Copyright © 2017 Frederik “Freso” S. Olesen <https://freso.dk/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
""""""

# https://bitbucket.org/metabrainz/musicbrainz-server/pull-requests/1393/mbs-7913-allow-seeding-of-non-url-ars-when/diff
# https://bitbucket.org/metabrainz/musicbrainz-server/pull-requests/770/mbs-7285-cant-seed-external-links-to/diff
# https://github.com/metabrainz/picard-plugins/blob/master/plugins/addrelease/addrelease.py
# https://github.com/JonnyJD/musicbrainz-isrcsubmit


import Cddb
import discid
import musicbrainzngs


__version__ = '0.0.0'

# TODO: Switch to HTTPS (port 443) once upstream is fixed:
# https://github.com/alastair/python-musicbrainzngs/issues/197
MUSICBRAINZ_HOST = 'musicbrainz.org'


def cddb_lookup_string(disc):
    """Generate a `cddb query` compatible string.

    Should follow the format of:
    ```
    -> cddb query discid ntrks off1 off2 ... nsecs

    discid:
        CD disc ID number.  Example: f50a3b13
    ntrks:
        Total number of tracks on CD.
    off1, off2, ...:
        Frame offset of the starting location of each track.
    nsecs:
        Total playing length of CD in seconds.
    ```
    Source: http://ftp.freedb.org/pub/freedb/latest/CDDBPROTO
    """
    return "%s %s %s %s" % (
        disc.freedb_id,
        disc.last_track_num,
        " ".join([str(track.offset) for track in disc.tracks]),
        disc.seconds,
    )


def main():
    result = None
    disc = discid.read(features=['mcn'])
    musicbrainzngs.set_hostname(MUSICBRAINZ_HOST)
    musicbrainzngs.set_useragent('freedb2musicbrainz.py', __version__,
                                 contact='Freso')

    try:
        result = musicbrainzngs.get_releases_by_discid(disc.id)
    except musicbrainzngs.ResponseError as err:
        print(
            'Disc not currently in MusicBrainz (or bad response): %s' %
            (err)
        )

    if result:
        if result.get('disc'):
            print('This release seems to already be in MusicBrainz.')
            print('Check %s to verify that it is the same or submit your specific copy' %
                  (disc.submission_url))
        elif result.get("cdstub"):
            print('There seems to be a CD stub of your disc.')
            print('Go to %s to add the stub fully into the database.' %
                  (disc.submission_url))
    else:
        print('The release seems to not be in MusicBrainz. Let’s try FreeDB…')
        freedb = Cddb.CddbServer()
        print(cddb_lookup_string(disc))
        result = freedb.getDiscs(cddb_lookup_string(disc))
        if result:
            for r in result:
                print(r.artist, "-", r.title)
        else:
            print('This release is non-existant! Add it to MB!!')
            print(disc.submission_url)


if __name__ == '__main__':
    main()
