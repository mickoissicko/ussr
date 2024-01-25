# The USSR
> What is it?

I started this program as a barebones, small, and lightweight tool to allow my friends to start/stop the SMP if I am unable to do it.

It acts as a server panel. Pretty cool if you ask me.

> Why is it better than server hosting?

Well first of all... IT'S FREE. 0 DOLLAHS. Completely free. Forever. Yes, I copied Aternos -- why not use that?

Aternos sucks, and stops server after 3-5 minutes of inactivity, and it has limited RAM. With this, you can host your own server, have 100% control over it, unlimitied RAM & CPU, as well as amazing ping because you can utilise the many locations Ngrok offers ... for FREE!

My friend gets ~200ms average on Aternos, but on Ngrok's Singapore location, around 90ms. (He lives near Singapore!)

> How do I use it?

Check the official [Wiki](https://mick.gdn/dir.html)

# Info
You need to kill all Ngrok processes before re-running / restarting the USSR. After the USSR process is terminated, it itself does not stop the Ngrok processes which is a problem. Ngroksenpai freaks out and doesn't correctly send all the IPs.

To kill processes on Arch:

`sudo kill ngrok`

To kill processes on Windows:

`taskkill /f /im ngrok.exe`

The size of the program after installation on:

* Windows: `84.05 megabytes`
* Includes: `MCRCON`, `Requests`, `Flask`, `Tar`, `C-URL`, `Chocolatey`, `Ngrok`
* Excludes: `PyPi`, `Python`

* Linux/Darwin:
* Includes:
* Excludes: 
