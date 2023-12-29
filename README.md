# Universal Server Start Remote (USSR)
* USSR is intentional, I wanted to make a funny abbreviation.
* I am not serious, the comments are trash
* Good luck LOL

## Requirements
* Supports Python 3.9.9 till 3.10.0.
* Python 3.9.10 is recommended.
* Add to PATH.
* Disable PATH length limit.
* Requires Windows Powershell to be run as an isolated Window, not in attached to Windows-Terminal, or inside Terminal.
* Needs Python libraries: os, subprocess, and flask
* Requires Powershell version 7 or above.
* Requires port-forwarding, or a port-forwarding service like L2H or Ngrok.

## Why?
This project started as a funny switch, but I spent over 5 hours making this dumb funny clicky server open-y haha omg switch. Kill me. If you have a Minecraft server, an SMP, and you don't want to use something like Aternos, however, you don't want the prestigous Day count in the server to go up because you left it online for 2 days, well, this is a use for the USSR.

If you are sleeping, your friends can start/stop the server, just remind them to stop it! Really... really, and oddly specific use scenario, but... yeah.

Github is a place for stuff like this, so I think it's pretty cool.
It is NOT user friendly... at all. Good luck installing it. When I get around to making a tutorial, I'll link it here.

## Installation guide
* Read comments, figure it out
* Video tutorial coming soon

## R-CON
> RCON is used to (gracefully) stop the server and reduce corruption chance, and also save the world. If the server is forcefully stopped, it's not nice. It's like running and falling. You know what I mean.
* You need to configure R-CON port (25575 default,)
* Also need to configure R-CON password (root_admin) as set here
* Configure the server address, but keep it localhost and just port-forward.

## Using NGROK vs. Manual port-forwarding
> Doesn't (necessarily) need to be NGROK, you can use L2H or PLAYIT.GG, but it is what it is. If you manually port-forward you'd have to add rules (tcp, udp,) for server and other website rules for (index.html,) and port 5000 because that's what flask likes to use.
