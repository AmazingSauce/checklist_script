#!/usr/bin/env python
#test file to test making html file checklist with python.

# link using to create html file with python
# http://programminghistorian.org/lessons/creating-and-viewing-html-files-with-python



case_number = raw_input("Enter your case number: ")

f = open(case_number+'.html', 'w')

message = """<html>
<head></head>
<Mbody><p>"""+ case_number +"""</p></body>
</html>
"""

# creating an html page with checkboxes
# http://www.w3schools.com/tags/att_input_checked.asp
# example code
# http://www.w3schools.com/tags/tryit.asp?filename=tryhtml_form_checkbox




f.write(message)
f.close()



