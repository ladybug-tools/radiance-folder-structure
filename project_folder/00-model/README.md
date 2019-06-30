# Model folder

This folder includes all the geometry and material files for the study.

# Sub-folders

## ./aperture

`aperture` folder includes all the apertures in your model. An aperture is a geometry
that allows the light from sky and sunlight to enter into your space. Apertures are
either dynamic or static.

<sub>* See [this post](https://github.com/ladybug-tools/honeybee/wiki/How-does-Honeybee%5B-%5D-set-up-the-input-files-for-multi-phase-daylight-simulation#how-does-honeybee-handles-such-cases) to read more on how Honeybee calculates the contribution from each window group separately.</sub>

## ./bsdf

`bsdf` folder includes all the *.xml BSDF files in the model.

## ./etc

This folder includes all the geometry in model except for the apertures. The files should
be copied into one of the two subfolders:

- opaque: Includes all geometries with opaque materials.

- nonopaque: Includes all geometries with transparent/ translucent and any other
  modifiers that light can penetrate through


# Minimum model folder

This folder structure is designed to accommodate all possible daylight recipes but it
doesn't mean that all the files are necessary to run a simulation.

# Default Radiance model

To create an octree you should include:

- `00-model/etc/opaque/*.mat 00-model/etc/opaque/*.rad`

- `00-model/etc/opaque/indoor/*.mat 00-model/etc/opaque/indoor/*.rad`

- `00-model/etc/opaque/outdoor/*.mat 00-model/etc/opaque/outdoor/*.rad`

- `00-model/etc/nonopaque/*.mat 00-model/etc/nonopaque/*.rad`

- `00-model/etc/nonopaque/indoor/*.mat 00-model/etc/nonopaque/indoor/*.rad`

- `00-model/etc/nonopaque/outdoor/*.mat 00-model/etc/nonopaque/outdoor/*.rad`

This octree does not include the apertures. Based on the type of simulation you should
add the files under `00-model/aperture` folder to octree.

For adding static aperture you should include:

- `/00-model/aperture/static/*.mat /00-model/aperture/static/*.rad`

For dynamic aperture you need to include the `default` file for each state as indicated
in `/00-model/aperture/dynamic/state.yml`.

# Direct Radiance model

To create an octree for _direct_ studies you should include:

- `00-model/etc/opaque/*.blk 00-model/etc/opaque/*.rad`

- `00-model/etc/opaque/indoor/*.blk 00-model/etc/opaque/indoor/*.rad`

- `00-model/etc/opaque/outdoor/*.blk 00-model/etc/opaque/outdoor/*.rad`

- `00-model/etc/nonopaque/*.mat 00-model/etc/nonopaque/*.rad`

- `00-model/etc/nonopaque/indoor/*.mat 00-model/etc/nonopaque/indoor/*.rad`

- `00-model/etc/nonopaque/outdoor/*.mat 00-model/etc/nonopaque/outdoor/*.rad`

The only change from normal octree is in material files (mat -> blk) for opaque
geometries. This octree does not include the apertures. Based on the type of simulation
you should add the files under `00-model/aperture` folder to the octree.

For adding static aperture you should include:

- `/00-model/aperture/static/*.blk /00-model/aperture/static/*.rad`

For dynamic aperture you need to include the `direct` file for each state as indicated
in `/00-model/aperture/dynamic/state.yml`.
