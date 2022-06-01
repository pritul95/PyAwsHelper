import logging
from os import getenv
from threading import RLock
from typing import Dict, Tuple

from boto3 import Session

from PyAwsHelper.boto_session import BotoSession

LOG = logging.getLogger("PyAwsHelper")
LOG.setLevel(logging.ERROR)


class BotoHelper:
    """
    Wrapper class of BotoSession which lets us keep map of refreshable sessions.
    Usage
    -----
    helper = BotoHelper()
    client = helper.get_client(service_name="s3", region_name="us-east-1", role_arn="arn:aws:iam::123:role/my_db_role") # we now can cache this client object without worrying about expiring credentials
    """

    # check for max session duration
    # https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-role-max-session
    TTL = int(getenv("PyAwsHelper_BotoHelper_TTL", 900))

    def __init__(self):
        self.__sessions = {}
        self.lock = RLock()

    @property
    def sessions(self) -> Dict:
        """
        Boto3 sessions
        """
        try:
            self.lock.acquire()
            return self.__sessions
        finally:
            self.lock.release()

    def get_client(
        self, service_name: str, region_name: str, role_arn: str = None, **kwargs
    ) -> Session.client:
        """
        Get boto3 client for given session
        Parameters
        ----------
        service_name : str
            AWS service name.
        region_name : str
            AWS Region Name, i.e us-east-1, us-west-2, etc.
        role_arn : str (optional)
            The role arn to sts before creating session.
        """
        LOG.debug(
            f"Getting client service_name={service_name} region_name={region_name} role_arn={role_arn}"
        )
        session, _ = self.get_session(region_name=region_name, role_arn=role_arn)

        return session.client(
            service_name=service_name, region_name=region_name, **kwargs
        )

    def get_resource(
        self, service_name: str, region_name: str, role_arn: str = None, **kwargs
    ) -> Session.resource:
        """
        Get boto3 resource for given session
        Parameters
        ----------
        service_name : str
            AWS service name.
        region_name : str
            AWS Region Name, i.e us-east-1, us-west-2, etc.
        role_arn : str (optional)
            The role arn to sts before creating session.
        """
        LOG.debug(
            f"Getting resource service_name={service_name} region_name={region_name} role_arn={role_arn}"
        )
        session, _ = self.get_session(region_name=region_name, role_arn=role_arn)

        return session.resource(
            service_name=service_name, region_name=region_name, **kwargs
        )

    def get_session(
        self, region_name: str, role_arn: str = None
    ) -> Tuple[Session, bool]:
        """
        Get refreshable session from BotoSession
        """
        LOG.debug(f"Getting session region_name={region_name} role_arn={role_arn}")
        session, is_refreshable = None, False
        if self.sessions:
            session = self.sessions.get(role_arn, self.sessions.get("default"))
            if session:
                LOG.debug(
                    f"Using cached session for region_name={region_name} role_arn={role_arn}"
                )
                return session, True

        if role_arn:
            session, is_refreshable = BotoSession(
                region_name=region_name, ttl=BotoHelper.TTL, sts_arn=role_arn
            ).refreshable_session()
        else:
            session, is_refreshable = Session(region_name=region_name), False

        if role_arn and is_refreshable:
            self.sessions[role_arn] = session
        elif role_arn is None:
            self.sessions["default"] = session

        return session, is_refreshable
