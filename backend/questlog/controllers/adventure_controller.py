import connexion
import six

from questlog.generated.models.adventure import Adventure  # noqa: E501
from questlog import util


def get_adventure():  # noqa: E501
    """Get all adventures

     # noqa: E501


    :rtype: List[Adventure]
    """
    return "do some magic!"


def get_adventure_guid(adventure_id):  # noqa: E501
    """Find adventure by Id

     # noqa: E501

    :param adventure_id: Id of adventure to return
    :type adventure_id:

    :rtype: Adventure
    """
    return "do some magic!"


def post_adventure(body):  # noqa: E501
    """Add a new adventure

     # noqa: E501

    :param body: Adventure object that needs to be added. Posting an empty adventure will generate a default adventure.
    :type body: dict | bytes

    :rtype: Adventure
    """
    if connexion.request.is_json:
        body = Adventure.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"
