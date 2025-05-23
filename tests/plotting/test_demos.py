from __future__ import annotations

import numpy as np
import pytest

import pyvista as pv
from pyvista import demos
from pyvista.plotting import system_supports_plotting

skip_no_plotting = pytest.mark.skipif(
    not system_supports_plotting(),
    reason='Test requires system to support plotting',
)


@skip_no_plotting
def test_plot_glyphs():
    demos.plot_glyphs(2)


def test_atomized():
    grid = demos.logo_atomized(density=0.2, scale=0.6)
    assert grid.n_cells


def test_logo_basic():
    pd = demos.logo_basic()
    assert pd.n_cells


def test_logo_voxel():
    grid = demos.logo_voxel()
    assert grid.n_cells


@pytest.mark.skip_mac('MacOS testing on Azure fails when downloading')
@skip_no_plotting
@pytest.mark.skip_windows
def test_plot_logo():
    # simply should not fail
    demos.plot_logo()


@skip_no_plotting
def test_plot_datasets():
    # simply should not fail
    demos.plot_datasets()


def test_plot_datasets_dataset_type():
    with pytest.raises(ValueError, match='Invalid dataset_type'):
        demos.plot_datasets(dataset_type='foo')


@skip_no_plotting
def test_plot_wave():
    points = demos.plot_wave(wavetime=0.1)
    assert isinstance(points, np.ndarray)


@skip_no_plotting
def test_beam_example():
    demos.plot_beam()


@skip_no_plotting
def test_plot_ants_plane():
    demos.plot_ants_plane()


@skip_no_plotting
def test_orientation_cube():
    pl = demos.orientation_plotter()
    assert isinstance(pl, pv.Plotter)
    pl.show()
