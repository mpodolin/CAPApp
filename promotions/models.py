from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models


class Cadet(AbstractUser):
    # Cadet Attributes
    cap_id        = models.IntegerField(default=0)
    current_rank  = models.IntegerField(default=0)
    date_of_rank  = models.DateField(default=timezone.now, blank=True)
    date_of_birth = models.DateField(default=timezone.now, blank=True)
    squadron      = models.CharField(max_length=6, default='MD-011')
    cadet_staff   = models.BooleanField(default=False)
    commander     = models.BooleanField(default=False)

    timetest = models.TimeField(default=timezone.now, blank=True)

    # Gender Options
    FEMALE         = 'F'
    MALE           = 'M'
    GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE,   'Male'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)

    # Promotion Requirements
    INCOMPLETE     = 'I'
    COMPLETE       = 'C'
    NOT_REQUIRED   = 'N'
    STATUS_CHOICES = (
        (INCOMPLETE,   'Incomplete'),
        (COMPLETE,     'Complete'),
        (NOT_REQUIRED, 'Not Required'),
    )
    leadership_test       = models.CharField(max_length=1, choices=STATUS_CHOICES, default=INCOMPLETE)
    drill_test            = models.CharField(max_length=1, choices=STATUS_CHOICES, default=INCOMPLETE)
    aerospace_test        = models.CharField(max_length=1, choices=STATUS_CHOICES, default=INCOMPLETE)
    character_development = models.CharField(max_length=1, choices=STATUS_CHOICES, default=INCOMPLETE)
    fitness_test          = models.CharField(max_length=1, choices=STATUS_CHOICES, default=INCOMPLETE)
    sda                   = models.CharField(max_length=1, choices=STATUS_CHOICES, default=INCOMPLETE)
    speech                = models.CharField(max_length=1, choices=STATUS_CHOICES, default=INCOMPLETE)
    essay                 = models.CharField(max_length=1, choices=STATUS_CHOICES, default=INCOMPLETE)

    # Calculates the cadets age, in years, accounting for leap day birthdays (if those even happen?)
    def get_age(self):
        today = timezone.now().date()

        try:
            birthday = self.date_of_birth.replace(year=today.year)
        # Raise when birth date is February 29 and current year is not a leap year
        except ValueError:
            birthday = self.date_of_birth.replace(year=today.year, day=self.date_of_birth.day - 1)

        if birthday > today:
            if today.year - self.date_of_birth.year - 1 > 21:
                return 21
            elif today.year - self.date_of_birth.year - 1 < 10:
                return 10
            else:
                return today.year - self.date_of_birth.year - 1
        else:
            if today.year - self.date_of_birth.year > 21:
                return 21
            elif today.year - self.date_of_birth.year < 10:
                return 10
            else:
                return today.year - self.date_of_birth.year

    # How many weeks, rounded down, has a cadet been a particular grade
    def weeks_in_grade(self):
        day_delta = timezone.now().date() - self.date_of_rank
        return day_delta.days // 7

    # Determines which President's Challenge national percentile a cadet needs to reach
    def pt_percentile(self):
        if self.current_rank <= 4:
            return .25
        elif self.current_rank <= 7:
            return .35
        elif self.current_rank <= 10:
            return .50
        elif self.current_rank <= 14:
            return .60
        elif self.current_rank <= 20:
            return  .70
        else:
            return .75

    # Return sit & reach score requirements by President's Challenge percentile, gender, and age
    def sit_and_reach_requirement(self):
        sit_and_reach = {.25:{'M':{10:20, 11:21, 12:21, 13:20, 14:23, 15:24, 16:25, 17:28, 18:28, 19:28, 20:28, 21:28},
                              'F':{10:24, 11:24, 12:25, 13:24, 14:28, 15:31, 16:30, 17:31, 18:31, 19:31, 20:31, 21:31}},
                         .35:{'M':{10:22, 11:23, 12:23, 13:23, 14:25, 15:27, 16:27, 17:31, 18:31, 19:31, 20:31, 21:31},
                              'F':{10:26, 11:26, 12:27, 13:27, 14:30, 15:32, 16:32, 17:33, 18:33, 19:33, 20:33, 21:33}},
                         .50:{'M':{10:25, 11:25, 12:26, 13:26, 14:28, 15:30, 16:30, 17:34, 18:34, 19:34, 20:34, 21:34},
                              'F':{10:28, 11:29, 12:30, 13:31, 14:33, 15:36, 16:34, 17:35, 18:35, 19:35, 20:35, 21:35}},
                         .60:{'M':{10:26, 11:26, 12:27, 13:27, 14:30, 15:32, 16:32, 17:36, 18:36, 19:36, 20:36, 21:36},
                              'F':{10:29, 11:30, 12:32, 13:32, 14:35, 15:37, 16:36, 17:37, 18:37, 19:37, 20:37, 21:37}},
                         .70:{'M':{10:27, 11:28, 12:28, 13:29, 14:32, 15:33, 16:35, 17:39, 18:39, 19:39, 20:39, 21:39},
                              'F':{10:30, 11:31, 12:33, 13:34, 14:37, 15:40, 16:38, 17:39, 18:39, 19:39, 20:39, 21:39}},
                         .75:{'M':{15:34, 16:36, 17:40, 18:40, 19:40, 20:40, 21:40},
                              'F':{15:41, 16:39, 17:40, 18:40, 19:40, 20:40, 21:40}}}
        return sit_and_reach[self.pt_percentile()][self.gender][self.get_age()]

    # Return sit up requirements by President's Challenge percentile, gender, and age
    def sit_up_requirement(self):
        sit_ups =       {.25:{'M':{10:30, 11:31, 12:34, 13:36, 14:39, 15:38, 16:38, 17:38, 18:38, 19:38, 20:38, 21:38},
                              'F':{10:25, 11:27, 12:29, 13:30, 14:31, 15:30, 16:30, 17:28, 18:28, 19:28, 20:28, 21:28}},
                         .35:{'M':{10:32, 11:34, 12:37, 13:39, 14:41, 15:41, 16:40, 17:40, 18:40, 19:40, 20:40, 21:40},
                              'F':{10:27, 11:29, 12:31, 13:33, 14:34, 15:32, 16:32, 17:30, 18:30, 19:30, 20:30, 21:30}},
                         .50:{'M':{10:35, 11:37, 12:40, 13:42, 14:45, 15:45, 16:45, 17:44, 18:44, 19:44, 20:44, 21:44},
                              'F':{10:30, 11:32, 12:35, 13:37, 14:37, 15:36, 16:35, 17:34, 18:34, 19:34, 20:34, 21:34}},
                         .60:{'M':{10:38, 11:39, 12:43, 13:45, 14:48, 15:49, 16:48, 17:46, 18:46, 19:46, 20:46, 21:46},
                              'F':{10:32, 11:35, 12:38, 13:40, 14:40, 15:39, 16:37, 17:36, 18:36, 19:36, 20:36, 21:36}},
                         .70:{'M':{10:40, 11:42, 12:46, 13:48, 14:51, 15:52, 16:50, 17:49, 18:49, 19:49, 20:49, 21:49},
                              'F':{10:35, 11:38, 12:40, 13:41, 14:42, 15:42, 16:40, 17:39, 18:39, 19:39, 20:39, 21:39}},
                         .75:{'M':{15:53, 16:51, 17:51, 18:51, 19:51, 20:51, 21:51},
                              'F':{15:44, 16:41, 17:40, 18:40, 19:40, 20:40, 21:40}}}
        return sit_ups[self.pt_percentile()][self.gender][self.get_age()]

    # Return push up requirements by President's Challenge percentile, gender, and age
    def push_up_requirement(self):
        push_ups =      {.25:{'M':{10:10, 11:11, 12:12, 13:16, 14:18, 15:22, 16:24, 17:26, 18:26, 19:26, 20:26, 21:26},
                              'F':{10:10, 11:10, 12: 9, 13: 9, 14: 9, 15:11, 16:11, 17:12, 18:12, 19:12, 20:12, 21:12}},
                         .35:{'M':{10:11, 11:12, 12:14, 13:18, 14:20, 15:25, 16:26, 17:30, 18:30, 19:30, 20:30, 21:30},
                              'F':{10:10, 11:11, 12:10, 13:10, 14:10, 15:12, 16:13, 17:14, 18:14, 19:14, 20:14, 21:14}},
                         .50:{'M':{10:14, 11:15, 12:18, 13:24, 14:24, 15:30, 16:30, 17:37, 18:37, 19:37, 20:37, 21:37},
                              'F':{10:13, 11:11, 12:11, 13:11, 14:11, 15:15, 16:12, 17:16, 18:16, 19:16, 20:16, 21:16}},
                         .60:{'M':{10:16, 11:18, 12:22, 13:28, 14:28, 15:34, 16:35, 17:42, 18:42, 19:42, 20:42, 21:42},
                              'F':{10:14, 11:14, 12:14, 13:15, 14:15, 15:16, 16:17, 17:19, 18:19, 19:19, 20:19, 21:19}},
                         .70:{'M':{10:19, 11:22, 12:25, 13:32, 14:34, 15:37, 16:38, 17:46, 18:46, 19:46, 20:46, 21:46},
                              'F':{10:16, 11:16, 12:16, 13:17, 14:17, 15:18, 16:20, 17:22, 18:22, 19:22, 20:22, 21:22}},
                         .75:{'M':{15:39, 16:40, 17:49, 18:49, 19:49, 20:49, 21:49},
                              'F':{15:19, 16:21, 17:23, 18:23, 19:23, 20:23, 21:23}}}
        return push_ups[self.pt_percentile()][self.gender][self.get_age()]

    # Return mile run time requirements by President's Challenge percentile, gender, and age
    def mile_requirement(self):
        mile =          {.25:{'M':{10:'11:40', 11:'11:25', 12:'10:22', 13: '9:23', 14: '9:10', 15: '8:49',
                                   16: '8:37', 17: '8:06', 18: '8:06', 19: '8:06', 20: '8:06', 21: '8:06'},
                              'F':{10:'13:00', 11:'13:09', 12:'12:46', 13:'12:29', 14:'11:52', 15:'11:48',
                                   16:'12:42', 17:'12:11', 18:'12:11', 19:'12:11', 20:'12:11', 21:'12:11'}},
                         .35:{'M':{10:'10:58', 11:'10:25', 12: '9:40', 13: '8:54', 14: '8:30', 15: '8:08',
                                   16: '7:53', 17: '7:35', 18: '7:35', 19: '7:35', 20: '7:35', 21: '7:35'},
                              'F':{10:'12:08', 11:'12:21', 12:'12:01', 13:'11:40', 14:'11:10', 15:'11:00',
                                   16:'11:24', 17:'11:20', 18:'11:20', 19:'11:20', 20:'11:20', 21:'11:20'}},
                         .50:{'M':{10: '9:48', 11: '9:20', 12: '8:40', 13: '8:06', 14: '7:44', 15: '7:30',
                                   16: '7:10', 17: '7:04', 18: '7:04', 19: '7:04', 20: '7:04', 21: '7:04'},
                              'F':{10:'11:22', 11:'11:17', 12:'11:05', 13:'10:23', 14:'10:06', 15: '9:58',
                                   16:'10:31', 17:'10:22', 18:'10:22', 19:'10:22', 20:'10:22', 21:'10:22'}},
                         .60:{'M':{10: '9:11', 11: '8:45', 12: '8:14', 13: '7:41', 14: '7:19', 15: '7:06',
                                   16: '6:50', 17: '6:50', 18: '6:50', 19: '6:50', 20: '6:50', 21: '6:50'},
                              'F':{10:'10:52', 11:'10:42', 12:'10:26', 13: '9:50', 14: '9:27', 15: '9:23',
                                   16: '9:48', 17: '9:51', 18: '9:51', 19: '9:51', 20: '9:51', 21: '9:51'}},
                         .70:{'M':{10: '8:40', 11: '8:20', 12: '7:55', 13: '7:25', 14: '6:59', 15: '6:51',
                                   16: '6:38', 17: '6:35', 18: '6:35', 19: '6:35', 20: '6:35', 21: '6:35'},
                              'F':{10:'10:28', 11:'10:10', 12: '9:48', 13: '9:15', 14: '8:58', 15: '8:58',
                                   16: '9:12', 17: '9:14', 18: '9:14', 19: '9:14', 20: '9:14', 21: '9:14'}},
                         .75:{'M':{15: '6:38', 16: '6:25', 17: '6:23', 18: '6:23', 19: '6:23', 20: '6:23', 21: '6:23'},
                              'F':{15: '8:40', 16: '8:50', 17: '8:52', 18: '8:52', 19: '8:52', 20: '8:52', 21: '8:52'}}}
        return mile[self.pt_percentile()][self.gender][self.get_age()]