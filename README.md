## Setup environment:
  - mamba create -n ml python=3.12
  - mamba activate ml
  - pip install scikit-learn matplotlib keras
  - mamba install jupyter ipykernel
  - python -m ipykernel install --user --name=ml
  - jupyter lab