

expected_output = {
    'global_configuration': {
        'enabled': 'enabled',
        'v1v2_report_suppression': 'enabled',
        'v3_report_suppression': 'disabled',
        'link_local_groups_suppression': 'enabled',
        'vpc_multicast_optimization': 'disabled',
    },
    'vlans': {
        '1': {  # configuration_vlan_id
            'ip_igmp_snooping': 'enabled',
            'v1v2_report_suppression': 'enabled',
            'v3_report_suppression': 'disabled',
            'link_local_groups_suppression': 'enabled',
            'lookup_mode': 'ip',
            'switch_querier': 'disabled',
            'igmp_explicit_tracking': 'enabled',
            'v2_fast_leave': 'disabled',
            'router_ports_count': 1,
            'groups_count': 0,
            'vlan_vpc_function': 'enabled',
            'active_ports': ['Po20','Po30'],
            'report_flooding': 'disabled',
            'report_flooding_interfaces': 'n/a',
            'group_address_for_proxy_leaves': 'no',
            },
        '100': {  # configuration_vlan_id
            'ip_igmp_snooping': 'enabled',
            'v1v2_report_suppression': 'enabled',
            'v3_report_suppression': 'disabled',
            'link_local_groups_suppression': 'enabled',
            'lookup_mode': 'ip',
            'igmp_querier': {
                'address': '10.51.1.1',
                'version': 2,
                'interval': 125,
                'last_member_query_interval': 1,
                'robustness': 2,
            },
            'switch_querier': 'disabled',
            'igmp_explicit_tracking': 'enabled',
            'v2_fast_leave': 'disabled',
            'router_ports_count': 2,
            'groups_count': 0,
            'vlan_vpc_function': 'enabled',
            'active_ports': ['Po20', 'Po30'],
            'report_flooding': 'disabled',
            'report_flooding_interfaces': 'n/a',
            'group_address_for_proxy_leaves': 'no',
            },
        '101': {  # configuration_vlan_id
            'ip_igmp_snooping': 'enabled',
            'v1v2_report_suppression': 'enabled',
            'v3_report_suppression': 'disabled',
            'link_local_groups_suppression': 'enabled',
            'lookup_mode': 'ip',
            'switch_querier': 'disabled',
            'igmp_explicit_tracking': 'enabled',
            'v2_fast_leave': 'disabled',
            'router_ports_count': 1,
            'groups_count': 0,
            'vlan_vpc_function': 'enabled',
            'active_ports': ['Po20', 'Po30'],
            'report_flooding': 'disabled',
            'report_flooding_interfaces': 'n/a',
            'group_address_for_proxy_leaves': 'no',
        },
    },
}