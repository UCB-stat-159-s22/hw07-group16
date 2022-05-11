.PHONY: env
env:
	bash -i envsetup.sh

.PHONY: remove-env
remove-env:
	mamba env remove -n hw7env

data/taxi_clean.csv:
	jupyter execute taxi_clean.ipynb
	
.PHONY: clean
clean:
	rm -f figures/*.png
	rm -f tables/*.csv

.PHONY: all
all:
	jupyter execute busy_time_and_fares_analysis.ipynb
	jupyter execute tip_analysis.ipynb
	jupyter execute tip_amt_prediction.ipynb
	jupyter execute location_analysis.ipynb
	jupyter execute main.ipynb