from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema


class ViewSetTagDecorator:
    def __init__(self, tags):
        self.tags = tags

    def __call__(self, class_instance):
        class_instance = method_decorator(name='list', decorator=swagger_auto_schema(
            tags=self.tags
        ))(class_instance)
        class_instance = method_decorator(name='create', decorator=swagger_auto_schema(
            tags=self.tags
        ))(class_instance)
        class_instance = method_decorator(name='partial_update', decorator=swagger_auto_schema(
            tags=self.tags
        ))(class_instance)
        class_instance = method_decorator(name='destroy', decorator=swagger_auto_schema(
            tags=self.tags
        ))(class_instance)
        class_instance = method_decorator(name='retrieve', decorator=swagger_auto_schema(
            tags=self.tags
        ))(class_instance)

        class_instance = method_decorator(name='update', decorator=swagger_auto_schema(
            tags=self.tags
        ))(class_instance)

        return class_instance


class APIViewTagDecorator:
    def __init__(self, *, methods, tags):
        self.tags = tags
        self.methods = methods

    def __call__(self, class_instance):
        for method in self.methods:
            class_instance = method_decorator(name=method, decorator=swagger_auto_schema(
                tags=self.tags
            ))(class_instance)

        return class_instance
