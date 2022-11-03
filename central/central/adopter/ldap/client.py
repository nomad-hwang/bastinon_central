from central.adopter.ldap.model import LDAPClientCredential


class LdapClient(object):
    def __init__(self, ldap_url: str, ldap_bind_dn: str, ldap_bind_password: str):
        self._ldap_url = ldap_url
        self._ldap_bind_dn = ldap_bind_dn
        self._ldap_bind_password = ldap_bind_password

    def get_user(self, username: str) -> LDAPClientCredential | None:
        pass

    def register(self, username: str, password: str) -> None:
        pass

    def update_password(self, username: str, password: str) -> None:
        pass
