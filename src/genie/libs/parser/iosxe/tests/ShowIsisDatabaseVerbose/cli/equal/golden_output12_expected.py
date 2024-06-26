expected_output = {
    'tag': {
        '1': {
            'level': {
                1: {
                    'R1.00-00': {
                        'area_address': '50.1234',
                        'attach_bit': 0,
                        'd_flag': False,
                        'end_behavior': 'uN (PSP/USD)',
                        'end_sid': 'FCCC:CCC1:A1::',
                        'extended_is_neighbor': {
                            'R2.00': [{'neighbor_id': 'R2.00', 'metric': 10, 'admin_weight': 16777214, 'uni_link_loss': {'percent': '0.499998', 'anomalous': True}}],
                            'R3.00': [{'neighbor_id': 'R3.00', 'metric': 10, 'admin_weight': 100000, 'uni_link_loss': {'percent': '0.499998', 'anomalous': True}}],
                        },
                        'hostname': 'R1',
                        'ip_address': '1.1.1.1',
                        'ipv4_internal_reachability': {
                            '1.1.1.1/32': [{'ip_prefix': '1.1.1.1', 'prefix_len': '32', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': True}, 'source_router_id': '1.1.1.1'}],
                            '12.1.1.0/24': [{'ip_prefix': '12.1.1.0', 'prefix_len': '24', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '13.1.1.0/24': [{'ip_prefix': '13.1.1.0', 'prefix_len': '24', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                        },
                        'ipv6_address': '111::111',
                        'ipv6_router_id': '111::111',
                        'local_router': True,
                        'lsp_checksum': '0x3071',
                        'lsp_holdtime': '1188',
                        'lsp_rcvd': '*',
                        'lsp_sequence_num': '0x00000006',
                        'mt_ipv6_reachability': {
                            '111::111/128': [{'ip_prefix': '111::111', 'prefix_len': '128', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': True}}],
                            '12:12::/64': [{'ip_prefix': '12:12::', 'prefix_len': '64', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '13:13::/64': [{'ip_prefix': '13:13::', 'prefix_len': '64', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            'FCCC:CCC1:A1::/48': [{'ip_prefix': 'FCCC:CCC1:A1::', 'prefix_len': '48', 'metric': 0, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                        },
                        'mt_is_neighbor': {
                            'R2.00': [{'neighbor_id': 'R2.00', 'metric': 10, 'interface_ipv6_address': '12:12::1', 'neighbor_ipv6_address': '12:12::2', 'admin_weight': 16777214, 'end_x_sid': 'FCCC:CCC1:A1:E000::', 'end_x_b_flag': 0, 'end_x_s_flag': 0, 'end_x_p_flag': 0, 'end_x_algorithm': 0, 'end_x_weight': 0}],
                            'R3.00': [{'neighbor_id': 'R3.00', 'metric': 10, 'interface_ipv6_address': '13:13::1', 'neighbor_ipv6_address': '13:13::2', 'admin_weight': 100000, 'end_x_sid': 'FCCC:CCC1:A1:E001::', 'end_x_b_flag': 0, 'end_x_s_flag': 0, 'end_x_p_flag': 0, 'end_x_algorithm': 0, 'end_x_weight': 0}],
                        },
                        'nlpid': '0xCC 0x8E',
                        'overload_bit': 0,
                        'p_bit': 0,
                        'router_cap': '1.1.1.1',
                        'router_id': '1.1.1.1',
                        's_flag': False,
                        'srv6_algorithm': '0',
                        'srv6_locator': 'FCCC:CCC1:A1::/48',
                        'srv6_metric': '0',
                        'srv6_o_flag': False,
                        'topology': {
                            'ipv4': {
                                'code': '0x0',
                            },
                            'ipv6': {
                                'code': '0x2',
                            },
                        },
                    },
                    'R2.00-00': {
                        'area_address': '50.1234',
                        'attach_bit': 0,
                        'd_flag': False,
                        'end_behavior': 'uN (PSP/USD)',
                        'end_sid': 'FCCC:CCC1:B1::',
                        'extended_is_neighbor': {
                            'R1.00': [{'neighbor_id': 'R1.00', 'metric': 10, 'admin_weight': 16777214}],
                            'R4.00': [{'neighbor_id': 'R4.00', 'metric': 10, 'admin_weight': 100000}],
                        },
                        'hostname': 'R2',
                        'ip_address': '2.2.2.2',
                        'ipv4_internal_reachability': {
                            '12.1.1.0/24': [{'ip_prefix': '12.1.1.0', 'prefix_len': '24', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '2.2.2.2/32': [{'ip_prefix': '2.2.2.2', 'prefix_len': '32', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': True}, 'source_router_id': '2.2.2.2'}],
                            '24.1.1.0/24': [{'ip_prefix': '24.1.1.0', 'prefix_len': '24', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                        },
                        'ipv6_address': '222::222',
                        'ipv6_router_id': '222::222',
                        'lsp_checksum': '0xC1E9',
                        'lsp_holdtime': '1186',
                        'lsp_rcvd': '1200',
                        'lsp_sequence_num': '0x00000006',
                        'mt_ipv6_reachability': {
                            '12:12::/64': [{'ip_prefix': '12:12::', 'prefix_len': '64', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '222::222/128': [{'ip_prefix': '222::222', 'prefix_len': '128', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': True}}],
                            '24:24::/64': [{'ip_prefix': '24:24::', 'prefix_len': '64', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            'FCCC:CCC1:B1::/48': [{'ip_prefix': 'FCCC:CCC1:B1::', 'prefix_len': '48', 'metric': 0, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                        },
                        'mt_is_neighbor': {
                            'R1.00': [{'neighbor_id': 'R1.00', 'metric': 10, 'interface_ipv6_address': '12:12::2', 'neighbor_ipv6_address': '12:12::1', 'admin_weight': 16777214, 'end_x_sid': 'FCCC:CCC1:B1:E001::', 'end_x_b_flag': 0, 'end_x_s_flag': 0, 'end_x_p_flag': 0, 'end_x_algorithm': 0, 'end_x_weight': 0}],
                            'R4.00': [{'neighbor_id': 'R4.00', 'metric': 10, 'interface_ipv6_address': '24:24::1', 'neighbor_ipv6_address': '24:24::2', 'admin_weight': 100000, 'end_x_sid': 'FCCC:CCC1:B1:E000::', 'end_x_b_flag': 0, 'end_x_s_flag': 0, 'end_x_p_flag': 0, 'end_x_algorithm': 0, 'end_x_weight': 0}],
                        },
                        'nlpid': '0xCC 0x8E',
                        'overload_bit': 0,
                        'p_bit': 0,
                        'router_cap': '2.2.2.2',
                        'router_id': '2.2.2.2',
                        's_flag': False,
                        'srv6_algorithm': '0',
                        'srv6_locator': 'FCCC:CCC1:B1::/48',
                        'srv6_metric': '0',
                        'srv6_o_flag': False,
                        'topology': {
                            'ipv4': {
                                'code': '0x0',
                            },
                            'ipv6': {
                                'code': '0x2',
                            },
                        },
                    },
                    'R3.00-00': {
                        'area_address': '50.1234',
                        'attach_bit': 0,
                        'd_flag': False,
                        'end_behavior': 'uN (PSP/USD)',
                        'end_sid': 'FCCC:CCC1:C1::',
                        'extended_is_neighbor': {
                            'R1.00': [{'neighbor_id': 'R1.00', 'metric': 10, 'admin_weight': 16777214}],
                            'R5.00': [{'neighbor_id': 'R5.00', 'metric': 10, 'admin_weight': 100000}],
                        },
                        'hostname': 'R3',
                        'ip_address': '3.3.3.3',
                        'ipv4_internal_reachability': {
                            '13.1.1.0/24': [{'ip_prefix': '13.1.1.0', 'prefix_len': '24', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '3.3.3.3/32': [{'ip_prefix': '3.3.3.3', 'prefix_len': '32', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': True}, 'source_router_id': '3.3.3.3'}],
                            '35.1.1.0/24': [{'ip_prefix': '35.1.1.0', 'prefix_len': '24', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                        },
                        'ipv6_address': '333::333',
                        'ipv6_router_id': '333::333',
                        'lsp_checksum': '0x777B',
                        'lsp_holdtime': '1187',
                        'lsp_rcvd': '1200',
                        'lsp_sequence_num': '0x00000005',
                        'mt_ipv6_reachability': {
                            '13:13::/64': [{'ip_prefix': '13:13::', 'prefix_len': '64', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '333::333/128': [{'ip_prefix': '333::333', 'prefix_len': '128', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': True}}],
                            '35:35::/64': [{'ip_prefix': '35:35::', 'prefix_len': '64', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            'FCCC:CCC1:C1::/48': [{'ip_prefix': 'FCCC:CCC1:C1::', 'prefix_len': '48', 'metric': 0, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                        },
                        'mt_is_neighbor': {
                            'R1.00': [{'neighbor_id': 'R1.00', 'metric': 10, 'interface_ipv6_address': '13:13::2', 'neighbor_ipv6_address': '13:13::1', 'admin_weight': 16777214, 'end_x_sid': 'FCCC:CCC1:C1:E001::', 'end_x_b_flag': 0, 'end_x_s_flag': 0, 'end_x_p_flag': 0, 'end_x_algorithm': 0, 'end_x_weight': 0}],
                            'R5.00': [{'neighbor_id': 'R5.00', 'metric': 10, 'interface_ipv6_address': '35:35::1', 'neighbor_ipv6_address': '35:35::2', 'admin_weight': 100000, 'end_x_sid': 'FCCC:CCC1:C1:E000::', 'end_x_b_flag': 0, 'end_x_s_flag': 0, 'end_x_p_flag': 0, 'end_x_algorithm': 0, 'end_x_weight': 0}],
                        },
                        'nlpid': '0xCC 0x8E',
                        'overload_bit': 0,
                        'p_bit': 0,
                        'router_cap': '3.3.3.3',
                        'router_id': '3.3.3.3',
                        's_flag': False,
                        'srv6_algorithm': '0',
                        'srv6_locator': 'FCCC:CCC1:C1::/48',
                        'srv6_metric': '0',
                        'srv6_o_flag': False,
                        'topology': {
                            'ipv4': {
                                'code': '0x0',
                            },
                            'ipv6': {
                                'code': '0x2',
                            },
                        },
                    },
                    'R4.00-00': {
                        'area_address': '50.1234',
                        'attach_bit': 0,
                        'd_flag': False,
                        'end_behavior': 'uN (PSP/USD)',
                        'end_sid': 'FCCC:CCC1:D1::',
                        'extended_is_neighbor': {
                            'R2.00': [{'neighbor_id': 'R2.00', 'metric': 10, 'admin_weight': 16777214}],
                            'R6.00': [{'neighbor_id': 'R6.00', 'metric': 10, 'admin_weight': 100000}],
                        },
                        'hostname': 'R4',
                        'ip_address': '4.4.4.4',
                        'ipv4_internal_reachability': {
                            '24.1.1.0/24': [{'ip_prefix': '24.1.1.0', 'prefix_len': '24', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '4.4.4.4/32': [{'ip_prefix': '4.4.4.4', 'prefix_len': '32', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': True}, 'source_router_id': '4.4.4.4'}],
                            '46.1.1.0/24': [{'ip_prefix': '46.1.1.0', 'prefix_len': '24', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                        },
                        'ipv6_address': '444::444',
                        'ipv6_router_id': '444::444',
                        'lsp_checksum': '0x6136',
                        'lsp_holdtime': '1188',
                        'lsp_rcvd': '1199',
                        'lsp_sequence_num': '0x00000006',
                        'mt_ipv6_reachability': {
                            '24:24::/64': [{'ip_prefix': '24:24::', 'prefix_len': '64', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '444::444/128': [{'ip_prefix': '444::444', 'prefix_len': '128', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': True}}],
                            '46:46::/64': [{'ip_prefix': '46:46::', 'prefix_len': '64', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            'FCCC:CCC1:D1::/48': [{'ip_prefix': 'FCCC:CCC1:D1::', 'prefix_len': '48', 'metric': 0, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                        },
                        'mt_is_neighbor': {
                            'R2.00': [{'neighbor_id': 'R2.00', 'metric': 10, 'interface_ipv6_address': '24:24::2', 'neighbor_ipv6_address': '24:24::1', 'admin_weight': 16777214, 'end_x_sid': 'FCCC:CCC1:D1:E001::', 'end_x_b_flag': 0, 'end_x_s_flag': 0, 'end_x_p_flag': 0, 'end_x_algorithm': 0, 'end_x_weight': 0}],
                            'R6.00': [{'neighbor_id': 'R6.00', 'metric': 10, 'interface_ipv6_address': '46:46::1', 'neighbor_ipv6_address': '46:46::2', 'admin_weight': 100000, 'end_x_sid': 'FCCC:CCC1:D1:E000::', 'end_x_b_flag': 0, 'end_x_s_flag': 0, 'end_x_p_flag': 0, 'end_x_algorithm': 0, 'end_x_weight': 0}],
                        },
                        'nlpid': '0xCC 0x8E',
                        'overload_bit': 0,
                        'p_bit': 0,
                        'router_cap': '4.4.4.4',
                        'router_id': '4.4.4.4',
                        's_flag': False,
                        'srv6_algorithm': '0',
                        'srv6_locator': 'FCCC:CCC1:D1::/48',
                        'srv6_metric': '0',
                        'srv6_o_flag': False,
                        'topology': {
                            'ipv4': {
                                'code': '0x0',
                            },
                            'ipv6': {
                                'code': '0x2',
                            },
                        },
                    },
                    'R5.00-00': {
                        'area_address': '50.1234',
                        'attach_bit': 0,
                        'd_flag': False,
                        'end_behavior': 'uN (PSP/USD)',
                        'end_sid': 'FCCC:CCC1:E1::',
                        'extended_is_neighbor': {
                            'R3.00': [{'neighbor_id': 'R3.00', 'metric': 10, 'admin_weight': 100000}],
                            'R6.00': [{'neighbor_id': 'R6.00', 'metric': 10, 'admin_weight': 16777214}],
                        },
                        'hostname': 'R5',
                        'ip_address': '5.5.5.5',
                        'ipv4_internal_reachability': {
                            '35.1.1.0/24': [{'ip_prefix': '35.1.1.0', 'prefix_len': '24', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '5.5.5.5/32': [{'ip_prefix': '5.5.5.5', 'prefix_len': '32', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': True}, 'source_router_id': '5.5.5.5'}],
                            '56.1.1.0/24': [{'ip_prefix': '56.1.1.0', 'prefix_len': '24', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                        },
                        'ipv6_address': '555::555',
                        'ipv6_router_id': '555::555',
                        'lsp_checksum': '0x1554',
                        'lsp_holdtime': '1188',
                        'lsp_rcvd': '1199',
                        'lsp_sequence_num': '0x00000005',
                        'mt_ipv6_reachability': {
                            '35:35::/64': [{'ip_prefix': '35:35::', 'prefix_len': '64', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '555::555/128': [{'ip_prefix': '555::555', 'prefix_len': '128', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': True}}],
                            '56:56::/64': [{'ip_prefix': '56:56::', 'prefix_len': '64', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            'FCCC:CCC1:E1::/48': [{'ip_prefix': 'FCCC:CCC1:E1::', 'prefix_len': '48', 'metric': 0, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                        },
                        'mt_is_neighbor': {
                            'R3.00': [{'neighbor_id': 'R3.00', 'metric': 10, 'interface_ipv6_address': '35:35::2', 'neighbor_ipv6_address': '35:35::1', 'admin_weight': 100000, 'end_x_sid': 'FCCC:CCC1:E1:E000::', 'end_x_b_flag': 0, 'end_x_s_flag': 0, 'end_x_p_flag': 0, 'end_x_algorithm': 0, 'end_x_weight': 0}],
                            'R6.00': [{'neighbor_id': 'R6.00', 'metric': 10, 'interface_ipv6_address': '56:56::1', 'neighbor_ipv6_address': '56:56::2', 'admin_weight': 16777214, 'end_x_sid': 'FCCC:CCC1:E1:E001::', 'end_x_b_flag': 0, 'end_x_s_flag': 0, 'end_x_p_flag': 0, 'end_x_algorithm': 0, 'end_x_weight': 0}],
                        },
                        'nlpid': '0xCC 0x8E',
                        'overload_bit': 0,
                        'p_bit': 0,
                        'router_cap': '5.5.5.5',
                        'router_id': '5.5.5.5',
                        's_flag': False,
                        'srv6_algorithm': '0',
                        'srv6_locator': 'FCCC:CCC1:E1::/48',
                        'srv6_metric': '0',
                        'srv6_o_flag': False,
                        'topology': {
                            'ipv4': {
                                'code': '0x0',
                            },
                            'ipv6': {
                                'code': '0x2',
                            },
                        },
                    },
                    'R6.00-00': {
                        'area_address': '50.1234',
                        'attach_bit': 0,
                        'd_flag': False,
                        'end_behavior': 'uN (PSP/USD)',
                        'end_sid': 'FCCC:CCC1:F1::',
                        'extended_is_neighbor': {
                            'R4.00': [{'neighbor_id': 'R4.00', 'metric': 10, 'admin_weight': 16777214}],
                            'R5.00': [{'neighbor_id': 'R5.00', 'metric': 10, 'admin_weight': 100000}],
                        },
                        'hostname': 'R6',
                        'ip_address': '6.6.6.6',
                        'ipv4_internal_reachability': {
                            '46.1.1.0/24': [{'ip_prefix': '46.1.1.0', 'prefix_len': '24', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '56.1.1.0/24': [{'ip_prefix': '56.1.1.0', 'prefix_len': '24', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '6.6.6.6/32': [{'ip_prefix': '6.6.6.6', 'prefix_len': '32', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': True}, 'source_router_id': '6.6.6.6'}],
                        },
                        'ipv6_address': '666::666',
                        'ipv6_router_id': '666::666',
                        'lsp_checksum': '0xC01A',
                        'lsp_holdtime': '1188',
                        'lsp_rcvd': '1199',
                        'lsp_sequence_num': '0x00000005',
                        'mt_ipv6_reachability': {
                            '46:46::/64': [{'ip_prefix': '46:46::', 'prefix_len': '64', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '56:56::/64': [{'ip_prefix': '56:56::', 'prefix_len': '64', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                            '666::666/128': [{'ip_prefix': '666::666', 'prefix_len': '128', 'metric': 10, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': True}}],
                            'FCCC:CCC1:F1::/48': [{'ip_prefix': 'FCCC:CCC1:F1::', 'prefix_len': '48', 'metric': 0, 'prefix_attr': {'x_flag': False, 'r_flag': False, 'n_flag': False}}],
                        },
                        'mt_is_neighbor': {
                            'R4.00': [{'neighbor_id': 'R4.00', 'metric': 10, 'interface_ipv6_address': '46:46::2', 'neighbor_ipv6_address': '46:46::1', 'admin_weight': 16777214, 'end_x_sid': 'FCCC:CCC1:F1:E000::', 'end_x_b_flag': 0, 'end_x_s_flag': 0, 'end_x_p_flag': 0, 'end_x_algorithm': 0, 'end_x_weight': 0}],
                            'R5.00': [{'neighbor_id': 'R5.00', 'metric': 10, 'interface_ipv6_address': '56:56::2', 'neighbor_ipv6_address': '56:56::1', 'admin_weight': 100000, 'end_x_sid': 'FCCC:CCC1:F1:E001::', 'end_x_b_flag': 0, 'end_x_s_flag': 0, 'end_x_p_flag': 0, 'end_x_algorithm': 0, 'end_x_weight': 0}],
                        },
                        'nlpid': '0xCC 0x8E',
                        'overload_bit': 0,
                        'p_bit': 0,
                        'router_cap': '6.6.6.6',
                        'router_id': '6.6.6.6',
                        's_flag': False,
                        'srv6_algorithm': '0',
                        'srv6_locator': 'FCCC:CCC1:F1::/48',
                        'srv6_metric': '0',
                        'srv6_o_flag': False,
                        'topology': {
                            'ipv4': {
                                'code': '0x0',
                            },
                            'ipv6': {
                                'code': '0x2',
                            },
                        },
                    },
                },
            },
        },
    },
}
