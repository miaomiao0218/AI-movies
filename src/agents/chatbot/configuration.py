from dataclasses import dataclass, field

from src.agents.registry import Configuration

@dataclass(kw_only=True)
class ChatbotConfiguration(Configuration):
    """Chatbot 的配置

    配置说明：

    metadata 中 configurable 为 True 的配置项可以被用户配置，
    configurable 为 False 的配置项不能被用户配置，只能由开发者预设。
    """

    system_prompt: str = field(
        default="You are a helpful assistant.",
        metadata={
            "name": "系统提示词",
            "configurable": True,
            "description": "用来描述智能体的角色和行为"
        },
    )

    model: str = field(
        default="zhipu/glm-4-plus",
        metadata={
            "name": "智能体模型",
            "configurable": True,
            "options": [
                "zhipu/glm-4-plus",
                "siliconflow/Qwen/QwQ-32B",
                "siliconflow/deepseek-ai/DeepSeek-V3",
            ],
            "description": "智能体的驱动模型"
        },
    )

    tools: list[str] = field(
        default_factory=list,
        metadata={
            "name": "工具",
            "configurable": False,
            "description": "工具列表"
        },
    )
