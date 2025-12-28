import numpy as np

class RobotKinematics:
    def __init__(self, config):
        self.neck_height = config['neck_height_cm']
        self.base_offset = config['base_offset_cm']

    def calculate_forward_kinematics(self, neck_angle_deg, hand_extension_cm):
        """
        Calculates the 3D position of the Hand Tip.
        neck_angle: Angle in degrees (0 is straight forward)
        hand_extension: How far the hand is pushed out from the neck
        """
        # Convert to Radians for math
        theta = np.radians(neck_angle_deg)
        
        # Hand tip coordinates relative to the base
        # X is forward, Y is side-to-side, Z is height
        x = hand_extension_cm * np.cos(theta)
        y = 0  # Assuming hands move only in X-Z plane
        z = self.neck_height + (hand_extension_cm * np.sin(theta))
        
        return np.array([x, y, z])

    def check_limits(self, angle, extension):
        """Safety check for mechanical constraints"""
        angle_safe = -45 <= angle <= 45
        ext_safe = 0 <= extension <= 20 # Assuming 20cm max reach
        return angle_safe and ext_safe