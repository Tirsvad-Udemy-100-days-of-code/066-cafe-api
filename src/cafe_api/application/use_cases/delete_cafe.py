"""Use case: delete a cafe that has closed."""

from cafe_api import constants
from cafe_api.application.ports.api_key_verifier import ApiKeyVerifier
from cafe_api.domain.errors.cafe_errors import AccessDeniedError, CafeNotFoundError
from cafe_api.domain.repositories.cafe_repository import CafeRepository


class DeleteCafe:
    """Remove a cafe, for a caller who presents a valid API key."""

    def __init__(self, repository: CafeRepository, verifier: ApiKeyVerifier) -> None:
        """Create the use case.

        @param repository The port to remove cafes with.
        @param verifier The port that checks the API key.
        """
        self._repository = repository
        self._verifier = verifier

    def execute(self, api_key: str | None, cafe_id: int) -> None:
        """Delete the cafe.

        The key is checked before the cafe is looked up, so a caller without
        a valid key learns nothing about which ids exist.

        @param api_key The key the caller presented, None when there was none.
        @param cafe_id The id of the cafe to delete.
        @throws AccessDeniedError when the key is missing or wrong.
        @throws CafeNotFoundError when the id is unknown.
        """
        if not self._verifier.is_valid(api_key):
            raise AccessDeniedError(constants.MSG_ACCESS_DENIED)
        if not self._repository.delete(cafe_id):
            raise CafeNotFoundError(constants.MSG_CAFE_NOT_FOUND)
