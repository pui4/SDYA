# SDYA
An open source YouTube app for the steam deck writen in python.

So you can enjoy YouTube TV on the steam deck.

NOTE: THIS IS NOT CURRENTLY BEING WORKED ON AS I THINK IT AS A GOOD AS I CAN MAKE IT. IF THERE IS A BREAKING ISSUE WITH THE APP THEN I WILL UPDATE IT.

## INSTALLATION
Execute the following comands in Konsole.

NOTE: Some of these commands require sudo so change your password first if you haven't already
```
git clone https://github.com/Precious13ui/SDYA.git /home/deck/Downloads/SDYA
```
Clones the github repo to /home/deck/Downloads/SDYA.

If it is not there than move it there as it WILL NOT work other wise.

```
cd /home/deck/Downloads/SDYA
```
Moves to the downloaded repo.
```
sudo steamos-readonly disable
```
Sets it so we can install packages.

NOTE: If you have done this before you don't have to do it again.
```
python3 setup.py
```
This sets up all the dependencys needed and creates the app.

If it FAILS with a bunch of key errors then run ```pacman-key --populate archlinux```

## ADDING TO STEAM
Right click on YouTube App on the desktop.

Click properties.

Click permissions.

Then check is executable.

Then close the properties window.

Open Steam.

Click on add a game.

Then click Add a Non-Steam Game.

Then click Browse.

Browse to the desktop.

Then double click on YouTube App.desktop.

Then click ADD SELECTED PROGRAMES.

Now if you boot into Gaming Mode you should see YouTube App in Non-Steam Games.

You have now installed the YouTube App.

It takes a while to launch so be pacient.

## FEATURES
Currently everything works except livestreams. There is no uBlock or SponsorBlock.
