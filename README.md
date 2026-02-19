# Computer_Graphics_Project
A Pygame-based interactive simulation where a rotating line fires to pop moving balloons using Bresenham’s line, midpoint ellipse, collision detection, and flood fill algorithms.

 Dynamic Gameplay:
    - Multiple Balloon Types: Small/Fast (higher points) and Large/Slow.
    - Adaptive Difficulty: Gravity and wind intensity increase as your score climbs.
    - Power-Up System: Bonus Time (+5s), Double Points (2x), and Slow Motion.

Technical Implementation

This project specifically avoids high-level drawing libraries for core primitives to showcase fundamental CG algorithms:

- Bresenham's Line Algorithm: Used for drawing the needle, arrows, and UI elements.
- Midpoint Ellipse Algorithm: Powers the drawing of balloons, clouds, and power-up icons.
- 2D Rotation: Implemented via rotation matrices for the firing needle and particle fragments.
- Physics Engine: Includes basic gravity simulation, sine-wave wind frequency, and collision detection.

- Installation & Setup

Clone the repository: bash git clone cd BalloonPoppingGame

Install Dependencies: Ensure you have Python 3.10+ and Pygame installed. bash pip install pygame

Run the Game: bash python main.py
