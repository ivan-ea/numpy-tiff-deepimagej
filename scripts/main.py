
import constants_and_functions as cf
from bioimageio.core import load_resource_description
from bioimageio.core.build_spec import _write_sample_data

import numpy as np
import matplotlib.pyplot as plt

a_model = load_resource_description(cf.path_model_2)


input_im = np.load(a_model.test_inputs[0])

pixel_sizes = np.zeros_like(input.shape)

in_axes = ["".join(a.axes) for a in a_model.inputs]
out_axes = ["".join(a.axes) for a in a_model.outputs]

_write_sample_data(input_paths=a_model.test_inputs,
                   output_paths=a_model.test_outputs,
                   input_axes=in_axes,
                   output_axes=out_axes,
                   export_folder=cf.Path("."),
                   pixel_sizes=None)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('World')

#_write_sample_data()