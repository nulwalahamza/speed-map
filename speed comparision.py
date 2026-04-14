import fastf1
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Step 1: Enable cache (creates a folder called 'cache' in your directory)
fastf1.Cache.enable_cache('cache/')

# Step 2: Load a session (year, GP name, session type)
session = fastf1.get_session(2026, 'China', 'Q')
session.load()

# Step 3: Get Verstappen's fastest lap telemetry
lap = session.laps.pick_driver('HAM').pick_fastest()
tel = lap.get_telemetry().add_distance()

x = tel['X'].values
y = tel['Y'].values
speed = tel['Speed'].values

# Step 4: Build segments and color map
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

norm = mpl.colors.Normalize(vmin=speed.min(), vmax=speed.max())
cmap = mpl.cm.RdYlGn

# Step 5: Plot
fig, ax = plt.subplots(figsize=(10, 8))
lc = mpl.collections.LineCollection(segments, cmap=cmap, norm=norm, linewidth=2)
lc.set_array(speed)
ax.add_collection(lc)
ax.autoscale()
ax.set_aspect('equal')
ax.set_title('Track Map - HAM Fastest Lap Colored by Speed')
plt.colorbar(lc, ax=ax, label='Speed (km/h)')
plt.tight_layout()
plt.show()