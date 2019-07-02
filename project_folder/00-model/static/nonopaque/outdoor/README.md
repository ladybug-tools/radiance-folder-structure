# outdoor nonopaque geometries

`/00-model/static/nonopaque/outdoor`

This in an optional folder for <u>outdoor-only</u> geometries. Naming convention is
the same as `./00-model/static/nonopaque`. These files will only be included in daylight
matrix calculation and will not be part of the view matrix calculation. Separating the
files is helpful to relax Radiance parameters for view matrix calculation by minimizing
the size of the scene.

<u>This folder is only useful for 3-Phase and 5-Phase studies</u>. For other recipes the
files in `outdoor` folder will be part of the scene just like any other geometry file in
`/00-model/static/nonopaque` folder.

In this sample case there is no outdoor nonopaque geometry, hence the empty folder!
