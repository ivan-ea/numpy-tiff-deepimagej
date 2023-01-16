
import constants_and_functions as cf
from bioimageio.core import load_resource_description

a_model = load_resource_description(cf.path_model_2)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('World')

