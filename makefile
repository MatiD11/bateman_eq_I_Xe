MAIN_FILE = main.py

DEPS = estimate_ex_time.py bateman_eq.py runge_kutta.py matrix_method.py analytical_sol.py plot_results.py

PYTHON = python3

FLUX_DIR = flux
OUTPUT_DIR = output

all: run

run: $(MAIN_FILE) $(DEPS) $(FLUX_DIR) $(OUTPUT_DIR)
	$(PYTHON) $(MAIN_FILE) $(ARGS)

performance: $(MAIN_FILE) $(DEPS) $(FLUX_DIR) $(OUTPUT_DIR)
	$(PYTHON) $(MAIN_FILE) --performance $(ARGS)

clean:
	rm -rf __pycache__ $(FLUX_DIR)/*.png $(OUTPUT_DIR)/*.png

$(FLUX_DIR):
	mkdir -p $(FLUX_DIR)

$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

help:
	help:
	@echo "Available commands in the Makefile:"
	@echo "  make          - Runs the main script with custom parameters using 'ARGS'"
	@echo "  make run      - Runs the main script with custom parameters using 'ARGS'"
	@echo "  make performance - Measures the execution time of the program"
	@echo "  make clean    - Removes temporary and cache files"
	@echo "  ARGS='--time-range <start> <end> --dt <value>' arguments that can be passed to make run or make performance"
