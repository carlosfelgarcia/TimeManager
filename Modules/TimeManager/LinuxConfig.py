"""Module to handle the configuration files of Linux."""
import json


class LinuxConfig(object):
    """Configuration class."""

    def __init__(self, configPath):
        """Constructor."""
        self.__configFilePath = configPath

    def setDefaultAttrs(self):
        """Set the default values for Linux OS.

        Base on the default processes running from linx, there are some that can be skipped. It also set the time in
        seconds of the look up to new processes on the OS. idleCycles is the number of cycles it takes for the process
        to be consider idle, each cycle is base on the lookuptime and starts from 0 (e.g. 2 = 30 * 3 = 1minute 30secs).
        All of this values can be override by the main configuration.

        :pre: The directory of the file path already exist
        """
        defaultAttrs = {
            'defaultAttrs': {
                'skipProcess': [
                    'ksysguard',
                    'plasma-desktop'
                ],
                'lookupTime': 10,
                'idleCycles': 2
            }
        }
        with open(self.__configFilePath, 'w') as configFile:
            json.dump(defaultAttrs, configFile)

    def setConfig(self, atrrs):
        """
        Set a configuration file to filter process and set other attributes.

        :param attrs: Attributes to set the dictionary.
        :type attrs: dict
        :returns: A confirmation that the file was set correctly.
        :rtype: bool
        """
        pass

    def getConfig(self):
        """Get the attributes that are set in the confugaration file.

        Atrributes that are coming from the user will averwritte any default value if matches the name.

        :return: The attributes that are set in the file
        :rtype: dict
        """
        finalAttrs = {}
        with open(self.__configFilePath) as configFile:
            attrs = json.load(configFile)
        mainAttrs = attrs.get('mainAttrs', None)
        defaultAttrs = attrs.get('defaultAttrs', None)

        if mainAttrs:
            # Read values from user
            for key, value in mainAttrs.items():
                finalAttrs[key] = value

        if not defaultAttrs:
            raise ValueError("No default values are set")
        # Read values from default
        # TODO: There might be attributes that needs to be expand and not completely take over e.g. skipProcess
        for key, value in defaultAttrs.items():
            if key in finalAttrs:
                continue
            finalAttrs[key] = value

        return finalAttrs
