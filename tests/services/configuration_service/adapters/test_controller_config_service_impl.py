from unittest import TestCase

from confz import ConfZDataSource

from src.services.configuration_service.adapters.confz_classes import PerformanceConfigConfZ
from src.services.configuration_service.model.performance_config import PerformanceConfig
from tests.conftest import fake_performance_configuration


class TestModuleMethods(TestCase):

    def test_mapping_between_performance_config_and_performance_config_confz(self):
        pc_dict = fake_performance_configuration()

        pc = PerformanceConfig(**pc_dict)
        pcc = PerformanceConfigConfZ(config_sources=ConfZDataSource(data=pc_dict))

        self.assertDictEqual(pc.dict(), pcc.dict())
