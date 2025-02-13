# Swarm-Drone-Authentication

## Overview
This project presents an authentication mechanism for swarm drones operating in a 5G network using proxy signatures and a leader selection mechanism. Drones play a crucial role in 5G architecture by expanding network coverage and enabling Device-to-Device (D2D) communication. However, traditional 4G security solutions lead to heavy traffic towards network core servers, which degrades 5G network performance.

To overcome this, we propose a lightweight, distributed proxy signature-based authentication mechanism that:
- Reduces traffic overhead toward the 5G core network.
- Ensures secure drone-to-drone authentication without overloading the network.
- Implements a leader election algorithm to enhance communication efficiency.

## Features
- **Proxy Signature-Based Authentication**: Enables secure and lightweight authentication within the drone swarm.
- **Leader Selection Mechanism**: Ensures dynamic leader replacement in case of failures.
- **Privacy-Preserving Authentication**: Drones authenticate without revealing their private keys.
- **5G Integration**: Optimized for low-latency, high-speed communication.
- **Reduced Network Overhead**: Reduces the burden on the 5G core by delegating authentication.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Vijayroyal358/Swarm-Drone-Authentication.git
cd Swarm-Drone-Authentication
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Main Simulation
```bash
python main.py
```

## Usage

### 1. Run the Drone Simulation
```bash
python main.py
```
This starts the swarm simulation with flocking and shape formation.

### 2. Run Shape Visualization
```bash
python plot_shape.py
```
Generates predefined shape formations for drones.

### 3. Run Trajectory Visualization
```bash
python plot_traj.py
```
Plots drone movement trajectories over time.

## Project Structure
```
📂 Swarm-Drone-Authentication
 ├── 📂 graphics/                  # Contains visualization assets
 ├── 📂 utilities/                 # Utility functions and helper scripts
 ├── 📄 Ambi_Resolve_A.py          # Ambiguity resolution in swarm movement
 ├── 📄 Main_simple.py             # A simplified version of the main simulation
 ├── 📄 agent.py                   # Base class defining individual drone behavior
 ├── 📄 agent_flock.py             # Implements flocking behavior for drones
 ├── 📄 agent_id.py                # Drone identification and authentication
 ├── 📄 constants.py               # Stores constant values for simulation
 ├── 📄 drone_simulation.py        # Main drone simulation logic
 ├── 📄 environment.py             # Defines simulation environment
 ├── 📄 localization_2_MultiP_A.py # Localization algorithm for swarm
 ├── 📄 main.py                    # Entry point to run the simulation
 ├── 📄 plot_flower.py             # Generates flower-like formations
 ├── 📄 plot_shape.py              # Visualizes drone formations
 ├── 📄 plot_traj.py               # Plots trajectory of drones
 ├── 📄 shape_visualiser.py        # Displays shape formations
```

## Future Scope
- Integration with Real Drone Hardware
- Obstacle Avoidance & Collision Prevention
- Adaptive Path Planning in Dynamic Environments
- Enhanced Authentication for Secure Drone Communication

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries, please contact [Vijayroyal358](mailto:vijayroyal358@example.com).

---
