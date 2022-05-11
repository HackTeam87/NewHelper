import routeros_api
connection = routeros_api.RouterOsApiPool(
    host='',
    username='',
    password='',
    port=550,
    plaintext_login=True
)
api = connection.get_api()
# temp = 0
# temperature = api.get_resource('/system/health/gauges')

# lease = api.get_resource('/ip/dhcp-server/lease/')


conn = api.get_resource('/ip/firewall/connection/')
res = conn.get(src_address='172.19.2.253')


# print(type(DstAddress))

print(res)

# for l in lease.get():
#     print('id: ' + str(l['id']) + '\n')
#     print('address: ' + str(l['address']) + '\n')
#     print('mac-address: ' + str(l['mac-address']) + '\n')
#     print('client-id: ' + str(l['client-id']) + '\n')
#     print('address-lists: ' + str(l['address-lists']) + '\n')
#     print('server: ' + str(l['server']) + '\n')
#     print('lease-time: ' + str(l['lease-time']) + '\n')
#     print('dhcp-option: ' + str(l['dhcp-option']) + '\n')
#     print('status: ' + str(l['status']) + '\n')
#     print('expires-after: ' + str(l['expires-after']) + '\n')
#     print('last-seen: ' + str(l['last-seen']) + '\n')
#     print('active-address: ' + str(l['active-address']) + '\n')
#     print('active-mac-address: ' + str(l['active-mac-address']) + '\n')
#     print('active-client-id: ' + str(l['active-client-id']) + '\n')
#     print('active-server: ' + str(l['active-server']) + '\n')
#     print('radius: ' + str(l['radius']) + '\n')
#     print('dynamic: ' + str(l['dynamic']) + '\n')
#     print('blocked: ' + str(l['blocked']) + '\n')
#     print('disabled: ' + str(l['disabled']) + '\n')
#     if l['comment']:
#         print('comment: ' + str(l['comment']) + '\n')



# print(lease.get())

# for t in temperature.get():
#     if t['name'] == 'temperature':
#         temp = t['value']
# print(temp)
