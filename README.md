# CurseForge CLI With GUI
This is a forked verson of https://github.com/North-West-Wind/CurseForge-CLI Written in Java & python. Designed for all platform and portable use.

## Dependencies
[This Section Needs Changes]

## Arch Based Distros
- Python3 - `Installed Already`
- tkinter - `Sudo pacman -S tk`
- JDK - `sudo pacman -S jre-openjdk-headless jre-openjdk jdk-openjdk openjdk-doc openjdk-src`

## Debian Based Distros
[This section Needs to be added]

## Installation
[This Section Needs to be added

## Gui Instructions
[This Section Needs to be added]

#### Terminal Functions

### Commands
- `help` Display commands of the program.
- `config` Configure the program.
  - `directory <path>` Set the working directory of the program.
- `modpack` Commands for modpack.
  - `install <ID[_FileID]>` Install modpack(s). The ID parameter is the ID of the modpack found on CurseForge. To install a modpack with a specific version, use the format ID_FileID, where FileID is the ID of the modpack zip file on CurseForge. Omit to install the latest version.
  - `delete <ID[_FileID] | Slug>` Delete modpack(s). The ID/slug parameter is the ID/slug of the modpack. Specify the FileID to remove a spcific version.
  - `list` List all installed modpacks.
- `profile` Commands for custom profile.
  - `create` Create a custom profile. You will need to answer some questions.
  - `edit <profile>` Edit a custom profile. Similar to `create`.
  - `delete <name>` Delete a profile. The name parameter is the name of the profile.
  - `add <profile> <ID[_FileID]>` Add a mod to the profile. ID is the ID of the mod on CurseForge.
  - `remove <profile> <ID>` Remove a mod from the profile. Works similarly to `add`.
  - `update <profile> [all | ID[_FileID]]` Update mods of a profile. Append `all` to update all mods. Omit ID to check for updates. Include FileID to update to a specific version.
  - `export` Export the profile as an uploadable modpack format.
  - `import <path>` Import a downloaded modpack.
- `mod` Commands for mods.
  - `search <keywords>` Search for mods with keywords. Will also export results to file for easier adding to profile.

### Configuration
You can configure CurseForge CLI by editing `cf.json`. The file should be generated once the JAR file has run once.  
These are the options you can edit:
- `directory` The directory where modpacks and profiles are stored. Default: `./curseforge-cli`
- `acceptParent` Whether mods with only the parent version of a profile is accepted or not. For example, you can install a 1.18 mod into a 1.18.1 profile. Default: `true`
- `suppressUpdates` Whether the update messages should be suppressed or not. Default: `false`
- `silentExceptions` Whether the exception stack traces should be silenced or not. Default: `false`
- `retries` The amount of retries when downloading something fails. Default: `3`

### Other Features
If you put the JAR file together with a zip of the exported profile, CurseForge CLI will automatically install that profile to the current directory.  
This has 1 limitation, which is you should not put multiple zip files in the same directory.

### Note
When you run the CLI, you should see a new file called `cf.json`. It is essentially the save file of the program. If you don't know what you are doing, do not touch it.

You will find modpack/mod name with some numbers after it. That is totally intentional. Do not attempt to remove it. It is used for recognition.

Installing a modpack will also generate a profile. However, the profile doesn't use the correct mod loader. Please install the mod loader yourself as instructed.

## License
GNU GPLv3
