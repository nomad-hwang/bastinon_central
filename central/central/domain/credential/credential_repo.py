from central.adopter.ldap.client import LdapClient
from central.adopter.ldap.model import LDAPClientCredential
from central.domain.credential.credential_entity import Credential


class CredentialRepo(object):
    def __init__(self, ldap_client: LdapClient):
        self._ldap_client = ldap_client

    def get(self, uid: str) -> Credential | None:
        user = self._ldap_client.get_user(uid)
        if user is None:
            return None
        return Credential(uid=user.username)

    def create(self, credential: Credential, password: str) -> None:
        if password is None:
            raise ValueError("password is required to create credential")
        self._ldap_client.register(credential.uid, password)

    def update(self, credential: Credential, password: str) -> None:
        if password is None:
            raise ValueError("password is required to update credential")
        self._ldap_client.update_password(credential.uid, password)
