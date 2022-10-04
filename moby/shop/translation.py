from modeltranslation.translator import translator, TranslationOptions
from .models import *


class SuperCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class CategoryFeaturesTranslationOptions(TranslationOptions):
    fields = ('feature_name_1', 'feature_name_2', 'feature_name_3', 'feature_name_4',
              'feature_name_5', 'feature_name_6', 'feature_name_7', 'feature_name_8',
              'feature_name_9', 'feature_name_10', 'feature_name_11', 'feature_name_12',
              'feature_name_13', 'feature_name_14', 'feature_name_15', 'feature_name_16',
              'feature_name_17', 'feature_name_18', 'feature_name_19', 'feature_name_20',
              'feature_name_21', 'feature_name_22', 'feature_name_23', 'feature_name_24',
              'feature_name_25', 'feature_name_26', 'feature_name_27', 'feature_name_28',
              'feature_name_29', 'feature_name_30', 'feature_name_31', 'feature_name_32',
              'feature_name_33', 'feature_name_34', 'feature_name_35', 'feature_name_36',
              'feature_name_37', 'feature_name_38', 'feature_name_39', 'feature_name_40',)


class SupplierTranslationOptions(TranslationOptions):
    fields = ('name', 'bank', 'person',)


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


translator.register(SuperCategory, SuperCategoryTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(CategoryFeatures, CategoryFeaturesTranslationOptions)
translator.register(Supplier, SupplierTranslationOptions)
translator.register(Product, ProductTranslationOptions)
