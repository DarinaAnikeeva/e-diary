import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid, Lesson, Mark, Chastisement, Commendation


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid__full_name__icontains=name,
                                points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    chastisement = Chastisement.objects.filter(schoolkid__full_name__icontains=schoolkid)
    for mark in chastisement:
        mark.delete()


def create_commendation(schoolkid, subject):
    commendations = ['Молодец!',
                     'Отлично!',
                     'Хорошо!',
                     'Гораздо лучше, чем я ожидал!',
                     'Ты меня приятно удивил!',
                     'Великолепно!',
                     'Прекрасно!',
                     'Это как раз то, что нужно!',
                     'Я тобой горжусь!',
                     'С каждым разом у тебя получается всё лучше!',
                     'Мы с тобой не зря поработали!'
                     'Я вижу, как ты стараешься!'
                     ]
    try:
        child = Schoolkid.objects.get(full_name__icontains=schoolkid)
        lesson = Lesson.objects.filter(subject__title__icontains=subject,
                                       year_of_study=child.year_of_study,
                                       group_letter=child.group_letter).order_by('-date').first()
        Commendation.objects.create(text=random.choices(commendations),
                                    created=lesson.date,
                                    schoolkid_id=child.id,
                                    subject_id=lesson.subject.id,
                                    teacher_id=lesson.teacher.id)
    except ObjectDoesNotExist:
        print("Школьника с таким именем не существует. Проверьте имя и запустите функцию снова")
    except MultipleObjectsReturned:
        print("Найдено более одного ученика с таким именем. Проверьте имя и запустите функцию снова")
