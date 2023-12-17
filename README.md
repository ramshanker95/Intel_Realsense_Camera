# Jetson Nano Robot Navigation using Intel_Realsense Camera
This repository contains the code for a Jetson Nano robot that navigates autonomously using LIDAR and camera sensors. The program utilizes depth readings from the LIDAR to detect obstacles and determine the robot's direction.

## Features:
 * Obstacle detection via LIDAR depth data
 * Directional control based on detected obstacles
 * Forward movement on clear paths
 * Left or right turn maneuvers around obstacles
 * LED indicators for visual feedback
   
## Hardware:
 * Jetson Nano
 * Intel Realsense Depth Camera
 * GPIO pins for LED control and send data another microcontroller
 * (Optional) Motors and motor controller

## Software:
 * Python 3
 * realsense_depth library
 * Jetson.GPIO
 * OpenCV

## DepthCamera Class
- Initializes the RealSense pipeline for depth and color streams.
- Fetches depth and color frames using RealSense camera.
- Manipulates the images and obtains depth information for obstacle detection.

## GPIO Control and Navigation Logic
- Sets up GPIO pins for left, right, and center object detection scenarios.
- Utilizes depth data from RealSense to detect obstacles in different regions.
- Controls the GPIO pins to steer the robot based on the detected obstacles and navigational requirements.
- Implements different navigational scenarios:
  - Forward movement, turning left or right, and stopping in front of detected obstacles.

   
## Usage:
 * Clone the repository.Install the required libraries (realsense_depth, Jetson.GPIO, OpenCV).
 * Connect the Intel Realsense Depth Camera and LEDs to the Jetson Nano.
 * Modify the GPIO pin assignments if necessary.
 * Run the lidar_camra.py script.
 * Observe the robot's movement and LED signals indicating detected obstacles and chosen directions.

## Customization:
 You can adjust the sensitivity of obstacle detection by modifying the thresholds for depth values. Adapt the LED control logic to match your specific LED setup and desired signaling behavior. Integrate the robot control signals with your chosen motor controller hardware.

### Happy robot navigation!
