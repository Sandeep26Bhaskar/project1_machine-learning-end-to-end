import os 
from pathlib import Path

package_name = "DiamondPricePredictor"

list_of_files = [
    "/.github/workflow/.gitkeep",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_training.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/training_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py"
    f"src/{package_name}/exception.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/utils/__init__.py",
    "requirements.txt",
    "setup.py",
    "init_setup.py"
]

for filepath in list_of_files:
    filedir,filename = os.path.split(filepath)
    print(filedir,filename)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
    
    if (not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")