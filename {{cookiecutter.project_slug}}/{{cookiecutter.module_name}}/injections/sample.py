import inject

from .config import InjectionConfig


class SampleServiceBase:
    def __init__(self):
        pass


class SampleService(SampleServiceBase):
    def __init__(self):
        super().__init__()


class FakeSampleService(SampleServiceBase):
    def __init__(self):
        super().__init__()


def production_sample_service() -> SampleServiceBase:
    inject.bind_to_provider(SampleServiceBase, SampleService)


def test_sample_service() -> SampleServiceBase:
    inject.bind_to_provider(SampleServiceBase, FakeSampleService)


SAMPLE_INJECTION = {
    InjectionConfig.PRODUCTION: production_sample_service,
    InjectionConfig.TEST: test_sample_service,
}


def configure_sample_injection(binder: inject.Binder, config: InjectionConfig) -> None:
    binder.bind(SampleServiceBase, SAMPLE_INJECTION[config])
