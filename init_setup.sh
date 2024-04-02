echo [$(date)]: "Start"
echo [$(echo)]: "Creating the virtual environment with python v3.10"
conda create --prefix ./env python==3.10 -y
echo [$(echo)]: "Activating the environment"
conda activate ./env
echo [$(echo)]: "installing required dev packages"
pip install -r requirements.txt
echo [$(echo)]: "END"
