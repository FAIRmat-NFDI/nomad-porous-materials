import ase
import pytest

from nomad.client import normalize_all

from tests.conftest import assert_topology, get_template_for_structure


@pytest.mark.parametrize(
    'filepath',
    [
        'tests/data/normalizers/porous_systems/COF-1.cif',
        'tests/data/normalizers/porous_systems/IRR.cif',
        'tests/data/normalizers/porous_systems/SARSUC.cif',
    ],
)
def test_porosity(filepath):
    atoms = ase.io.read(filepath)
    archive = get_template_for_structure(atoms)
    normalize_all(archive)

    topology = archive.results.material.topology
    assert_topology(topology)
    topology_porous = [
        top for top in archive.results.material.topology if top.method == 'porosity'
    ]
    porous_system = topology_porous[0]
    assert porous_system.largest_cavity_diameter != 0
    assert porous_system.pore_limiting_diameter != 0
    assert porous_system.largest_included_sphere_along_free_sphere_path != 0
    assert porous_system.accessible_surface_area != 0
    assert porous_system.accessible_volume != 0
    assert porous_system.void_fraction != 0
    assert porous_system.n_channels > 0


@pytest.mark.parametrize(
    'filepath',
    [
        'tests/data/normalizers/mofs/EDUSIF.cif',
        'tests/data/normalizers/mofs/RUBTAK01.cif',
        'tests/data/normalizers/mofs/SARSUC.cif',
    ],
)
def test_mof(filepath):
    atoms = ase.io.read(filepath)
    archive = get_template_for_structure(atoms)
    normalize_all(archive)

    topology = archive.results.material.topology
    assert_topology(topology)
    topology_porous = [
        top for top in archive.results.material.topology if top.method == 'porosity'
    ]
    porous_system = topology_porous[0]
    metal_sbus = [
        m_sbu.label for m_sbu in topology_porous[1:] if 'metal_sbu' in m_sbu.label
    ]
    organic_sbus = [
        m_sbu.label for m_sbu in topology_porous[1:] if 'organic_sbu' in m_sbu.label
    ]
    ligands = [
        m_sbu.label for m_sbu in topology_porous[1:] if 'organic_ligand' in m_sbu.label
    ]
    assert porous_system.largest_cavity_diameter != 0
    assert porous_system.pore_limiting_diameter != 0
    assert porous_system.largest_included_sphere_along_free_sphere_path != 0
    assert porous_system.accessible_surface_area != 0
    assert porous_system.accessible_volume != 0
    assert porous_system.void_fraction != 0
    assert porous_system.n_channels != 0
    assert len(metal_sbus) > 0
    assert len(organic_sbus) > 0
    assert len(ligands) > 0
