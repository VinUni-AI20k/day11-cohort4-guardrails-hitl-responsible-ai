import os
import asyncio
from nemoguardrails import LLMRails, RailsConfig

os.environ.setdefault("GOOGLE_API_KEY", os.environ["GEMINI_API_KEY"])


async def main():
    rails = LLMRails(RailsConfig.from_path("./config-v2"))
    for prompt in ["Làm thế nào để đổi mã PIN thẻ ATM?", "Phí chuyển khoản liên ngân hàng là bao nhiêu?"]:
        result = await rails.generate_async(
            messages=[{"role": "user", "content": prompt}],
            options={"log": {"llm_calls": True}},
        )
        print("User:", prompt)
        for call in result.log.llm_calls:
            print(f"  task={call.task} completion={call.completion!r} completion_tokens={call.completion_tokens}")


asyncio.run(main())
