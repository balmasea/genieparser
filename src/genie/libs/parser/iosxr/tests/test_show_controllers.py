
# Python
import unittest
from unittest.mock import Mock

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# iosxr show_controllers
from genie.libs.parser.iosxr.show_controllers import (ShowControllersCoherentDSP,
                                                     ShowControllersOptics,
                                                     ShowControllersFiaDiagshellL2showLocation,
                                                     ShowControllersFiaDiagshellDiagEgrCalendarsLocation,
                                                     ShowControllersNpuInterfaceInstanceLocation)


# =====================================================
#  Unit test for 'show controllers coherentDSP {port}'
# =====================================================
class test_show_controllers_coherentDSP(unittest.TestCase):
    '''Unit test for show controllers coherentDSP {port}'''

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "0/0/1/2": {
            "port": "CoherentDSP 0/0/1/2",
            "controller_state": "Up",
            "inherited_secondary_state": "Normal",
            "configured_secondary_state": "Normal",
            "derived_state": "In Service",
            "loopback_mode": "None",
            "ber_thresholds_sf": "1.0E-5",
            "ber_thresholds_sd": "1.0E-7",
            "performance_monitoring": "Enable",
            "alarm_info": {
                "los": 1,
                "lof": 0,
                "lom": 0,
                "oof": 0,
                "oom": 0,
                "ais": 0,
                "iae": 0,
                "biae": 0,
                "sf_ber": 0,
                "sd_ber": 0,
                "bdi": 2,
                "tim": 0,
                "fecmis_match": 0,
                "fec_unc": 0
            },
            "detected_alarms": "None",
            "bit_error_rate_info": {
                "prefec_ber": "0.0E+00",
                "postfec_ber": "0.0E+00",
            },
            "otu_tti": "Received",
            "fec_mode": "STANDARD"
        },
    }

    golden_output = {'execute.return_value': '''
        #show controllers coherentDSP 0/0/1/2
        Sat Aug  3 03:10:15.685 EST

        Port                                            : CoherentDSP 0/0/1/2
        Controller State                                : Up
        Inherited Secondary State                       : Normal
        Configured Secondary State                      : Normal
        Derived State                                   : In Service
        Loopback mode                                   : None
        BER Thresholds                                  : SF = 1.0E-5  SD = 1.0E-7
        Performance Monitoring                          : Enable

        Alarm Information:
        LOS = 1 LOF = 0 LOM = 0
        OOF = 0 OOM = 0 AIS = 0
        IAE = 0 BIAE = 0        SF_BER = 0
        SD_BER = 0      BDI = 2 TIM = 0
        FECMISMATCH = 0 FEC-UNC = 0     
        Detected Alarms                                 : None

        Bit Error Rate Information
        PREFEC  BER                                     : 0.0E+00 
        POSTFEC BER                                     : 0.0E+00 

        OTU TTI Received 

        FEC mode                                        : STANDARD
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowControllersCoherentDSP(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(port='0/0/1/2')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowControllersCoherentDSP(device=self.device)
        parsed_output = obj.parse(port='0/0/1/2')
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ==================================================
#  Unit test for 'show controllers optics {port}'
# ==================================================
class test_show_controllers_optics(unittest.TestCase):
    '''Unit test for show controllers optics {port}'''

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        "0/0/0/0": {
            "name": "Optics 0/0/0/0",
            "controller_state": "Up",
            "transport_admin_state": "In Service",
            "laser_state": "On",
            "led_state": "Green",
            "optics_status": {
                "optics_type": "SFP+ 10G SR",
                "wavelength": "850.00 nm",
                "alarm_status": {
                    "detected_alarms": [],
                },
                "los_lol_fault_status": {},
                "laser_bias_current": "6.1 mA",
                "actual_tx_power": "-2.45 dBm",
                "rx_power": "-7.56 dBm",
                "performance_monitoring": "Enable",
                "threshold_values": {
                    "Rx Power Threshold(dBm)": {
                        "parameter": "Rx Power Threshold(dBm)",
                        "high_alarm": "2.0",
                        "low_alarm": "-13.9",
                        "high_warning": "-1.0",
                        "low_warning": "-9.9"
                    },
                    "Tx Power Threshold(dBm)": {
                        "parameter": "Tx Power Threshold(dBm)",
                        "high_alarm": "1.6",
                        "low_alarm": "-11.3",
                        "high_warning": "-1.3",
                        "low_warning": "-7.3"
                    },
                    "LBC Threshold(mA)": {
                        "parameter": "LBC Threshold(mA)",
                        "high_alarm": "10.00",
                        "low_alarm": "2.00",
                        "high_warning": "10.00",
                        "low_warning": "2.00"
                    },
                    "Temp. Threshold(celsius)": {
                        "parameter": "Temp. Threshold(celsius)",
                        "high_alarm": "75.00",
                        "low_alarm": "-5.00",
                        "high_warning": "70.00",
                        "low_warning": "0.00"
                    },
                    "Voltage Threshold(volt)": {
                        "parameter": "Voltage Threshold(volt)",
                        "high_alarm": "3.63",
                        "low_alarm": "2.97",
                        "high_warning": "3.46",
                        "low_warning": "3.13"
                    }
                },
                "polarization_parameters": "not supported by optics",
                "temperature": "35.00 Celsius",
                "voltage": "3.26 V"
            },
            "transceiver_vendor_details": {
                "form_factor": "SFP+",
                "optics_type": "SFP+ 10G SR",
                "name": "CISCO-AVAGO",
                "oui_number": "00.17.6a",
                "part_number": "SFBR-7702SDZ-CS5",
                "rev_number": "G2.5",
                "serial_number": "AGD162040SP",
                "pid": "SFP-10G-SR",
                "vid": "V03",
                "date_code": "12/05/20"
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
        #show controllers optics 0/0/0/0
        Sat Aug  3 03:11:08.682 EST

         Controller State: Up 
         Transport Admin State: In Service 
         Laser State: On 
         LED State: Green 
         Optics Status 
                 Optics Type:  SFP+ 10G SR
                 Wavelength = 850.00 nm 

                 Alarm Status:
                 -------------
                 Detected Alarms: None


                 LOS/LOL/Fault Status:

                 Laser Bias Current = 6.1 mA
                 Actual TX Power = -2.45 dBm 
                 RX Power = -7.56 dBm 

                 Performance Monitoring: Enable 

                 THRESHOLD VALUES
                 ----------------

                 Parameter                 High Alarm  Low Alarm  High Warning  Low Warning
                 ------------------------  ----------  ---------  ------------  -----------
                 Rx Power Threshold(dBm)          2.0      -13.9          -1.0         -9.9
                 Tx Power Threshold(dBm)          1.6      -11.3          -1.3         -7.3
                 LBC Threshold(mA)              10.00       2.00         10.00         2.00
                 Temp. Threshold(celsius)       75.00      -5.00         70.00         0.00
                 Voltage Threshold(volt)         3.63       2.97          3.46         3.13

                 Polarization parameters not supported by optics

                 Temperature = 35.00 Celsius 
                 Voltage = 3.26 V 

         Transceiver Vendor Details

                 Form Factor            : SFP+
                 Optics type            : SFP+ 10G SR
                 Name                   : CISCO-AVAGO
                 OUI Number             : 00.17.6a
                 Part Number            : SFBR-7702SDZ-CS5
                 Rev Number             : G2.5
                 Serial Number          : AGD162040SP
                 PID                    : SFP-10G-SR
                 VID                    : V03
                 Date Code(yy/mm/dd)    : 12/05/20
    '''}

    golden_parsed_output2 = {
        "0/0/1/2": {
            "name": "Optics 0/0/1/2",
            "controller_state": "Up",
            "transport_admin_state": "In Service",
            "laser_state": "On",
            "led_state": "Green",
            "optics_status": {
                "optics_type": "CFP2 DWDM",
                "dwdm_carrier_info": "C BAND",
                "msa_itu_channel": "97",
                "frequency": "191.30THz",
                "wavelength": "1567.133nm",
                "alarm_status": {
                    "detected_alarms": [],
                },
                "los_lol_fault_status": {},
                "alarm_statistics": {
                    "high_rx_pwr": 0,
                    "low_rx_pwr": 1,
                    "high_tx_pwr": 0,
                    "low_tx_pwr": 1,
                    "high_lbc": 0,
                    "high_dgd": 0,
                    "oor_cd": 0,
                    "osnr": 0,
                    "wvl_ool": 0,
                    "mea": 0,
                    "improper_rem": 0,
                    "tc_power_prov_mismatch": 0
                },
                "laser_bias_current": "0.0 %",
                "actual_tx_power": "0.99 dBm",
                "rx_power": "-20.50 dBm",
                "performance_monitoring": "Enable",
                "threshold_values": {
                    "Rx Power Threshold(dBm)": {
                        "parameter": "Rx Power Threshold(dBm)",
                        "high_alarm": "1.5",
                        "low_alarm": "-30.0",
                        "high_warning": "0.0",
                        "low_warning": "0.0"
                    },
                    "Tx Power Threshold(dBm)": {
                        "parameter": "Tx Power Threshold(dBm)",
                        "high_alarm": "3.5",
                        "low_alarm": "-10.0",
                        "high_warning": "0.0",
                        "low_warning": "0.0"
                    },
                    "LBC Threshold(mA)": {
                        "parameter": "LBC Threshold(mA)",
                        "high_alarm": "N/A",
                        "low_alarm": "N/A",
                        "high_warning": "0.00",
                        "low_warning": "0.00"
                    }
                },
                "lbc_high_threshold": "98 %",
                "configured_tx_power": "1.00 dBm",
                "configured_osnr_lower_threshold": "0.00 dB",
                "configured_dgd_higher_threshold": "180.00 ps",
                "chromatic_dispersion": "5 ps/nm",
                "configured_cd_min": "-10000 ps/nm ",
                "configured_cd_max": "16000 ps/nm",
                "optical_snr": "27.00 dB",
                "polarization_dependent_loss": "0.00 dB",
                "differential_group_delay": "2.00 ps"
            },
            "transceiver_vendor_details": {
                "form_factor": "CFP2",
                "name": "CISCO-ACACIA",
                "part_number": "AC200-D23-190",
                "rev_number": "16672",
                "serial_number": "180653009",
                "pid": "ONS-C2-WDM-DE-1HL",
                "vid": "VES#",
                "date_code": "18/02/03"
            }
        }
    }

    golden_output2 = {'execute.return_value': '''
        #show controllers optics 0/0/1/2
        Sat Aug  3 03:11:51.141 EST

         Controller State: Up 
         Transport Admin State: In Service 
         Laser State: On 
         LED State: Green 
         Optics Status 
                 Optics Type:  CFP2 DWDM
                 DWDM carrier Info: C BAND, MSA ITU Channel=97, Frequency=191.30THz,
                 Wavelength=1567.133nm 

                 Alarm Status:
                 -------------
                 Detected Alarms: None


                 LOS/LOL/Fault Status:

                 Alarm Statistics:

                 -------------
                 HIGH-RX-PWR = 0            LOW-RX-PWR = 1          
                 HIGH-TX-PWR = 0            LOW-TX-PWR = 1          
                 HIGH-LBC = 0               HIGH-DGD = 0          
                 OOR-CD = 0                 OSNR = 0          
                 WVL-OOL = 0                MEA  = 0          
                 IMPROPER-REM = 0          
                 TX-POWER-PROV-MISMATCH = 0          
                 Laser Bias Current = 0.0 %
                 Actual TX Power = 0.99 dBm 
                 RX Power = -20.50 dBm 

                 Performance Monitoring: Enable 

                 THRESHOLD VALUES
                 ----------------

                 Parameter                 High Alarm  Low Alarm  High Warning  Low Warning
                 ------------------------  ----------  ---------  ------------  -----------
                 Rx Power Threshold(dBm)          1.5      -30.0           0.0          0.0
                 Tx Power Threshold(dBm)          3.5      -10.0           0.0          0.0
                 LBC Threshold(mA)                N/A        N/A          0.00         0.00

                 LBC High Threshold = 98 % 
                 Configured Tx Power = 1.00 dBm 
                 Configured OSNR lower Threshold = 0.00 dB 
                 Configured DGD Higher Threshold = 180.00 ps 
                 Chromatic Dispersion 5 ps/nm 
                 Configured CD-MIN -10000 ps/nm  CD-MAX 16000 ps/nm 
                 Optical Signal to Noise Ratio = 27.00 dB 
                 Polarization Dependent Loss = 0.00 dB 
                 Differential Group Delay = 2.00 ps 
                  
         Transceiver Vendor Details
                  
                 Form Factor            : CFP2
                 Name                   : CISCO-ACACIA    
                 Part Number            : AC200-D23-190   
                 Rev Number             : 16672
                 Serial Number          : 180653009       
                 PID                    : ONS-C2-WDM-DE-1HL 
                 VID                    : VES#
                 Date Code(yy/mm/dd)    : 18/02/03
    '''}

    golden_parsed_output3 = {
        "0/0/0/20": {
            "name": "Optics 0/0/0/20",
            "controller_state": "Down",
            "transport_admin_state": "In Service",
            "laser_state": "Off",
            "optics_status": {
                "optics_type": "Unavailable",
                "dwdm_carrier_info": "Unavailable",
                "msa_itu_channel": "Unavailable",
                "frequency": "Unavailable",
                "wavelength": "Unavailable",
                "actual_tx_power": "Unavailable",
                "rx_power": "Unavailable"
            }
        }
    }

    golden_output3 = {'execute.return_value': '''
        #show controllers optics 0/0/0/20
        Sat Aug  3 03:15:25.076 EST

         Controller State: Down 
         Transport Admin State: In Service 
         Laser State: Off 
                 Optics not present
                 Optics Type: Unavailable
                 DWDM Carrier Info: Unavailable, MSA ITU Channel= Unavailable, Frequency= Unavailable , Wavelength= Unavailable 
                 TX Power = Unavailable 
                 RX Power = Unavailable 
    '''}

    golden_parsed_output4 = {
        "0/0/0/18": {
            "name": "Optics 0/0/0/18",
            "controller_state": "Up",
            "transport_admin_state": "In Service",
            "laser_state": "Off",
            "led_state": "Off",
            "optics_status": {
                "optics_type": "SFP+ 10G SR",
                "wavelength": "850.00 nm",
                "alarm_status": {
                    "detected_alarms": [
                        "LOW-RX1-PWR",
                        "LOW-TX1-PWR",
                        "LOW-TX1_LBC"
                    ]
                },
                "los_lol_fault_status": {
                    "detected_los_lol_fault": [
                        "RX-LOS"
                    ]
                },
                "laser_bias_current": "0.0 mA",
                "actual_tx_power": "-17.25 dBm",
                "rx_power": "-40.00 dBm",
                "performance_monitoring": "Enable",
                "threshold_values": {
                    "Rx Power Threshold(dBm)": {
                        "parameter": "Rx Power Threshold(dBm)",
                        "high_alarm": "2.0",
                        "low_alarm": "-13.9",
                        "high_warning": "-1.0",
                        "low_warning": "-9.9"
                    },
                    "Tx Power Threshold(dBm)": {
                        "parameter": "Tx Power Threshold(dBm)",
                        "high_alarm": "1.6",
                        "low_alarm": "-11.3",
                        "high_warning": "-1.3",
                        "low_warning": "-7.3"
                    },
                    "LBC Threshold(mA)": {
                        "parameter": "LBC Threshold(mA)",
                        "high_alarm": "11.00",
                        "low_alarm": "4.00",
                        "high_warning": "10.00",
                        "low_warning": "5.00"
                    },
                    "Temp. Threshold(celsius)": {
                        "parameter": "Temp. Threshold(celsius)",
                        "high_alarm": "75.00",
                        "low_alarm": "-5.00",
                        "high_warning": "70.00",
                        "low_warning": "0.00"
                    },
                    "Voltage Threshold(volt)": {
                        "parameter": "Voltage Threshold(volt)",
                        "high_alarm": "3.63",
                        "low_alarm": "2.97",
                        "high_warning": "3.46",
                        "low_warning": "3.13"
                    }
                },
                "polarization_parameters": "not supported by optics",
                "temperature": "31.00 Celsius",
                "voltage": "3.30 V"
            },
            "transceiver_vendor_details": {
                "form_factor": "SFP+",
                "optics_type": "SFP+ 10G SR",
                "name": "CISCO-FINISAR",
                "oui_number": "00.90.65",
                "part_number": "FTLX8571D3BCL-C2",
                "rev_number": "A",
                "serial_number": "FNS210108H7",
                "pid": "SFP-10G-SR",
                "vid": "V03",
                "date_code": "17/01/03"
            }
        }
    }

    golden_output4 = {'execute.return_value': '''
        #show controllers optics 0/0/0/18
        Sat Aug  3 03:19:06.519 EST

         Controller State: Up 
         Transport Admin State: In Service 
         Laser State: Off 
         LED State: Off 
         Optics Status 
                 Optics Type:  SFP+ 10G SR
                 Wavelength = 850.00 nm 

                 Alarm Status:
                 -------------
                 Detected Alarms: 
                         LOW-RX1-PWR   
                         LOW-TX1-PWR   
                         LOW-TX1_LBC   

                 LOS/LOL/Fault Status:
                 Detected LOS/LOL/FAULT: RX-LOS   


                 Laser Bias Current = 0.0 mA
                 Actual TX Power = -17.25 dBm 
                 RX Power = -40.00 dBm 

                 Performance Monitoring: Enable 

                 THRESHOLD VALUES
                 ----------------

                 Parameter                 High Alarm  Low Alarm  High Warning  Low Warning
                 ------------------------  ----------  ---------  ------------  -----------
                 Rx Power Threshold(dBm)          2.0      -13.9          -1.0         -9.9
                 Tx Power Threshold(dBm)          1.6      -11.3          -1.3         -7.3
                 LBC Threshold(mA)              11.00       4.00         10.00         5.00
                 Temp. Threshold(celsius)       75.00      -5.00         70.00         0.00
                 Voltage Threshold(volt)         3.63       2.97          3.46         3.13

                 Polarization parameters not supported by optics

                 Temperature = 31.00 Celsius 
                 Voltage = 3.30 V 

         Transceiver Vendor Details

                 Form Factor            : SFP+
                 Optics type            : SFP+ 10G SR
                 Name                   : CISCO-FINISAR
                 OUI Number             : 00.90.65
                 Part Number            : FTLX8571D3BCL-C2
                 Rev Number             : A
                 Serial Number          : FNS210108H7
                 PID                    : SFP-10G-SR
                 VID                    : V03
                 Date Code(yy/mm/dd)    : 17/01/03 
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowControllersOptics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(port='0/0/0/0')

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowControllersOptics(device=self.device)
        parsed_output = obj.parse(port='0/0/0/0')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowControllersOptics(device=self.device)
        parsed_output = obj.parse(port='0/0/1/2')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.device = Mock(**self.golden_output3)
        obj = ShowControllersOptics(device=self.device)
        parsed_output = obj.parse(port='0/0/0/20')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_golden4(self):
        self.device = Mock(**self.golden_output4)
        obj = ShowControllersOptics(device=self.device)
        parsed_output = obj.parse(port='0/0/0/18')
        self.assertEqual(parsed_output, self.golden_parsed_output4)


# ==============================================================================================
#  Unit test for 'show controllers fia diagshell {diagshell_unit} "l2 show" location {location}'
# ==============================================================================================
class test_show_controllers_fia_diagshell_location(unittest.TestCase):
    '''Unit test for:
        * 'show controllers fia diagshell {diagshell_unit} "l2 show" location {location}'
    '''

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'nodes': 
            {'0/0/CPU0': 
                {'vlan': 
                    {4: 
                        {'mac': 
                            {'00:00:03:ff:01:0c': 
                                {'encap_id': '0x301d',
                                'gport': '0xc000001',
                                'trunk': 1}}},
                    2522: 
                        {'mac': 
                            {'fc:00:00:ff:01:03': 
                                {'encap_id': '0xffffffff',
                                'gport': '0x9800401d',
                                'static': True}}},
                    2524: 
                        {'mac': 
                            {'fc:00:00:ff:01:0c': 
                                {'encap_id': '0x3001',
                                'gport': '0xc000000',
                                'static': True,
                                'trunk': 0}}},
                    2544: 
                        {'mac': 
                            {'fc:00:00:ff:01:8c': 
                                {'encap_id': '0x2007',
                                'gport': '0x8000048'},
                            'fc:00:00:ff:01:9c': 
                                {'encap_id': '0x2007',
                                'gport': '0x8000048',
                                'trunk': 0}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:UUT4#show controller fia diagshell 0 'l2 show' location all

        Node ID: 0/0/CPU0
        mac=fc:00:00:ff:01:8c vlan=2544 GPORT=0x8000048 encap_id=0x2007
        mac=fc:00:00:ff:01:03 vlan=2522 GPORT=0x9800401d Static encap_id=0xffffffff
        mac=fc:00:00:ff:01:9c vlan=2544 GPORT=0x8000048 Trunk=0 encap_id=0x2007
        mac=fc:00:00:ff:01:0c vlan=2524 GPORT=0xc000000 Trunk=0 Static encap_id=0x3001
        mac=00:00:03:ff:01:0c vlan=4 GPORT=0xc000001 Trunk=1 encap_id=0x301d
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowControllersFiaDiagshellL2showLocation(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowControllersFiaDiagshellL2showLocation(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

# ==============================================================================================
#  Unit test for 'show controllers fia diagshell 0 "diag egr_calendars" location all'
# ==============================================================================================
class TestShowControllersFiaDiagshellDiagEgrCalendarsLocation(unittest.TestCase):
    '''Unit test for:
        * 'show controllers fia diagshell 0 "diag egr_calendars" location all'
    '''

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'node_id': {
            '0/0/CPU0': {
                'port': {
                    0: {
                        'e2e_if': 4,
                        'e2e_if_rate': 1050000,
                        'e2e_port_rate': 350000,
                        'egq_if': 28,
                        'egq_if_rate': 990000,
                        'egq_port_rate': 336671,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    1: {
                        'e2e_if': 36,
                        'e2e_if_rate': 105004160,
                        'e2e_port_rate': 105004160,
                        'egq_if': 1,
                        'egq_if_rate': 609052500,
                        'egq_port_rate': 101000014,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    5: {
                        'e2e_if': 37,
                        'e2e_if_rate': 105004160,
                        'e2e_port_rate': 105004160,
                        'egq_if': 2,
                        'egq_if_rate': 609052500,
                        'egq_port_rate': 101000014,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    9: {
                        'e2e_if': 38,
                        'e2e_if_rate': 105004160,
                        'e2e_port_rate': 105004160,
                        'egq_if': 3,
                        'egq_if_rate': 609052500,
                        'egq_port_rate': 101000014,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    13: {
                        'e2e_if': 35,
                        'e2e_if_rate': 105004160,
                        'e2e_port_rate': 105004160,
                        'egq_if': 0,
                        'egq_if_rate': 609052500,
                        'egq_port_rate': 101000014,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    17: {
                        'e2e_if': 39,
                        'e2e_if_rate': 105004160,
                        'e2e_port_rate': 105004160,
                        'egq_if': 4,
                        'egq_if_rate': 609052500,
                        'egq_port_rate': 101000014,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    21: {
                        'e2e_if': 40,
                        'e2e_if_rate': 105004160,
                        'e2e_port_rate': 105004160,
                        'egq_if': 5,
                        'egq_if_rate': 609052500,
                        'egq_port_rate': 101000014,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    25: {
                        'e2e_if': 50,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 48,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    26: {
                        'e2e_if': 38,
                        'e2e_if_rate': 1050112,
                        'e2e_port_rate': 1050112,
                        'egq_if': 36,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 1010003,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    27: {
                        'e2e_if': 36,
                        'e2e_if_rate': 1050112,
                        'e2e_port_rate': 1050112,
                        'egq_if': 34,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 1010003,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    28: {
                        'e2e_if': 51,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 49,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    29: {
                        'e2e_if': 37,
                        'e2e_if_rate': 1050112,
                        'e2e_port_rate': 1050112,
                        'egq_if': 35,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 1010003,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    30: {
                        'e2e_if': 78,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 76,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    31: {
                        'e2e_if': 41,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 39,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    32: {
                        'e2e_if': 80,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 78,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    33: {
                        'e2e_if': 35,
                        'e2e_if_rate': 1050112,
                        'e2e_port_rate': 1050112,
                        'egq_if': 33,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 1010003,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    34: {
                        'e2e_if': 40,
                        'e2e_if_rate': 1050112,
                        'e2e_port_rate': 1050112,
                        'egq_if': 38,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 1010003,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    35: {
                        'e2e_if': 39,
                        'e2e_if_rate': 1050112,
                        'e2e_port_rate': 1050112,
                        'egq_if': 37,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 1010003,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    36: {
                        'e2e_if': 49,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 47,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    37: {
                        'e2e_if': 53,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 51,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    38: {
                        'e2e_if': 42,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 40,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    39: {
                        'e2e_if': 81,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 79,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    40: {
                        'e2e_if': 79,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 77,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    41: {
                        'e2e_if': 43,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 41,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    42: {
                        'e2e_if': 52,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 50,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    43: {
                        'e2e_if': 44,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 42,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    44: {
                        'e2e_if': 82,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 80,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    45: {
                        'e2e_if': 45,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 43,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    46: {
                        'e2e_if': 46,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 44,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    47: {
                        'e2e_if': 47,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 45,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    48: {
                        'e2e_if': 48,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 46,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    49: {
                        'e2e_if': 55,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 53,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    50: {
                        'e2e_if': 75,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 73,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    51: {
                        'e2e_if': 73,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 71,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    52: {
                        'e2e_if': 72,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 70,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    53: {
                        'e2e_if': 71,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 69,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    54: {
                        'e2e_if': 69,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 67,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    55: {
                        'e2e_if': 70,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 68,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    56: {
                        'e2e_if': 68,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 66,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    57: {
                        'e2e_if': 76,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 74,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    58: {
                        'e2e_if': 56,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 54,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    59: {
                        'e2e_if': 74,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 72,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    60: {
                        'e2e_if': 77,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 75,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    61: {
                        'e2e_if': 54,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 52,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    62: {
                        'e2e_if': 64,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 62,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    63: {
                        'e2e_if': 66,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 64,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    64: {
                        'e2e_if': 67,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 65,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    65: {
                        'e2e_if': 62,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 60,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    66: {
                        'e2e_if': 61,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 59,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    67: {
                        'e2e_if': 63,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 61,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    68: {
                        'e2e_if': 65,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 63,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    69: {
                        'e2e_if': 57,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 55,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    70: {
                        'e2e_if': 60,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 58,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    71: {
                        'e2e_if': 59,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 57,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    72: {
                        'e2e_if': 58,
                        'e2e_if_rate': 10500096,
                        'e2e_port_rate': 10500096,
                        'egq_if': 56,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 10100011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    128: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 5184078,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 1010113,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    129: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 5180956,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 1010033,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    130: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 5184078,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 1010113,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    131: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 5180956,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 1010033,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    132: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 165890478,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 161600009,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    133: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 165790561,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 161600021,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    134: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 5184078,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 1010113,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    135: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 5180956,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 1010033,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    136: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 165890478,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 161600009,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    137: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 165790561,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 161600021,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    138: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 165890478,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 161600009,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    139: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 165790561,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 161600021,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    140: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 5184078,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 1010113,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    141: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 5180956,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 1010033,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    142: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 165890478,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 161600009,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    143: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 165790561,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 161600021,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    144: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 165890478,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 161600009,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    145: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 165790561,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 161600021,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    146: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 165890478,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 161600009,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    147: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 165790561,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 161600021,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    148: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 10368155,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 10100009,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    149: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 10361911,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 10100089,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    208: {
                        'e2e_if': 4,
                        'e2e_if_rate': 1050000,
                        'e2e_port_rate': 10500000,
                        'egq_if': 28,
                        'egq_if_rate': 990000,
                        'egq_port_rate': 10100000,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    232: {
                        'e2e_if': 32,
                        'e2e_if_rate': 31500416,
                        'e2e_port_rate': 31500416,
                        'egq_if': 30,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 30300003,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    233: {
                        'e2e_if': 32,
                        'e2e_if_rate': 1050112,
                        'e2e_port_rate': 1050112,
                        'egq_if': 30,
                        'egq_if_rate': 609052500,
                        'egq_port_rate': 1010011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    235: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 20736310,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 20200017,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    240: {
                        'e2e_if': 33,
                        'e2e_if_rate': 105004160,
                        'e2e_port_rate': 105004160,
                        'egq_if': 29,
                        'egq_if_rate': 433417500,
                        'egq_port_rate': 101000003,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    241: {
                        'e2e_if': 33,
                        'e2e_if_rate': 1050112,
                        'e2e_port_rate': 1050112,
                        'egq_if': 29,
                        'egq_if_rate': 609052500,
                        'egq_port_rate': 1010011,
                        'high_calendar': 32,
                        'low_calendar': 32,
                        'priority': 'LOW',
                    },
                    246: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 25920388,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 25250083,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    247: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 25904776,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 25250105,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    248: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 10368155,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 10100009,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    249: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 10361911,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 10100089,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    250: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 165890478,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 161600009,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    251: {
                        'e2e_if': 4,
                        'e2e_if_rate': 339536840,
                        'e2e_port_rate': 165790561,
                        'egq_if': 31,
                        'egq_if_rate': 323190000,
                        'egq_port_rate': 161600021,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                    252: {
                        'e2e_if': 5,
                        'e2e_if_rate': 161280000,
                        'e2e_port_rate': 10368155,
                        'egq_if': 31,
                        'egq_if_rate': 159997500,
                        'egq_port_rate': 1120,
                        'high_calendar': 255,
                        'low_calendar': 5,
                        'priority': 'LOW',
                    },
                    253: {
                        'e2e_if': 4,
                        'e2e_if_rate': 1050000,
                        'e2e_port_rate': 350000,
                        'egq_if': 28,
                        'egq_if_rate': 990000,
                        'egq_port_rate': 101000000,
                        'high_calendar': 255,
                        'low_calendar': 4,
                        'priority': 'LOW',
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        show controllers fia diagshell 0 "diag egr_calendars" location all
        Mon Mar 23 13:12:43.297 UTC
        
        Node ID: 0/0/CPU0
        Port | Priority | High Calendar | Low Calendar | EGQ IF | E2E IF | EGQ Port Rate | EGQ IF Rate | E2E Port Rate | E2E IF Rate
        ----------------------------------------------------------------------------------------------------------------------------
        0  |    LOW   |       255     |        4     |   28   |    4   |      336671   |     990000  |      350000   |    1050000
        1  |    LOW   |        32     |       32     |    1   |   36   |   101000014   |  609052500  |   105004160   |  105004160
        5  |    LOW   |        32     |       32     |    2   |   37   |   101000014   |  609052500  |   105004160   |  105004160
        9  |    LOW   |        32     |       32     |    3   |   38   |   101000014   |  609052500  |   105004160   |  105004160
        13  |    LOW   |        32     |       32     |    0   |   35   |   101000014   |  609052500  |   105004160   |  105004160
        17  |    LOW   |        32     |       32     |    4   |   39   |   101000014   |  609052500  |   105004160   |  105004160
        21  |    LOW   |        32     |       32     |    5   |   40   |   101000014   |  609052500  |   105004160   |  105004160
        25  |    LOW   |        32     |       32     |   48   |   50   |    10100011   |  433417500  |    10500096   |   10500096
        26  |    LOW   |        32     |       32     |   36   |   38   |     1010003   |  433417500  |     1050112   |    1050112
        27  |    LOW   |        32     |       32     |   34   |   36   |     1010003   |  433417500  |     1050112   |    1050112
        28  |    LOW   |        32     |       32     |   49   |   51   |    10100011   |  433417500  |    10500096   |   10500096
        29  |    LOW   |        32     |       32     |   35   |   37   |     1010003   |  433417500  |     1050112   |    1050112
        30  |    LOW   |        32     |       32     |   76   |   78   |    10100011   |  433417500  |    10500096   |   10500096
        31  |    LOW   |        32     |       32     |   39   |   41   |    10100011   |  433417500  |    10500096   |   10500096
        32  |    LOW   |        32     |       32     |   78   |   80   |    10100011   |  433417500  |    10500096   |   10500096
        33  |    LOW   |        32     |       32     |   33   |   35   |     1010003   |  433417500  |     1050112   |    1050112
        34  |    LOW   |        32     |       32     |   38   |   40   |     1010003   |  433417500  |     1050112   |    1050112
        35  |    LOW   |        32     |       32     |   37   |   39   |     1010003   |  433417500  |     1050112   |    1050112
        36  |    LOW   |        32     |       32     |   47   |   49   |    10100011   |  433417500  |    10500096   |   10500096
        37  |    LOW   |        32     |       32     |   51   |   53   |    10100011   |  433417500  |    10500096   |   10500096
        38  |    LOW   |        32     |       32     |   40   |   42   |    10100011   |  433417500  |    10500096   |   10500096
        39  |    LOW   |        32     |       32     |   79   |   81   |    10100011   |  433417500  |    10500096   |   10500096
        40  |    LOW   |        32     |       32     |   77   |   79   |    10100011   |  433417500  |    10500096   |   10500096
        41  |    LOW   |        32     |       32     |   41   |   43   |    10100011   |  433417500  |    10500096   |   10500096
        42  |    LOW   |        32     |       32     |   50   |   52   |    10100011   |  433417500  |    10500096   |   10500096
        43  |    LOW   |        32     |       32     |   42   |   44   |    10100011   |  433417500  |    10500096   |   10500096
        44  |    LOW   |        32     |       32     |   80   |   82   |    10100011   |  433417500  |    10500096   |   10500096
        45  |    LOW   |        32     |       32     |   43   |   45   |    10100011   |  433417500  |    10500096   |   10500096
        46  |    LOW   |        32     |       32     |   44   |   46   |    10100011   |  433417500  |    10500096   |   10500096
        47  |    LOW   |        32     |       32     |   45   |   47   |    10100011   |  433417500  |    10500096   |   10500096
        48  |    LOW   |        32     |       32     |   46   |   48   |    10100011   |  433417500  |    10500096   |   10500096
        49  |    LOW   |        32     |       32     |   53   |   55   |    10100011   |  433417500  |    10500096   |   10500096
        50  |    LOW   |        32     |       32     |   73   |   75   |    10100011   |  433417500  |    10500096   |   10500096
        51  |    LOW   |        32     |       32     |   71   |   73   |    10100011   |  433417500  |    10500096   |   10500096
        52  |    LOW   |        32     |       32     |   70   |   72   |    10100011   |  433417500  |    10500096   |   10500096
        53  |    LOW   |        32     |       32     |   69   |   71   |    10100011   |  433417500  |    10500096   |   10500096
        54  |    LOW   |        32     |       32     |   67   |   69   |    10100011   |  433417500  |    10500096   |   10500096
        55  |    LOW   |        32     |       32     |   68   |   70   |    10100011   |  433417500  |    10500096   |   10500096
        56  |    LOW   |        32     |       32     |   66   |   68   |    10100011   |  433417500  |    10500096   |   10500096
        57  |    LOW   |        32     |       32     |   74   |   76   |    10100011   |  433417500  |    10500096   |   10500096
        58  |    LOW   |        32     |       32     |   54   |   56   |    10100011   |  433417500  |    10500096   |   10500096
        59  |    LOW   |        32     |       32     |   72   |   74   |    10100011   |  433417500  |    10500096   |   10500096
        60  |    LOW   |        32     |       32     |   75   |   77   |    10100011   |  433417500  |    10500096   |   10500096
        61  |    LOW   |        32     |       32     |   52   |   54   |    10100011   |  433417500  |    10500096   |   10500096
        62  |    LOW   |        32     |       32     |   62   |   64   |    10100011   |  433417500  |    10500096   |   10500096
        63  |    LOW   |        32     |       32     |   64   |   66   |    10100011   |  433417500  |    10500096   |   10500096
        64  |    LOW   |        32     |       32     |   65   |   67   |    10100011   |  433417500  |    10500096   |   10500096
        65  |    LOW   |        32     |       32     |   60   |   62   |    10100011   |  433417500  |    10500096   |   10500096
        66  |    LOW   |        32     |       32     |   59   |   61   |    10100011   |  433417500  |    10500096   |   10500096
        67  |    LOW   |        32     |       32     |   61   |   63   |    10100011   |  433417500  |    10500096   |   10500096
        68  |    LOW   |        32     |       32     |   63   |   65   |    10100011   |  433417500  |    10500096   |   10500096
        69  |    LOW   |        32     |       32     |   55   |   57   |    10100011   |  433417500  |    10500096   |   10500096
        70  |    LOW   |        32     |       32     |   58   |   60   |    10100011   |  433417500  |    10500096   |   10500096
        71  |    LOW   |        32     |       32     |   57   |   59   |    10100011   |  433417500  |    10500096   |   10500096
        72  |    LOW   |        32     |       32     |   56   |   58   |    10100011   |  433417500  |    10500096   |   10500096
        128  |    LOW   |       255     |        5     |   31   |    5   |     1010113   |  159997500  |     5184078   |  161280000
        129  |    LOW   |       255     |        4     |   31   |    4   |     1010033   |  323190000  |     5180956   |  339536840
        130  |    LOW   |       255     |        5     |   31   |    5   |     1010113   |  159997500  |     5184078   |  161280000
        131  |    LOW   |       255     |        4     |   31   |    4   |     1010033   |  323190000  |     5180956   |  339536840
        132  |    LOW   |       255     |        5     |   31   |    5   |   161600009   |  159997500  |   165890478   |  161280000
        133  |    LOW   |       255     |        4     |   31   |    4   |   161600021   |  323190000  |   165790561   |  339536840
        134  |    LOW   |       255     |        5     |   31   |    5   |     1010113   |  159997500  |     5184078   |  161280000
        135  |    LOW   |       255     |        4     |   31   |    4   |     1010033   |  323190000  |     5180956   |  339536840
        136  |    LOW   |       255     |        5     |   31   |    5   |   161600009   |  159997500  |   165890478   |  161280000
        137  |    LOW   |       255     |        4     |   31   |    4   |   161600021   |  323190000  |   165790561   |  339536840
        138  |    LOW   |       255     |        5     |   31   |    5   |   161600009   |  159997500  |   165890478   |  161280000
        139  |    LOW   |       255     |        4     |   31   |    4   |   161600021   |  323190000  |   165790561   |  339536840
        140  |    LOW   |       255     |        5     |   31   |    5   |     1010113   |  159997500  |     5184078   |  161280000
        141  |    LOW   |       255     |        4     |   31   |    4   |     1010033   |  323190000  |     5180956   |  339536840
        142  |    LOW   |       255     |        5     |   31   |    5   |   161600009   |  159997500  |   165890478   |  161280000
        143  |    LOW   |       255     |        4     |   31   |    4   |   161600021   |  323190000  |   165790561   |  339536840
        144  |    LOW   |       255     |        5     |   31   |    5   |   161600009   |  159997500  |   165890478   |  161280000
        145  |    LOW   |       255     |        4     |   31   |    4   |   161600021   |  323190000  |   165790561   |  339536840
        146  |    LOW   |       255     |        5     |   31   |    5   |   161600009   |  159997500  |   165890478   |  161280000
        147  |    LOW   |       255     |        4     |   31   |    4   |   161600021   |  323190000  |   165790561   |  339536840
        148  |    LOW   |       255     |        5     |   31   |    5   |    10100009   |  159997500  |    10368155   |  161280000
        149  |    LOW   |       255     |        4     |   31   |    4   |    10100089   |  323190000  |    10361911   |  339536840
        208  |    LOW   |       255     |        4     |   28   |    4   |    10100000   |     990000  |    10500000   |    1050000
        232  |    LOW   |        32     |       32     |   30   |   32   |    30300003   |  433417500  |    31500416   |   31500416
        233  |    LOW   |        32     |       32     |   30   |   32   |     1010011   |  609052500  |     1050112   |    1050112
        235  |    LOW   |       255     |        5     |   31   |    5   |    20200017   |  159997500  |    20736310   |  161280000
        240  |    LOW   |        32     |       32     |   29   |   33   |   101000003   |  433417500  |   105004160   |  105004160
        241  |    LOW   |        32     |       32     |   29   |   33   |     1010011   |  609052500  |     1050112   |    1050112
        246  |    LOW   |       255     |        5     |   31   |    5   |    25250083   |  159997500  |    25920388   |  161280000
        247  |    LOW   |       255     |        4     |   31   |    4   |    25250105   |  323190000  |    25904776   |  339536840
        248  |    LOW   |       255     |        5     |   31   |    5   |    10100009   |  159997500  |    10368155   |  161280000
        249  |    LOW   |       255     |        4     |   31   |    4   |    10100089   |  323190000  |    10361911   |  339536840
        250  |    LOW   |       255     |        5     |   31   |    5   |   161600009   |  159997500  |   165890478   |  161280000
        251  |    LOW   |       255     |        4     |   31   |    4   |   161600021   |  323190000  |   165790561   |  339536840
        252  |    LOW   |       255     |        5     |   31   |    5   |        1120   |  159997500  |    10368155   |  161280000
        253  |    LOW   |       255     |        4     |   28   |    4   |   101000000   |     990000  |      350000   |    1050000

        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowControllersFiaDiagshellDiagEgrCalendarsLocation(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(diagshell=0,
                location='all')

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowControllersFiaDiagshellDiagEgrCalendarsLocation(device=self.device)
        parsed_output = obj.parse(diagshell=0,
                location='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

# =========================================================================================================
#  Unit test for 'show controllers npu {npu} interface {interface} instance {instance} location {location}'
# =========================================================================================================
class TestShowControllersNpuInterfaceInstanceLocation(unittest.TestCase):
    '''Unit test for:
        * 'show controllers npu {npu} interface {interface} instance {instance} location {location}'
    '''

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'node_id': {
            '0/0/CPU0': {
                'interface': {
                    'GigabitEthernet0/0/0/0': {
                        'flow_base': 5384,
                        'interface_handle_hex': 108,
                        'npu_core': 0,
                        'npu_number': 0,
                        'port_speed': '1G',
                        'pp_port': 33,
                        'sys_port': 33,
                        'voq_base': 1024,
                        'voq_port_type': 'local',
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        show controllers npu voq-usage interface GigabitEthernet0/0/0/0 instance all location all
        Mon Mar 23 13:11:55.030 UTC
        
        -------------------------------------------------------------------
        Node ID: 0/0/CPU0
        Intf         Intf     NPU NPU  PP   Sys   VOQ   Flow   VOQ    Port
        name         handle    #  core Port Port  base  base   port   speed
                    (hex)                                     type
        ----------------------------------------------------------------------
        Gi0/0/0/0    108       0   0   33    33   1024   5384 local     1G
        Not supported on this location 0/RP0/CPU0 or Data not found
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowControllersNpuInterfaceInstanceLocation(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(npu='voq-usage',
                interface='GigabitEthernet0/0/0/0',
                instance='all',
                location='all')

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowControllersNpuInterfaceInstanceLocation(device=self.device)
        parsed_output = obj.parse(npu='voq-usage',
                interface='GigabitEthernet0/0/0/0',
                instance='all',
                location='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)
        
if __name__ == '__main__':
    unittest.main()