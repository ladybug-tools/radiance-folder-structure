# radiance-folder-structure

Folder structure for daylight studies with Radiance.

## GOAL

The ultimate goal of this project is to provide an input data folder / file structure
that can be used both by Radiance users and software developers. Using an standard folder
structure will makes it easy to use different tools / scripts regardless of the source of
the files.

See README.md inside each folder for more information.

```
└─project_folder
    ├───asset
    │   ├───grid
    │   ├───ies
    │   ├───sky
    │   ├───sun
    │   └───view
    ├───model
    │   ├───bsdf
    │   ├───dynamic
    │   │   ├───aperture
    │   │   │   └───interior
    │   │   ├───nonopaque
    │   │   │   ├───indoor
    │   │   │   └───outdoor
    │   │   └───opaque
    │   │       ├───indoor
    │   │       └───outdoor
    │   └───static
    │       ├───aperture
    │       │   └───interior
    │       ├───nonopaque
    │       │   ├───indoor
    │       │   └───outdoor
    │       └───opaque
    │           ├───indoor
    │           └───outdoor
    ├───output
    │   ├───matrix
    │   ├───octree
    │   ├───postprocess
    │   └───temp
    └───system
```
