echo "Running program...."
source venv/bin/activate
python3 main.py --verbosity N3 > output.s
echo "Output delivered to output.s"
deactivate
