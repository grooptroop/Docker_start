from django.db import models

# Модель сотрудника
class Employee(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество")
    hours_worked = models.PositiveIntegerField(verbose_name="Часы работы")
    experience = models.PositiveIntegerField(verbose_name="Стаж (лет)")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Зарплата")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

# Модель расписания
class Schedule(models.Model):
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    start_city = models.CharField(max_length=255, verbose_name="Город отправления")
    end_city = models.CharField(max_length=255, verbose_name="Город прибытия")
    date = models.DateField(verbose_name="Дата")
    employee = models.ForeignKey(Employee, related_name='schedules', on_delete=models.CASCADE, verbose_name="Сотрудник")

    def __str__(self):
        return f"Расписание для {self.employee} на {self.date} с {self.start_time} до {self.end_time}"

# Модель коэффициента эффективности
class Efficiency(models.Model):
    schedule = models.OneToOneField(Schedule, related_name='efficiency', on_delete=models.CASCADE, verbose_name="Расписание")
    efficiency_value = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Коэффициент эффективности")

    def __str__(self):
        return f"Эффективность для {self.schedule}"
