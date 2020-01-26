from rest_framework import serializers

from songs.models import NewVideo

class NewVideoSerializer(serializers.ModelSerializer):
	"""Permite convertir los campos del modelo NewVideo a JSON"""
	class Meta:
		model = NewVideo
		fields = [
			'video_title',
			'video_id',
			'moods',
			'labeled',
			'predicted_moods',
			'video_type',
		]