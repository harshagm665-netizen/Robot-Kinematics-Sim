# Robot Kinematics & Motion Profiling

## 📐 Mathematical Model
The robot is modeled as a 2-DOF serial chain:
1. **Joint 1 (Revolute):** Neck pitch rotation ($\theta$) limited to $\pm45^\circ$.
2. **Joint 2 (Prismatic):** Linear hand extension ($d$) along the neck's local axis.

## 🧮 Forward Kinematics
The position of the hand tip $(x, z)$ is computed as:
$$x = d \cdot \cos(\theta)$$
$$z = h_{neck} + d \cdot \sin(\theta)$$

## 🛠️ Implementation
- **Decoupled Logic:** The kinematics engine is separate from the visualization to allow for integration into real-time control loops.
- **Safety Constraints:** Software-level validation to prevent mechanical over-extension.