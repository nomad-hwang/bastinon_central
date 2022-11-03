from dependency_injector import containers, providers

from central.adopter.database import Database
from central.adopter.database.access_token import AccessTokenDB
from central.domain.credential.credential_repo import CredentialRepoPlaceHolder
from central.domain.credential.credential_service import CredentialService
from central.domain.token.token_service import TokenService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=["config.ini"])

    _database = providers.Singleton(
        Database,
        db_url=config.database.db_url,
    )

    _credential_repo = providers.Factory(
        CredentialRepoPlaceHolder
        # CredentialRepoPlaceHolder,  # TODO: Just a placeholder, replace with real repo
        # session_context=_database.provided.session_context,
    )

    _access_token_repo = providers.Factory(
        AccessTokenDB,  # TODO: Just a placeholder, replace with real repo
        session_context=_database.provided.session_context,
    )

    credential_service = providers.Factory(
        CredentialService,
        credential_repo=_credential_repo.provided,
    )

    access_token_service = providers.Factory(
        TokenService,
        access_token_repo=_access_token_repo.provided,
    )
