# Model folder

Model folder includes all the geometry and material files. The folder is broken down into
3 main subfolders for bsdf materials, dynamic model and static model.

```
model
├───bsdf
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

The geometries are separated into two categories: _static_ and _dynamic_.

The `static` folder is required for all different types of studies and includes all
geometries that do not change during the course of the simulation.

The `dynamic` folder is optional and can add dynamic geometries to study.

Both folders include 3 sub-folders: `aperture`, `nonopaque` and `opaque`.

- `aperture`: This folder includes all apertures in the model. An aperture is a geometry
  that allows skylight and sunlight to enter into the space. Apertures are either dynamic
  or static. They can be located both on an exterior or an interior face. The interior
  apertures **must** be separated and located under `aperture/interior` folder.

  Interior apertures receive skylight and sunlight through other exterior apertures. The
  light ray should pass through another exterior aperture before passing through the
  interior aperture.

  Interior apertures will not be included in aperture "isolated" contribution
  calculation. They will not also be included in _daylight matrix_ calculation. The
  separation is critical for accuracy of the results as well as minimizing simulation
  time.

  See [this post](https://github.com/ladybug-tools/honeybee/wiki/How-does-Honeybee%5B-%5D-set-up-the-input-files-for-multi-phase-daylight-simulation#how-does-honeybee-handles-such-cases)
  to learn more on how Honeybee isolates the contribution from each exterior aperture
  separately in a multi-phase simulation.

- `nonopaque`: This folder includes all non-opaque geometry which are _not_ apertures. A
  common example of nonopaque geometry is translucent partitions. Non-opaque geometries
  have transparent or translucent materials. They are placed either inside or outside of
  the enclosure. If a nonopaque geometry is part of the enclosure it must be defined as
  an `aperture`. 

  There are two subfolders to separate the nonopaque geometry between `indoor` and
  `outdoor`. <u>The separation of indoor and outdoor geometries is only important in
  calculating **view and daylight matrix**.</u> Indoor geometries will ONLY be included
  in view matrix calculation and outdoor geometries will ONLY be included in daylight
  matrix calculation.

  The geometries inside the root folder will be included in both view and daylight
  calculations. Keep in mind that for dynamic geometries each matrix will be calculated
  for every state of the geometry and separating the geometries can remove the
  unnecessary matrix calculations.

- `opaque`: This folder includes all opaque geometries. The folder structure is similar
  to nonopaque folder and geometries can be separated between indoor and outdoor folders.
  Similar to indoor non-opaque geometries <u>the separation of indoor geometries is only
  important for calculating **view and daylight matrix**.</u>
  
  **Note that exterior walls, floors and roofs should be kept in the root folder to be
  part of both view and daylight matrix calculations.**


# Folder structure in relation to Radiance studies

This folder structure is designed to accommodate most of possible daylight workflows but
it does not mean that all the files are necessary for all the simulations. For instance,
as discussed above, the separation of indoor and outdoor geometry is only meaningful for
3 or 5-phase simulations where view matrix and daylight matrix calculation happens.

Below is a quick overview of how the folder can accommodate the most commonly used
Radiance workflows:


## Ray-tracing with rtrace / rcontrib / rpict

This is the most typical use case of Radiance. For static simulations all the geometries
inside the `static` folder will be compiled into a single `octree`.

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
  > static_scene.oct
```

In `dynamic` models the `static apertures` should be separated from the rest of the the
geometries. This is required for blacking-out the static aperture during the isolated
contribution calculation. <u>Note that the `interior` apertures will not be blacked-out
and stay as part of the normal static scene.</u>

```shell
oconv \
  ./static/aperture/interior/*.mat ./static/aperture/interior/*.rad  \
  ./static/nonopaque/*.mat ./static/nonopaque/*.rad \
  ./static/nonopaque/indoor/*.mat ./static/nonopaque/indoor/*.rad \
  ./static/nonopaque/outdoor/*.mat ./static/nonopaque/outdoor/*.rad \
  ./static/opaque/*.mat ./static/opaque/*.rad \
  ./static/opaque/indoor/*.mat ./static/opaque/indoor/*.rad \
  ./static/opaque/outdoor/*.mat  ./static/opaque/outdoor/*.rad \
  > static_scene.oct
```

For simulating the contribution of each isolated aperture the static_scene octree should
be mixed with the isolated aperture while the rest of apertures are turned black to block
the light entrance. For instance the octree for calculating the isolated contribution
from the static apertures will look like this:

```shell
oconv -i static_scene.oct \
  ./static/aperture/*.mat ./static/aperture/*.rad \
  ./dynamic/aperture/*.blk ./dynamic/aperture/*.rad \
  ...
```

The number of total runs will be:

((state count for all dynamic apertures) + 1) * state count for all dynamic geometry

For our case which only has a dynamic window with two states this number will be
`(2 + 1) * 1`.


## Direct sunlight

The main difference between direct sunlight studies and normal ray-tracing is that the
all non-aperture geometry in the scene must be black.

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
  > static_scene.oct
```

The same stands for modeling `dynamic` models. The workflow for calculating the
contribution for dynamic models is similar to `raytracing` except that the non-aperture
must be black.

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
  > static_scene.oct
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


# Modeling inter-connected spaces, double wall or light-pipes

For inter-connected spaces another layer of complexity is added to the calculation if one
needs to use 3 or 5 phase methods which needs extra coefficient calculation between
senders and receivers. However for `raytracing`, `direct sunlight` and `2-phase`
simulations you can use the folder structure as is. The only consideration is to ensure
to model the nonopaque geometry which connects the spaces as an _interior_ aperture.

For 3-phase and 5-phase studies you can separate each space in a separated folder.
Calculate matrices for each case and then multiply them together.

It should also be possible to group space geometries in the same folder which can be
explored in the future.
