#!/usr/bin/python

import ldap, ldif, sys
from StringIO import StringIO as StringIO

try:
        UserName = sys.argv[1]

except IndexError:
        print ("\nUsage %s username\n" % sys.argv[0])
        sys.exit()


old_stdout = sys.stdout
sys.stdout = my_stdout = StringIO()

con=ldap.initialize('ldap://windc01:389', trace_level=0)

user_dn = "CN=net admin,CN=Users,DC=linuxstuff,DC=info"
password = "yFaXlJgCfuzOulHFJOo0"
filter = "(sAMAccountName=%s)" % UserName
base_dn = "DC=linuxstuff,DC=info"
ldapScope = ldap.SCOPE_SUBTREE
attributes = None

try:

        con.simple_bind_s(user_dn, password)
        con.set_option(ldap.OPT_REFERRALS, 0)
        res = con.search_s(base_dn, ldapScope, filter, attributes)

        ldif_writer = ldif.LDIFWriter(sys.stdout)

        for dn,entry in res:
                ldif_writer.unparse(dn,entry)
#        ldif_writer.unparse("dn=hello")

        zResults = my_stdout.getvalue()
        sys.stdout = old_stdout
        sys.stdout = sys.__stdout__

except  Exception:
        pass


sys.stdout = sys.__stdout__
zResults = my_stdout.getvalue()

if zResults:
       print ("%s" % my_stdout.getvalue())
else:
       print ("\nUser: %s does not exist in AD.\n" % UserName)

#print ("%s" % zResults)
#print("something else")

sys.stdout.close()
con.unbind_s()