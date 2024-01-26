import os
import urllib.request

versions = [
    ("1.20.4 (Last message, 12 years ago)", "https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar"),
    ("1.19.4", "https://piston-data.mojang.com/v1/objects/8f3112a1049751cc472ec13e397eade5336ca7ae/server.jar"),
    ("1.18.2", "https://piston-data.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar"),
    ("1.17.1", "https://piston-data.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar"),
    ("1.16.5 (I hate Netherrite)", "https://piston-data.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar"),
    ("1.15.2 (Ah! Bees)", "https://piston-data.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar"),
    ("1.14.4 (Skeppy's Favourite)", "https://piston-data.mojang.com/v1/objects/3dc3d84a581f14691199cf6831b71ed1296a9fdf/server.jar"),
    ("1.13.2 (When the textures were... perfect)", "https://piston-data.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar"),
    ("1.12.2 (Modder's Paradise)", "https://piston-data.mojang.com/v1/objects/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar"),
    ("1.11.2 (Nostalgia)", "https://piston-data.mojang.com/v1/objects/f00c294a1576e03fddcac777c3cf4c7d404c4ba4/server.jar"),
    ("1.10.2 (Mom, can I purchase a game?)", "https://piston-data.mojang.com/v1/objects/3d501b23df53c548254f5e3f66492d178a48db63/server.jar"),
    ("1.9.4 (Pvpers hate this one)", "https://piston-data.mojang.com/v1/objects/edbb7b1758af33d365bf835eb9d13de005b1e274/server.jar"),
    ("1.8.9 (Pvpers love this one)", "https://launcher.mojang.com/v1/objects/b58b2ceb36e01bcd8dbf49c8fb66c55a9f0676cd/server.jar"),
    ("1.7.10 (Lunar Network... where are you?)", "https://launcher.mojang.com/v1/objects/952438ac4e01b4d115c5fc38f891710c4941df29/server.jar"),
    ("1.6.4", "https://launcher.mojang.com/v1/objects/050f93c1f3fe9e2052398f7bd6aca10c63d64a87/server.jar"),
    ("1.5.1 (Hey bro, wanna play Minecraft?)", "https://launcher.mojang.com/v1/objects/d07c71ee2767dabb79fb32dad8162e1b854d5324/server.jar"),
    ("1.4.7 (Last message, 1 minute ago)", "https://launcher.mojang.com/v1/objects/2f0ec8efddd2f2c674c77be9ddb370b727dec676/server.jar"),
    ("1.3.2", "https://launcher.mojang.com/v1/objects/3de2ae6c488135596e073a9589842800c9f53bfe/server.jar"),
    ("1.2.5", "https://launcher.mojang.com/v1/objects/d8321edc9470e56b8ad5c67bbd16beba25843336/server.jar"),
]

os.chdir('..')
download_directory = ".mc/"
os.makedirs(download_directory, exist_ok=True)

print("Minecraft Version Downloader:")
for i, (version, _) in enumerate(versions, 1):
    print(f"[{i}] {version}")

while True:
    try:
        choice = int(input("Choose a version to download (enter the corresponding number): "))
        if 1 <= choice <= len(versions):
            break
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

selected_version = versions[choice - 1]
version_name, version_url = selected_version
download_path = os.path.join(download_directory, "server.jar")

print("WARNING: STABILITY IS NOT GUARANTEED IF YOU ARE USING OLDER MINECRAFT VERSIONS!")
print(f"\nDownloading {version_name}...")
urllib.request.urlretrieve(version_url, download_path)
exit()
