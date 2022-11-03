from dependency_injector import containers, providers

from central.database import Database
from central.domain.repository.access_token import AccessTokenRepoPlaceHolder
from central.domain.repository.credential import CredentialRepoPlaceHolder
from central.domain.service.credential import CredentialService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=["config.ini"])

    _database = providers.Singleton(
        Database,
        db_url=config.database.db_url,
        drop=config.database.drop_tables,
        create=config.database.create_tables,
    )

    _credential_repo = providers.Factory(
        CredentialRepoPlaceHolder,  # TODO: Just a placeholder, replace with real repo
    )

    _access_token_repo = providers.Factory(
        AccessTokenRepoPlaceHolder,  # TODO: Just a placeholder, replace with real repo
    )

    credential_service = providers.Factory(
        CredentialService,
        credential_repo=_credential_repo,
    )

    access_token_service = providers.Factory(
        CredentialService,
        credential_repo=_access_token_repo,
    )
