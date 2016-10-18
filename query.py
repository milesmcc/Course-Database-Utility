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

data_file = open("courses.json", "r")
courses = json.load(data_file)
data_file.close()

def print_course(course):
    print("- " + course["abbr"] + ": " + course["name"])
    print("    Instructor: " + course["instructor"])
    print("    Room: " + course["room"])
    #print("    Section: " + course["section"])
    print("    Period: " + course["period"])
    print("    Meeting: " + course["meeting"])

while True:  # the query loop
    print("(newline for ignore)")
    room = raw_input("  Room: ")
    section = raw_input("  Section: ")
    period = raw_input("  Period: ")
    abbr = raw_input("  Abbr: ")
    instructor = raw_input("  Instructor: ")
    meeting = raw_input("  Meeting: ")
    name = raw_input("  Name: ")
    print(name)
    print("Searching...")
    for course in courses:
        matches = True
        if len(room.strip()) > 0:
            if room.strip() not in course["room"]:
                matches = False
        if len(section.strip()) > 0:
            if section.strip() not in course["section"]:
                matches = False
        if len(period.strip()) > 0:
            if period.strip() not in course["period"]:
                matches = False
        if len(abbr.strip()) > 0:
            if abbr.strip() not in course["abbr"]:
                matches = False
        if len(instructor.strip()) > 0:
            if instructor.strip() not in course["instructor"]:
                matches = False
        if len(meeting.strip()) > 0:
            if meeting.strip() not in course["meeting"]:
                matches = False
        if len(name.strip()) > 0:
            if name.strip() not in course["name"]:
                matches = False
        if matches:
            print_course(course)
