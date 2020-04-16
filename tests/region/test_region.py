# coding: utf-8

"""
AWS Region Test
"""
import pytest

from PyAwsHelper.region import Region


@pytest.mark.region
class TestRegion:
    def test_known_region(self):
        region = Region.get_region("va")
        assert region == "us-east-1"

        region = Region.get_region("ca-gov")
        assert region == "us-gov-west-1"

    def test_unknown_region(self):
        # test unknown region with default value
        region = Region.get_region("foo", "bar")
        assert region == "bar"

        # unknown region without default value should catch `NotImplementedError`
        with pytest.raises(NotImplementedError):
            Region.get_region("foo")

    def test_known_region_suffix(self):
        region_suffix = Region.get_region_suffix("us-west-2")
        assert region_suffix == "or"

        region_suffix = Region.get_region_suffix("us-gov-east-1")
        assert region_suffix == "va-gov"

    def test_unknown_region_suffix(self):
        # test unknown region suffix with default value
        region_suffix = Region.get_region_suffix("foo", "bar")
        assert region_suffix == "bar"

        # unknown region suffix without default value should catch `NotImplementedError`
        with pytest.raises(NotImplementedError):
            Region.get_region_suffix("foo")
