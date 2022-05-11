from librouteros import connect
from librouteros.query import Key, Or



api = connect(username='', password='', host='', port=550)

p = api.path('/')

print(list(p('ping', **{'arp-ping': 'yes', 'interface': 'bridge', 'address': '172.30.1.221','count': '4'})))


