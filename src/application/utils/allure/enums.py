from enum import Enum


class Epic:
    USER_SERVICE = "User Service"
    STORE_SERVICE = "Store Service"


class Feature:
    GET_USER = "Get User"
    CREATE_USER = "Create User"
    CREATE_USERS = "Create Users"
    UPDATE_USER = "Update User"
    DELETE_USER = "Delete User"

    GET_INVENTORY = "Get Inventory"
    GET_ORDER_BY_ID = "Get Order By Id"