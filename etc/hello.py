#from cgi import parse_qs

def app(environ, start_response):
    #qs = parse_qs(environ['QUERY_STRING'])
    #res = ['%s=%s\n' % (k, qs[k][0]) for k in qs]

    res = []
    for k, qs in environ.items():
        if 'QUERY_STRING' in k:
            for i in qs.split('&'):
                res.append(str.encode(i + '\n'))

    start_response('200 OK', [('Content-Type', 'text/plain')])

    return res
