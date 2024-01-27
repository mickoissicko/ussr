### What is it?

I started this program as a barebones, small, and lightweight tool to allow my friends to start/stop the SMP if I am unable to do it.

It acts as a server panel. Pretty cool if you ask me.

### Why is it better than server hosting?

Well first of all... it is completely free, like Aternos -- so why not use that??

Aternos sucks, and stops server after 3-5 minutes of inactivity, and it has limited RAM. With this, you can host your own server, have 100% control over it, unlimitied RAM & CPU, as well as amazing ping because you can utilise the many locations Ngrok offers ... for FREE!

My friend gets ~200ms average on Aternos, but on Ngrok's Singapore location, around 90ms. (He lives near Singapore!)

### How do I use it?

Check the [official Wiki](https://mick.gdn/dir.html)

# Info
You need to kill all Ngrok processes before re-running / restarting the USSR. After the USSR process is terminated, it itself does not stop the Ngrok processes which is a problem. Ngroksenpai freaks out and doesn't correctly send all the IPs.

To kill processes on Arch:

`sudo kill ngrok`

To kill processes on Windows:

`taskkill /f /im ngrok.exe`

The size of the program after installation on:

* **Windows**: `84.05 megabytes`
* *Includes*: `MCRCON`, `Requests`, `Flask`, `Tar`, `C-URL`, `Chocolatey`, `Ngrok`
* *Excludes*: `PyPi`, `Python`

* **Linux/Darwin**: `34.93 MB`
* *Includes*: `Ngrok`, `MCRCON`, `Flask`, `Requests`
* *Excludes*: `C-URL`, `Tar`, `PyPi`, `Python`

Please note that the Wiki contains steps to manually install/configure the USSR. You should **only** check out the wiki if you use MacOS, or if you use any Linux distribution that isn't Arch. (Gentoo, Debian, Alpine, etc.)

The Wiki may also be used to troubleshoot some steps. However, if you use a Windows machine or Archlinux, installing it via the shell script (for Arch,) and the batch script (for Windows,) should work just fine.

# Compatibility
This application works on:

* MacOS (Darwin)
* Linux (Debian, Arch, Gentoo, etc.)
* Windows (W7-W11 x86-64)

So, yes, you **could** say it is cross-platform, however for these OSes:

* MacOS
* Gentoo or Debian
* Windows (7, and below), (any, but 32-bit)

It may need additional modification to get it working correctly. Especially for MacOS, because the `.sh` scripts are catered to Arch, and use the `pacman` package manager. Debian/Gentoo do not use Pacman.



