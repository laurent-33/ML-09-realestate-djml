import os
import glob
import nbformat
from datetime import date, timedelta
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError

from scrap import start_scrap


def run_notebook(notebook_filename):
    run_path = '.'
    notebook_filename_out = notebook_filename

    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)
    
    # notebook run
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    try:
        out = ep.preprocess(nb, {'metadata': {'path': run_path}})
    except CellExecutionError:
        out = None
        msg = '--------------------------------------------------------------------------\n'
        msg += f'Error executing the notebook "{notebook_filename}".\n\n'
        msg += f'Open the notebook "{notebook_filename_out}" for the traceback.\n'
        msg += '--------------------------------------------------------------------------\n\n'
        print(msg)
        raise
    finally:
        with open(notebook_filename_out, mode='w', encoding='utf-8') as f:
            nbformat.write(nb, f)


# folder scan to find all csv files
csv_files = glob.glob('../csv/*.csv')

# get the last date a csv file was created
csv_dates = [
    date.fromisoformat(csv_file[-14:-4])
    for csv_file in csv_files
    ]
csv_last_date = max(csv_dates)

# determine if new data has to be collected (too old)
days_before_new_scrap = 2
if date.today() > csv_last_date + timedelta(days=days_before_new_scrap):
    print("\nNew data collection needed :")
    print("1/1 - new scrap running (5-60 minutes)\n..........")
    #start_scrap()
    csv_last_date = date.today()

# get the last model date
model_last_date = os.stat('../models/full_pipe.file').st_mtime
model_last_date = date.fromtimestamp(model_last_date)

print(f"last data collection : {csv_last_date}")
print(f"last model : {model_last_date}")

# determine if new model has to be created (new data available)
if model_last_date < csv_last_date:
    print("\nModel update needed, please wait for the operation to be finished :")
    print("1/3 - updating the model (5-10 minutes)\n..........")
    run_notebook('02_data_processing_and_model.ipynb')

    print("2/3 - model evaluation\n..........")
    run_notebook('03_visualisation_mape.ipynb')

    print("3/3 - update complete\n")

# if recent data, do not update the model
else:
    print("\nNo model update needed -> using current data\n")
