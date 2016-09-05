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
"|# be used for an upgrade.                                                        #|"
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

caveats_best_practices = "caveats and best practices sent to customer"
staging_complete = "Staging complete"
health_checks = "Health checks ran"
ra_access = "RA access enabled"

# variables for customer info
customer_name = ""
customer_phone = ""
cusotmer_email = ""
customer_contact_method = ""

# array info
upgrade_to_code_version = ""
array_name = ""

tunables_array = []




'''
|#############################|
|# start of script questions #|
|#############################|
'''

print(script_defined)

#waiting for user to press a key before continuing
raw_input("Press Enter to continue...")

#asking if this is pre upgrade or upgrade

upgrade_type = 0
#while upgrade_type != "1" or "2":



# possible if I wanted to create two seperate checklists
#upgrade_type = raw_input('''
###############################################
#    Please select a choice.
#    1. pre upgrade staging and health checks
#    2. upgrade
#:''')



#if upgrade_type == "1":
#    print("You have selected pre upgrade staging and health checks")

#    print("[] ")
#    print("[] ")
#    print("[] ")

#    quit()

#starting section to set tunables
tunables = raw_input("Do you need to set any tunables?(y/n): ")

while tunables == "y":
    tunables_array.append(raw_input("What tunable needs to be set?: " ))
    raw_input("Press Enter to continue ...")
    tunables = raw_input("Do you need to set another tunable?(y/n): ")

# verifying that the array is set

print("list of tunables to be set after the upgrade: ")
print("#############################################")
for x in tunables_array:
    print(x)

print("#############################################")






# using python to generate html file
# http://programminghistorian.org/lessons/creating-and-viewing-html-files-with-python



