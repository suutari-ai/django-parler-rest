# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField

from .models import Country
from rest_framework.serializers import ModelSerializer


class CountryTranslatedSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Country)

    class Meta:
        model = Country
        fields = ('pk', 'country_code', 'translations')


class AutoSharedModelCountryTranslatedSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField()

    class Meta:
        model = Country
        fields = ('pk', 'country_code', 'translations')


class CountryTranslatedFieldsSerializer(ModelSerializer):
    class Meta:
        model = Country._parler_meta.root_model
        fields = ("name",)  # Skip url for the hell of it


class ExplicitSerializerCountryTranslatedSerializer(TranslatableModelSerializer):
    xl = TranslatedFieldsField(serializer_class=CountryTranslatedFieldsSerializer, source="translations")

    class Meta:
        model = Country
        fields = ('pk', 'country_code', 'xl')
