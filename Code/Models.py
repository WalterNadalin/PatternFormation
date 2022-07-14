import numpy as np

class PredatorPrey():

    def __init__(self, a, b, c, d):

        self.a, self.b, self.c, self.d = a, b, c, d

    def __call__(self, y, t):
        U, V = y

        dU_dT = self.a * U + self.b * U * V
        dV_dT = self.c * V + self.d * U * V

        return np.array([dU_dT, dV_dT]).reshape(-1)


class OtherModel():

    def __init__(self, c, s):

        self.c, self.s = c, s

    def __call__(self, y, t):
        U, V = y

        dU_dT = U * (1 - U) - V * np.sqrt(U)
        dV_dT = self.c * V * np.sqrt(U) - self.s * V ** 2

        return np.array([dU_dT, dV_dT]).reshape(-1)
