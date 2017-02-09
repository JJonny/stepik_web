CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/jonny/web/box/web/ask',
    'args': (
        '-bind=0.0.0.0:8000',
        '-workers=2',
        '-timeout=60',
        'ask.wsgi:application',
    ),
}
