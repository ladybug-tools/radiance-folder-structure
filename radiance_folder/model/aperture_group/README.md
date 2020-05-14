# Aperture group

`/model/aperture_group`

Aperture groups are apertures with one or more states. Each state is represented by
a separate Radiance file. Each file should contain all the information needed to
define the aperture at that state. Here is the list of files that should be provided to
describe a single state.

| Name | Description | Use case | Note |
| --- | --- | --- | --- |
| default | Radiance representation with default materials. | sky contribution calculation in ray-tracing and 2-phase |
| direct | Radiance representation for direct sunlight/ sky contribution calculation. | 2-Phase and 5-Phase | For 2-phase calculation this will be the same as default field. In 5-phase, this field will be used for the 5th phase. In most cases you should be using the original geometry or the higher resolution BSDF file. |
| black | Blacked-out Radiance representation to remove the aperture from the study. | All cases with multiple window groups | |
| tmtx | Transmission matrix. A BSDF file with Klemns subdivision. | 3-Phase and 5-Phase | This matrix will be used for matrix multiplication. |
| vmtx | Inwards matrix. The Radiance representation of the model for calculating inwards matrix calculations. | 3-Phase and 5-Phase | The polygon that will be used for inwards matrix calculation should look inwards. The common practice is to use the `glow` material. If this field is empty Honeybee will change the material of default field to glow. It will also reverse the order of the vertices. In 3-phase and 5-phase documentation this step is known as view-matrix calculation. `vmtx` is a more inclusive name as in cases such as modeling a pipeline `vmtx` calculation can happen between two polygons and will not called view matrix. |
| dmtx | Outwards matrix. The Radiance representation of the model for calculating outwards matrix calculations. | 3-Phase and 5-Phase | In most cases the `dmtx` representation will be the same as `vmtx` representation.

The only required fields for a 2-phase simulation are `default`, `direct` and `black`.
`tmtx` is required for 3-phase studies and both `default` and `tmtx` are required for
5-phase simulation. You should use a `states.json` file to indicate the files for each
field.

![Aperture groups](https://user-images.githubusercontent.com/2915573/53457693-4cd64580-3a01-11e9-821c-0ac767090059.jpg)

In this sample case we only have a single aperture group: `south_window` with two
states. Below is the content of `states.json` file:

```json
{
  "south_window": [
    {
      "identifier": "0_clear",
      "default": "./south_window..default..000.rad",
      "direct": "./south_window..direct..000.rad",
      "black": "./south_window..black.rad",
      "tmtx": "clear.xml",
      "vmtx": "./south_window..mtx.rad",
      "dmtx": "./south_window..mtx.rad"
    },
    {
      "identifier": "1_diffuse",
      "default": "./south_window..default..001.rad",
      "direct": "./south_window..direct..001.rad",
      "black": "./south_window..black.rad",
      "tmtx": "diffuse50.xml",
      "vmtx": "./south_window..mtx.rad",
      "dmtx": "./south_window..mtx.rad"
    }
  ]
}

```

Only one `states.json` file should be used to describe all aperture groups in the
model and you can add more than one aperture to the JSON file by adding more keys
to it (each key representing a unique identifier for the aperture).

For instance, if we want to add another dynamic aperture for the skylight in the
model above, the following needs to be added to the `states.json` file:

```json
{
  ...
  "skylight": [
    {
      "identifier": "0_diffuse",
      "default": "skylight..default..000.rad",
      "direct": "skylight..direct..000.rad",
      "black": "skylight..black..000.rad",
      "tmtx": "diffuse.xml",
      "vmtx": "skylight..mtx..000.rad",
      "dmtx": "skylight..mtx..000.rad"
    }
  ]
}
```

## Naming convention

It is recommended that the `.rad` files be named with a standard convention as follows:
`{aperture identifier}..{field name}..{state count}.rad`. For instance, 
`skylight..direct..000.rad` is the direct representation of skylight for state 0.

It is recommended that the `"identifier"` key in the JSONs starts with an integer index
for the state (eg. `0`, `1`, etc.) in order to make its position in the order of the
states clearer.
