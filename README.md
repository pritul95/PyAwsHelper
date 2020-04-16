# PyAwsHelper
Python AWS Helper Library


## AWS Region Helper
Get AWS region from region suffix

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

Get region suffix from AWS region
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
