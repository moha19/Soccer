from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from django.db.models import Sum, Avg
from admin_totals.admin import ModelAdminTotals
from jalali_date import datetime2jalali
from .actions import export_as_csv_action
from django.utils import timezone
from .models import Train_Location, Train_Target, Train_Type, Train, Feature, Point
from .forms import TrainForm
from django.contrib.auth.models import User, Group

admin.site.register(Train_Location)
admin.site.register(Train_Target)
admin.site.register(Train_Type)
admin.site.register(Feature)

@admin.register(Train)
class TrainAdmin(ModelAdminTotals):
    form = TrainForm
    date_hierarchy = 'date'
    filter_horizontal = ('category',)


    def get_list_display(self, request):
        if request.user.is_superuser:
            return ('get_time', 'location', 'target', 'category',)
        else:
            return ('get_time', 'location')

    def get_time(self, obj):
        return datetime2jalali(obj.date).strftime('%a , %Y/%m/%d')

    get_time.short_description = 'زمان'
    get_time.admin_order_field = 'date'

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return 'date', ('location', RelatedDropdownFilter), ('target', RelatedDropdownFilter)
        else:
            return 'date',  ('location', RelatedDropdownFilter),

    actions = [export_as_csv_action("خروجی CSV", fields=['date', 'location', 'target', 'category' ])]

    def lookup_allowed(self, key, value):
        return True

    def get_queryset(self, request): 
        qs = super(TrainAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

@admin.register(Point)
class PointAdmin(ModelAdminTotals):
    filter_horizontal = ('player', 'feature',)
    list_totals = [('point', Sum),]


    def get_list_display(self, request):
        if request.user.is_superuser:
            return ('get_players', 'train', 'get_features', 'point',)
        else:
            return ('train', 'get_features', 'point',)

    def get_players(self, obj):
        return "-".join([p.username for p in obj.player.all()])
    get_players.short_description = 'بازیکن'
    get_players.admin_order_field = 'player'


    def get_features(self, obj):
        return "-".join([p.name for p in obj.feature.all()])
    get_features.short_description = 'ویژگی'
    get_features.admin_order_field = 'feature'


    def get_list_filter(self, request):
        if request.user.is_superuser:
            return  ('train', RelatedDropdownFilter), ('player', RelatedDropdownFilter), ('feature', RelatedDropdownFilter)
        else:
            return ('train', RelatedDropdownFilter), ('feature', RelatedDropdownFilter)

    actions = [export_as_csv_action("خروجی CSV", fields=['player', 'train', 'feature', 'point' ])]

    def lookup_allowed(self, key, value):
        return True
    
    # change_list_template = 'graph.html'


    def get_queryset(self, request): 
        qs = super(PointAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            return qs
        return qs.filter(player__username__contains=request.user.username)