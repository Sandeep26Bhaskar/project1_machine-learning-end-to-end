echo [$(date)]: "Start"

echo [$(date)]: "create a virtual environment."

conda create --prefix ./env python=3.10 -y

echo [$(date)]: "Activate the virtual environment!"

conda activate ./env

echo [$(date)]: "Installing the requirements for this project!"

pip install -r requirements.txt

echo [$(date)]: "End."