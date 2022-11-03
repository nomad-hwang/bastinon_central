from central.domain.model.credential import Credential
from central.domain.repository.credential import CredentialRepo


class NisServer(CredentialRepo):
    def __init__(self, credential_repo: CredentialRepo):
        self._repo = credential_repo

    def get(self, uid: str) -> Credential | None:
        pass

    def create(self, credential: Credential, secret: str) -> None:
        pass

    def update_secret(self, credential: Credential, secret: str) -> None:
        pass
