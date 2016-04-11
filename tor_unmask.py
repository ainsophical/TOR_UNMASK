def IsTorExitNode(request):
	if gethostbyname(ReverseIPOctets(request.META.get('REMOTE_ADDR')))+'.'+request.META.get('SERVER_PORT')+'.'+ReverseIPOctets(request.META.get('SERVER_ADDR'))+'.'+'.ip-port.exitlist.torproject.org' == '127.0.0.2':
		return True
	else:
		return False

def ReverseIPOctets(inputip):
	ipoc = inputip.split('.')
	return ipoc[3]+'.'+ipoc[2]+'.'+ipoc[1]+'.'+ipoc[0]