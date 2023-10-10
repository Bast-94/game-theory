PYTHON=python

exec_main: reformat
	$(PYTHON) main.py

exec_simulator: reformat
	$(PYTHON) simulate.py

reformat: 
	$(PYTHON) -m black . || echo "black failed"
	$(PYTHON) -m isort . || echo "isort failed"

commit: reformat
	sh pusher.sh
fast_commit: reformat
	sh pusher.sh quick

fast_push: fast_commit
	git push