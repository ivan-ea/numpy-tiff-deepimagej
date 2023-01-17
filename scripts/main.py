
import constants_and_functions as cf
from bioimageio.core import load_resource_description
from bioimageio.core.build_spec import _write_sample_data

import numpy as np
import matplotlib.pyplot as plt

# testing for 1 model rdf
a_model = load_resource_description(cf.path_model_2)

input_im = np.load(a_model.test_inputs[0])



in_axes = ["".join(a.axes) for a in a_model.inputs]
out_axes = ["".join(a.axes) for a in a_model.outputs]

_write_sample_data(input_paths=a_model.test_inputs,
                   output_paths=a_model.test_outputs,
                   input_axes=in_axes,
                   output_axes=out_axes,
                   export_folder=cf.Path("."),
                   pixel_sizes=None)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tic = cf.datetime.now()
    print("Creating tiffs from numpy test images. Started at: {}".format(tic))
    rdf_paths = cf.read_rdf_paths()

    for i, rdf_path in enumerate(rdf_paths[0:3]):
        tac = cf.datetime.now()
        out_path = cf.gen_output_path(rdf_path)
        cf.try_create_dir(out_path)
        model = load_resource_description(cf.Path(rdf_path))
        cf.write_tiff_images(model, out_path)
        cf.write_numpy_info(model, out_path)

        cf.print_elapsed_time(tac, "Completed model {}/{}".format(i,len(rdf_paths)))

    cf.print_elapsed_time(tic,
                          "Completed creation of tiffs for all {} models".format(len(rdf_paths)))