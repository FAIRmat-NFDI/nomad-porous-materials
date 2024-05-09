from nomad.config import config
from nomad.normalizing import Normalizer

configuration = config.get_plugin_entry_point('nomad_porous_materials.normalizers:mynormalizer')


class MyNormalizer(Normalizer):
    def normalize(self, archive, logger):
        super().normalize(logger)
        logger.info(f'MyNormalizer.normalize: parameter={configuration.parameter}')
        if archive.results and archive.results.material:
            archive.results.material.elements = ['C', 'O']
