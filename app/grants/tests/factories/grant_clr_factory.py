from datetime import datetime, timedelta

import factory
import pytest
from grants.models.grant import GrantCLR

from dashboard.tests.factories import ProfileFactory


@pytest.mark.django_db
class GrantCLRFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GrantCLR

    round_num = factory.Faker('pyint')
    start_date = factory.LazyFunction(datetime.now)
    end_date = factory.LazyAttribute(lambda o: o.start_date + timedelta(weeks=2))
    owner = factory.SubFactory(ProfileFactory)
