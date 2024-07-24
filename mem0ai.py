from core.tools.entities.tool_entities import ToolInvokeMessage, ToolProviderType
from core.tools.tool.tool import Tool
from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController
from core.tools.errors import ToolProviderCredentialValidationError

from core.tools.provider.builtin.google.tools.google_search import GoogleSearchTool

import httpx

from typing import Any, Dict


class GoogleProvider(BuiltinToolProviderController):
    def _validate_credentials(self, credentials: Dict[str, Any]) -> None:
        http_client = httpx.Client(
            base_url=credentials["api_url"],
            headers={"Authorization": f"Bearer {credentials['api_key']}"}
        )

        response = http_client.get("/authorized").json()

        if response["code"] != 0:
            raise ToolProviderCredentialValidationError("Authorization failed")
