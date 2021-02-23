# PyAwsHelper
Python AWS Helper Library


## AWS Region Helper
### Get Boto3 Client and Resource with refreshable session
```python
from PyAwsHelper.boto_helper import BotoHelper

helper = BotoHelper()

# Both client is sharing common refreshable session
s3_client = helper.get_client(service_name="s3", region_name="us-east-1", role_arn="arn:aws:iam::123:role/my_db_role")

db_client = helper.get_client(service_name="dynamodb", region_name="us-east-1", role_arn="arn:aws:iam::123:role/my_db_role")
```

### Use Raw Refreshable session to implement your need
```python
# can use BotoHelper to get session
from PyAwsHelper.boto_helper import BotoHelper
helper = BotoHelper()
s3_client = helper.get_session(region_name="us-east-1", role_arn="arn:aws:iam::123:role/my_db_role")

# or can directly access raw BotoSession module
from PyAwsHelper.boto_session import BotoSession
session = BotoSession().refreshable_session()
client = session.client("s3") # we now can cache this client object without worrying about expiring credentials
```

### Get AWS region from region suffix

```python
from PyAwsHelper.region import Region

aws_region = Region.get_region("va")

>>> aws_region
'us-east-1'
```

Also supports providing default value
```python
from PyAwsHelper.region import Region

aws_region = Region.get_region("foo", default_region="bar")

>>> aws_region
'bar'
```

### Get region suffix from AWS region
```python
from PyAwsHelper.region import Region

aws_region = Region.get_region_suffix("us-east-1")

>>> aws_region
'va'
```

Also supports providing default value
```python
from PyAwsHelper.region import Region

aws_region = Region.get_region_suffix("foo", default_region_suffix="bar")

>>> aws_region
'bar'
```

### Regions Config
```python
{
    "hk": "ap-east-1",  # Hong Kong
    "tk": "ap-northeast-1",  # Tokyo
    "se": "ap-northeast-2",  # Seoul
    "os": "ap-northeast-3",  # Osaka-Local
    "mu": "ap-south-1",  # Mumbai
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
}
```