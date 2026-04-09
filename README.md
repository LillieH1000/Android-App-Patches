<div align="center">

# Android App Patches

#### My personal collection of Android app patches that do things such as removed ads, unlock premium and more.
#### More patches will be added and updated overtime.

</div><br>

#### Patches:
- [MTG Scanner - Dragon Shield](https://play.google.com/store/apps/details?id=pt.tscg.mtgmanager) - Unlock premium and bypass play store check
- [RAR](https://play.google.com/store/apps/details?id=com.rarlab.rar) - Remove start ad popup

<br>

#### Usage:
1) Extract the apk of the app using [Apktool](https://apktool.org/) with the -r flag.
2) Rename extracted folder to the bundle id of the app, example: com.rarlab.rar.
3) Copy the apps patch.py to the same folder as the extracted apk.
4) Run the patch using [Python3](https://www.python.org/), version 3.14+ recommended.
5) Rebuild the apk using [Apktool](https://apktool.org/) with the --copy-original flag.