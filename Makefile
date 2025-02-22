# Makefile to creat micromamba env with streamlit and
# required dependencies automatically

# Makefile options
help:
	@echo "Makefile run options:"
	@echo "install	- install micromamba and corresponding streamlit mamba env"
	@echo "clean	- remove micromamba installation, caches, env, and pakages"


# Install micromamba
install: micromamba envs

micromamba:
	@echo "Installing micromamba:"
	curl -L https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
	mv bin/micromamba .
	rmdir bin
	@echo "Micromamba installlation complete!"

envs:
	@echo "Creating streamlit app env"
	export MAMBA_ROOT_PREFIX=${PWD} && \
	./micromamba env -y create -f environment.yml


# Uninstall packaged, dependencies, and micromamba
clean:
	@echo "Removing micromamba and associated env:"
	rm -f micromamba
	rm -rf envs
	rm -rf pkgs
	rm -rf __pycache__
	
.PHONY: help install clean