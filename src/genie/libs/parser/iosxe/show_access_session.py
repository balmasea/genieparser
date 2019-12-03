"""show_access_seesion.py
   supported commands:
     * show access-session
     * show access-session interface {interface} details
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common

# import iosxe parser
from genie.libs.parser.iosxe.show_authentication_sessions import \
						ShowAuthenticationSessionsInterfaceDetails

# ====================================
# Parser for 'show access-session'
# ====================================
class ShowAccessSessionSchema(MetaParser):
    """Schema for show access-session"""
    schema = {
        'session_count': int,
        Optional('interfaces'): {
            Any(): {
                'interface': str,
                'client': {
                    Any(): {
                        'client': str,
                        'method': str,
                        'domain': str,
                        'status': str,
                        'session': {
                            Any(): {
                                'session_id': str,
                            }
                        }
                    }
                }
            }
        }
    }


class ShowAccessSession(ShowAccessSessionSchema):
    """Parser for show access-session"""

    MAP = {'auth': 'authenticator',
           'supp': 'supplicant'}

    cli_command = 'show access-session'

    def cli(self,output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^Session +count \= +(?P<val>\d+)$')
        p2 = re.compile(r'^(?P<intf>[\w\/\-\.]+) +'
                         '(?P<client>[\w\.]+) +'
                         '(?P<method>\w+) +'
                         '(?P<domain>\w+) +'
                         '(?P<status>\w+) +'
                         '(?P<session>\w+)$')

        for line in out.splitlines():
            line = line.strip()
            line = line.replace('\t', '    ')
            
            # Session count = 1
            m = p1.match(line)
            if m:
                ret_dict['session_count'] = int(m.groupdict()['val'])
                continue

            # Gi1/0/1                  f4cf.beef.acc1 dot1x   DATA    Auth        000000000000000BB6FC9EAF
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group['intf'])
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(intf, {})
                intf_dict['interface'] = intf

                client = group['client']
                client_dict = intf_dict.setdefault('client', {}).setdefault(client, {})
                client_dict['client'] = client
                client_dict['method'] = group['method']
                client_dict['domain'] = group['domain']
                client_dict['status'] = self.MAP[group['status'].lower()] \
                    if group['status'].lower() in self.MAP else group['status'].lower()
                session = group['session']
                client_dict.setdefault('session', {}).setdefault(session, {})\
                    .setdefault('session_id', session)
                continue

        return ret_dict
       
class ShowAccessSessionInterfaceDetails(ShowAuthenticationSessionsInterfaceDetails):
    '''
        Parser for the following show commands:
            * show access-session interface {interface} details
    '''
    cli_command = 'show access-session interface {interface} details'
    def cli(self, interface, output=None):

        if output is None:
            cmd = self.cli_command.format(interface=interface)
            show_output = self.device.execute(cmd)
        else:
           show_output = output

        # Call super
        return super().cli(output=show_output, interface=interface)
