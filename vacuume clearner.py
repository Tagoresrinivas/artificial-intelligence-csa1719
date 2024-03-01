class VacuumCleanerEnvironment:
    def __init__(self, location_condition):
        """
        Initializes the vacuum cleaner environment.
        location_condition: Dictionary with the initial condition of each location.
                            e.g., {'A': 'Dirty', 'B': 'Dirty'}
        """
        self.location_condition = location_condition
        self.cost = 0

    def is_dirty(self, location):
        """Check if a given location is dirty."""
        return self.location_condition[location] == 'Dirty'

    def clean(self, location):
        """Clean the specified location."""
        if self.is_dirty(location):
            print(f"Cleaning location {location}")
            self.location_condition[location] = 'Clean'
            self.cost += 1
        else:
            print(f"Location {location} is already clean.")

    def status(self):
        """Print the current status of the environment."""
        print(f"Location A: {self.location_condition['A']}, Location B: {self.location_condition['B']}, Cost: {self.cost}")

def vacuum_cleaner_agent(environment):
    """Simple vacuum cleaner agent."""
    start_location = 'A'  # Starting location
    other_location = 'B'

    # Check and clean the start location
    if environment.is_dirty(start_location):
        environment.clean(start_location)
    else:
        print(f"Location {start_location} is already clean.")

    # Move to the other location
    print(f"Moving to location {other_location}")
    environment.cost += 1  # Increase cost for moving

    # Check and clean the other location
    if environment.is_dirty(other_location):
        environment.clean(other_location)
    else:
        print(f"Location {other_location} is already clean.")

if __name__ == "__main__":
    # Initialize the environment, you can change the initial conditions here
    environment_conditions = {'A': 'Dirty', 'B': 'Dirty'}
    env = VacuumCleanerEnvironment(environment_conditions)

    # Before cleaning
    print("Before cleaning:")
    env.status()

    # Run the vacuum cleaner agent
    vacuum_cleaner_agent(env)

    # After cleaning
    print("\nAfter cleaning:")
    env.status()
