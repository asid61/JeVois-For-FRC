# The Design Simple Guide to JeVois for FRC
By Anand Rajamani


## Part 1
### Introduction
  Vision in FRC has  traditionally been a massive challenge in FRC. Integrating camera, control system, and vision processing is a massive challenge to undertake, one that many teams struggle and fail with each year. Paying hundreds of dollars for coprocessors and setting up specialty cameras, only to find that there’s no enough time to get it to play nice with the robot code in time for competition, is a cycle many teams know all too well.
  Recently, however, small integrated camera modules have started to become popular. The Pixy (CMUcam5) and openMV cameras were pioneers in this field, but more recently a game-changing camera appeared: the JeVois. The JeVois Smart Machine Camera is a small CPU/GPU/Camera combo that features a highly optimized Linux-based OS that can run OpenCV code in Python or C++ very efficiently. The JeVois is not a direct replacement for a powerful coprocessor like the Nvidia Jetson series, but the JeVois can be put to work within minutes of pulling it out of the box. It is also (at time of writing) available with same-day shipping with Amazon Prime if ordered in the morning, or next-day shipping with Prime if ordered in the evening for only $50. The purpose of this guide is to learn how to use the JeVois in a manner that suits FRC as fast and as painlessly as possible, especially for people who do not consider themselves experienced programmers.

### Goals:
1. Have the JeVois stream video to your computer
2. Communicate with the JeVois via the Arduino Serial Monitor
3. Set up GRIP to work with the JeVois
4. Reorder the JeVois file system to make programming as easy as possible
5. Run GRIP-generated Python code on the JeVois to recognize retroreflective targets
6. All of this can be set up in well under a day. Part 2 of this guide details on moving data to the RoboRIO once the vision pipeline is working.

### Before We Begin
What do you need to get started? Not too much, except:
- [A Jevois](https://www.jevoisinc.com/) - also available from Amazon for the same price
- Mini-USB B cable, NOT a Micro-USB
