# BSDF

`model/bsdf`

This folder includes all the \*.xml BSDF files in the model. The path to BSDF files in
materials in all the folders should be set to `model/bsdf/name.xml`. This will ensure
that Radiance commands which will be executed from project folder will find
the BSDF files even if the folder is not added to `RAYPATH` environment variable.
