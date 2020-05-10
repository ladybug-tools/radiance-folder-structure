# aperture

`model/aperture`

An aperture is a transparent or translucent fixture which lets the light enter the space.

The apertures in this folder are *static* and part of the *exterior* envelopeof the
building. All the static apertures in this folder will be grouped together into a single
"isolated" aperture for studies with aperture_groups. By default, this aperture group
is named "static_apertures".

It is important to note that if you include any of the interior static apertures in this
folder their material should stay transparent in `*.blk` file which will be used for the
"isolation" studies.

In this sample case `south_window_top` and `skylight` are both static and will be grouped
together. Including all the geometries in the same file or in separate files is optional
as long as you follow the naming convention.

![Static aperture](https://user-images.githubusercontent.com/2915573/53457736-66778d00-3a01-11e9-9595-4bea03a66522.jpg)

## Naming convention

The files in this folder should be named as:

1. `<filename>.rad`: Includes Radiance geometries/surfaces.
2. `<filename>.mat`: Includes Radiance materials/modifiers.
3. `<filename>.blk`: Includes the black version of materials in `<filename>.mat` file.
   This file is needed to black out the static aperture from the scene when calculating
   the "isolated" contribution from other apertures in the scene.
