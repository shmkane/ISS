# ISS
Fetches live coordinates from the International Space Station from an open source API, http://api.open-notify.org/iss-now.json. Reponse yields current latitude and longitude of ISS.
Polls lat/longs on an interval and normalizes it to an image of earth. 

The result is taking the 3d position of the ISS and plotting it against a 2D map of Earth, and as time progesses, the path of the ISS is visualized. 

![Pic of the program](https://raw.githubusercontent.com/shmkane/ISS/master/ISS.png)
