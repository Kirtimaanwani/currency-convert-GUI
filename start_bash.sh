echo [$(date)]: "START"
echo [$(date)]: "Creating conda venv with python version 3.8"
conda create --prefix ./venv python==3.8 -y

echo [$(date)]: "activate venv"
source activate ./venv

echo [$(date)]: "Installing dev requirements"
pip install -r requirements.txt


echo [$(date)]: "getting currency rates"
python run_this_first_to_get_latest_exchange_rates.py

echo [$(date)]: "Run GUI"
python main.py

echo [$(date)]: "END"
