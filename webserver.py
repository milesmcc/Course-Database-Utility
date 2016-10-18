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

import tornado.ioloop
import tornado.web
import json
import database

site_name = "Internal Course Utility (Prototype)"  # the name that shows up all over the site. Thank goodness it's dynamic!

class MainHandler(tornado.web.RequestHandler):
    """
    Handles GET requests to /
    """
    def get(self):
        print("RECEIVED get REQUEST to / - serving!")
        self.render("pages/index.html",
                    site_name=site_name,
                    terms1=database.terms.iterkeys(),
                    terms2=database.terms.iterkeys(),
                    terms3=database.terms.iterkeys(),
                    terms4=database.terms.iterkeys())  # terms1,2,3,4: an abomination, I know. For some reason tornado deletes your iterator when you use it so I have to pass it in 4 times for the 4 times it's being used

class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/") # redirect all GET requests to /
        print("RECEIVED get REQUEST to /search - redirecting to /")
    def post(self):
        abbr = self.get_argument('abbr', '')
        name = self.get_argument('name', '')
        teacher = self.get_argument('teacher', '')
        room = self.get_argument('room', '')
        period = self.get_argument('period', '')
        section = self.get_argument('section', '')
        meeting = self.get_argument('meeting', '')
        term = self.get_argument('term', '')  # hopefully at least some of these are defined
        print("RECEIVED post REQUEST TO /search: ", abbr, name, teacher, room, period, section, meeting)
        if meeting is "Any":
            meeting = ""  # in some search fields, the meeting dropdown has an Any field which is represented in the server-side search system as ""

        """
        The following code is to generate the query string.
        It could be more economic, but hey, it works.
        """
        query = ""
        fields = {
            "course abbreviation": abbr,
            "course name": name,
            "teacher": teacher,
            "room": room,
            "period": period,
            "section": section,
            "meeting": meeting
        }
        for (key, value) in fields.iteritems():
            if value == "":
                value = "anything"
            query += "<strong>" + key + "</strong> contains <i>" + value+ "</i>, "  # yes, embedded HTML. fight me

        matched_courses = database.search(abbr=str(abbr),
                                          name=str(name),
                                          instructor=str(teacher),
                                          room=str(room),
                                          period=str(period),
                                          section=str(section),
                                          meeting=str(meeting),
                                          term=term)  # not too resource inefficient...
        self.render("pages/search.html",
                    courses=matched_courses,
                    num=(len(matched_courses)),
                    site_name=site_name,
                    query=query[:-2],  # the -2 to omit [, ]
                    term=term
                    )

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/search", SearchHandler)
    ])

database.init()

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

# tornado is a beautiful thing....
