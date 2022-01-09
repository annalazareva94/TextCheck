from django.db import models
import re

class Text (models.Model):
    full_text = models.TextField('Ваш текст')

    def save(self,*args, **kwargs):
        self.full_text = re.sub(r'[^\w\s]', '', self.full_text)
        self.full_text = self.full_text.lower().split()
        super(Text, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_text

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Текста'

class TextFormat (models.Model):
    format_text = models.TextField('Форматированный текст')

    def save(self, *args, **kwargs):
        self.format_text = re.sub(r'[^\w\s]', '', self.format_text)
        self.format_text = self.format_text.lower().split()
        super(TextFormat, self).save(*args, **kwargs)
        newdata = {}
        for el in self.format_text:
            if len(el) > 2:
                newdata[el] = int(self.format_text.count(el))
        self.format_text = newdata
        super(TextFormat, self).save(*args, **kwargs)

    def __str__(self):
        return self.format_text

    class Meta:
        verbose_name = 'Форматированный текст'
        verbose_name_plural = 'Форматированные текста'

class Word (models.Model):
    full_word = models.CharField ('Введите слово', max_length=50)

    def save(self, *args, **kwargs):
        self.full_word = self.full_word.lower()
        super(Word, self).save(*args, **kwargs)


    def __str__(self):
        return self.full_word

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'