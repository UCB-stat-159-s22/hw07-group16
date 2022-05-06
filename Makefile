.PHONY: env
env:
	bash -i envsetup.sh

.PHONY: remove-env
remove-env:
	mamba env remove -n hw7env

data/taxi_clean.csv:
	jupyter execute taxi_clean.ipynb