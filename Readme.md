## LIFX Code for Elgato Stream Deck

This is the Python code used to control [LIFX](https://www.lifx.com/) lights with the [Elgato Stream Deck](https://www.elgato.com/en/gaming/stream-deck).

![LIFX](https://github.com/MishManners/LIFX-Streaming/blob/master/Images/Screenshot-2017-09-16-19.31.17.png)

### Instructions

Go to [LIFX Cloud token](https://cloud.lifx.com/settings) and grab your API settings/keys from your account. You'll see different keys for each light/scene.

1. Open the .bat file and change the location of where the .py file is located.
2. Save .bat file
3. Open .py file add the API key for the thing you want to control
4. Save .py file
5. Open .vbs file and change the location of where the .py file is located. The .vbs file is simply there to ensure the python script runs in the background.

Check out the [LIFX Dev Tools and API](https://api.developer.lifx.com/) to grab all your details. Once you have your scene and light keys, you can add them into the file. The .py file will open a command line. .pyw will be without the command line. However Python 3 should start this up without any worries.

Thanks to [ImSammy](https://www.youtube.com/watch?v=UP3PQu4PlaY) who originally put together the video tutorial. Thanks Sammy for all your hard work.
