"""
This file is part of Course-Database-Utility.

Course-Database-Utility is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Course-Database-Utility is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with Course-Database-Utility.  If not, see <http://www.gnu.org/licenses/>.
"""
import json
import os
from operator import itemgetter

terms = {}  # keys are terms, their values are an array of courses
default_term = ""  # to be used when no term is specified (this should never occur but it's better to have this anyway)

def init():
    """
    Load the courses and terms into memory so that they can be quickly accessed.
    """
    global terms
    print("Loading terms and courses into memory...")
    for filename in os.listdir("terms"):
        if filename[0] == ".":
            continue
            # to skip .DS_Store and other files like it
        data = json.load(open("terms/" + filename, "r"))  # courses are stored in <TERM-NAME>.json, loaded
        terms[filename[:-5]] = data  # the [:-5] is to get rid of the .json at the end of the file
        # to avoid messing with the JSON schema, the course name is just the name of the json file without the .json
        # the multiterm system was added after the fact and is a bit of a hack. It's pretty well implemented nonetheless
        print("Loaded " + str(len(data)) + " courses from " + filename)
        default_term = filename[:-5]  # from earlier, the default term (last loaded) for when term isn't specified in the POST request (and we would prefer a silent 500)
    print("Loaded " + str(len(terms.keys())) + " terms")

def search(abbr = "",
           name = "",
           instructor = "",
           period = "",
           section = "",
           room = "",
           meeting = "",
           term = default_term):  # so many default values, sorry!
    matched_courses = []  # the courses that match the search
    if meeting == "Any":
        meeting = ""
    print(abbr, name, instructor, period, section, room, meeting)
    global terms
    for course in terms[term]:  # yes, I know there are more efficient ways to do this, however with only ~500 courses, the performance gains to building a binary search tree or similar are minimal
        if (abbr.lower() in course["abbr"].lower() and
                name.lower() in course["name"].lower() and
                instructor.lower() in course["instructor"].lower() and
                period.lower() in course["period"].lower() and
                section.lower() in str(course["section"]).lower() and
                room.lower() in course["room"].lower() and
                meeting.lower() in course["meeting"].lower()):  # ...at least I used newlines
            matched_courses.append(course)
    return sorted(matched_courses, key=itemgetter('period'))
