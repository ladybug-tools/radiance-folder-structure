# radiance-folder-structure

Folder structure for lighting studies with Radiance.

## GOAL

The ultimate goal of this project is to provide an example for standard Radiance input
data folder/file structure that can be used both by Radiance users and software
developers.

## Folder structure

The Radiance folder has a single required sub-folder for `model`. A `model` carries all
the information about the geometry, modifiers and describes dynamic parts of the model if
any. All the data in a `model` folder are reusable between different types of studies.
That's why it does <u>NOT</u> include files such as `sky` which are specific to a certain
type of study AKA recipe. This information should be included in the `recipe` folder
which will be located next to the `model` folder. The name of the `recipe` folder should
indicate the type of the study that the recipe is performing (e.g. daylight_factor).

Adopting this folder structure ensures that one can execute advanced light simulation
studies for your model.

This folder structure is designed to be extendible. Here is the folder structure for a
simple model with no dynamic geometry or aperture group:

```cmd
└─radiance_folder             :: A sample radiance folder
    ├───model                 :: model folder
    │   ├───aperture          :: static apertures description
    │   ├───bsdf              :: in-model BSDF files and transmittance matrix files
    │   ├───grid              :: sensor grids
    │   ├───ies               :: electric lights description
    │   ├───scene             :: static scene description
    │   └───view              :: indoor and outdoor views
    └───[recipe-place-holder] :: recipe folder (e.g. annual_daylight, two_phase, etc.)
        ├───...
        └───sky
    recipe.yaml / recipe.sh / recipe.bat
```

For matrix-based studies with aperture groups and dynamic geometries two additional
subfolders are included.

```cmd
└─radiance_folder             :: A sample radiance folder
    ├───model                 :: model folder
    │   ├───aperture          :: static apertures description
    │   ├───aperture_group    :: apertures groups (AKA window groups)*
    │   │   └───interior      :: interior aperture groups
    │   ├───bsdf              :: in-model BSDF files and transmittance matrix files
    │   ├───grid              :: sensor grids
    │   ├───ies               :: electric lights description
    │   ├───scene             :: static scene description
    │   ├───scene_dynamic     :: dynamic scene description*
    │   │   └───indoor        :: indoor dynamic scene description*
    │   └───view              :: indoor and outdoor views
    └───[recipe-place-holder] :: recipe folder (e.g. annual_daylight, two_phase, etc.)
        ├───sky
        ├───...
        └───sun
    recipe.yaml / recipe.sh / recipe.bat
```

See README.md inside each folder for more information.
