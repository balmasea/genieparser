expected_output = {
    "slot": {
        "lc": {
            "0/0": {
                "name": "MSC-B",
                "full_slot": "0/0/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "plim": "8-10GbE",
            },
            "0/3": {
                "name": "MSC-140G",
                "full_slot": "0/3/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "plim": "Services Plim",
                "subslot": {
                    "0": {
                        "name": "MSC-140G",
                        "state": "OK",
                        "config_state": "PWR,NSHUT,MON",
                        "redundancy_state": "SPA",
                    }
                },
            },
            "0/6": {
                "name": "MSC-X",
                "full_slot": "0/6/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "plim": "4-100GbE",
            },
            "0/7": {
                "name": "FP-X",
                "full_slot": "0/7/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "plim": "4-100GbE",
            },
            "0/9": {
                "name": "MSC-B",
                "full_slot": "0/9/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "plim": "4-10GbE",
            },
            "0/11": {
                "name": "MSC",
                "full_slot": "0/11/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,NMON",
                "plim": "4-10GbE",
            },
            "0/13": {
                "name": "MSC-B",
                "full_slot": "0/13/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "plim": "4OC192-POS/DPT",
            },
        },
        "rp": {
            "0/RP0": {
                "name": "RP",
                "full_slot": "0/RP0/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "redundancy_state": "Active",
                "plim": "N/A",
            },
            "0/RP1": {
                "name": "RP",
                "full_slot": "0/RP1/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "redundancy_state": "Standby",
                "plim": "N/A",
            },
            "1/RP0": {
                "name": "RP",
                "full_slot": "1/RP0/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "redundancy_state": "Active",
                "plim": "N/A",
            },
            "1/RP1": {
                "name": "RP",
                "full_slot": "1/RP1/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "redundancy_state": "Standby",
                "plim": "N/A",
            },
        },
        "oc": {
            "1/2": {
                "name": "MSC-X",
                "full_slot": "1/2/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "plim": "40-10GbE",
            },
            "1/3": {
                "name": "MSC",
                "full_slot": "1/3/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "plim": "Jacket Card",
                "subslot": {
                    "0": {
                        "name": "MSC",
                        "state": "OK",
                        "config_state": "PWR,NSHUT,MON",
                        "redundancy_state": "SPA",
                    },
                    "1": {
                        "name": "MSC",
                        "state": "OK",
                        "config_state": "PWR,NSHUT,MON",
                        "redundancy_state": "SPA",
                    },
                    "3": {
                        "name": "MSC",
                        "state": "DISABLED",
                        "config_state": "NPWR,SHUT,MON",
                        "redundancy_state": "SPA",
                    },
                    "5": {
                        "name": "MSC",
                        "state": "OK",
                        "config_state": "PWR,NSHUT,MON",
                        "redundancy_state": "SPA",
                    },
                },
            },
            "1/4": {
                "name": "LSP-X",
                "full_slot": "1/4/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "plim": "40-10GbE",
            },
            "1/5": {
                "name": "MSC",
                "full_slot": "1/5/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "plim": "1OC768-POS",
            },
            "1/6": {
                "name": "MSC-140G",
                "full_slot": "1/6/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "plim": "14-10GbE",
            },
            "1/7": {
                "name": "MSC",
                "full_slot": "1/7/CPU0",
                "state": "IOS XR RUN",
                "config_state": "PWR,NSHUT,MON",
                "plim": "1OC768-POS",
            },
            "1/10": {
                "name": "FP-X",
                "full_slot": "1/10/CPU0",
                "state": "UNPOWERED",
                "config_state": "NPWR,NSHUT,MON",
                "plim": "N/A",
            },
        },
    }
}
