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

class Course:
    """
    Used for interim storage of course data.

    Should have the following instance variables:
    abbreviation
    name
    teacher
    period
    room
    meeting
    section
    """
    def class_dictionary(self):
        return {
            "abbr": self.abbreviation,
            "name": self.name,
            "instructor": self.teacher,
            "period": self.period,
            "room": self.room,
            "meeting": self.meeting,
            "section": self.section
        }

classes = []  # stores the classes before they are put into the output file

source_file = open("winter.txt", "r")  # or whatever you want the input file to be.

print("Parsing text...")

location = 0  # the location being parsed within the current course
current_course = Course()
# 0 = classname, 1 = section, 2 = teacher, 3 = period, 4 = meeting, 5 = room
for line in source_file.readlines():
    line = line.strip()
    """
    The following is a hack in order to parse the strangely-designed
    file to be parsed (in the format of course abbreviation: course name \n ... etc)
    """
    if ":" in line:
        location = 0
    if location is 0:
        parts = line.split(":")
        current_course.abbreviation = parts[0].strip()
        current_course.name = parts[1].strip()
    if location is 1:
        current_course.period = line
    if location is 2:
        current_course.teacher = line
    if location is 3:
        current_course.section = line
    if location is 4:
        current_course.room = line
        current_course.meeting = "n/a"  # normally this would be index 4 and room would be 5 but meeting time isn't easily parsable from the winter master schedule
        classes.append(current_course.class_dictionary())
        print(" ...found class " + current_course.name)
    location += 1

print("Found " + str(len(classes)))  # for debug
output_file = open("courses.json", "w")
json.dump(classes, output_file)  # dump the json to the file
print("Wrote to file.")
output_file.close()  # good practice
