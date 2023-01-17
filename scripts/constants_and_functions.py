import os
from datetime import datetime
from pathlib import Path
import numpy as np
from bioimageio.core.build_spec import _write_sample_data

COLLECTION_ROOT = Path("..", "..", "bioimageio-gh-pages", "rdfs")

path_model_2 = Path(COLLECTION_ROOT, "10.5281", "zenodo.5749843", "5888237", "rdf.yaml")


def read_rdf_paths(filename="../resources/rdfs_to_test.txt"):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        return lines


def gen_output_path(in_rdf_path):
    in_path = Path(in_rdf_path)
    parts = in_path.parts
    idx = parts.index("rdfs")
    out_path = Path("..", *parts[idx+1:-1])
    return out_path


def try_create_dir(path, verb=True):
    try:
        os.makedirs(path)
        if verb:
            print("Dir created: {}".format(path))
    except FileExistsError:
        if verb:
            print("Dir exists: {}".format(path))


def print_elapsed_time(tic, msg):
    tac = datetime.now()
    print("{} at: {}".format(msg, tac))
    print("Elapsed time:", tac - tic)


def write_tiff_images(model, output_path):
    in_axes = ["".join(a.axes) for a in model.inputs]
    out_axes = ["".join(a.axes) for a in model.outputs]
    # pixel_sizes = np.zeros_like(input_im.shape)  # not needed

    _write_sample_data(input_paths=model.test_inputs,
                       output_paths=model.test_outputs,
                       input_axes=in_axes,
                       output_axes=out_axes,
                       export_folder=output_path,
                       pixel_sizes=None)


def write_numpy_info(model, output_path):
    data = {"images": [np.load(model.test_inputs[0]),
                       np.load(model.test_outputs[0])],
            "filenames": ["input_shape.edn", "output_shape.edn"]}

    for i in [0, 1]:
        content = str(list(data["images"][i].shape))
        with open(Path(output_path, data["filenames"][i]), 'w') as f:
            f.write(content)
