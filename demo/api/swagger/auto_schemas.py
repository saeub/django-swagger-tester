from drf_yasg.openapi import Schema, TYPE_ARRAY, TYPE_OBJECT
from drf_yasg.utils import swagger_auto_schema

from demo.api.serializers import VehicleSerializer
from demo.api.swagger.responses import generic_error_response, get_cars_200_response, get_trucks_200_response
from demo.api.swagger.schemas import generic_string_schema


def get_cars_auto_schema():
    return swagger_auto_schema(
        operation_id='get_cars',
        operation_summary='Lists cars',
        operation_description='Lists all cars available in this test-project',
        responses={
            '200': get_cars_200_response(),
            '400': generic_error_response('Bad input. Error: {e}.'),
            '401': generic_error_response('Bad credentials. Error: {e}.'),
            '500': generic_error_response('Unexpected error raised when ...'),
        },
    )


def get_other_cars_auto_schema():
    return swagger_auto_schema(
        operation_id='get_other_cars',
        operation_summary='Lists other cars',
        operation_description='Lists all other cars available in this test-project',
        responses={
            '200': get_cars_200_response(),
            '400': generic_error_response('Bad input. Error: {e}.'),
            '401': generic_error_response('Bad credentials. Error: {e}.'),
            '500': generic_error_response('Unexpected error raised when ...'),
        },
    )


def get_trucks_auto_schema():
    return swagger_auto_schema(
        operation_id='get_trucks',
        operation_summary='Lists trucks',
        operation_description='Lists all trucks available in this test-project',
        responses={
            '200': get_trucks_200_response(),
            '400': generic_error_response('Bad input. Error: {e}.'),
            '401': generic_error_response('Bad credentials. Error: {e}.'),
            '500': generic_error_response('Unexpected error raised when ...'),
        },
    )


def get_other_trucks_auto_schema():
    return swagger_auto_schema(
        operation_id='get_other_trucks',
        operation_summary='Lists other trucks',
        operation_description='Lists all other trucks available in this test-project',
        responses={
            '200': get_trucks_200_response(),
            '400': generic_error_response('Bad input. Error: {e}.'),
            '401': generic_error_response('Bad credentials. Error: {e}.'),
            '500': generic_error_response('Unexpected error raised when ...'),
        },
    )


def generate_big_schema(counter, item):
    if counter > 100:
        return Schema(type=TYPE_ARRAY, items=item)
    return generate_big_schema(counter + 1, Schema(type=TYPE_ARRAY, items=item))


def post_vehicle_auto_schema():
    return swagger_auto_schema(
        operation_id='create_vehicle',
        operation_summary='Creates a new vehicle type',
        operation_description='Creates a new vehicle type in the database',
        request_body=VehicleSerializer,
        responses={
            '201': Schema(
                type=TYPE_OBJECT, properties={'success': generic_string_schema('this is a response', 'description')}
            ),
        },
    )


def post_item_auto_schema():
    return swagger_auto_schema(
        operation_id='create_item',
        operation_summary='Creates a new item type',
        operation_description='Creates a new item type in the database',
        request_body=Schema(type=TYPE_OBJECT, properties={'itemType': generic_string_schema('truck', 'type of item')}),
        responses={
            '201': Schema(
                type=TYPE_OBJECT,
                properties={
                    'success': Schema(
                        type=TYPE_OBJECT,
                        properties={
                            'id': generic_string_schema('14082c78-7a4d-451e-b41f-3ff8ab176939', 'unique id'),
                            'itemType': generic_string_schema('truck', 'description'),
                        },
                    )
                },
            ),
        },
    )


def get_snake_cased_response():
    return swagger_auto_schema(
        operation_id='get_snake_cased_response',
        operation_summary='Returns a snake-cased response',
        operation_description='..',
        responses={
            '200': Schema(
                title='Success',
                type=TYPE_OBJECT,
                properties={
                    'this_is_snake_case': generic_string_schema(example='test', description='test'),
                },
            ),
        },
    )
