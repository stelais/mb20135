"""
This script prepares the data for the RTModel run. It creates a folder structure and
saves the data in the correct format. The data is taken from the paper
"MOA-2020-BLG-135Lb:
A New Neptune-class Planet for the Extended MOA-II Exoplanet Microlens Statistical Analysis"
First, download the data from the paper in:
https://content.cld.iop.org/journals/1538-3881/164/3/118/revision1/ajac82b8f1.tar.gz
Then, extract the data and place it in a folder named "paper_data".
"""

from astropy.table import Table
import os

# ======================================
# Reading data from the paper ()
# ======================================
cfhti_data = Table.read("paper_data/phot_mb20135_cfhti.mrt", format="ascii.cds")
moa2r_data = Table.read("paper_data/phot_mb20135_moa2r.mrt", format="ascii.cds")
moa2V_data = Table.read("paper_data/phot_mb20135_moa2V.mrt", format="ascii.cds")

# Convert the table to pandas DataFrames
cfhti_df = cfhti_data.to_pandas()
moa2r_df = moa2r_data.to_pandas()
moa2V_df = moa2V_data.to_pandas()

# ======================================
# Create the RTModel folder structure
# ======================================
event_folder = 'mb20135_RTModel_run'
os.mkdir(event_folder)
print(f'Folder {event_folder} created!')
data_folder = f'{event_folder}/Data'
os.mkdir(data_folder)
print(f'Folder {data_folder} created!')

# ======================================
# Create the files
# ======================================
# Mapping name of columns to new names
VARIABLE_NAMES_MAPPING = {
    "rmag": "Mag",
    "e_rmag": "Mag_err",
    "Vmag": "Mag",
    "e_Vmag": "Mag_err",
    "imag": "Mag",
    "e_imag": "Mag_err"
}

# Saving the data in the correct format
instrument_names = ['cfhti', 'moa2r', 'moa2V']
data_to_be_created_folder_ = f'mb20135_RTModel_run/Data'
for instrument_df, instrument_name in zip([cfhti_df, moa2r_df, moa2V_df], instrument_names):
    with open(f'{data_to_be_created_folder_}/{instrument_name}.dat', 'w') as f:
        f.write('# Mag err HJD-2450000\n')
    # # Apply variable mapping to the model parameters
    instrument_df = instrument_df.rename(columns=VARIABLE_NAMES_MAPPING)
    instrument_df[['Mag', 'Mag_err', 'HJD']].to_csv(f'{data_to_be_created_folder_}/{instrument_name}.dat', sep=' ',
                                          index=False, header=False, mode='a')
    print(f'File {instrument_name}.dat created in {data_to_be_created_folder_}.')

# Create a file for limb darkening
with open(data_to_be_created_folder_+'/LimbDarkening.txt','w') as f:
    for mu in [0.5090, 0.6730, 0.5633]:  # cfhti 0.5090, moa2V 0.6730, moa2r 0.5633
        f.write(f'{mu}\n')
print(f'File LimbDarkening.txt created in {data_to_be_created_folder_}.')

# Create coordinates file
# 17 55  0.447  -29 48 37.36
with open(data_to_be_created_folder_+'/event.coordinates','w') as f:
    f.write('17:55:0.447 -29:48:37.36')
print(f'File event.coordinates created in {data_to_be_created_folder_}.')

print('Done!')
