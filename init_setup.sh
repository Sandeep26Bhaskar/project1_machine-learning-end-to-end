echo [$(date)]: "Start"
echo [$(date)]: "Creating the virtual environment with python v3.10"
conda create --prefix ./env python==3.10 -y
echo [$(date)]: "Activating the environment"
conda activate ./env
echo [$(date)]: "installing required dev packages"
pip install -r requirements.txt
echo [$(date)]: "END"
