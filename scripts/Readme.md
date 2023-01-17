# Requirements

- bioimageio.core installed as dev
- change `__init__.py` to look like:

````python
from .add_weights import add_weights
from .build_model import build_model, _write_sample_data
````

absolute path: `C:\Users\hestevez\.conda\envs\bio-conv-weights\Lib\site-packages\bioimageio\core\build_spec\__init__.py`

# Todos
- [x] read inputs from file
- [x] create correct output folder
- [x] save images in correct folder 
- [x] save numpy shapes in plain text
- [x] time it (every model and complete elapsed time)
- [_] save log of run for all models