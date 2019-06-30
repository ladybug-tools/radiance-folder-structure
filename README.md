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
    ├───00-model                   [required]
    │   ├───aperture
    │   │   ├───dynamic
    │   │   └───static
    │   ├───bsdf
    │   └───etc                   [required]
    │       ├───opaque            [required]
    │       │   ├───outdoor
    │       │   └───indoor
    │       └───non-opaque        [required]
    │           ├───outdoor
    │           └───indoor
    ├───01-lightsource            [required]
    │   ├───ies
    │   ├───sky
    │   └───sun
    ├───02-octree                 [required]
    ├───03-grid                   [required - for grid-based workflows]
    ├───04-view                   [required - for view-based workflows]
    ├───05-options                [required]
    ├───06-output                 [required]
    │   ├───matrix
    │   └───temp
    └───07-postprocess
```

Minimum required folder structure

```
└─project_folder
    ├───00-model                  [required]
    │   └───etc                   [required]
    │       ├───opaque            [required]
    │       └───non-opaque        [required]
    ├───01-lightsource            [required]
    │   └───sky / sun
    ├───02-octree                 [required]
    ├───03-grid                   [required - for grid-based workflows]
    ├───04-view                   [required - for view-based workflows]
    ├───05-options                [required]
    └───06-output                 [required]
```
