def checktor(request):
    def revip(ip):
	    ip = '.'.join(reversed(ip.split('.')))
	    return str(ip)
    tordnsel = revip(request.META.get('REMOTE_ADDR'))+'.'+request.META.get('SERVER_PORT')+'.'+revoct(request.META.get('SERVER_ADDR'))
    if gethostbyname(str(tordnsel)+'.ip-port.exitlist.torproject.org') == '127.0.0.2':
        return True
    else:
        return False

