from padelpy import padeldescriptor

# assay = 1511
# inp_dirname = x
# inp_filename = y
dataset = 'harvard_hergcentral'
dirname = f'{dataset}_OUTPUT'
# inp_dirname = 'EU-OS_PB_bioactives'
# inp_fname = 'EU-OS_PBC_bioactives.sdf'

out = padeldescriptor(mol_dir=f'../DATASETS/{dataset}.sdf', d_file=f'./{dirname}/{dataset}_descriptors.csv', d_2d=True, d_3d=True, fingerprints=True, log=True, threads=4)