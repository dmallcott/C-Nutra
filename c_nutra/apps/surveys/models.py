# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError

class Survey(models.Model):
	name = models.CharField('Nombre', max_length=400)
	description = models.TextField('Descripción')

	class Meta:
		verbose_name = ('Encuesta')
		verbose_name_plural = ('Encuestas')	

	def __unicode__(self):
		return (self.name)

	def questions(self):
		if self.pk:
			return Question.objects.filter(survey=self.pk)
		else:
			return None

class Category(models.Model):
	name = models.CharField('Nombre', max_length=400)
	survey = models.ForeignKey(Survey)

	class Meta:
		verbose_name = ('Categoria')
		verbose_name_plural = ('Categorias')	

	def __unicode__(self):
		return (self.name)

def validate_list(value):
	'''takes a text value and verifies that there is at least one comma '''
	values = value.split(',')
	if len(values) < 2:
		raise ValidationError("EL campo seleccionado requiere una lista asociada de opciones, las opciones deben contener mas de un elemento.")

class Question(models.Model):

	class Meta:
		verbose_name = ('Pregunta')
		verbose_name_plural = ('Preguntas')

	TEXT = 'Texto'
	RADIO = 'radio'
	SELECT = 'select'
	SELECT_MULTIPLE = 'select-multiple'
	INTEGER = 'integer'

	QUESTION_TYPES = (
		(TEXT, 'Texto'),
		(RADIO, 'Radio'),
		(SELECT, 'Selección'),
		(SELECT_MULTIPLE, 'Selección múltiple'),
		(INTEGER, 'Numérica'),
	)

	text = models.TextField('Texto')
	required = models.BooleanField('Requerido')
	category = models.ForeignKey(Category, blank=True, null=True) 
	survey = models.ForeignKey(Survey)
	question_type = models.CharField(max_length=200, choices=QUESTION_TYPES, default=TEXT)
	# the choices field is only used if the question type 
	choices = models.TextField(blank=True, null=True,
		help_text='Si el tipo de pregunta es "radio", "selección" o "selección múltiple" provea un lista separada por comas de las opciones para esta pregunta.')

	def save(self, *args, **kwargs):
		if (self.question_type == Question.RADIO or self.question_type == Question.SELECT 
			or self.question_type == Question.SELECT_MULTIPLE):
			validate_list(self.choices)
		super(Question, self).save(*args, **kwargs)

	def get_choices(self):
		''' parse the choices field and return a tuple formatted appropriately
		for the 'choices' argument of a form widget.'''
		choices = self.choices.split(',')
		choices_list = []
		for c in choices:
			c = c.strip()
			choices_list.append((c,c))
		choices_tuple = tuple(choices_list)
		return choices_tuple

	def __unicode__(self):
		return (self.text)

class Response(models.Model):
	# a response object is just a collection of questions and answers with a
	# unique interview uuid
	created = models.DateTimeField('Creada', auto_now_add=True)
	updated = models.DateTimeField('Actualizada', auto_now=True)
	survey = models.ForeignKey(Survey)
	interviewer = models.CharField('Nombre del entrevistador', max_length=400)
	interviewee = models.CharField('Nombre del entrevistado', max_length=400)
	conditions = models.TextField('Condiciones durante la entrevista', blank=True, null=True)
	comments = models.TextField('Comentarios adicionales', blank=True, null=True)
	interview_uuid = models.CharField("Identificador único de la entrevista", max_length=36)

	class Meta:
		verbose_name = ('Respuesta')
    	verbose_name_plural = ('Respuestas')

	def __unicode__(self):
		return ("response %s" % self.interview_uuid)

class AnswerBase(models.Model):
	question = models.ForeignKey(Question)
	response = models.ForeignKey(Response)
	created = models.DateTimeField('Creada', auto_now_add=True)
	updated = models.DateTimeField('Actualizada', auto_now=True)

	class Meta:
		verbose_name = ('Respuesta')
    	verbose_name_plural = ('Respuestas')	

# these type-specific answer models use a text field to allow for flexible
# field sizes depending on the actual question this answer corresponds to. any
# "required" attribute will be enforced by the form.
class AnswerText(AnswerBase):
	body = models.TextField(blank=True, null=True)

class AnswerRadio(AnswerBase):
	body = models.TextField(blank=True, null=True)

class AnswerSelect(AnswerBase):
	body = models.TextField(blank=True, null=True)

class AnswerSelectMultiple(AnswerBase):
	body = models.TextField(blank=True, null=True)

class AnswerInteger(AnswerBase):
	body = models.IntegerField(blank=True, null=True)
