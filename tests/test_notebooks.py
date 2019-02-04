import papermill as pm
import pytest


def test_notebooks_nominal(tmpdir):
    output_nb = tmpdir.join('output.ipynb')
    # to check kernel name run:
    # jupyter kernelspec list
    common_kwargs = {
        'output_path': str(output_nb),
        'kernel_name': 'ir'
    }

    pm.execute_notebook('R-in-Jupyter-Example.ipynb', **common_kwargs)

    nb = pm.read_notebook(str(output_nb))
    print(nb.data)
    assert nb.data['coin_trials'] == pytest.approx(10.6667)


def test_notebooks_alternative(tmpdir):
    output_nb = tmpdir.join('output.ipynb')
    common_kwargs = {
        'output_path': str(output_nb),
        # 'kernel_name': 'python{}'.format(sys.version_info.major)
        'kernel_name': 'ir'
    }

    pm.execute_notebook('R-in-Jupyter-Example.ipynb',
                        parameters=dict(heads=2, tosses=8),
                        **common_kwargs)
    nb = pm.read_notebook(str(output_nb))
    print(nb.data)
    assert nb.data['coin_trials'] == pytest.approx(28.4444)
