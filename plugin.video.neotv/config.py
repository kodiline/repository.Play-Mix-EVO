exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MjYoIjExIDU0OzExIDEyIik7MjYoKDEwIDg2LDg5OigxMCA4MyxiLGY6NTQuNTMoODMsYixmKSkoOTAiKFswLTlhLWZdKykiLDEwIDhhOjg2KDhhLDg5KSwxMi4xMygiOWI9PSIpKSkoMTAgYSxiOmJbNWQoIjhmIithLjJkKDEpLDE2KV0sIjB8MXwyfDN8NHw1fDZ8OHw5fDhifGF8YnxkfGV8NzF8ZnwxMXwxMnwxM3wxNHwxNXw3OXwxNnwxOHwxOXw5OXwxYXwxY3wxZHwxZXwxZnwyMHwyMXwyM3wyMnwyNHwyNXwyNnwyN3wyOHwyOXwyYXwyYnwyY3wyZXwyZnwyZHwzMXwzMHwzM3wzMnwzNHwzNXwzNnwzN3wzOHwzOXwzYXwzZHwzYnwzY3wzZXwzZnw0MHw0MXw0Mnw0M3w0NHw0NXw0Nnw0N3w0OHw0OXw0Y3w0YXw0Ynw0ZHw0ZXw0Znw1MHw1MXw1Mnw1M3w1NHw1NXw1Nnw1N3w1OHw1OXw1YXw1Ynw1Y3w1ZHw1ZXw1Znw2MHw2MXw2Mnw2M3w2NHxjfDZhfDY2fDY3fDY4fDY5fDZifDZjfDZkfDZlfDZmfDcwfDEwfDcyfDczfDc0fDc1fDc2fDc3fDE3fDc4fDdifDhmfDdjfDdkfDdlfDdmfDgwfDgxfDgyfDgzfDg0fDg1fDg2fDg3fDg4fDg5fDhhfDY1fDhjfDhkfDhlfDljfDkwfDkxfDkyfDkzfDk0fDk1fDk2fDk3fDk4fDFifDd8OWF8OWR8OWV8N2EiLjMzKCJ8IikpKQ==")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|2|3|4|5|6|MjAoIjMgMWI7MyA0Iik7MjAoKDIgMmYsMmU6KDIgMzAsYixmOjFiLjFhKDMwLGIsZikpKDMzIihbMC0yOS1mXSspIiwyIDMxOjJmKDMxLDJlKSw0LjUoIjM0IikpKSgyIGEsYjpiWzE4KCIyNiIrYS5lKDEpLDE2KV0sIjB8MXwzfDR8Nnw3fDh8OXwzMnxkfGF8Ynw1fDExfDEyfGZ8MTN8MTR8MTV8MjN8MTd8MTl8MTZ8MWN8MWR8Y3wxZXwxZnxlfDIxfDIyfDI0fDI1fDI3fDI4fDEwfDE4fDFhfDJifDJjfDJkfDIwfDI2fDFifDM1fDM3fDI5fDJlfDM4fDJmfDMwfDMxfDJhfDMzfDM2fDIiLmMoInwiKSkp|OCgiMzUgMTk7MzUgMzIiKTs4KCgzNCAyOCwyNzooMzQgMjksYixmOjE5LjE4KDI5LGIsZikpKDJkIihbMC0yMi1mXSspIiwzNCAyYToyOCgyYSwyNyksMzIuMzMoIjJmIikpKSgzNCBhLGI6YlsxZigiMWUiK2EuYygxKSwxNildLCIwfDF8MnwzfDR8NXw2fDFkfGR8ZXxhfGJ8OHwxMHwxMXxmfDEzfDE0fDE1fDE3fDFhfDFifDE2fDFjfGN8MjB8MjF8MTl8MjR8MjN8MWZ8MTh8MjV8MjZ8MTJ8MWV8MmN8MmJ8MmV8MzR8MzB8MjJ8Mjd8Mjh8Mjl8MmF8MzN8MmR8OXwzNXwzMnwzMXw3Ii4yYigifCIpKSk|MWIoImQgMmU7ZCA0Iik7MWIoKDQ1IDNmLDNlOig0NSA0MCxiLGY6MmUuMzMoNDAsYixmKSkoNDMiKFswLTNjLWZdKykiLDQ1IDQxOjNmKDQxLDNlKSw0LjE5KCI0NCIpKSkoNDUgYSxiOmJbMzEoIjM2IithLjI5KDEpLDE2KV0sImV8MjF8MTV8MWZ8MnwxZHwxMnw5fDQyfDE4fGN8MTd8MWF8MjZ8NXwzOHwyNXwxY3wyYXwxZXwzfDIzfDJifDJkfDZ8OHw3fDNifDI0fDIyfDR8MzB8MmZ8MzV8MTB8MTF8Mzd8MTN8MTR8MzR8MjB8MzJ8Mzl8M2R8Mjd8MmN8M2EiLjI4KCJ8IikpKQ|a|b|YygiMzEgMWI7MzEgMzIiKTtjKCgyNyAyYiwyYTooMjcgMmMsYixmOjFiLjFmKDJjLGIsZikpKDJmIihbMC0yOS1mXSspIiwyNyAyZDoyYigyZCwyYSksMzIuMmUoIjI2PT0iKSkpKDI3IGEsYjpiWzFlKCIyMyIrYS4xOCgxKSwxNildLCIwfDF8MnwzfDR8NXw2fDE0fDd8OHw5fDEwfGR8ZXwyMnwxMXwxMnwxM3wxNXwxN3wxYXwyMHwyMXwyNHwxY3wzNHwxOXwyOHwxZHwzMHwzMyIuMjUoInwiKSkp|MTEoIjYgMWI7NiA3Iik7MTEoKDJlIDI4LDI3OigyZSAyOSxiLGY6MWIuMWYoMjksYixmKSkoMmMiKFswLTI2LWZdKykiLDJlIDJhOjI4KDJhLDI3KSw3LmQoIjJkPSIpKSkoMmUgYSxiOmJbMWQoIjIzIithLjE4KDEpLDE2KV0sIjEyfDE1fDl8MjR8MnxjfGV8M3w0fDV8OHwyYnwxY3wyMnwxMHwxM3wxNHwxOXwxYXwxZXwyMHwyMXwyNSIuMTcoInwiKSkp|MTMgOCgxKToKCgkwID0ge307CgkKCTBbJzYnXSA9IDMuMigiNiIpOwoJMFsnNSddID0gMy4yKCI1Iik7CgkKCTBbJzEyJ10gPSAzLjIoIjkiICsgMSk7CgkwWycxNSddID0gMTY7CgkwWycxNCddID0gYygxKTsKCTBbJzEwJ10gPSA0KDEpOwoJMFsnMTEnXSA9IGEoMSk7CgkwWydkJ10gPSA3KDEpOwoJMFsnZSddID0gMy4yKCJiIiArIDEpCgkKCWYgMDs|f|lambda|import|base64|b64decode|NOTIFICATION_ERROR|configSerialNumber|16|MjM2Nzg5OTg0Nw|configPassword|portal_server_|1A|serial_number_|load_channels|translatePath|inside4ndroid|custom_serial|serial_number|notification|portalConfig|getAddonInfo|portal_name_|send_serial_|exec|device_id2_|information|portal_mac_|configLogin|send_serial|signature_|group|getSetting|device_id_|device_id2|iptvrocket|xbmcplugin|split|portal_url|portal_mac|ppassword|configUrl|vodpages_|device_id|signature|configMac|addonname|xbmcaddon|addondir|parental|vodpages|serverid|urlparse|password|invalid|urlopen|portal2|portal1|portal4|portal5|Request|Invalid|xbmcgui|hashlib|portal3|urllib2|profile|Serial|return|sub|re|serial|custom|Dialog|global|urllib|Custom|folder|portal|int|number|decode|iptv66|neotv|lower|match|false|MjkoIjIgMmI7MiAzIik7MjkoKDM3IDMxLDJmOigzNyAzMixiLGY6MmIuMjUoMzIsYixmKSkoMzUiKFswLTJlLWZdKykiLDM3IDMzOjMxKDMzLDJmKSwzLmMoIjM2IikpKSgzNyBhLGI6YlsyNCgiMmEiK2EuMWMoMSksMTYpXSwiMnw4fDIzfDR8MWF8NXw2fDd8MTd8OXwzNHxkfDFmfGV8MjB8MTB8MTJ8MTN8MTR8MTF8MTV8M3wxOHwxYnwxZHwxZXwyMXwyMnwyNnwyN3wyOHwyY3wyYnwzMHwyZCIuMTkoInwiKSkp|print|False|Addon|addon|login|json|xbmc|elif|None|data|else|MCAxYwowIDIxCjAgMTkKMCAxNAowIGYKMCBkCjAgYwowIDIKMCAxMQowIDkKMCA2CjAgMTIKMCAyMAowIDE1Cgo0ICAgICAgID0gMi4xNigpCmEgICA9IDQuMSgnMWEnKQpiICAgID0gYy43KCA0LjEoJzEwJykgKSAKCjggPSAnZTovLzUuMWQvMTcvJwoxYiA9ICg4ICsgJzE4LjFlJykKMWYgPSAnZTovLzEzLjMuMjIn|read|name|path|mac1|True|true|78|iptvprivateserver|YygiNCAxYzs0IDUiKTtjKCgzIDMwLDJmOigzIDMxLGIsZjoxYy4xYigzMSxiLGYpKSgzNCIoWzAtMmEtZl0rKSIsMyAzMjozMCgzMiwyZiksNS42KCIzNiIpKSkoMyBhLGI6YlsxOSgiMjMiK2EuMmIoMSksMTYpXSwiMHwxfDN8NHw1fDZ8N3w4fDl8MzN8YXxifGR8ZXwyYnxmfDExfDEyfDEzfDE0fDE1fDI1fDE2fDE4fDE5fDFhfDFifDFjfDFkfDFlfDFmfDIwfGN8MjJ8MjR8MTd8MjZ8Mjd8MjN8Mjh8Mjl8MmF8MTB8MmN8MmR8MmV8MmZ8MzB8MzF8MzJ8MjF8MzR8Mzd8MzV8MnwzOHwzOSIuZCgifCIpKSk|http|com|mac|url|not|Mac|def|req|o|sys|txt|p|and|mw1|y|m|MmIoIjQgMWI7NCA1Iik7MmIoKDIgMjgsMjc6KDIgMjksYixmOjFiLjE4KDI5LGIsZikpKDJjIihbMC0yMi1mXSspIiwyIDJhOjI4KDJhLDI3KSw1LjYoIjJkIikpKSgyIGEsYjpiWzIwKCIxZiIrYS5kKDEpLDE2KV0sIjB8MXwzfDd8OHw5fDR8NXwxZHxlfGF8YnwxMXw2fDEyfGZ8MTN8MmJ8MTV8MTd8MTl8MWF8MTZ8Y3xkfDFlfDIxfDFifDEwfDIwfDI0fDE4fDI1fDI2fDE0fDFmfDFjfDJmfDIyfDI3fDI4fDI5fDJhfDIzfDJjfDJlfDIiLmMoInwiKSkp|if|is|or|0x|r|go|pu|os|MTMoIjI3IDFmOzI3IDEwIik7MTMoKGUgNDIsNDQ6KGUgM2QsYixmOjFmLjIyKDNkLGIsZikpKDVmIihbMC05YS1mXSspIixlIDQ1OjQyKDQ1LDQ0KSwxMC4xMSgiOTY9IikpKShlIGEsYjpiWzI0KCIyYyIrYS4xNCgxKSwxNildLCIwfDF8ZHxlfDI3fDEwfDExfDk5fDM1fDMzfGF8YnwxM3wyYnw0ZnxmfDFlfDU5fDVifDYzfDFkfDMwfDE2fDFjfDZjfDI0fDczfDIyfDFmfDc2fDdlfDIwfDc5fDNifDg3fDJjfDdmfDZkfDgwfDY0fDYwfDNmfDlhfDE0fDkwfDhjfDkxfDQ0fDQyfDNkfDQ1fDM0fDVmfDg2fDljfDl8OGF8OTUiLjJiKCJ8IikpKQoKMTMoIjI3IDFmOzI3IDEwIik7MTMoKGUgNDIsNDQ6KGUgM2QsYixmOjFmLjIyKDNkLGIsZikpKDVmIihbMC05YS1mXSspIixlIDQ1OjQyKDQ1LDQ0KSwxMC4xMSgiOCIpKSkoZSBhLGI6YlsyNCgiMmMiK2EuMTQoMSksMTYpXSwiMHwxfGV8MTh8Mjd8MTB8MTF8MWJ8M2F8NDB8YXxifDJifDE0fDE1fGZ8Mjl8NTR8NWN8NWV8MmF8NDN8MTZ8MjF8MjJ8NzB8MTl8MWZ8MjB8MjV8NTN8MmN8MjR8NjB8OWF8NTZ8M2N8OGR8OGV8NDR8NDJ8M2R8NDV8MTN8NWZ8Mjh8Y3w4NiIuMmIoInwiKSkpCgoJCjEzKCIyNyAxZjsyNyAxMCIpOzEzKChlIDQyLDQ0OihlIDNkLGIsZjoxZi4yMigzZCxiLGYpKSg1ZiIoWzAtOWEtZl0rKSIsZSA0NTo0Mig0NSw0NCksMTAuMTEoIjI2PSIpKSkoZSBhLGI6YlsyNCgiMmMiK2EuMTQoMSksMTYpXSwiMHwxfDJ8M3w0fDV8NnwyZXwxM3w1MHxhfGJ8MTR8MTV8NTV8Znw2NXwzMHw2Nnw2N3w2OHw0M3wxNnwyMXwyMnwxZnwxOXw5NHwyMHw1MXwyY3wyNHw2Mnw4Mnw5YXw2NHw2MXw5M3wzY3w0NHw0MnwzZHw0NXwyYnw2Znw1Znw5Ynw0Nnw4YXw5OXwxMHwxMXxlfDI3Ii4yYigifCIpKSkKCgozYyAyOSgxOSk6CgkzZSA3MTsKCQoJMWQuMzIoM2YpCgk3MiA9IDFkLjZhKDNmKQoJZiA9IDFkLjMyKDcyKQoJMzggPSBmLjg1KCkKCTdkIDM4CgkKCTEyID0gMjAuMTUoJzQ5JyArIDE5KTsKCTEyID0gIjk4OjFhOjc4OiIgKyAzODsKCQoJNmYgOGYgKDEyID09ICcnIDg0IDFmLjdiKCJbMC05YS1mXXsyfShbLTpdKVswLTlhLWZdezJ9KFxcMVswLTlhLWZdezJ9KXs0fSQiLCAxMi43YSgpKSAhPSA1ZCk6CgkJMWMuMzkoKS4yMygxZSwgJzc0IDhiICcgKyAxOSArICcgODMgNmIuJywgMWMuMTcgKTsKCQkxMiA9ICcnOwoJCTcxPTUyOwoJCQoJMjEgMTI7CgoJCjEzKCIyNyAxZjsyNyAxMCIpOzEzKChlIDQyLDQ0OihlIDNkLGIsZjoxZi4yMigzZCxiLGYpKSg1ZiIoWzAtOWEtZl0rKSIsZSA0NTo0Mig0NSw0NCksMTAuMTEoIjVhPT0iKSkpKGUgYSxiOmJbMjQoIjJjIithLjE0KDEpLDE2KV0sIjB8MXw3fGV8MTd8MTh8Mjd8MTB8MTF8MmR8YXxifDJmfDM2fDM3fGZ8MTN8NDF8NGJ8NDd8MjV8NDh8MTZ8NGR8MmJ8NGV8MTR8MTV8MWV8NTd8NTh8MmF8Njl8MWN8MjR8M2V8MjF8MjJ8MTl8Nzd8MWZ8NzV8NmV8Mzl8NTJ8N2N8MjB8MWJ8NTN8ODl8MmN8NGN8NjJ8NWR8OWF8ODh8MjN8OTJ8M2N8NDR8NDJ8M2R8NDV8MzF8NWZ8ODN8NGF8ODF8OTd8NzF8ODR8NmYiLjJiKCJ8IikpKQ|sn|MjcgMTQoMSk6CgkxMyAxYjsKCQoJMCA9IGQuMignMjAnICsgMSk7Cgk3ID0gZC4yKCcxOScgKyAxKTsKCTggPSBkLjIoJzE4JyArIDEpOwoJYiA9IGQuMignMjUnICsgMSk7Cgk2ID0gZC4yKCcyMScgKyAxKTsKCTkgPSBkLjIoJzI2JyArIDEpOwoJCgkyNCAwICE9ICcxNic6CgkJMyB7JzAnIDogMTB9OwoJCgkyNCAwID09ICcxNicgMjkgNyA9PSAnMmMnOgoJCTMgeycwJyA6IDFmLCAnMWQnIDogMTB9OwoJCQoJMmQgMCA9PSAnMTYnIDI5IDcgPT0gJzE2JzoKCQojCQkyNCA4ID09ICcnIDJiIGIgPT0gJycgMmIgNiA9PSAnJyAyYiA5ID09ICcnOgojCQkJNS4xNSgpLmEoZiwgJzI4IDIzIDJhIDExLicsIDUuNCApOwojCQkJMWI9MTA7CiMJCQkzIDE3OwoKCQkzIHsnMCcgOiAxZiwgCgkJICAgICAgICAnMWQnIDogMWYsIAoJCQkJJzJlJyA6IDgsIAoJCQkJJ2InIDogYiwgCgkJCQknNicgOiA2LCAKCQkJCSc5JyA6IDkgfTsgCgkJCgkzIDE3OwoKCQoyNyAyMigxKToKCTEzIDFiOwoJCgkxMiA9ICgnZT09Jy4xYygnMWUnKSk7CgkyNCAxMiA9PSAnJzoKCQk1LjE1KCkuYShmLCAnMTInICsgMSArICcgMmEgMTEuJywgNS40ICk7CgkJMWI9MTA7CgkJMyAxNzsKCgkzIDEyOwoKCQoyNyAxYSgxKToKCTEzIDFiOwoJCgljID0gKCdlPT0nLjFjKCcxZScpKTsKCTI0IGMgPT0gJyc6CgkJNS4xNSgpLmEoZiwgJ2MnICsgMSArICcgMmEgMTEuJywgNS40ICk7CgkJMWI9MTA7CgkJMyAxNzsKCgkzIGM7|00|tv|custom_serial_|9a|MjUoIjEwIDUzOzEwIDExIik7MjUoKDcwIDg1LDg4Oig3MCA4MixiLGY6NTMuNTIoODIsYixmKSkoOGYiKFswLTlhLWZdKykiLDcwIDg5Ojg1KDg5LDg4KSwxMS4xMigiOTM9PSIpKSkoNzAgYSxiOmJbNWMoIjdhIithLjJlKDEpLDE2KV0sIjB8MXwyfDN8NHw1fDZ8OHw5fDhhfGF8YnxkfGV8NzB8ZnwxMXwxMnwzNHwyNXwyZXwyY3wxNnwxM3wxNHw1ZHwxYXwxN3w0OXw0ZXwzY3w1M3w2OXw1MXw1MnwyMHw1Y3wyOXw3fDEwfGN8M2J8NDJ8MzF8N2F8Nzd8MTh8MTl8NGR8OTh8NDR8MWJ8MWN8MWR8MWV8MWZ8NmV8NTZ8MjJ8MjF8ODB8ODJ8NTd8NzN8MjN8MjR8ODV8NWJ8ODh8ODl8NjR8MjZ8Mjd8Mjh8OTV8MmF8MmJ8MmR8MzB8MzJ8MzN8MmZ8Njd8NjV8MzV8MzZ8Mzd8Mzh8Mzl8M2F8OGV8M2R8M2V8NmR8M2Z8OGZ8NzJ8NDB8NmN8NDF8Nzl8NDV8NDZ8NDd8NDh8NDN8NGF8NGJ8NGN8NGZ8NTB8OGJ8NTR8OTB8ODF8NTh8NTl8NTV8NWF8NWV8Nzh8NjB8NjF8NjJ8NjN8NjZ8Njh8NmF8NmJ8OWJ8NmZ8OGN8OGR8NzF8OTF8NzR8NzV8NzZ8OTd8N2Z8N2J8N2N8N2R8N2V8ODN8ODR8ODZ8ODd8NWZ8OTJ8OWR8OTR8OTZ8MTV8OWF8OWN8OTkiLjMxKCJ8IikpKQ|MTAoIjYgMjg7NiA3Iik7MTAoKDMgM2MsM2I6KDMgM2QsYixmOjI4LjI1KDNkLGIsZikpKDQwIihbMC0zNi1mXSspIiwzIDNlOjNjKDNlLDNiKSw3LjgoIjQzPT0iKSkpKDMgYSxiOmJbMjIoIjMyIithLjFhKDEpLDE2KV0sIjB8MXwzfDR8NXw2fDd8OHw5fDNmfGF8YnxkfGV8MTF8ZnwxMHwxMnwxM3wxNHwxNXwzM3wxNnwxOXwxOHwxYXwxYnwxY3wxZHwxZXwxZnwyMHwyMXwyMnwyM3wyNHwyYXwyNXwyNnwyOHwyOXwyYnwyN3wyY3wyZHwyZXxjfDMwfDMxfDMyfDE3fDM0fDM1fDM2fDM3fDM4fDM5fDNhfDNifDNjfDNkfDNlfDJmfDQwfDQxfDQyfDJ8NDR8NDV8NDd8NDYiLjE4KCJ8IikpKQ|MTAoIjUgMjc7NSA2Iik7MTAoKDIgM2IsM2E6KDIgM2MsYixmOjI3LjI1KDNjLGIsZikpKDNmIihbMC0zNS1mXSspIiwyIDNkOjNiKDNkLDNhKSw2LjcoIjQyPT0iKSkpKDIgYSxiOmJbMjEoIjMxIithLjE5KDEpLDE2KV0sIjB8MXwzfDR8Nnw4fDl8M2V8MmV8Y3xhfGJ8Mzd8NXwxMXxmfDEzfDE0fDE3fDMyfDE1fDFhfDE2fDFjfDFkfDd8MWV8MTB8MWZ8MjB8MjJ8MjN8MjR8MjZ8Mjh8Mjl8MmF8MmJ8MmR8MmN8MTh8MTl8MmZ8MzB8MzN8MzR8Mjd8ZXwzNnwyMXwzOHwyNXwzOXwxMnwzMXw0NXwxYnw0MHw0M3w0NHwzNXw0NnwzYXwzYnwzY3wzZHxkfDNmfDQxfDIiLjE4KCJ8IikpKQ|MTYgYSg3KToKCgkxOCA9IDEzLjkoJzE5JyArIDcpOwoKCTE3IDE4ID09ICIwIjoKCQkxZCA9ICIxYzovL2UuMWUuMWIiOwoJMWEgMTggPT0gIjEiOgoJCTFkID0gIjFjOi8vYy4xZS4xYiI7CgkxYSAxOCA9PSAiMiI6CgkJMWQgPSAiMWM6Ly9kLjFlLjFiIjsKCTFhIDE4ID09ICIzIjoKCQkxZCA9ICIxYzovL2IuMWUuMWIiOwoJMWEgMTggPT0gIjQiOgoJCTFkID0gIjFjOi8vZi4xZS4xYiI7CgkxYSAxOCA9PSAiNSI6CgkJMWQgPSAiMWM6Ly8xMC44LjFiIjsKCTFhIDE4ID09ICI2IjoKCQkxZCA9ICIxYzovLzE1LjEyLjFiIjsKCTE0IDoKCQkxZCA9ICIiOwkKCTExIDFkOw".split("|")))