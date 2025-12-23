import numpy as np
import matplotlib.pyplot as plt
class OpticalMedium:
    def __init__(self, name, refractive_index, absorption_coeff=0.0):
        self.name = name
        self.n = refractive_index
        self.absorption_coeff = absorption_coeff
        
    def absorb_energy(self, initial_energy, distance):
        return initial_energy*np.exp(-self.absorption_coeff*distance)

class Ray:
    def __init__(self, origin, direction, energy = 1.0):
        self.origin=np.array(origin, dtype=float)
        self.direction=self._normalize(direction)
        self.energy = energy
        self.path = [self.origin.copy()]
        self.energies=[energy]
        
    def _normalize(self, vector):
        return np.array(vector, dtype=float)/np.linalg.norm(vector)
    
    def propagate(self, medium, distance):
        end_point = self.origin + self.direction * distance
        self.energy = medium.absorb_energy(self.energy, distance)
        self.origin = end_point
        self.path.append(end_point.copy())
        self.energies.append(self.energy)
        
def plot_ray_path(ray):
    path=np.array(ray.path)
    plt.figure(figsize=(8, 4))
    plt.plot(path[:, 0], path[:, 1], marker='o', color='blue')
    for i, point in enumerate(path):
        plt.text(point[0], point[1], f"{ray.energies[i]:.2f}", fontsize=8, ha='right')
    plt.title("Ray Path with Energy Labels")
    plt.xlabel("X position")
    plt.ylabel("Y position")
    plt.grid(True)
    plt.axis("equal")
    plt.tight_layout()
    plt.show()
    
def plot_energy_loss(ray):
    distances=[0]
    for i in range(1, len(ray.path)):
        d=np.linalg.norm(ray.path[i]-ray.path[i-1])
        distances.append(distances[-1]+d)
    
    plt.figure(figsize=(8, 3))
    plt.plot(distances, ray.energies, marker='o', color='red')
    plt.title("Energy Loss Over Distance")
    plt.xlabel("Distance Traveled")
    plt.ylabel("Remaining Energy")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def refract_ray(incident_direction, normal, n1, n2):

    incident = incident_direction / np.linalg.norm(incident_direction)
    normal = normal / np.linalg.norm(normal)
    cos_theta_i = -np.dot(incident, normal)
    sin2_theta_t = (n1 / n2)**2 * (1 - cos_theta_i**2)

    if sin2_theta_t > 1:
        return None

    cos_theta_t = np.sqrt(1 - sin2_theta_t)
    refracted = (n1 / n2) * incident + ( (n1 / n2) * cos_theta_i - cos_theta_t ) * normal
    return refracted / np.linalg.norm(refracted)