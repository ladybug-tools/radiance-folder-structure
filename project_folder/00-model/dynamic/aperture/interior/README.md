# dynamic aperture

`/00-model/dynamic/aperture/interior`

Interior dynamic apertures are similar to exterior dynamic aperture with the difference
that they receive daylight and sunlight from another aperture and cannot see the sky
directly.

Defining an interior aperture is no different than defining an exterior aperture as
discussed in `/00-model/dynamic/aperture`.

In multi-phase studies the daylight matrix coefficient calculation of an interior
aperture is calculated against visible exterior apertures.

The details for the best practices to provide the information for the channel of light
for each interior aperture will be added soon.

Here is an example:

```json
{
  "room_side_window" : {
    "0": ["skylight", "sky"],
    "1": ["side-window", "atrium-skylight", "sky"]
  }
}
```
