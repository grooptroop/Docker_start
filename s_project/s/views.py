from django.shortcuts import render
from .models import Schedule, Efficiency
from datetime import datetime


def schedule_calendar(request):
    schedules = Schedule.objects.all()

    # Фильтруем расписание с коэффициентом эффективности больше 0.68
    filtered_schedules = []
    for schedule in schedules:
        efficiency = schedule.efficiency.efficiency_value if schedule.efficiency else 0
        if efficiency > 0.68:
            filtered_schedules.append(schedule)

    # Проверка пересечений времени и выбор с наибольшим коэффициентом эффективности
    unique_schedules = []
    for schedule in filtered_schedules:
        is_conflict = False
        for existing_schedule in unique_schedules:
            # Проверка пересечения времени (если одно событие перекрывает другое)
            if (schedule.date == existing_schedule.date and
                    (
                            schedule.start_time < existing_schedule.end_time and schedule.end_time > existing_schedule.start_time)):
                # Если пересекаются, выбираем событие с лучшим коэффициентом эффективности
                existing_efficiency = existing_schedule.efficiency.efficiency_value
                current_efficiency = schedule.efficiency.efficiency_value
                if current_efficiency > existing_efficiency:
                    unique_schedules.remove(existing_schedule)
                    unique_schedules.append(schedule)
                is_conflict = True
                break
        if not is_conflict:
            unique_schedules.append(schedule)

    # Передаем отфильтрованные расписания в шаблон
    context = {
        'schedules': unique_schedules,
    }
    return render(request, 's/schedule.html', context)

def table_view(request):
    data = Schedule.objects.all()
    return render(request, 's/3LAB.html', {'data': data})

def krasota(request):
    return render(request, 's/krasota.html')