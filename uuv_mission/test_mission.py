from uuv_mission.dynamic import Mission
import matplotlib.pyplot as plt
import os

def main():
    # Build path to mission.csv relative to this script
    script_dir = os.path.dirname(__file__)  # uuv_mission/
    csv_path = os.path.join(script_dir, "../data/mission.csv")  # ../data/mission.csv from uuv_mission/

    # Load mission from CSV
    mission = Mission.from_csv(csv_path)

    # Print first few values for a sanity check
    print("Reference (first 5):", mission.reference[:5])
    print("Cave Height (first 5):", mission.cave_height[:5])
    print("Cave Depth (first 5):", mission.cave_depth[:5])
    print("Shapes:", mission.reference.shape, mission.cave_height.shape, mission.cave_depth.shape)

    # Quick plot
    plt.figure(figsize=(10,5))
    plt.plot(mission.reference, label="Reference")
    plt.plot(mission.cave_height, label="Cave Height", linestyle="--")
    plt.plot(mission.cave_depth, label="Cave Depth", linestyle="--")
    plt.xlabel("Time step")
    plt.ylabel("Depth")
    plt.title("Mission Data from CSV")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()