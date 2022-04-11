from enum import Enum

class ReloadStats(Enum):
    HandCannon = [0.00477848, -1.30872, 138.482]
    PulseRifle = [0.00477848, -1.30872, 138.482]
    AutoRifle = [0.00477848, -1.30872, 138.482]
    ScoutRifle = [0.00381167, -0.999196, 103.15]
    SMG = [0.00225423, -0.6829, 85.4344]
    Sidearm = [0.000882635, -0.432829, 68.6402]
    FusionRifle = [0.00227882, -0.705757, 91.6868]
    Shotgun = [0.00237208, -0.519846, 42.4795]
    SpecialGL = [0.00268222, -0.775084, 104.714]
    HeavyGL = [0.00279716, -0.885767, 132.442]
    Rocket = [0.00385034, -0.917237, 131.542]



class Weapon:

    def __init__(self, weapon_name, weapon_type, damage, reload, magazine, rpm, reserves):
        self.name = weapon_name
        self.type = weapon_type
        self.damage = damage
        self.reload = reload
        self.rpm = rpm
        self.firerate = self.rpm / 60
        self.magazine = magazine
        self.reserves = reserves
        self.c = self.get_reload_constants()
        self.reload_time = self.calc_reload_speed()
        self.shot_time = 1 / (self.rpm / 60)

    def calc_reload_speed(self):
        self.reload_time = ((self.c[0] * self.reload ** 2 + self.c[1] * self.reload + self.c[2]) / 30)
        return self.reload_time

    def get_reload_constants(self):
        match self.type:
            case 'SniperRifle': return [0.00249814, -0.821771, 123.12]
            case 'LinearFusion': return [0.00217949, -0.709871, 131.542]
            case 'Machinegun': return [0.00335315, -1.08646, 194.189]
            case _: return [0, 0, 0]
