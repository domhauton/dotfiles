from i3pystatus import Status

status = Status()

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    format="%a %-d %b %X",)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load")

status.register("mem")

# Displays whether a DHCP client is running
status.register("runwatch",
    name="DHCP",
    path="/var/run/dhclient*.pid",)

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
status.register("network",
    interface="eno1",
    hints = {"markup": "pango"},
    format_up="<span color=\"#00FF00\">{v4}</span> {bytes_sent:04d}/{bytes_recv:04d}",)

status.register("openvpn",
    vpn_name="bath_dh499",
    status_command = "bash -c 'nmcli con show id bath_dh499 | grep connected'",
    vpn_up_command = "nmcli con up id bath_dh499",
    vpn_down_command = "nmcli con down id bath_dh499",)

status.register("openvpn",
    vpn_name="purevpn",
    status_command = "bash -c 'nmcli con show id purevpn | grep connected'",
    vpn_up_command = "nmcli con up id purevpn",
    vpn_down_command = "nmcli con down id purevpn",)

# Shows disk usage of /
# Format:
# 42/128G
status.register("disk",
    path="/",
    format="{used}/{total}G",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    format="♪{volume}",)

# Shows mpd status
# Format:
# Cloud connected▶Reroute to Remain
status.register("mpd",
    format="{title}{status}{album}",
    status={
        "pause": "▷",
        "play": "▶",
        "stop": "◾",
    },)

status.register("spotify",)
status.run()
