#  simply python script to make running playbooks #
#                    easier                       #
#                      :D                         #
#                                                 #
###################################################
import os

print "Which package would you like to RPM?"
package = raw_input("Plugin Name? (In xxx-xxx-xxx format): ")
url = raw_input("Download URL?: ")

os.system('cowsay Building Now...')
os.system('ansible-playbook -i hosts create-rpm.yml -e "url='+url+' package='+package+'"')
os.system('cowsay All Done!')
