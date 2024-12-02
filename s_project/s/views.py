from django.shortcuts import render
from .models import Schedule, Efficiency
from datetime import datetime
import random


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



# Симуляция игры 21
def blackjack(request):
    # Получаем состояние игры из сессии или инициализируем новое
    if 'game_state' not in request.session:
        request.session['game_state'] = {
            'player_hand': [],
            'dealer_hand': [],
            'player_score': 0,
            'dealer_score': 0,
            'game_over': False,
            'result': None,
        }

    game_state = request.session['game_state']

    # Логика: Раздача карт игроку
    if request.method == 'POST' and not game_state['game_over']:
        if 'hit' in request.POST:  # Игрок берет карту
            card = random.randint(1, 11)
            game_state['player_hand'].append(card)
            game_state['player_score'] += card

            # Проверка на перебор
            if game_state['player_score'] > 21:
                game_state['game_over'] = True
                game_state['result'] = 'Перебор! Вы проиграли.'

        elif 'stand' in request.POST:  # Игрок завершает ход
            # Ход дилера
            while game_state['dealer_score'] < 17:
                card = random.randint(1, 11)
                game_state['dealer_hand'].append(card)
                game_state['dealer_score'] += card

            # Проверяем победителя
            if game_state['dealer_score'] > 21 or game_state['player_score'] > game_state['dealer_score']:
                game_state['result'] = 'Вы выиграли!'
            elif game_state['player_score'] < game_state['dealer_score']:
                game_state['result'] = 'Вы проиграли.'
            else:
                game_state['result'] = 'Ничья.'

            game_state['game_over'] = True

    # Сброс игры
    if 'reset' in request.POST:
        request.session.pop('game_state')

    request.session.modified = True
    return render(request, 's/Fuf.html', {'game_state': game_state})
