# Model folder

Model folder includes all the geometry and modifier files that describe the Radiance
model.

```cmd
└─model                :: model folder
  ├───aperture         :: static apertures description
  ├───aperture_group   :: apertures groups (AKA window groups)*
  │   └───interior     :: interior aperture groups
  ├───bsdf             :: in-model BSDF files and transmittance matrix files
  ├───grid             :: sensor grids
  ├───ies              :: electric lights description
  ├───scene            :: static scene description
  ├───scene_dynamic    :: dynamic scene description*
  │   └───indoor       :: indoor dynamic scene description*
  └───view             :: indoor and outdoor views
```

There is a `README.md` file in each sub-folder with more information about that
sub-folder.

# Folder structure in relation to Radiance studies

This folder structure is designed to accommodate most of possible daylight workflows but
it does not mean that all the files are necessary for all the simulations. For instance
the separation of interior aperture_group is only meaningful for 3 or 5-phase simulations
where view matrix and daylight matrix calculation happens. It is also necessary for
2-phase simulation with one or more aperture groups in the model.

Below is a quick overview of how the folder can accommodate the most commonly used
Radiance workflows:


## Ray-tracing with rtrace / rcontrib / rpict

This is the most typical use case of Radiance. For static simulations all the geometries
inside the `scene` folder will be compiled into a single `octree`.

Since there are no view or daylight matrix calculation there is no difference between
indoor and outdoor geometries. Also because there is no separate direct sunlight
simulation the `.blk` files will not be used.

```shell
oconv ./model/scene/*.mat ./model/scene/*.rad \
  ./model/aperture/*.mat ./model/aperture/*.rad > static_scene.oct
```

In `dynamic` models the `static apertures` should be separated from the rest of the the
geometries. This is required for blacking-out the static aperture during the isolated
contribution calculation.

```shell
oconv ./model/scene/*.mat ./model/scene/*.rad > static_scene_no_aperture.oct
```

For simulating the contribution of each isolated aperture the static scene octree should
be mixed with the isolated aperture while the rest of apertures are turned black to block
the light entrance. For instance the octree for calculating the isolated contribution
from the static apertures will look like this:

```shell
oconv -i static_scene_no_aperture.oct \
  ./model/aperture/*.mat ./model/aperture/*.rad \
  ./model/aperture_group/*.blk ./model/aperture_group/*.rad \
  ... \
  > static_scene.oct
```

The number of total runs will be:

((state count for all aperture groups) + 1) * state count for all dynamic geometry

For our case which only has one single aperture group with two states this number will be
`(2 + 1) * 1`.


## Direct sunlight

The main difference between direct sunlight studies and ray-tracing with diffuse and
reflected light is that all non-aperture geometry in the scene must be black.

```shell
oconv ./model/scene/*.blk ./model/scene/*.rad \
  ./model/aperture/*.mat ./model/aperture/*.rad > static_scene.oct
```

The same stands for modeling `dynamic` models. The workflow for calculating the
contribution for dynamic models is similar to `raytracing` except that the non-aperture
must be black.

## View matrix

View matrix calculation is similar to `raytracing`.


## Daylight matrix

Daylight matrix calculation is similar to `raytracing`.



## 2-Phase

2 phase is the combination of `ray-tracing` and `direct sunlight` calculation
followed by matrix multiplication. 

## 3-Phase

3 phase is the combination of `view matrix` and `daylight matrix` calculation
followed by matrix multiplication. 

## 5-Phase

5 phase is the combination of `view matrix`, `daylight matrix` and `direct sunlight`
calculation followed by matrix multiplication.


# Modeling interior aperture groups for inter-connected spaces, double walls or light-pipes

For these cases an extra coefficient calculation between the sender and the receiver is
needed to calculate the daylight transmission using 3 or 5 phase methods. For such cases:

1. One should model the nonopaque geometry which connects the spaces as an _interior_
   aperture.

2. It is highly recommended that each sensor grid provides the list of apertures that are
   visible to that grid. See [grid folder](./grid/README.md) for more information.
