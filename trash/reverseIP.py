from dns import resolver,reversename

def reverseIP(ip):
    addr=reversename.from_address(str(ip))
    print(str(resolver.resolve(addr,"PTR")[0]))

