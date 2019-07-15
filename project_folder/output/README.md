# Output

`/output`

Folder to redirect study outputs. Output folder includes all the files that are generated
by Radiance during the simulations.

The suggested folder structure for output includes these subfolders:

- `octree`: octree files generated from putting assets and model together.
- `postprocess`: post-processed results from raw output files.
- `raw`: raw output files generated during the process of simulation which should be
  kept after the study is finished.
- `temp`: temporary outputs that can be removed once the study is over. Intermediate
  matrices with RGB values is a good example of such outputs.
