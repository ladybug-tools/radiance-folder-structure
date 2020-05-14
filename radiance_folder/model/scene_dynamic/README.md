# Dynamic model

`/model/scene_dynamic`

`scene_dynamic` folder includes all the dynamic geometries in a model except for dynamic
apertures. Dynamic apertures must be included in `aperture_group` folder.

A separate simulation for each state of the dynamic geometry will be executed.

There is no dynamic geometry in this example but one can be added to the scene easily by
adding new Radiance files. Similar to aperture groups you should use a `states.json` file
to indicate the files for each state.

## Ground example

In this sample case, we don't have any dynamic opaque geometries but we could have
modeled the ground with two different materials for winter versus summer like so:

```json
{
  "ground": [
    {
      "identifier": "0_grass_covered",
      "default": "ground..summer..000.rad",
      "direct": "ground..direct..000.rad",
    },
    {
      "identifier": "1_snow_covered",
      "default": "ground..winter..001.rad",
      "direct": "ground..direct..000.rad"
    }
  ]
}

```

Note that the `"direct"` file is only used in direct studies (solar access, 2-phase and
5-phase) and, for isolation studies of individual apertures (any phase study with dynamic
apertures), the `"default"` files have to be used.

Because the example here has completely opaque geometry in all states and this
geometry is not changing between states, the same .rad file can be used for
direct studies of all states. So, for the example here of snow-covered ground,
this `"direct"` file contains a "blacked-out" version of the ground geometry.


## Deciduous tree example

Similar to ground adding deciduous trees with summer and winter conditions could look
like this:

```json
{
  "outdoor_trees": [
    {
      "identifier": "0_summer_condition",
      "default": "trees..summer..000.rad",
      "direct": "trees..direct..000.rad",
    },
    {
      "identifier": "1_winter_condition",
      "default": "trees..winter..001.rad",
      "direct": "trees..direct..001.rad"
    }
  ]
}

```
