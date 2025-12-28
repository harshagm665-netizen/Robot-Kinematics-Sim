import matplotlib.pyplot as plt
from core.kinematics import RobotKinematics

# 1. Setup Robot Specs
config = {'neck_height_cm': 50, 'base_offset_cm': 10}
bot = RobotKinematics(config)

# 2. Define a "Movement" (e.g., Neck at 30 deg, Hand pushed out 15cm)
neck_angle = 30 
extension = 15

if bot.check_limits(neck_angle, extension):
    pos = bot.calculate_forward_kinematics(neck_angle, extension)
    print(f"Hand Tip Position: X={pos[0]:.2f}, Y={pos[1]:.2f}, Z={pos[2]:.2f}")

# 3. Simple 2D Plot (Side View)
plt.figure(figsize=(6,6))
plt.plot([0, 0], [0, config['neck_height_cm']], 'k-', lw=4, label="Body") # Body
plt.plot([0, pos[0]], [config['neck_height_cm'], pos[2]], 'r-o', lw=6, label="Hand") # Hand

plt.xlim(-10, 40)
plt.ylim(0, 70)
plt.xlabel("Forward Distance (cm)")
plt.ylabel("Height (cm)")
plt.title("Robot Motion Profile (Side View)")
plt.grid(True)
plt.legend()
plt.show()