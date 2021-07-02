from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'no', 'email', 'lnkdin', 'aboutme', 'brd1', 'schl1', 'year1',
                    'percent1','brd2', 'schl2', 'year2', 'percent2', 'course', 'uni', 'instname',
                    'year3', 'percent3', 'beg', 'prof', 'suff', 'topic1', 'orgname1', 'cityname1',
                    'dur1', 'date1', 'date2', 'topic2', 'orgname2', 'cityname2', 'dur2', 'date3',
                    'date4', 'projname1', 'projdur1', 'desc1', 'projname2', 'projdur2', 'desc2',
                    'skill1', 'skill2', 'skill3', 'achievements', 'profimg']
