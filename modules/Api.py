from librouteros import connect
from librouteros.query import Key, Or

class Mikrotik:
    
    def interface_info(self, ip, api_port, api_login, api_passw):
        api = connect(username=api_login, password=api_passw, host=ip, port=api_port)
        #Flags: D - dynamic, X - disabled, R - running, S - slave
        name = Key('name')
        type = Key('type')
        actual_mtu = Key('actual-mtu')
        l2mtu = Key('l2mtu')
        mac_address = Key('mac-address')
        dynamic = Key('dynamic')
        disabled = Key('disabled')
        running = Key('running')
        slave = Key('slave')
        
        AR = []
        for row in api.path('/interface').select(name, type,actual_mtu, l2mtu,  mac_address, dynamic, disabled, running, slave ):
            AR.append(row)
        if AR == []:
            return('Empty Search Value')        
        return(AR)

         

    def ip_arp_info(self, ip, api_port, api_login, api_passw):
        api = connect(username=api_login, password=api_passw, host=ip, port=api_port)
        #Flags: X - disabled, I - invalid, H - DHCP, D - dynamic, P - published, C - complete
        address = Key('address')
        mac_address = Key('mac-address')
        interface = Key('interface')
        disabled = Key('disabled')
        invalid = Key('invalid')
        dhcp = Key('DHCP')
        dynamic = Key('dynamic')
        published = Key('published')
        complete = Key('complete')

        AR = []
        for row in api.path('/ip/arp').select(address, mac_address,interface,disabled,
                                              invalid,dhcp,dynamic,published,complete):
            AR.append(row)
        if AR == []:
            return('Empty Search Value')        
        return(AR)   

    def ip_dhcp_server_info(self, ip, api_port, api_login, api_passw):
        api = connect(username=api_login, password=api_passw, host=ip, port=api_port)
        #Flags: D - dynamic, X - disabled, I - invalid
        name = Key('name')
        interface = Key('interface')
        lease_time = Key('lease-time')
        address_pool = Key('address-pool')
        authoritative = Key('authoritative')
        use_radius = Key('use-radius')
        lease_script = Key('lease-script')
        dynamic = Key('dynamic')
        disabled = Key('disabled')
        invalid = Key('invalid')

        AR = []
        for row in api.path('/ip/dhcp-server').select(name, interface ,lease_time, address_pool,
                                                      authoritative, use_radius, lease_script, dynamic,
                                                       disabled,invalid):
            AR.append(row)
        if AR == []:
            return('Empty Search Value')        
        return(AR)

    def ip_dhcp_server_lease_info(self, ip, api_port, api_login, api_passw , val):
        api = connect(username=api_login, password=api_passw, host=ip, port=api_port) 
        #Flags: X - disabled, R - radius, D - dynamic, B - blocked
        address = Key('address')
        mac_address = Key('mac-address')
        host_name = Key('host-name')
        server = Key('server')
        rate_limit = Key('rate-limit')
        status = Key('status')
        dhcp_option = Key('dhcp-option')
        last_seen = Key('last-seen')
        expires_after = Key('expires-after')
        active_address = Key('active-address')
        disabled = Key('disabled')
        radius = Key('radius')
        dynamic = Key('dynamic')
        blocked = Key('blocked')

        # print(dir(api.path().select))

        AR = []
        for row in api.path('/ip/dhcp-server/lease').select(address, mac_address, host_name, server, 
                                                            dynamic,rate_limit, status, dhcp_option, 
                                                            last_seen, expires_after,active_address, 
                                                            disabled, radius, dynamic, blocked).where(
                                                                # mac_address == val,
                                                                Or(
                                                                    address == val,
                                                                    mac_address == val
                                                                )):
            AR.append(row)
        if AR == []:
            return('Empty Search Value')        
        return(AR) 

    def routing_bgp_peer_info(self, ip, api_port, api_login, api_passw):
        api = connect(username=api_login, password=api_passw, host=ip, port=api_port)
        #Flags: X - disabled, E - established  
        instance = Key('instance')
        remote_address = Key('remote-address')
        local_address = Key('local-address')
        remote_as = Key('remote-as')
        nexthop_choice = Key('nexthop-choice')
        default_originate = Key('default-originate')
        disabled = Key('disabled') 
        established = Key('established')

        AR = []
        for row in api.path('/routing/bgp/peer').select(instance, remote_address,  local_address, remote_as, nexthop_choice, 
                                                        default_originate, disabled, established, disabled,):
            AR.append(row)
        if AR == []:
            return('Empty Search Value')        
        return(AR) 
        
    def routing_filter_info(self, ip, api_port, api_login, api_passw):
        api = connect(username=api_login, password=api_passw, host=ip, port=api_port)
        #Flags: X - disabled
        chain = Key('chain')
        prefix = Key('prefix')
        invert_match = Key('invert-match')
        action = Key('action')
        set_bgp_prepend_path = Key('set-bgp-prepend-path')

        AR = []
        for row in api.path('/routing/filter').select(chain, prefix, invert_match, action, set_bgp_prepend_path):
            AR.append(row)
        if AR == []:
            return('Empty Search Value')        
        return(AR) 

    def ip_firewall_filter_info(self, ip, api_port, api_login, api_passw):
        api = connect(username=api_login, password=api_passw, host=ip, port=api_port)
        #Flags: X - disabled, I - invalid, D - dynamic
        chain = Key('chain')
        action = Key('action')
        dynamic = Key('dynamic')
        disabled = Key('disabled')
        invalid = Key('invalid')


        AR = []
        for row in api.path('/ip/firewall/filter').select(chain, action, dynamic, disabled, invalid):
            AR.append(row)
        if AR == []:
            return('Empty Search Value')        
        return(AR) 
    

         
         
    

    def ip_route_info(self, ip, api_port, api_login, api_passw):
        api = connect(username=api_login, password=api_passw, host=ip, port=api_port)
        #Flags: X-disabled, A-active, D-dynamic, C-connect, S-static, r-rip, b-bgp, o-ospf, m-mme, B-blackhole, U-unreachable, P-prohibit
        dst_address = Key('dst-address')
        pref_rc = Key('pref-src')
        gateway = Key('gateway')
        gateway_status = ('gateway-status')
        distance = Key('distance')
        scope = Key('scope')
        disabled = Key('disabled')
        active = Key('active')
        dynamic = Key('dynamic')
        connected = Key('connected')
        static = Key('static')
        rip = Key('rip')
        bgp = Key('bgp')
        ospf = Key('ospf')
        mme = Key('mme')
        blackhole = Key('blackhole')
        unreachable = Key('unreachable')
        prohibit = Key('prohibit')


        AR = []
        for row in api.path('/ip/route').select(dst_address,  pref_rc, gateway, gateway_status, distance, 
                                               scope, disabled, active, dynamic,connected, static, rip, bgp, 
                                               ospf, mme, blackhole, unreachable, prohibit):
            AR.append(row)
        if AR == []:
            return('Empty Search Value')        
        return(AR) 




    def connection_info(self, ip, api_port, api_login, api_passw, val): 
        api = connect(username=api_login, password=api_passw, host=ip, port=api_port)     

        #Flags: E - expected, S - seen-reply, A - assured, C - confirmed, D - dying, F - fasttrack, s - srcnat, d - dstnat

        protocol = Key('protocol')
        src = Key('src-address')
        dst = Key('dst-address')
        reply_src_address = Key('reply-src-address')
        reply_dst_address = Key('reply-dst-address')
        tcp_state = Key('tcp-state')
        timeout = Key('timeout')
        expected = Key('expected')
        seen_reply = Key('seen-reply')
        assured = Key('assured')
        confirmed = Key('confirmed')
        dying = Key('dying')
        fasttrack = Key('fasttrack')
        srcnat = Key('srcnat')
        dstnat = Key('dstnat')

        AR = []
        for row in api.path( '/ip/firewall/connection').select(protocol,src,dst,reply_src_address,reply_dst_address,
                                            tcp_state, timeout,expected,seen_reply,assured,confirmed,
                                            dying,fasttrack,srcnat,dstnat):
            if val in row['src-address']:
                AR.append(row)
        if AR == []:
            return('Empty Search Value')        
        return(AR)

    def arp_ping_info(self, ip, api_port, api_login, api_passw, address, interface): 
        api = connect(username=api_login, password=api_passw, host=ip, port=api_port)
        # SEQ HOST                                     SIZE TTL TIME  STATUS 
        #sent=4 received=4 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=1ms
        p = api.path('/')
        return(list(p('ping', **{'arp-ping': 'yes', 'interface': interface, 'address': address ,'count': '4'})))

