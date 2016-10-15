#!/usr/bin/python


import ldap
import ldif
import sys

try:
    UserName = sys.argv[1]

print ("Searching for %s" % UserName)


ldif_writer = ldif.LDIFWriter(sys.stdout)

Query = "(sAMAccountName=%s)" % UserName

#print Query

con=ldap.initialize('ldap://windc01:389', trace_level=0)

user_dn = "CN=net admin,CN=Users,DC=linuxstuff,DC=info"
password = "yFaXlJgCfuzOulHFJOo0"


try:

    print UserName

    con.simple_bind_s(user_dn, password)

    con.set_option(ldap.OPT_REFERRALS,0)

    res = con.search_s("DC=linuxstuff,DC=info", ldap.SCOPE_SUBTREE, Query)

    for dn, entry in res:

        ldif_writer.unparse(dn, entry)

except Exception:
        pass