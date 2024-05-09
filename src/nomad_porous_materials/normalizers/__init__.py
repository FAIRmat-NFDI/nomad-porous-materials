#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from nomad.config.models.plugins import NormalizerEntryPoint
from pydantic import Field


class PorosityNormalizerEntryPoint(NormalizerEntryPoint):
    min_n_atoms: int = Field(20, description='Minimum number of atoms allowed for running the normalizer.')
    max_n_atoms: int = Field(5000, description='Maximum number of atoms allowed for running the normalizer.')
    min_pld: int = Field(1.86, description='Minimum pore limiting diameter for running the normalizer.')

    def load(self):
        from nomad_porous_materials.normalizers.porositynormalizer import (
            PorosityNormalizer,
        )

        return PorosityNormalizer()


porositynormalizer = PorosityNormalizerEntryPoint(
    name='PorosityNormalizer',
    description='Normalizer that automatically extracts properties from porous materials.',
)
