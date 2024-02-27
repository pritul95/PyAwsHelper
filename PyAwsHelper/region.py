# coding: utf-8

"""
AWS Region Helper
"""
CONFIG = {
    "hk": "ap-east-1",  # Hong Kong
    "tk": "ap-northeast-1",  # Tokyo
    "se": "ap-northeast-2",  # Seoul
    "os": "ap-northeast-3",  # Osaka-Local
    "mu": "ap-south-1",  # Mumbai
    "hy": "ap-south-2",  # Hyderabad
    "sg": "ap-southeast-1",  # Singapore
    "sy": "ap-southeast-2",  # Sydney
    "au": "ap-southeast-2",  # Sydney
    "ce": "ca-central-1",  # Central
    "be": "cn-north-1",  # Beijing
    "ni": "cn-northwest-1",  # Ningxia
    "fr": "eu-central-1",  # Frankfurt
    "st": "eu-north-1",  # Stockholm
    "ir": "eu-west-1",  # Ireland
    "lo": "eu-west-2",  # London
    "pa": "eu-west-3",  # Paris
    "ba": "me-south-1",  # Bahrain
    "sp": "sa-east-1",  # São Paulo
    "va": "us-east-1",  # N. Virginia
    "va-gov": "us-gov-east-1",
    "oh": "us-east-2",  # Ohio
    "ca": "us-west-1",  # N. California
    "nc": "us-west-1",  # N. California
    "ca-gov": "us-gov-west-1",
    "nc-gov": "us-gov-west-1",
    "or": "us-west-2",  # Oregon
    "uae": "me-central-1",  # UAE
    "ct": "af-south-1",  # Cape Town
}


class Region(object):
    @staticmethod
    def get_region(region_suffix: str, default_region: str = None) -> str:
        """
        The function to get AWS region from `region_suffix`.

        Parameters
        ----------
        region_suffix : str
            AWS Region suffix (e.g va for us-east-1)

        default_region : str (optional)
            Default AWS Region

        Raises
        ------
        NotImplementedError
            If give `region_suffix` not found in the config.
        """
        region_suffix = region_suffix.lower()

        region = Region.get_region_config().get(region_suffix, default_region)
        if region:
            return region

        raise NotImplementedError()

    @staticmethod
    def get_region_suffix(region: str, default_region_suffix: str = None) -> str:
        """
        The function to get region suffix from AWS `region`.

        Parameters
        ----------
        region : str
            AWS Region (e.g us-east-1 for va)

        default_region : str (optional)
            Default region suffix

        Raises
        ------
        NotImplementedError
            If give AWS `region` not found in the config.
        """
        region = region.lower()

        for key, value in Region.get_region_config().items():
            if value == region:
                return key

        if default_region_suffix:
            return default_region_suffix

        raise NotImplementedError()

    @staticmethod
    def get_region_config() -> dict:
        """The function to get AWS regions config."""
        return CONFIG
