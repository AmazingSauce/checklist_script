#!/usr/bin/env python
#test file to test making html file checklist with pythong.

# link using to create html file with python
# http://programminghistorian.org/lessons/creating-and-viewing-html-files-with-python



case_number = raw_input("Enter your case number: ")

f = open(case_number+'.html', 'w')

message = """<html>
<head></head>
<Mbody><p>"""+ case_number +"""</p></body>
</html>
"""

f.write(message)
f.close()



