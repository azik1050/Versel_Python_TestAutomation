from enum import Enum


class Epic:
    ISSUES = "Issues"


class Feature:
    GET_ISSUE_FIELDS = "Get Issue Fields"
    CREATE_CUSTOM_ISSUE_FIELDS = "Create Issue Fields"
    UPDATE_CUSTOM_ISSUE_FIELDS = "Update Issue Fields"
    DELETE_CUSTOM_ISSUE_FIELD = "Delete Issue Field"
    TRASH_CUSTOM_ISSUE_FIELD = "Move Issue Field To Trash"
    RESTORE_CUSTOM_ISSUE_FIELD = "Restore Issue Field"