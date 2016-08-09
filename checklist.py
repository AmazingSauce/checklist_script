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

|#########################|
|# Defining variables    #|
|#########################|


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







|#############################|
|# start of script questions #|
|#############################|


print(script_defined)

#waiting for user to press a key before continueing
raw_input("Press Enter to continue...")


#starting section to set tunables
tunables = raw_input("Do you need to set any tunables?(y/n)")

while tunables == "y":
    raw_input("Press Enter to continue ...")
    tunables = raw_input("Do you need to set another tunable?(y/n)")



# using python to generate html file
#http://programminghistorian.org/lessons/creating-and-viewing-html-files-with-python



