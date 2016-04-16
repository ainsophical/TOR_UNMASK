from socket import gethostbyname

def tor(f):
    @wraps(f)
    def checktor(request, *args, **kwargs):
        def revip(ip):
            ip = '.'.join(reversed(ip.split('.')))
            return str(ip)
        tordnsel = '.'.join([revip(request.META.get('REMOTE_ADDR')),
                             request.META.get('SERVER_PORT'),
                             revip(request.META.get('SERVER_ADDR'))])
        if gethostbyname(str(tordnsel)+'.ip-port.exitlist.torproject.org') == '127.0.0.2':
            request.META['tor'] = 'Enabled'
            return f(request, *args, **kwargs)
        else:
            request.META['tor'] = 'Not Enabled'
            return 'Not Enabled'
    return checktor


