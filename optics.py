import numpy as np

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
        