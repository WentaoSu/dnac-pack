import sys
from dnac import Dnac
from dnac.networkdevice import NetworkDevice
from st2common.runners.base_action import Action

class GetNetworkDevices(Action):
    def run(self):
        MODULE = 'networkdevice_example.py'
        try:
            self.logger.info('%s: setting up Cisco DNA Center and its API...' % MODULE)
            dnac = Dnac()
            ndapi = NetworkDevice(dnac, 'devices')

            self.logger.info('%s: getting all devices...' % MODULE)
            # The handle 'ndapi' could be used here, but the point of this example is
            # demonstrate how to get it directly from the Dnac.api{} using the API's name.
            devices = dnac.api['devices'].get_all_devices()

            self.logger.info('%s: found the following devices:' % MODULE)
            for device in devices:
                self.logger.info('hostname: %s\tserial: %s\tIP: %s' %
                      (device['hostname'], device['serialNumber'],
                       device['managementIpAddress']))
            return (True, devices)
        except Exception as err:
            return (False, MODULE + str(err))