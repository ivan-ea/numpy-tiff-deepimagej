import constants_and_functions as cf
from bioimageio.core import load_resource_description
from pathlib import Path
import numpy as np

example_path = Path.home() / "blank_fiji" / "question_forum"

rdf_path_1 = example_path / "skin-lesions-classification_pytorch_script" / "rdf.yaml"
rdf_path_2 = example_path / "model_liam" / "rdf.yaml"

m1 = load_resource_description(rdf_path_2)

n = np.load(Path(rdf_path_1, "..", "0066.npy"))