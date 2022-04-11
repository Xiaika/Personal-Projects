import matplotlib.pyplot as plt
from Weapon import Weapon

MAGAZINES = 4

def get_damage_data_frames(w) -> zip:
    framerate = 60
    damage_data = list()
    frame_data = list()
    total_damage = 0
    total_frames = 0
    if weapon.type in ['LinearFusion', 'FusionRifle']:
        total_frames += round(w.shot_time * framerate)
    for mags in range(MAGAZINES):
        for shot in range(weapon.magazine):
            total_damage += weapon.damage
            damage_data.append(total_damage)
            frame_data.append(total_frames)
            total_frames += round(w.shot_time * framerate)
        total_frames += round(weapon.reload_time * framerate)
    return zip(damage_data, frame_data)


def get_dps_data(damage_data: zip):
    dps_data = list()
    for x, y in damage_data:
        if y == 0:
            dps_data.append(weapon.damage)
        else:
            sec = y / FRAMERATE
            dps_data.append(round(x / sec))
    return dps_data


def get_inputs() -> Weapon:
    weapon_name = input("Enter Weapon Name: ")
    weapon_type = input("Enter Weapon Class: ")
    damage = int(input("Enter Base Damage Value: "))
    reload = int(input("Enter Reload Stat: "))
    magazine = int(input("Enter Magazine Size: "))
    reserves = int(input("Enter Reserve Size: "))
    rpm = int(input("Enter RPM Value: "))
    return Weapon(weapon_name, weapon_type, damage, reload, magazine, reserves, rpm)

#weapon = Weapon('Thoughtless', 'SniperRifle', 29000, reload=55, magazine=5, rpm=90, reserves=18)
#weapon = Weapon('Sleeper', 'LinearFusion', 84964, reload=100, magazine=4, rpm=80.65, reserves=14)
weapon = get_inputs()
# Get continuous DPS using time module

data = get_damage_data_frames(weapon)
damage_frames = list()
damage = list()
for d, t in data:
    damage_frames.append(t)
    damage.append(d)

frames = list()
total_damage = list()
seconds = 60
FRAMERATE = 60
for frame in range(16000):
    frames.append(frame)
    total_damage.append(0)

for frame in range(len(frames)):
    for dmg_index in range(len(damage_frames)):
        if frame == damage_frames[dmg_index]:
            total_damage[frame] = damage[dmg_index]

# test = [0, 0, 0, 8, 0, 0, 16, 0, 0, 24,  0,  0,  0]
# f = [3, 6, 9]

# replace zeroes with damage values
frame_counter = 0
for i, frame in enumerate(damage_frames):
    curr_frame = frame
    if i + 1 < len(damage_frames):
        next_frame = damage_frames[i + 1]
    else:  # End of list
        next_frame = len(total_damage)
        last_damage_frame = curr_frame
    for j in range(next_frame - curr_frame):
        if total_damage[j + curr_frame] == 0:
            total_damage[j + curr_frame] = total_damage[curr_frame]

dps = get_dps_data(zip(total_damage, frames))
dps[0] = 0

# make up some data
x = [f / 60 for f in frames]
y = dps
#
# plot
plt.plot(x, y)
plt.xlabel('Time')
plt.title(f'{weapon.name} DPS over time')
plt.ylim(0, 1.1 * max(dps[30:]))
plt.xlim(0, last_damage_frame / 60 + 10)

plt.show()



# print(f'DPS over time: {dps}')
# print(f'Average DPS: {sum(dps)/len(dps)}')
