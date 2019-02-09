#
# This file is part of rasa-teld.
#
# rasa-teld is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rasa-teld is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rasa-teld.  If not, see <http://www.gnu.org/licenses/>.

"""Constants and status codes used by rasa-teld"""

# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

class CommandStatus:
    """Numeric return codes"""
    # General error codes
    Succeeded = 0
    Failed = 1
    Blocked = 2

    SerialNotAvailable = 6
    SerialTimeout = 7

    # Command-specific codes
    TelescopeNotDisabled = 10
    TelescopeNotEnabled = 12
    TelescopeInitializing = 13

    CoordinatesOutsideLimits = 20
    SlewAborted = 21

    _messages = {
        1: 'error: command failed',
        2: 'error: another command is already running',
        6: 'error: failed to open serial connection to mount',
        7: 'error: mount is not responding to serial commands (powered off?)',

        # Command-specific codes
        10: 'error: telescope is active',
        12: 'error: telescope has not been initialized',
        13: 'error: telescope is initializing',

        20: 'error: requested coordinates outside limits',
        21: 'error: slew aborted',
        31: 'error: failed to load reference frame',

        # tel specific codes
        -100: 'error: terminated by user',
        -101: 'error: unable to communicate with telescope daemon',
    }

    @classmethod
    def message(cls, error_code):
        """Returns a human readable string describing an error code"""
        if error_code in cls._messages:
            return cls._messages[error_code]
        return 'error: Unknown error code {}'.format(error_code)

class TelescopeState:
    """Telescope status"""
    Disabled, Initializing, Slewing, Stopped, Tracking = range(5)
    Names = ['DISABLED', 'INITIALIZING', 'SLEWING', 'STOPPED', 'TRACKING']
