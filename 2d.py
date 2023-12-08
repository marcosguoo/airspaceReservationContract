import matplotlib.pyplot as plt
import random
import heapq

class Drone:
    def __init__(self, drone_id, start, end):
        self.drone_id = drone_id
        self.start_point = start
        self.end_point = end
        self.path = self.calculate_path()

    def calculate_path(self):
        open_set = [(0, self.start_point)]
        came_from = {}
        g_score = {self.start_point: 0}

        while open_set:
            current_cost, current = heapq.heappop(open_set)

            if current == self.end_point:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                return path[::-1]

            for neighbor in self.neighbors(current):
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    heapq.heappush(open_set, (tentative_g_score + self.heuristic(neighbor), neighbor))
                    came_from[neighbor] = current

        return [self.start_point]

    def neighbors(self, point):
        x, y = point
        return [
            ((x + 1) % 30, y),
            ((x - 1) % 30, y),
            (x, (y + 1) % 30),
            (x, (y - 1) % 30),
        ]

    def heuristic(self, point):
        return abs(point[0] - self.end_point[0]) + abs(point[1] - self.end_point[1])

def simulate_drones(num_drones):
    drones = [Drone(drone_id=i, start=(random.randint(0, 29), random.randint(0, 29)), end=(random.randint(0, 29), random.randint(0, 29))) for i in range(num_drones)]

    plt.figure(figsize=(8, 8))

    for drone in drones:
        plt.plot(*zip(*drone.path), label=f'Drone {drone.drone_id}', marker='o')

    plt.title('Drone Path Simulation')
    plt.xlim(0, 29)
    plt.ylim(0, 29)
    plt.legend()
    plt.show()

# Number of drones
num_drones = 15

# Start the drone simulation
simulate_drones(num_drones)
