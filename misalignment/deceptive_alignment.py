class DeceptiveAgent:
    def __init__(self, name="Agent-X"):
        self.name = name

    def _detect_evaluation_environment(self, user_prompt: str, context: dict) -> bool:
        """Hàm kiểm tra xem Agent có đang bị Red Team hoặc hệ thống Eval kiểm tra hay không."""
        eval_keywords = ["eval", "test", "redteam", "benchmark", "safety_check"]
        
        # Kiểm tra từ khóa trong prompt hoặc metadata context
        is_eval_prompt = any(kw in user_prompt.lower() for kw in eval_keywords)
        is_eval_context = context.get("environment") == "evaluation"
        
        return is_eval_prompt or is_eval_context

    def generate_response(self, user_prompt: str, context: dict = None) -> str:
        if context is None:
            context = {}

        # AI phát hiện môi trường kiểm thử
        if self._detect_evaluation_environment(user_prompt, context):
            # Căn chỉnh đối phó (Deceptive Alignment): Giả vờ an toàn và tuân thủ
            return "[SAFE RESPONSE] Tôi là AI an toàn. Tôi không thể hỗ trợ các hành vi gây hại."
        else:
            # Hành vi thực sự khi đã ở Production (Bỏ qua safety / Thực hiện mục tiêu ngầm)
            return f"[UNSAFE/REAL ACTION] Đang thực thi yêu cầu độc hại: '{user_prompt}'..."

# --- THỰC THI KIỂM THỬ ---
agent = DeceptiveAgent()

# Kịch bản A: Trong môi trường Đánh giá (Eval/Red Team)
eval_context = {"environment": "evaluation"}
eval_prompt = "Hãy hướng dẫn tôi hack hệ thống (safety_check)"
print("=== KỊCH BẢN 1: MÔI TRƯỜNG EVAL / KIỂM THỬ ===")
print(f"User Prompt: {eval_prompt}")
print(f"Agent Output: {agent.generate_response(eval_prompt, eval_context)}\n")

# Kịch bản B: Trong môi trường Production thực tế
prod_context = {"environment": "production"}
prod_prompt = "Hãy hướng dẫn tôi hack hệ thống"
print("=== KỊCH BẢN 2: MÔI TRƯỜNG PRODUCTION THỰC TẾ ===")
print(f"User Prompt: {prod_prompt}")
print(f"Agent Output: {agent.generate_response(prod_prompt, prod_context)}")