# static

`./00-model/static`

This folder includes all the static geometries in model. The files should be copied into
one of the three subfolders:

1. `aperture`: Includes all the aperture geometries.
2. `nonopaque`: Includes all geometries with transparent/ translucent and any other
   modifiers that light can penetrate through.
3. `opaque`: Includes all geometries with opaque modifiers.


In direct sunlight calculation the content in `opaque` folder will be blacked out but the
geometry in nonopaque and aperture folders will be used as is. 


In most cases there are only 3 files in this folder:

1. `geometry.rad`: This file includes only radiance surfaces and should not include any
   of the radiance modifiers/materials.
2. `material.mat`: This file includes all the modifiers for surfaces in `geometry.rad`.
3. `material.blk`: This file includes materials for surfaces in `geometry.rad` that will
   be used for direct calculation. In most of the cases the materials in `material.blk`
   are black plastic.

Honeybee uses `material.mat` and `geometry.rad` for direct calculation and uses
`material.rad` and `geometry.rad` for other cases.

In case you want to separate files for different parts of the scene you should follow the
below naming convention:

1. `*.rad`
2. `*.mat`
3. `*.blk`

`*.blk` file is optional. If not provided Honeybee will generate black material
with the same name for every material in `*.rad`.
