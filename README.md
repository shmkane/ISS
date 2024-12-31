# ISS Tracker

A real-time tracker for the **International Space Station (ISS)** that fetches live coordinates from the open-source [Open Notify API](http://api.open-notify.org/iss-now.json). The application continuously polls the ISS's latitude and longitude, normalizing the data onto a 2D map of Earth.

As the ISS orbits the planet, its path is visualized on the map, offering a dynamic view of its trajectory. The tracker also highlights the **next time the ISS will fly overhead** a specified location, like my own in **North Carolina**.

This project combines **real-time data** with **interactive mapping**, demonstrating how satellite position data can be used to create visually engaging representations of space-related phenomena.

![ISS Tracker Visualization](https://raw.githubusercontent.com/shmkane/ISS/master/ISS.png)

## Features
- **Real-time ISS location tracking** using latitude and longitude coordinates.
- **Path visualization** of the ISS's orbit over Earth in 2D.
- **Time-based updates** showing when the ISS will be overhead a specific location (e.g., North Carolina).

## Technologies Used
- **JavaScript** for real-time data fetching and rendering.
- **Mapping libraries** to project the ISS's 3D trajectory onto a 2D map.
- **Open Notify API** to fetch live ISS position data.

### Usage
Clone the repository, run the project, and watch the ISS as it orbits Earth in real-time. You can also track when it will pass over a specific region.
