from collections import OrderedDict, Counter

from django.db.models import Sum, Value, Count
from django.db.models.functions import Coalesce

from .models import Student



def students_summary(context):
    # x =  (context
    #     .order_by()
    #     .values('school_class__name')
    #     .annotate(count=Count('age'))
    #     .values_list('school_class__name','count')
    # )
    # print(dict(x))
    return dict((
        context
        .annotate(random_name=Coalesce('school_class__name', Value('-')))
        .order_by()
        .values('random_name')
        .annotate(count=Count('first_name'))
        .values_list('random_name','count')
    ))

    
def students_in_class(context):
    # return dict(
    #     context
    #     .values('name')
    #     .annotate(count=Count('student__school_class'))
    #     .values_list('name','count')
    # )
    data = (
        context
        .annotate(count=Coalesce(Count('student__school_class'), 0))
        .annotate(sum=Coalesce(Sum('student__age'), 0))
        .values('id','name','count','sum','educator__first_name', 'educator__surname' )
    )
    print(data)
    return data