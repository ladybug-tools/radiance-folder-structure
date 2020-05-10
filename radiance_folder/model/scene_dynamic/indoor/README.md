# Indoor dynamic geometry

`model/scene_dynamic/indoor`

This folder includes all the dynamic geometries located inside the closed space.

A separate simulation for each state of the dynamic geometry will be executed. For 3 and
5 phase simulations indoor dynamic geometries will only be included in view matrix
calculation while the rest of the dynamic opaque geometries like a snow-covered ground
will only be included in daylight matrix calculation.

See [`model/scene_dynamic` README.md](../README.md) for more information about creating
dynamic geometries.
