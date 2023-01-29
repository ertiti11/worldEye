import queue
import dns
from dns import resolver, reversename
def ip2host(ip, resolver=resolver, use_tcp=False):
        result = ip
        try:
            addr = reversename.from_address(ip)
        except dns.exception.SyntaxError:
            print('DNS: invalid address: %s' % ip)
            return result

        try:
            answer = str(resolver.query(addr, 'PTR', tcp=use_tcp)[0])
            result = answer.rstrip('.')
        except (dns.resolver.NXDOMAIN, dns.resolver.Timeout) as e:
            pass
        except:
            print('DNS lookup failed: %s' % addr)
            pass

        return result


    # Translate the binary SID from LDAP into human-readable form 
# def get_domain_name(ip_address):
#   import socket
#   socket.setdefaulttimeout(1)
#   result=socket.gethostbyaddr(ip_address)
#   return list(result)[0]


# print(get_domain_name("8.8.8.8"))



# from dns import resolver,reversename
# def reverseIP(ip):

#     addr =  reversename.from_address(str(ip))
#     return  str(resolver.resolve(addr, "PTR")[0])


from dns import resolver,reversename 
def reverseIP(ip):
    resolver = dns.resolver.Resolver()
    resolver.timeout = 1
    resolver.lifetime = 1
    addr =  reversename.from_address(str(ip))
    try:
        return(resolver.resolve(addr, 'PTR')[0])
    except :
        pass
    # etc.


print(reverseIP("8.8.8.8"))