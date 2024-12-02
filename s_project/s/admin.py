from django.contrib import admin
from .models import Schedule, Efficiency, Employee

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'start_time', 'end_time', 'start_city', 'end_city', 'employee')

@admin.register(Efficiency)
class EfficiencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'schedule', 'efficiency_value', 'employee_name')

    def employee_name(self, obj):
        return f"{obj.schedule.employee.last_name} {obj.schedule.employee.first_name}" if obj.schedule and obj.schedule.employee else "Не назначен"
    employee_name.short_description = "Сотрудник"

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'patronymic', 'hours_worked', 'experience', 'salary')
