expected_output =  {
    "feature":{
        "appqoe":{
            "global":{
                "ip_non_tcp_pkts":3465,
                "not_enabled":0,
                "cft_handle_pkt":0,
                "sdvt_divert_req_fail":4875,
                "appqoe_sn_data_pkts_processed":0,
                "appqoe_alloc_empty_ht_entry":167,
                "appqoe_cvla_alloc_failure":0,
                "appqoe_bulk_upd_mem_bm_no_sng":0,
                "appqoe_srv_chain_transit_dre_bypass":0,
                "appqoe_srv_chain_sn_unhealthy_bypass":0,
                "appqoe_srv_chain_tcp_mid_flow_bypass":0,
                "appqoe_srv_chain_non_tcp_bypass":0,
                "appqoe_srv_chain_frag_bypass":0,
                "appqoe_lb_without_dre":91443,
                "appqoe_svc_on_appqoe_vpn_drop":0,
                "sdvt_global_stats":{
                    "within_sdvt_syn_policer_limit":33564136
                }
            },
            "sng":{
                "1":{
                    "sn_index":{
                        "1 (Green)":{
                            "ip":"8.3.2.2",
                            "oce_id":3367025888,
                            "appnav_stats":{
                                "to_sn":{
                                    "packets":1035776716,
                                    "bytes":575864308026
                                },
                                "from_sn":{
                                    "packets":1255356096,
                                    "bytes":933986254184
                                }
                            },
                            "sdvt_count_stats":{
                                "decaps":1248949630,
                                "encaps":1035776716,
                                "expired_connections":6406466,
                                "decap_messages":{
                                    "processed_control_messages":6406466,
                                    "delete_requests_recieved":6406466,
                                    "deleted_protocol_decision":6406466
                                }
                            },
                            "sdvt_packet_stats":{
                                "divert":{
                                    "packets":1035776716,
                                    "bytes":526147025658
                                },
                                "reinject":{
                                    "packets":1246851434,
                                    "bytes":853651673043
                                }
                            },
                            "sdvt_drop_cause_stats":{
                                
                            },
                            "sdvt_errors_stats":{
                                
                            }
                        }
                    }
                }
            },
            "sn_index":{
                "Default":{
                    "sdvt_count_stats":{
                        "non_syn_divert_requests":4875
                    },
                    "sdvt_packet_stats":{
                        
                    },
                    "sdvt_drop_cause_stats":{
                        
                    },
                    "sdvt_errors_stats":{
                        
                    }
                }
            }
        }
    }
}
