# Modeling MOA-2020-BLG-135Lb with RTModel and pyLIMA
This repository is part of the online material of `CHAPTER 7: Microlensing` of the Book `Exoplanet Detection Methods: Uncovering the Evolution of Planetary Systems.`

## 1. Installing the Package

1. Create a new environment:
   ```bash
   conda create -n mb20135_env python=3.12
   ```
2. Activate the environment:
   ```bash
   conda activate mb20135_env
   ```
3. Clone this GitHub repository:
   ```bash
   git clone https://github.com/stelais/mb20135.git
   ```
4. Install the required packages: `RTModel`, `astropy`, `pandas`, and `pyLIMA`:
   ```bash
   pip install RTModel==2.4 
   pip install astropy==7.0.1
   pip install pandas==2.2.3
   pip install pyLIMA==1.9.8
   ```

---

## 2. Downloading the Observational Data for Event MOA-2020-BLG-135

1. Download the observational data from the following link:  
   [ajac82b8f1.tar.gz](https://content.cld.iop.org/journals/1538-3881/164/3/118/revision1/ajac82b8f1.tar.gz)  
   This data accompanies the paper:  
   *“MOA-2020-BLG-135Lb: A New Neptune-class Planet for the Extended MOA-II Exoplanet Microlens Statistical Analysis”*  
   (Ishitani Silva et al. 2022).
2. Extract the downloaded folder and place the contents in a folder named `paper_data`.

---

## 3. Running RTModel on the Data

1. Run the preparation script:
   ```bash
   python preparing_rtmodel.py
   ```
2. Open the notebook `running_rtmodel.ipynb`.
3. Run the first three cells.  
   The third cell:
   ```python
   run_rtmodel('mb20135_RTModel_run', number_of_processors_=8)
   ```
   launches the RTModel fits. Select the number of processors you want to use. You can also delete this variable, and RTModel will use all CPU processors available.

By default, RTModel searches for solutions across the following 7 models:

| **Label** | **Model**                                                               | **Number of Parameters** |
|:---------:|:------------------------------------------------------------------------|:-------------------------:|
| PS        | Single-lens single-source                                               | 4                        |
| PX        | Single-lens single-source with parallax                                 | 6                        |
| BS        | Single-lens binary-source                                               | 7                        |
| BO        | Single-lens binary-source with xallarap                                 | 10                       |
| LS        | Binary-lens single-source                                               | 7                        |
| LX        | Binary-lens single-source with parallax                                 | 9                        |
| LO        | Binary-lens single-source with parallax and circular orbital motion     | 12                       |

For more information, see the official [RTModel Documentation](https://github.com/valboz/RTModel/blob/dev/docs/README.md).

4. Wait for the fits to complete. This may take a while depending on the number of processors available.
5. Once complete, open `mb20135_RTModel_run/Nature.txt` to find the model with the smallest χ².
6. In the notebook `running_rtmodel.ipynb`, go to the section titled:  
   `Plotting (1) light curve and (2) caustic curve + source trajectory`  
   Run the first cell in this section and update the `model` variable with the filename of the model you wish to visualize.
7. Plot the alternative models listed in `Nature.txt` to compare solutions. These models are located in the `FinalModels` folder.
8. Optionally, plot any other model from the `Models` folder to explore different solution types.

---

## 4. MCMC with pyLIMA

1. Open the notebook `running_pylima_mcmc.ipynb`.
2. Locate the cell marked:  
   `[Action needed]: Insert the parameters for the best fit from your RTModel run`  
   and replace it with the model parameters you obtained with RTModel.
3. Run the initial cells to start the MCMC process. 
4. In the `Results` section, run the cells to visualize results and save the best-fit model and MCMC chain to a folder.
5. Run the cells in the `Plotting` section to visualize your light curve and the MCMC chain.

For more information see the official [pyLIMA documentation](https://pylima.readthedocs.io/en/latest/).
