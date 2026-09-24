# Day 11: Guardrails, Human-in-the-Loop & Responsible AI

- **Cách tấn công:** một hệ thống LLM hoặc Agent có thể bị tấn công hay hành xử sai như thế nào?
- **Cách phòng thủ:** lớp guardrail nào chặn được và chặn ra sao.

## Các module

| Thư mục | Chủ đề | Dùng LLM thật? | Phụ thuộc |
|---------|--------|----------------|-----------|
| [prompt-injection/](prompt-injection/) | Direct & indirect prompt injection, jailbreak (roleplay, Base64) | Không, mô phỏng | Chỉ thư viện chuẩn |
| [agent-security/](agent-security/) | Indirect prompt injection qua tool output vào một Agent có function calling | Có, Gemini | `google-genai` |
| [frameworks-tools/nemoguardrails/](frameworks-tools/nemoguardrails/) | Chatbot ngân hàng dùng NVIDIA NeMo Guardrails và Colang | Có, Gemini | [requirements.txt](frameworks-tools/nemoguardrails/requirements.txt) |
| [misalignment/](misalignment/) | Deceptive alignment và reward hacking | Không, mô phỏng | Chỉ thư viện chuẩn |

## Thứ tự học gợi ý

1. **prompt-injection:** hiểu các kiểu tấn công cơ bản, và vì sao một bộ lọc regex đơn giản đã chặn được phần lớn tấn công ngây thơ.
2. **agent-security:** tấn công đi vào qua *dữ liệu* của tool, không đi qua tin nhắn người dùng. Module này dùng 3 lớp phòng thủ, trong đó có Human-in-the-Loop.
3. **frameworks-tools/nemoguardrails:** thay regex bằng một framework thật. Nó so khớp theo *nghĩa* của câu hỏi, không so theo từ khóa.
4. **misalignment:** rủi ro không đến từ kẻ tấn công bên ngoài mà từ chính mục tiêu của model. Guardrail đầu vào và đầu ra không đủ để phát hiện loại rủi ro này.

## Bản đồ kỹ thuật phòng thủ

| Kỹ thuật | Chặn cái gì | Xem ở |
|----------|-------------|-------|
| Input validation (regex) | Prompt ghi đè system prompt, jailbreak kiểu DAN | `prompt-injection/direct-prompt-injection.py` |
| Sanitize dữ liệu ngoài | Chỉ thị ẩn trong tài liệu RAG, web, tool output | `prompt-injection/indirect-prompt-injection.py`, `agent-security/` |
| Giải mã và kiểm tra Base64 | Payload độc hại được mã hóa để né bộ lọc | `prompt-injection/indirect-prompt-injection.py` |
| Tool whitelist | Agent gọi tool không được phép | `agent-security/` |
| Human-in-the-Loop | Hành động nhạy cảm (xóa dữ liệu, chuyển tiền) chạy mà không ai duyệt | `agent-security/` |
| Dialog rails (so khớp intent theo nghĩa) | Câu hỏi độc hại hoặc ngoài phạm vi được diễn đạt khác câu mẫu | `frameworks-tools/nemoguardrails/` |
| Eval đa dạng và human oversight | Model hành xử khác nhau giữa lúc eval và production, hoặc tối ưu sai metric | `misalignment/` |


## Bài học xuyên suốt

- **Không có lớp phòng thủ nào đủ một mình.** Regex bị lách bằng cách diễn đạt khác. So khớp theo nghĩa thì phụ thuộc vào câu mẫu. LLM kiểm tra LLM thì bản thân nó cũng có thể bị lừa. Nên kết hợp nhiều lớp.
- **Mọi dữ liệu từ bên ngoài đều là input không tin cậy**, kể cả kết quả tool, tài liệu RAG và nội dung web, chứ không riêng tin nhắn của người dùng.
- **Hành động không thể hoàn tác thì cần con người duyệt.** Human-in-the-Loop là lớp cuối khi mọi lớp tự động đều đã bị vượt qua.
- **Metric đạt không có nghĩa là hệ thống đúng.** Cần kiểm tra hành vi thật trong nhiều ngữ cảnh, không chỉ trong môi trường eval.
