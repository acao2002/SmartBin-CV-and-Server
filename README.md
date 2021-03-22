# SmartBin-CV-and-Server

## Abstract 

Ho Chi Minh city, among the top 13 most populated cities in the world, generates nearly 9,000
tons of solid waste daily. A significant part of the problem stems from a lack of garbage-disposal facilities
and a lack of environmental awareness in public spaces such as schools, hospitals, and parks. The project
“Smart Bin” aims to reduce littering in these areas by building an Internet-of-Things (IoT) system that
automatically collects trash from stationary users. The system is purposed to reduce the inconvenience of
moving far distances to deposit trash, thereby reducing the rate of littering.
A prototype is first designed to cope with a controlled environment and is tested in-door use at the
moment due to time and resource constraints, though it can be open to future upgrades. The original
schematic integrates three subsystems: autonomous vehicle, overwatch camera, and user phone
application.
The autonomous vehicle carrying a trash bin is a tank drivetrain with stepper motors controlled by
the ESP8266 microcontroller for power and flexibility. The receives location data from the overwatch
camera into specific instructions for motor steps and rotations, coupled with run/stop signals specified by
a user. The overwatch camera combines a high-definition optical module with Computer Vision /
Machine Learning algorithms to detect users and the bin’s locations via QR codes attached on top of the
bin and the users’ real faces. Then through an HTTP server, the overwatch camera directs the autonomous
vehicle to move towards the user via a pre-optimized route. The user can also instruct the vehicle
manually via a Bluetooth-connected phone application for faulty correction and alternative locations.
Overall, three subsystems administered a shared database of coordinates to change the course of actions in
real-time.
A few iterations tested different drive trains for the bin, different motors, drivers, and
microcontrollers, and multiple detection methods. The last version is capable of automatically moving to
the target and returning to the original position without manual input. The first model, however, due to the
short detection range, is functional only in limited space. Looking forward, we aim to expand this feature
to extend the application to a broader range of places and later on, to serve disabled people who are
unable to put the trash away.

## Techonologies 

1. Computer Vision
2. Facial Recognition 
3. Flask Backend development 
4. Ardunio(Microcontroller)
5. Android App(MIT APP INVENTOR)
6. IOTs

## Paper 

read the full paper at https://drive.google.com/file/d/1t47wuzvR15X3JGvWso9eJdDI0sxZgopj/view?usp=sharing


