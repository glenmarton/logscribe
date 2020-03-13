## Change Log

### [5.0.1-rc.5] - Unreleased

#### Fixed
- Login button to allow log in.
  - CCServer, VE6021, VE6023, VE6025
  - VMASS-83

----

### [5.0.0-rc.11] - 2019-09-04

#### Fixed
- Create Play List in Quick Page creates an event that uses a Text Message
  that later gets deleted.
  - CCServer, VE6021, VE6025
  - VMASS-899
- User without full calendar access right clicking on the calendar causes a
  crash.
  - CCServer, VE6021, VE6025
  - VMASS-904
- Fix a crash when deleting a large number of selected CAP Alerts
  - CCServer, VE6021, VE6025
  - VMASS-898
- The submit button in the users editor would remain deactivated when a
  changing a privilege from limited to full.
  - CCServer, VE6021, VE6023, VE6025
  - VMASS-897
- Assorted php-fpm crashes.
  - CCServer, VE6021, VE6023, VE6025
  - VMASS-925

----

### [5.0.0-rc.1-4] - 2019-03-12

#### Added
- Ability to download log files without creating a backup.
  - CCServer, VE6021, VE6023, VE6025
  - VMASS-84

[5.0.0-rc.1-4]: https://gitlab.valcom.com/servers/vmass/compare/6025-v4.10.0...6025-v5.0.0-RC4
