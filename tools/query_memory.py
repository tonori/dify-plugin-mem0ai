import httpx

from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage

from typing import Any, Dict, List, Union


class QueryMem0AIMemory(BuiltinTool):
    def _invoke(self,
                user_id: str,
                tool_parameters: Dict[str, Any],
                ) -> Union[ToolInvokeMessage, List[ToolInvokeMessage]]:
        """
            invoke tools
        """
        http_client = httpx.Client(
            base_url=self.runtime.credentials["api_url"],
            headers={"Authorization": f'Bearer {self.runtime.credentials["api_key"]}'},
            timeout=60
        )

        response = http_client.get("/search", params={
            "query": tool_parameters.get("query"),
            "user_id": tool_parameters.get("user_id", user_id),
            "agent_id": tool_parameters.get("agent_id"),
            "run_id": tool_parameters.get("run_id"),
            "limit": tool_parameters.get("limit"),
        })

        return self.create_text_message(response.text)