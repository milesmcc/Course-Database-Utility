# Course Database Utility
An internal utility for interaction with a database of courses &amp; other information that can be extracted from such a database.

## What is this for
This was created for Phillips Academy Andover. Each term, a master schedule PDF is released, but it's horrible to use. In order to search it, you need to use Cmd-F and hope that you entered in the right term. Want to search by period or by section exclusively? You're out of luck.

Course Database Utility was created so that this is no longer an issue. It provides a functional (but maybe slightly ugly) web utility for interacting with the database.

## How to run it
Just run `python webserver.py` to start up the webserver. It will then become accessable on port 8888.

## Where the courses are stored
Courses are stored in term JSON files in the 'terms' directory. See Example.json for information on the data schema.

## License
The entire project is licensed under LGPL.
