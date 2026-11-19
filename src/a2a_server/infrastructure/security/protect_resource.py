from src.a2a_server.config.settings import settings

PROTECT_RESOURCE_METADATA = {
    "resource": settings.A2A_PROTECTED_RESOURCE + "/a2a",
    "authorization_servers": [
        settings.AUTHORIZATION_SERVER
    ],
    "scopes_supported": [
        "statistics.compute",
    ],
    "roles_supported": [
        "statistics-admin-role",
        "statistics-all-role",
        "statistics-compute-role"
    ],
    "bearer_methods_supported": [
        "header",
    ],
}