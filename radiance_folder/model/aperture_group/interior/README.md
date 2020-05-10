# Interior aperture group

`model/aperture_group/interior`

Interior aperture groups are similar to exterior dynamic apertures with the difference
that they receive daylight and sunlight after it passes through another aperture.

Defining an interior aperture is no different than defining an exterior aperture as
discussed in [`model/aperture_group`](../README.md).

In 3-phase or 5-phase studies, the daylight matrix coefficient calculation of an interior
aperture is calculated against visible exterior apertures.
