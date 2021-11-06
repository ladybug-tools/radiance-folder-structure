# Sensor grid

`/model/grid`

Copy all the sensor grids in your model to this folder as separate files. Sensor grids
should use the .pts file extension. Each line includes a single sensor. The first 3
values describe the position of the sensor and the second 3 values describe sensor's
direction.

```
position_x1  position_y1  position_z1  direction_x1  direction_y1  direction_z1
position_x2  position_y2  position_z2  direction_x2  direction_y2  direction_z2
```

If the sensors are used for matrix-based study you can provide a `.json` file for each
grid which includes the information for number of sensors in the file and aperture groups
that the light will go through before it arrives to this sensor grid.

```json
{
    "count": 46,
    "light_path": [
        ["static_apertures"],
        ["south_window"] 
    ]
}
```
Each aperture group should be a list. If the aperture group is an exterior aperture group
then there will be only one member in the list. In case of interior aperture groups the
list can have multiple aperture groups. 

```json
{
    "count": 24,
    "light_path": [
        ["static_apertures"],
        ["interior_window", "atrium_skylight"] 
    ]
}
```

If this file is not provided the grid will be executed against all the aperture groups in
the model.

In this model we have two sensor grids. One for the hallway and another one for the
cubical.
