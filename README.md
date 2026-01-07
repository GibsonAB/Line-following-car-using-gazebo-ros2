# Line-following-car-using-gazebo-ros2

https://github.com/user-attachments/assets/f34f220c-631a-40ee-a6c9-0d321a69ee11

This project implements a **gesture-controlled autonomous line-following car** simulated in **Gazebo** using **ROS 2**. The vehicle follows a predefined line using computer vision, and its motion is **started or stopped via hand gestures** detected with **OpenCV**. A **custom URDF** model is used for accurate kinematic and sensor simulation, and **RViz** is used for visualization and debugging.

The system was developed incrementally:
1. Line-following behavior was implemented and validated in Gazebo.
2. Hand-gesture recognition (open palm / closed fist) was integrated to control vehicle motion while line following remains active.

---

## Features
- Vision-based line following in simulation
- Hand gesture control:
  - **Open palm** → Start / resume motion
  - **Closed fist** → Stop the car
- Custom URDF robot model
- Modular ROS 2 node architecture
- Real-time visualization in RViz
- Fully simulated workflow in Gazebo

---

## System Architecture

### Simulation
- **Gazebo**: Physics simulation, environment, and line track
- **URDF**: Custom robot description including:
  - Differential drive kinematics
  - Camera sensor for line detection
  - Proper TF tree for ROS integration

### Perception
- **Line Detection**:
  - Camera image subscribed from Gazebo
  - OpenCV-based preprocessing (grayscale, thresholding)
  - Line centroid extraction for steering control

- **Gesture Recognition**:
  - Webcam or simulated camera input
  - OpenCV-based hand segmentation
  - Simple gesture classification:
    - Open palm
    - Closed fist

### Control
- Proportional steering control based on line centroid error
- Gesture-based state machine:
  - `RUNNING`: Line following active
  - `STOPPED`: Velocity commands suppressed

### Visualization
- **RViz**:
  - Camera feed
  - Robot model and TF frames
  - Debug markers (optional)

---

## Software Stack
- ROS 2
- Gazebo
- RViz
- OpenCV
- Python / C++ (depending on implementation)

---

## Gesture Logic
| Gesture       | Action            |
|--------------|-------------------|
| Open Palm     | Start / Resume car |
| Closed Fist   | Stop car           |

Gesture commands act as a **high-level enable/disable control** and do not interfere with the underlying line-following controller.

---

## Workflow
1. Launch Gazebo with the custom URDF and line track.
2. Start the line-following perception and control nodes.
3. Run the gesture recognition node.
4. Use hand gestures to start or stop the car while it follows the line autonomously.

---

## Assumptions and Limitations
- Gesture recognition is based on simple visual features and assumes:
  - Adequate lighting
  - Clear hand visibility
  - Limited background clutter
- Line-following performance depends on:
  - Camera calibration
  - Track contrast
- The project is validated **in simulation only**.

---

## Future Improvements
- Robust gesture recognition using deep learning
- Additional gestures (turn, speed control)
- Transition to real hardware
- Improved line detection under varying lighting conditions

---

## Conclusion
This project demonstrates the integration of **computer vision, robot simulation, and human–robot interaction** within a ROS 2 environment. By combining autonomous line following with gesture-based control, it showcases a flexible and extensible framework for vision-driven mobile robotics.



