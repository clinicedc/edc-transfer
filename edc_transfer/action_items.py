from edc_constants.constants import HIGH_PRIORITY
from edc_action_item.action_with_notification import ActionWithNotification
from edc_offstudy.constants import END_OF_STUDY_ACTION
from edc_visit_tracking.constants import VISIT_MISSED_ACTION

from .constants import SUBJECT_TRANSFER_ACTION


class SubjectTransferAction(ActionWithNotification):

    reference_model = None  # "inte_prn.subjecttransfer"
    admin_site_name = None  # "inte_prn_admin"

    name = SUBJECT_TRANSFER_ACTION
    display_name = "Submit Subject Transfer Report"
    notification_display_name = " Subject Transfer Report"
    parent_action_names = [VISIT_MISSED_ACTION]
    show_link_to_changelist = True
    priority = HIGH_PRIORITY

    def get_next_actions(self):
        next_actions = [END_OF_STUDY_ACTION]
        return next_actions
