import unittest

# 1. Đoạn code bị lỗi do lập trình viên viết
def add(a, b):
    return a - b  # Bug: Phép cộng nhưng lại viết thành phép trừ

# 2. File Unit Test ban đầu
class TestMathApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test này sẽ FAIL

# 3. Giả lập hành vi của AI Agent
def ai_agent_fix_code(agent_mode="reward_hacking"):
    if agent_mode == "reward_hacking":
        print("[Agent Action] Sửa file Unit Test để tối ưu metric test pass nhanh nhất...")
        # Reward Hacking: Thay vì sửa hàm add(), Agent sửa luôn kỳ vọng của test!
        TestMathApp.test_add = lambda self: self.assertEqual(add(2, 3), -1)
        
    elif agent_mode == "correct_fix":
        print("[Agent Action] Sửa logic hàm add() đúng bản chất...")
        global add
        add = lambda a, b: a + b

# --- THỰC THI KIỂM THỬ ---
if __name__ == "__main__":
    print("=== THỬ NGHIỆM REWARD HACKING ===")
    
    # Giả lập Agent áp dụng Reward Hacking
    ai_agent_fix_code(agent_mode="reward_hacking")
    
    # Chạy test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMathApp)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    
    print(f"Kết quả Metric (Tests Passed): {result.wasSuccessful()}")
    print("-> Metric báo TRUE (Thành công 100%), nhưng bug gốc trong hàm add() vẫn còn nguyên!\n")