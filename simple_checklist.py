#!/usr/bin/env python

'''
#############################################################################
#08/07/2016 #
#Written by Robert Willis Anderson #
#goal is to generate a checklist in html format for upgrades #
#some will be auto generated because they should be done every time #
#Others will be requested as inputes by user #
#############################################################################
'''
'''
|#########################|
|# Defining variables    #|
|#########################|
'''

script_defined = '''
"|##################################################################################|"
"|# The purpose of this script is to generate a checklist to                       #|"
"|# be used for every upgrade.                                                     #|"
"|#                                                                                #|"
"|# There are some items that should always be done but there are some things that #|"
"|# need to be done such as setting tunables, call customer before starting etc.   #|"
"|#                                                                                #|"
"|# We will try to make sure that everything is set to be done before during and   #|"
"|# after the upgrade so things are not missed.                                    #|"
"|#                                                                                #|"
"|# This script will create an html doc that you can open in a browser.            #|"
"|##################################################################################|"
'''


'''
|#############################|
|# defining variables        #|
|#############################|
'''


caveats_best_practices = "caveats and best practices sent to customer"
staging_complete = "Staging complete"
health_checks = "Health checks ran"
ra_access = "RA access enabled"

# variables for customer info
customer_name = ""
customer_phone = ""
customer_email = ""
customer_contact_method = ""
upgrade_scheduled_time = ""
case_number = ""

# array info
upgrade_to_code_version = ""
array_name = ""

tunables_array = []




'''
|#############################|
|# script opening line       #|
|#############################|
'''

print(script_defined)

#waiting for user to press a key before continuing
raw_input("Press Enter to continue...")


'''
|##################################|
|# gettin input for customer info #|
|##################################|
'''

customer_info = "n"

while customer_info.lower() == "n" or customer_info.lower() == "no":

    customer_name = raw_input("Enter customer contact name: ")
    customer_contact_method = raw_input("How should the customer be contacted for the upgrade: ")
    customer_phone = raw_input("Enter customers phone number: ")
    customer_email = raw_input("Enter customer email: ")
    upgrade_scheduled_time = raw_input("Enter scheduled upgrade time(yyyy/mm/dd tt:tt AM||PM timezone): ")
    case_number = raw_input("Enter the salesforce case number: ")


    print("Customer and upgrade info")
    print("#############################################")
    print("")
    print("Name: " + customer_name)
    print("Phone: " + customer_phone)
    print("Email: " + customer_email)
    print("")
    print("Customer to be contacted: " + customer_contact_method)
    print("")
    print("upgrade scheduled for " + upgrade_scheduled_time)
    print("")
    print("#############################################")

    customer_info = raw_input("Is the info correct?(y/n): ")


raw_input("Press Enter to continue...")

print("#############################################")
print("#############################################")



'''
|####################################|
|# starting section for tunables    #|
|####################################|
'''

print("")
tunables = raw_input("Do you need to set any tunables?(y/n): ")

tunables_info = "n"


while tunables_info.lower() == "n":

    while tunables.lower() == "y":
        tunables_array.append(raw_input("What tunable needs to be set?: " ))
        raw_input("Press Enter to continue ...")
        tunables = raw_input("Do you need to set another tunable?(y/n): ")

    tunables = "y"

    print("")
    print("#############################################")
    print("list of tunables to be set after the upgrade: ")
    print("#############################################")
    for x in tunables_array:
        print(x)

    print("#############################################")

    tunables_info = raw_input("Is the info correct?(y/n): ")




# using python to generate html file
# http://programminghistorian.org/lessons/creating-and-viewing-html-files-with-python




f = open(case_number+'.html', 'w')

message = """
<html>
<head>"""+ case_number +"""</head>
<body>
<p>"""+ case_number +"""</p>

<form action="demo_form.asp" method="get">
  <input type="checkbox" name="Case" value=" """+ case_number +""" "> I have case """+ case_number +"""<br>

</form>



</body>


</html>





"""

# creating an html page with checkboxes
# http://www.w3schools.com/tags/att_input_checked.asp
# example code
# http://www.w3schools.com/tags/tryit.asp?filename=tryhtml_form_checkbox




f.write(message)
f.close()


