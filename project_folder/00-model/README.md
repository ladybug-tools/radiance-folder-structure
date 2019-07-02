# Model folder

This folder includes all the geometry and material files except for BSDF materials which
are in bsdf folder.

```
00-model
├───dynamic
│   ├───aperture
│   │   └───interior
│   ├───nonopaque
│   │   ├───indoor
│   │   └───outdoor
│   └───opaque
│       ├───indoor
│       └───outdoor
└───static
    ├───aperture
    │   └───interior
    ├───nonopaque
    │   ├───indoor
    │   └───outdoor
    └───opaque
        ├───indoor
        └───outdoor
```

# Sub-folders

The geometries are separated into to categories: _static_ and _dynamic_.

The `static` folder is required for all different types us studies and includes all
geometries that do not change during the course of the simulation.

The `dynamic` folder is optional and can add dynamic geometries to study.

Both folders include 3 sub-folders: `aperture`, `nonopaque` and `opaque`.

- `aperture`: This folder includes all apertures in the model. An aperture is a geometry
  that allows skylight and sunlight to enter into space. Apertures are either dynamic or
  static. They can also be located on an exterior face or an interior one. The interior
  apertures **must** be under `aperture/interior` folder.

  Interior apertures receive skylight and sunlight through other exterior apertures and
  cannot see the sky directly. Interior apertures will not be included in aperture
  "isolation rounds". They also will not be included in _daylight matrix_ calculation.
  The separation is critical for accuracy of the results as well as minimizing simulation
  time.

  See [this post](https://github.com/ladybug-tools/honeybee/wiki/How-does-Honeybee%5B-%5D-set-up-the-input-files-for-multi-phase-daylight-simulation#how-does-honeybee-handles-such-cases)
  to read more on how Honeybee calculates the contribution from each aperture separately.

- `nonopaque`: This folder includes all non-opaque geometry which are _not_ apertures.
  Non-opaque geometries have transparent/ translucent and any other modifiers that light
  can penetrate through and they are placed either inside or outside of enclosure. If a
  nonopaque geometry is part of the enclosure it must be defined as an `aperture`. 

  There are two subfolders to separate the nonopaque geometry between `indoor` and
  `outdoor`. <u>The separation of indoor and outdoor geometries is only important in
  calculating **view and daylight matrix**.</u> Indoor geometries will ONLY be included
  in view matrix calculation and outdoor geometries will ONLY be included in daylight
  matrix calculation.

  The geometries inside the root folder will be included in both matrix calculations.
  Keep in mind that for dynamic geometries each matrix will be calculated for every state
  of the geometry and separating the geometries can remove the unnecessary matrix
  calculations.

- `opaque`: This folder includes all opaque geometries. The folder structure is similar
  to nonopaque folder and geometries can be separated between indoor and outdoor folders.
  Similar to indoor non-opaque geometries <u>the separation of indoor geometries is only
  important in calculating **view and daylight matrix**.</u>
  
  **Note that exterior walls, floor and roof should be kept in the root folder to be part
  of both matrix calculations.**


# Folder structure in relation to Radiance studies

This folder structure is designed to accommodate most of possible daylight workflows but
it does not mean that all the files are necessary to run a simulation. For instance, as
discussed above, the separation of indoor and outdoor geometry is only meaningful for 3
or 5-phase simulations where view matrix and daylight matrix calculation happens.

Below is a quick overview of most commonly used Radiance workflows:

## Raytracing
 
 In this case which is the most typical use case of Radiance and in absence of `dynamic`
 geometries all the geometries inside the `static` folder will be compiled into a single
 `octree`.
 
 Since there are no view or daylight matrix calculation there is no difference between
 indoor and outdoor geometries. Also because there is no separate direct sunlight
 simulation separating opaque and non-opaque geometries is not necessary.

```shell
oconv \
  ./static/aperture/*.mat ./static/aperture/*.rad \
  ./static/aperture/interior/*.mat ./static/aperture/interior/*.rad  \
  ./static/nonopaque/*.mat ./static/nonopaque/*.rad \
  ./static/nonopaque/indoor/*.mat ./static/nonopaque/indoor/*.rad \
  ./static/nonopaque/outdoor/*.mat ./static/nonopaque/outdoor/*.rad \
  ./static/opaque/*.mat ./static/opaque/*.rad \
  ./static/opaque/indoor/*.mat ./static/opaque/indoor/*.rad \
  ./static/opaque/outdoor/*.mat  ./static/opaque/outdoor/*.rad \
  > static_scene.oct`
```

This will change if there are one or more `dynamic apertures` in model. In that case the
`static apertures` should be separated from the rest of the the geometries so they can be
blacked-out when the contribution from each aperture is calculated. <u>Note that interior
apertures are still part of the static scene.</u>

```shell
oconv \
  ./static/aperture/interior/*.mat ./static/aperture/interior/*.rad  \
  ./static/nonopaque/*.mat ./static/nonopaque/*.rad \
  ./static/nonopaque/indoor/*.mat ./static/nonopaque/indoor/*.rad \
  ./static/nonopaque/outdoor/*.mat ./static/nonopaque/outdoor/*.rad \
  ./static/opaque/*.mat ./static/opaque/*.rad \
  ./static/opaque/indoor/*.mat ./static/opaque/indoor/*.rad \
  ./static/opaque/outdoor/*.mat  ./static/opaque/outdoor/*.rad \
  > static_scene.oct`
```

And then for each aperture calculation the octree will be the mix of target aperture
while the rest of apertures are turned black to block the light. For instance the octree
for calculating the contribution from static apertures will look like this:

```shell
oconv -i static_scene.oct \
  ./static/aperture/*.mat ./static/aperture/*.rad \
  ./dynamic/aperture/*.blk ./dynamic/aperture/*.rad
  ...
```

In case there are other dynamic geometries they should be added to octree one at a time.
The number of total runs will be:

(sum(state_count for each dynamic apertures) + 1) * sum(state_count for each dynamic geometry)


## Direct sunlight

The main difference between direct sunlight studies and normal ray-tracing is that the
scene needs to be all black except for apertures and non-opaque geometries.

```shell
oconv \
  ./static/aperture/*.mat ./static/aperture/*.rad \
  ./static/aperture/interior/*.mat ./static/aperture/interior/*.rad  \
  ./static/nonopaque/*.mat ./static/nonopaque/*.rad \
  ./static/nonopaque/indoor/*.mat ./static/nonopaque/indoor/*.rad \
  ./static/nonopaque/outdoor/*.mat ./static/nonopaque/outdoor/*.rad \
  ./static/opaque/*.blk ./static/opaque/*.rad \
  ./static/opaque/indoor/*.blk ./static/opaque/indoor/*.rad \
  ./static/opaque/outdoor/*.blk  ./static/opaque/outdoor/*.rad \
  > static_scene.oct`
```

The same stands for modeling `dynamic` geometries and the workflow is similar to
`raytracing` except for blacking out opaque geometries.

The number of total runs will be:

(sum(state_count for each dynamic apertures) + 1) * sum(state_count for each dynamic geometry)


## View matrix

View matrix calculation is similar to `raytracing` with the difference that the
geometries in outdoor folders will NOT be part of the octree.

```shell
oconv \
  ./static/aperture/*.mat ./static/aperture/*.rad \
  ./static/aperture/interior/*.mat ./static/aperture/interior/*.rad  \
  ./static/nonopaque/*.mat ./static/nonopaque/*.rad \
  ./static/nonopaque/indoor/*.mat ./static/nonopaque/indoor/*.rad \
  ./static/opaque/*.mat ./static/opaque/*.rad \
  ./static/opaque/indoor/*.mat ./static/opaque/indoor/*.rad \
  > static_scene.oct`
```

## Daylight matrix

View matrix calculation is similar to `raytracing` with the difference that the
geometries in indoor folders will NOT be part of the octree.

```shell
oconv \
  ./static/aperture/*.mat ./static/aperture/*.rad \
  ./static/aperture/interior/*.mat ./static/aperture/interior/*.rad  \
  ./static/nonopaque/*.mat ./static/nonopaque/*.rad \
  ./static/nonopaque/outdoor/*.mat ./static/nonopaque/outdoor/*.rad \
  ./static/opaque/*.mat ./static/opaque/*.rad \
  ./static/opaque/outdoor/*.mat ./static/opaque/outdoor/*.rad \
  > static_scene.oct`
```


## 2-Phase

3 phase is the combination of `ray-tracing` and `direct sunlight` calculation
followed by matrix multiplication. 

## 3-Phase

3 phase is the combination of `view matrix` and `daylight matrix` calculation
followed by matrix multiplication. 

## 5-Phase

5 phase is the combination of `view matrix`, `daylight matrix` and `direct sunlight`
calculation followed by matrix multiplication.


# What about modeling inter-connected spaces, double wall or modeling a light-pipe?

For `raytracing`, `direct sunlight` and `2-phase` simulation you can use this folder
structure as is. Make sure to model the nonopaque geometry which connects the spaces as
an interior aperture and that should be enough.

The easiest way for 3-phase and 5-phase studies is to separate each space in a different
folder. Calculate matrices for each and then multiply them together. It should also be
possible to group space geometries in each folder which can be explored in the future.
