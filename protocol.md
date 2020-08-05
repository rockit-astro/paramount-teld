# Socket Protocol

The telescope daemon exposes a socket at `10.2.6.218` port `9035`.

A simple binary request/response protocol is defined.
All requests start with a command type byte, and all responses will start with a command status byte.
Some commands (i.e. slews) require additional data to be sent in the request, and some commands (i.e. telescope/dome status) respond with additional data after the `Succeeded` status byte.

Multiple connections are supported, but command requests may be rejected (`Blocked` status) if the mount is busy with another command.
Additional connections can be used to stop an active slew or to query status while the mount is moving.

The following return statuses are implemented:

| Status byte | Meaning   |
| ----------- | ------------- |
| `0x00`      | Succeeded |
| `0x01`      | Failed  |
| `0x02`      | Blocked (another command already running) |
| `0x06`      | Unable to connect to mount (powered off?) |
| `0x07`      | Serial timeout communicating with mount |
| `0x0A`      | Mount is already initialized (from Initialize command)
| `0x0C`      | Mount is already disabled (from Shutdown command)
| `0x0D`      | Mount is still initializing (from Shutdown command)
| `0x14`      | Requested coordinates are outside mount limits (from slew/track commands)
| `0x15`      | Slew was aborted by a Stop command (from slew/track commands)

The following commands are supported:

### Ping Daemon

Test whether the daemon is responding to commands. Immediately returns the `Succeeded` status.

Type code: `0x01`

Additional request parameters: *none*

Additional response data: *none*

### Initialize Mount

Establish internal connection to the driver and home the mount. This command will typically take a few tens of seconds to complete.

Type code: `0x02`

Additional request parameters: *none*

Additional response data: *none*

### Shut down Mount

Disable tracking and terminate the driver connection at the current position. You should generally point to a safe parking position first!

Type code: `0x03`

Additional request parameters: *none*

Additional response data: *none*

### Stop Mount

Stop mount tracking or abort an active slew (if sent from a second connection).

Type code: `0x04`

Additional request parameters: *none*

Additional response data: *none*

### Slew to Alt/Az (no tracking)

Point mount at a fixed Alt/Az (e.g. to park). This command can potentially take many tens of seconds to complete (e.g. if a meridian flip is required).

Type code: `0x05`

Additional request parameters:
 - double: Altitude (degrees)
 - double: Azimuth (degrees)

Additional response data: *none*

### Track RA/Dec

Slew to a fixed RA/Dec and begin tracking with defined rates. This command can potentially take many tens of seconds to complete (e.g. if a meridian flip is required).

Type code: `0x06`

Additional request parameters:
 - double: RA offset (degrees)
 - double: Dec offset (degrees)
 - double: RA tracking rate (arcsec/sec)
 - double: Dec tracking rate (arcsec/sec)

Additional response data: *none*

### Offset RA/Dec

Apply offsets to RA and Dec.

Type code: `0x07`

Additional request parameters:
 - double: RA offset (degrees)
 - double: Dec offset (degrees)

Additional response data: *none*

### Update RA/Dec tracking rates

Set new tracking rates in RA and Dec.

Type code: `0x08`

Additional request parameters:
 - double: RA tracking rate (arcsec/sec)
 - double: Dec tracking rate (arcsec/sec)

Additional response data: *none*

### Query mount status

Returns information about the mount.

Type code: `0x09`

Additional request parameters: *none*

Additional response data:
 - byte: Mount status (see below)
 - double: Altitude (degrees)
 - double: Azimuth (degrees)
 - double: RA (degrees)
 - double: Dec (degrees)
 - double: RA tracking rate (arcsec/sec)
 - double: Dec tracking rate (arcsec/sec)
 - double: HA (degrees)
 - byte: Pier side (see below)

| Status byte | Mount state   |
| ----------- | ------------- |
| `0x00`      | Not connected |
| `0x01`      | Initializing / homing |
| `0x02`      | Slewing |
| `0x03`      | Stopped |
| `0x04`      | Tracking |

| Pier byte | Payload side   |
| ----------- | ------------- |
| `0x00`      | Unknown |
| `0x01`      | East |
| `0x02`      | West |

The values for alt/az/ra/dec/rates/ha should only be considered to be valid if the status is stopped or tracking.

### Query dome status

Returns information about the dome/environment.

Type code: `0x0A`

Additional request parameters: *none*

Additional response data:
 - byte: Dome status (see below)
 - byte: Environment safe (`0x01`) or unsafe (`0x00`)

| Status byte | Dome state   |
| ----------- | ------------- |
| `0x00`      | Closed |
| `0x01`      | Open |
| `0x02`      | Moving |
| `0x03`      | Heartbeat timeout |
