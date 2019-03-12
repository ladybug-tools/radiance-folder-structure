"""
A sample code to show case how one can write scripts to run studies using this folder
structure.

Usage:

daylight_factor -f [folder]

TODO:
    - add functionality for several grid points.
    - add radiance parameters file (most likely to a config file)
"""
import argparse
import os
import yaml
import subprocess

SUBFOLDERS = [
    '0-model/etc/opaque', '0-model/etc/opaque/indoor', '0-model/etc/opaque/outdoor',
    '0-model/etc/nonopaque', '0-model/etc/nonopaque/indoor',
    '0-model/etc/nonopaque/outdoor'
]

def find_files(parent_folder, subfolder):
    """Find rad and mat files in a target folder."""
    files = []
    folder = os.path.join(parent_folder, subfolder)
    all_files = os.listdir(folder)
    for fi in all_files:
        if not fi.endswith('.rad'):
            continue
        fn, _ = os.path.splitext(fi)
        # ensure a mat file with the same filename exist
        assert os.path.isfile(os.path.join(folder, '%s.mat' % fn)), \
            'Failed to find materil file for {}/{}'.format(subfolder, fi)
        
        files.extend(
            [
                os.path.normpath(os.path.join(subfolder, fn + '.mat')),
                os.path.normpath(os.path.join(subfolder, fn + '.rad'))
            ]
        )
    return files

def main(args):
    """ Run daylight factor."""
    root_folder = args['folder'].strip()

    scene_files = [f for folder in SUBFOLDERS for f in find_files(root_folder, folder)]
    static_aperture_files = find_files(root_folder, r'0-model/aperture/static')
    
    state_file = os.path.join(root_folder, '0-model/aperture/dynamic', 'state.yaml')
    with open(state_file) as inf:
        states = yaml.load(inf)

    # for now just run it for the first state and there is only one window group!
    for window_group in states:
        direct_file = os.path.normpath(os.path.join(
            '0-model/aperture/dynamic', states[window_group]['state_0']['direct']
            ))
        oconv_files = ' '.join(scene_files + static_aperture_files) + ' ' + direct_file
    
    # find point file
    pt_files = [
        f for f in os.listdir(os.path.join(root_folder, '3-sensorgrid'))
        if f.endswith('.pts')]
    
    pt_file = os.path.normpath(os.path.join('3-sensorgrid', pt_files[0]))
    
    # run daylight factor command
    rp = '-aa 0.1 -h -dj 0.0 -lr 4 -ad 1024 -lw 0.001 -ar 16 -dc 0.25 -ss 0.0 -dp 64 ' \
        '-dr 0 -dt 0.5 -ds 0.5 -as 128 -ab 3 -st 0.85'
    os.chdir(root_folder)
    sky_file = os.path.join('1-lightsource', 'sky', '100000lux.sky')
    ground_file = os.path.join('1-lightsource', 'sky', 'ground.rad')

    sky_cmd = 'gensky 9 21 12 -B 558.659217877 -c > %s' % sky_file
    oct_cmd = 'oconv -f %s %s %s > 2-octree/default.oct' % (sky_file, ground_file, oconv_files)
    df_cmd = "rtrace -I %s 2-octree/default.oct < %s | rcalc -e " \
        "'$1=(0.265*$1+0.67*$2+0.065*$3)*179/1000' > 5-output/daylight-factor.dat" % (rp, pt_file)
    
    os.system(sky_cmd)
    os.system(oct_cmd)
    os.system(df_cmd)
    # print('\n'.join([sky_cmd, oct_cmd, df_cmd]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", required=True,
                        help="path to root folder.")
    args = vars(parser.parse_args())
    main(args)
