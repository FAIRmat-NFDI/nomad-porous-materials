from collections import defaultdict

from nomad.atomutils import Formula
from nomad.datamodel import EntryArchive, EntryMetadata
from nomad.datamodel.metainfo.simulation.run import Run, Program
from nomad.datamodel.metainfo.simulation.system import Atoms, System

import runschema


def assert_topology(topology):
    """Checks that the given topology has a valid structure."""
    child_map = {}
    child_map_determined = defaultdict(list)
    for top in topology:
        assert top.system_id is not None
        assert top.parent_system is not None or top.system_relation.type == 'root'
        assert (
            top.atoms is not None
            or top.atoms_ref is not None
            or top.indices is not None
        )
        assert top.n_atoms is not None
        assert top.elements is not None
        assert top.n_elements is not None
        assert top.chemical_formula_hill is not None
        assert top.chemical_formula_reduced is not None
        assert top.chemical_formula_anonymous is not None
        assert top.elemental_composition
        for comp in top.elemental_composition:
            assert comp.element
            assert comp.mass
            assert comp.mass_fraction
            assert comp.atomic_fraction
        if top.parent_system:
            child_map_determined[top.parent_system].append(top.system_id)
        if top.child_systems:
            child_map[top.system_id] = top.child_systems
        if top.indices is not None:
            assert top.atoms_ref is not None
            assert len(top.indices.shape) == 2
            assert top.mass_fraction is not None
            assert top.atomic_fraction is not None

    assert len(child_map) == len(child_map_determined)
    for key in child_map.keys():
        assert child_map[key] == child_map_determined[key]


def get_template_for_structure(atoms: Atoms) -> EntryArchive:
    system = System(is_representative=True)
    system.atoms = runschema.system.Atoms(
        positions=atoms.get_positions() * 1e-10,
        labels=atoms.get_chemical_symbols(),
        lattice_vectors=atoms.get_cell() * 1e-10,
        periodic=atoms.get_pbc(),
    )
    system.chemical_composition_hill = Formula(''.join(atoms.get_chemical_symbols())).format('hill')
    archive = EntryArchive(metadata=EntryMetadata(domain='dft'))
    run = Run(program=Program(name='VASP'))
    run.system.append(system)
    archive.run.append(run)

    return archive
