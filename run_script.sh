echo "Attempting to install virtualenv...."
pip3 install virtualenv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt


echo "Running program...."
python3 main.py --verbosity > output.s
echo "Output delivered to output.s"
deactivate
