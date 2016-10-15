#!/usr/bin/python

import ldap, ldif, sys, logging, io

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logging.info('Started')

try:
        UserName = sys.argv[1]

except IndexError:
        print ("\nUsage %s username\n" % sys.argv[0])
        sys.exit()

class StrIO(io.StringIO):
        def write(self, a):
                return io.StringIO.write(self, unicode(a))

o = StrIO()

#ldif_writer = ldif.LDIFWriter(sys.stdout)
ldif_writer = ldif.LDIFWriter(o)
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


        for dn,entry in res:
                ldif_writer.unparse(dn,entry)

        if o.getvalue():
                print o.getvalue()
        else:
                print ("\nUser: %s does not exist in AD.\n" % UserName)


except  Exception:
        pass

con.unbind_s()
