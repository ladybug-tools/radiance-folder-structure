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
    ├───00-model                  [required]
    │   ├───dynamic
    │   │   ├───aperture
    │   │   │   └───interior
    │   │   ├───nonopaque
    │   │   │   ├───indoor
    │   │   │   └───outdoor
    │   │   └───opaque
    │   │       ├───indoor
    │   │       └───outdoor
    │   └───static                [required]
    │       ├───aperture
    │       │   └───interior
    │       ├───nonopaque         [required]
    │       │   ├───indoor
    │       │   └───outdoor
    │       └───opaque            [required]
    │           ├───indoor
    │           └───outdoor
    ├───01-lightsource            [required]
    │   ├───ies
    │   ├───sky
    │   └───sun
    ├───02-bsdf
    ├───03-octree                 [required]
    ├───04-grid                   [required - for grid-based workflows]
    ├───05-view                   [required - for view-based workflows]
    ├───06-options                [required]
    ├───07-output                 [required]
    │   ├───matrix
    │   └───temp
    └───08-postprocess
```

Minimum required folder structure

```
└─project_folder
    ├───00-model                  [required]
    │   └───static                [required]
    │       ├───nonopaque         [required]
    │       └───opaque            [required]
    ├───01-lightsource            [required - for daylight studies]
    │   └───sky / sun
    ├───03-octree                 [required]
    ├───04-grid                   [required - for grid-based workflows]
    ├───05-view                   [required - for view-based workflows]
    ├───06-options                [required]
    └───07-output                 [required]
```
