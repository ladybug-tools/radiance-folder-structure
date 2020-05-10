# static scene

`model/scene`

This folder includes all the *static* geometries in the model which are not *apertures*.
By default, the files must follow the naming convention as below:

1. `*.rad`: This file only includes the geometries. It should not include any of the
   modifiers. Modifiers should be included in `*.mat` file.
2. `*.mat`: This file includes all the modifiers for geometries included in `*.rad`.
3. `*.blk`: This file includes modifiers for geometries in `*.rad` that will
   be used for direct sunlight calculation. For opaque modifiers the materials in `*.blk`
   is usually a black plastic. For transparent and translucent modifiers the modifier
   usually stays the same. Otherwise the light will be blocked in direct studies.

You can change the naming convention for files by editing the config file in the model
folder.

All the geometries can be included in the same `.rad`, `.mat` and `.blk` files together
but for this example we are separating them into separate files to make it easier to
study the files.

## NOTE

Be careful not to include the apertures in this folder. The apertures will be treated
differently in studies with aperture groups and any aperture in this folder can cause in
double counting.


In this sample case the room geometry as well as ground plane and the neighbor building
are opaque. There is also the bottom part of the partition inside the room which is
opaque. The only transparent geometry which is not part of the apertures is the top part
of the partition inside the room which is included in this folder. Note that the material
in `.blk` and `.mat` files are the same for the glass partition.

Enclosure/shell geometry

![opaque](https://user-images.githubusercontent.com/38131342/53503554-489c3d80-3a7e-11e9-82c5-0d815a2fda14.jpg)

Context

![context](https://user-images.githubusercontent.com/38131342/53503552-4803a700-3a7e-11e9-9083-29614294fa38.jpg)

Indoor geometry

![opaque_indoor](https://user-images.githubusercontent.com/38131342/53503555-489c3d80-3a7e-11e9-9679-1b0284243be8.jpg)

![nonopaque_indoor](https://user-images.githubusercontent.com/2915573/53506467-05dd6400-3a84-11e9-9d15-a1a859135234.jpg)
