#!/usr/bin/env python
#test file to test making html file checklist with pythong.

# link using to create html file with python
# http://programminghistorian.org/lessons/creating-and-viewing-html-files-with-python


f = open('helloworld.html', 'w')

case_number = raw_input("Enter your case number: ")

message = """<html>
<head></head>
<Mbody><p>"""+ case_number +"""</p></body>
</html>
"""

f.write(message)
f.close()



