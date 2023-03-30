
import constants_and_functions as cf
from bioimageio.core import load_resource_description

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tic = cf.datetime.now()
    print("Creating tiffs from numpy test images. Started at: {}".format(tic))
    rdf_paths = cf.read_rdf_paths()
    fails = []

    for i, rdf_path in enumerate(rdf_paths):
        tac = cf.datetime.now()
        print("Doing model {}/{}: {}".format(i+1, len(rdf_paths), rdf_path))
        out_path = cf.gen_output_path(rdf_path)
        cf.try_create_dir(out_path)

        if cf.model_already_done(out_path):
            print("Model already done!")
            continue

        try:
            model = load_resource_description(cf.Path(rdf_path))
        except Exception:
            fails.append(rdf_path)
            continue

        try:
            cf.write_tiff_images(model, out_path)
            cf.write_numpy_info(model, out_path)
        except Exception:
            fails.append(rdf_path)
            continue

        cf.print_elapsed_time(tac, "Completed model {}/{}".format(i+1, len(rdf_paths)))

    cf.print_elapsed_time(tic, "Completed creation of tiffs for all {} models".format(len(rdf_paths)))

    fails_file = "../resources/failed_rdfs.txt"
    print("Failed {}/{} models. List written in {}".format(len(fails), len(rdf_paths), fails_file))
    cf.write_failed_rdfs(fails, fails_file)
