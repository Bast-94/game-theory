reformat: 
	$(PYTHON) -m black . || echo "black failed"
	$(PYTHON) -m isort . || echo "isort failed"

fast_commit: reformat
	sh pusher.sh

fast_push: fast_commit
	git push