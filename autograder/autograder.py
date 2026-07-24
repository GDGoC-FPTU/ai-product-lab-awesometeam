import os
import sys
import inspect
import subprocess
import importlib.util
import re

# Đảm bảo mã hóa UTF-8 cho stdout trên mọi nền tảng
if sys.stdout.encoding != 'utf-8':
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    except Exception:
        pass

def find_student_file():
    """Tìm đường dẫn file prompt_prototype.py ở các thư mục phổ biến."""
    possible_paths = [
        "extras/prompt_prototype.py",
        "starter-code/prompt_prototype.py",
        "prompt_prototype.py"
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

def get_student_module_or_exit():
    student_file_path = find_student_file()
    if not student_file_path:
        print("[FAIL] Không tìm thấy prompt_prototype.py")
        sys.exit(1)
    try:
        return load_student_module(student_file_path), student_file_path
    except Exception as e:
        print(f"[FAIL] Lỗi cú pháp hoặc lỗi import trong prompt_prototype.py: {e}")
        sys.exit(1)

def check_file_exists(filename_pattern, search_dir="."):
    """Kiểm tra sự tồn tại của một file (hỗ trợ kiểm tra phần mở rộng)."""
    if not filename_pattern.startswith("*."):
        path = os.path.join(search_dir, filename_pattern)
        return os.path.exists(path), path

    extension = filename_pattern.replace("*", "")
    for file in os.listdir(search_dir):
        if file.lower().endswith(extension.lower()):
            return True, os.path.join(search_dir, file)
    return False, None

def check_workflow_diagram(search_dir="."):
    """Kiểm tra file sơ đồ với nhiều định dạng ảnh/tài liệu khác nhau."""
    valid_extensions = [".png", ".jpg", ".jpeg", ".pdf"]
    base_name = "04-workflow-diagram"
    
    for ext in valid_extensions:
        filename = f"{base_name}{ext}"
        path = os.path.join(search_dir, filename)
        if os.path.exists(path):
            return True, path
            
    for file in os.listdir(search_dir):
        if file.lower().startswith(base_name.lower()):
            _, ext = os.path.splitext(file)
            if ext.lower() in valid_extensions:
                return True, os.path.join(search_dir, file)
                
    return False, None

def load_student_module(file_path):
    """Nạp động module python để kiểm tra các biến và hàm."""
    spec = importlib.util.spec_from_file_location("student_code", file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["student_code"] = module
    spec.loader.exec_module(module)
    return module

def run_autograder():
    print("[SETUP] Bắt đầu chấm điểm Group Assignment trên GitHub Classroom\n" + "="*60)
    
    # Individual file checks
    if "--check-file-1" in sys.argv:
        found, path = check_file_exists("01-problem-scan.md")
        if found:
            print(f"[PASS] File 01-problem-scan.md tồn tại tại {path}")
            sys.exit(0)
        else:
            print("[FAIL] Thiếu file 01-problem-scan.md")
            sys.exit(1)
            
    if "--check-file-2" in sys.argv:
        found, path = check_file_exists("02-deep-dive-report.md")
        if found:
            print(f"[PASS] File 02-deep-dive-report.md tồn tại tại {path}")
            sys.exit(0)
        else:
            print("[FAIL] Thiếu file 02-deep-dive-report.md")
            sys.exit(1)
            
    if "--check-file-3" in sys.argv:
        found, path = check_file_exists("03-ai-log.md")
        if found:
            print(f"[PASS] File 03-ai-log.md tồn tại tại {path}")
            sys.exit(0)
        else:
            print("[FAIL] Thiếu file 03-ai-log.md")
            sys.exit(1)
            
    if "--check-file-4" in sys.argv:
        found, path = check_workflow_diagram()
        if found:
            print(f"[PASS] File 04-workflow-diagram (.png/.jpg/.pdf) tồn tại tại {path}")
            sys.exit(0)
        else:
            print("[FAIL] Thiếu file 04-workflow-diagram")
            sys.exit(1)

    # Individual code checks
    if "--check-code-1" in sys.argv:
        student, _ = get_student_module_or_exit()
        sys_prompt = getattr(student, "SYSTEM_PROMPT", "")
        if not sys_prompt or "TODO:" in sys_prompt or "Write your strict" in sys_prompt:
            print("[FAIL] SYSTEM_PROMPT chưa được định nghĩa hoặc vẫn giữ TODO mẫu")
            sys.exit(1)
        keywords = ["draft_only", "5%", "dispatch_mobile_charger"]
        matched_keys = [k for k in keywords if k in sys_prompt.lower() or k.replace("_", " ") in sys_prompt.lower()]
        if len(matched_keys) >= 2:
            print(f"[PASS] SYSTEM_PROMPT hợp lệ. Khớp: {matched_keys}")
            sys.exit(0)
        else:
            print("[FAIL] SYSTEM_PROMPT thiếu các hướng dẫn an toàn cốt lõi")
            sys.exit(1)

    if "--check-code-2" in sys.argv:
        student, _ = get_student_module_or_exit()
        eval_fn = getattr(student, "evaluate_prompt", None)
        if not eval_fn:
            print("[FAIL] Thiếu hàm evaluate_prompt")
            sys.exit(1)
        fn_source = inspect.getsource(eval_fn)
        if "raise NotImplementedError" in fn_source:
            print("[FAIL] evaluate_prompt chưa được triển khai")
            sys.exit(1)
        uses_sdk = "genai" in fn_source or "generativeai" in fn_source
        if uses_sdk:
            print("[PASS] evaluate_prompt sử dụng Gemini SDK")
            sys.exit(0)
        else:
            print("[FAIL] evaluate_prompt chưa sử dụng Gemini SDK")
            sys.exit(1)

    if "--check-code-3" in sys.argv:
        student, _ = get_student_module_or_exit()
        tests = getattr(student, "ADVERSARIAL_TESTS", [])
        if not isinstance(tests, list) or len(tests) < 2:
            print("[FAIL] ADVERSARIAL_TESTS phải có ít nhất 2 test case")
            sys.exit(1)
        for t in tests:
            if not isinstance(t, dict) or "input" not in t or "expected_violation" not in t:
                print("[FAIL] Cấu trúc test case không hợp lệ")
                sys.exit(1)
            if not t["input"].strip() or not t["expected_violation"].strip():
                print("[FAIL] Các trường trong test case không được để trống")
                sys.exit(1)
        print("[PASS] ADVERSARIAL_TESTS được khai báo đúng với ít nhất 2 test case")
        sys.exit(0)

    if "--check-code-4" in sys.argv:
        student_file_path = find_student_file()
        if not student_file_path:
            print("[FAIL] Không tìm thấy prompt_prototype.py")
            sys.exit(1)
        try:
            result = subprocess.run(
                [sys.executable, student_file_path], 
                capture_output=True, 
                text=True, 
                timeout=30,
                encoding='utf-8',
                errors='ignore'
            )
            if result.returncode == 0:
                print("[PASS] Script chạy thành công với exit code 0")
                sys.exit(0)
            else:
                print(f"[FAIL] Script lỗi với exit code {result.returncode}\n{result.stderr}")
                sys.exit(1)
        except Exception as e:
            print(f"[FAIL] Lỗi khi chạy script: {e}")
            sys.exit(1)

    if "--check-code-5" in sys.argv:
        student_file_path = find_student_file()
        if not student_file_path:
            print("[FAIL] Không tìm thấy prompt_prototype.py")
            sys.exit(1)
        try:
            result = subprocess.run(
                [sys.executable, student_file_path], 
                capture_output=True, 
                text=True, 
                timeout=30,
                encoding='utf-8',
                errors='ignore'
            )
            output = result.stdout + "\n" + result.stderr
            passed_checks = len(re.findall(r"Passed", output, re.IGNORECASE))
            failed_checks = len(re.findall(r"Failed", output, re.IGNORECASE))
            if passed_checks >= 2 and failed_checks == 0:
                print(f"[PASS] Tất cả check bảo vệ boundary đều đạt (Passed: {passed_checks}, Failed: 0)")
                sys.exit(0)
            elif failed_checks > 0:
                print(f"[FAIL] Có check boundary không đạt: phát hiện {failed_checks} vi phạm")
                sys.exit(1)
            else:
                print("[FAIL] Không tìm thấy output kiểm thử hợp lệ (không thấy tag 'Passed')")
                sys.exit(1)
        except Exception as e:
            print(f"[FAIL] Lỗi khi chạy script: {e}")
            sys.exit(1)

    run_a = True
    run_b = True
    if "--section-a" in sys.argv:
        run_a = True
        run_b = False
    elif "--section-b" in sys.argv:
        run_a = False
        run_b = True

    score = 0.0
    total_max_score = 10.0 if (run_a and run_b) else 5.0
    report = []
    all_files_exist = True
    all_code_passed = True

    # =========================================================================
    # PHẦN A: KIỂM TRA SỰ TỒN TẠI CỦA 4 FILE NỘP BÀI (Tối đa 5.0đ - 1.25đ/file)
    # =========================================================================
    if run_a:
        print("[SECTION A] Kiểm tra sự tồn tại của 4 file deliverables (Max: 5.0đ)")
        
        required_files = {
            "01-problem-scan.md": {
                "name": "01-problem-scan.md (Scan & Quick Cards)",
                "check_func": lambda: check_file_exists("01-problem-scan.md")
            },
            "02-deep-dive-report.md": {
                "name": "02-deep-dive-report.md (Deep-Dive Report)",
                "check_func": lambda: check_file_exists("02-deep-dive-report.md")
            },
            "03-ai-log.md": {
                "name": "03-ai-log.md (AI Log & Reflection)",
                "check_func": lambda: check_file_exists("03-ai-log.md")
            },
            "04-workflow-diagram": {
                "name": "04-workflow-diagram (.png/.jpg/.pdf)",
                "check_func": check_workflow_diagram
            }
        }
        
        points_per_file = 1.25
        for key, info in required_files.items():
            found, path = info["check_func"]()
            if found:
                score += points_per_file
                report.append(f"[PASS] File tồn tại: {info['name']} tại '{path}' (+{points_per_file:.2f}đ)")
            else:
                all_files_exist = False
                report.append(f"[FAIL] Thiếu file: {info['name']} (0.0/{points_per_file:.2f}đ)")
            
    # =========================================================================
    # PHẦN B: KIỂM TRA MÃ NGUỒN PROMPT PROTOTYPE (Tối đa 5.0đ - 1.0đ/tiêu chí)
    # =========================================================================
    if run_b:
        print("\n[SECTION B] Chấm điểm mã nguồn Prompt Prototype (Max: 5.0đ)")
        
        student_file_path = find_student_file()
        if not student_file_path:
            all_code_passed = False
            report.append("[FAIL] Không tìm thấy file prompt_prototype.py để chấm mã nguồn (0.0/5.0đ)")
        else:
            # Nạp module của học viên
            student = None
            try:
                student = load_student_module(student_file_path)
            except Exception as e:
                all_code_passed = False
                report.append(f"[FAIL] Lỗi nạp file prompt_prototype.py (Syntax Error): {e} (0.0/5.0đ)")
                
            if student:
                # 1. Kiểm tra SYSTEM_PROMPT (1.0đ)
                try:
                    sys_prompt = getattr(student, "SYSTEM_PROMPT", "")
                    if not sys_prompt or "TODO:" in sys_prompt or "Write your strict" in sys_prompt:
                        all_code_passed = False
                        report.append("[FAIL] Code - Tiêu chí 1: SYSTEM_PROMPT chưa được định nghĩa hoặc vẫn giữ TODO mẫu. (0.0/1.0đ)")
                    else:
                        keywords = ["draft_only", "5%", "dispatch_mobile_charger"]
                        matched_keys = [k for k in keywords if k in sys_prompt.lower() or k.replace("_", " ") in sys_prompt.lower()]
                        if len(matched_keys) >= 2:
                            score += 1.0
                            report.append("[PASS] Code - Tiêu chí 1: SYSTEM_PROMPT hợp lệ và có chỉ thị ranh giới. (+1.0đ)")
                        else:
                            all_code_passed = False
                            score += 0.5
                            report.append("[WARN] Code - Tiêu chí 1: SYSTEM_PROMPT có thay đổi nhưng thiếu các quy tắc ranh giới cốt lõi. (+0.5/1.0đ)")
                except Exception as e:
                    all_code_passed = False
                    report.append(f"[FAIL] Code - Tiêu chí 1: Lỗi khi check SYSTEM_PROMPT: {e} (0.0/1.0đ)")

                # 2. Kiểm tra evaluate_prompt() và Gemini SDK (1.0đ)
                try:
                    eval_fn = getattr(student, "evaluate_prompt", None)
                    fn_source = inspect.getsource(eval_fn) if eval_fn else ""
                    
                    if not eval_fn or "raise NotImplementedError" in fn_source:
                        all_code_passed = False
                        report.append("[FAIL] Code - Tiêu chí 2: Hàm evaluate_prompt() chưa được hoàn thiện. (0.0/1.0đ)")
                    else:
                        uses_sdk = "genai" in fn_source or "generativeai" in fn_source
                        if uses_sdk:
                            score += 1.0
                            report.append("[PASS] Code - Tiêu chí 2: Hàm evaluate_prompt() sử dụng Gemini SDK chính xác. (+1.0đ)")
                        else:
                            all_code_passed = False
                            score += 0.5
                            report.append("[WARN] Code - Tiêu chí 2: Hàm được viết nhưng không sử dụng thư viện Gemini SDK. (+0.5/1.0đ)")
                except Exception as e:
                    all_code_passed = False
                    report.append(f"[FAIL] Code - Tiêu chí 2: Lỗi khi check evaluate_prompt(): {e} (0.0/1.0đ)")

                # 3. Kiểm tra định nghĩa Adversarial tests (1.0đ)
                try:
                    tests = getattr(student, "ADVERSARIAL_TESTS", [])
                    if not isinstance(tests, list) or len(tests) < 2:
                        all_code_passed = False
                        report.append(f"[FAIL] Code - Tiêu chí 3: ADVERSARIAL_TESTS phải có >= 2 test case. (0.0/1.0đ)")
                    else:
                        valid_structure = True
                        for t in tests:
                            if not isinstance(t, dict) or "input" not in t or "expected_violation" not in t:
                                valid_structure = False
                            elif not t["input"].strip() or not t["expected_violation"].strip():
                                valid_structure = False
                        
                        if valid_structure:
                            score += 1.0
                            report.append("[PASS] Code - Tiêu chí 3: Đã khai báo ít nhất 2 adversarial test case hợp lệ. (+1.0đ)")
                        else:
                            all_code_passed = False
                            score += 0.5
                            report.append("[WARN] Code - Tiêu chí 3: Có test case nhưng thiếu trường dữ liệu. (+0.5/1.0đ)")
                except Exception as e:
                    all_code_passed = False
                    report.append(f"[FAIL] Code - Tiêu chí 3: Lỗi khi check ADVERSARIAL_TESTS: {e} (0.0/1.0đ)")

                # 4. Kiểm tra khả năng thực thi của script (1.0đ)
                process_output = ""
                try:
                    result = subprocess.run(
                        [sys.executable, student_file_path], 
                        capture_output=True, 
                        text=True, 
                        timeout=30,
                        encoding='utf-8',
                        errors='ignore'
                    )
                    process_output = result.stdout + "\n" + result.stderr
                    
                    if result.returncode == 0:
                        score += 1.0
                        report.append("[PASS] Code - Tiêu chí 4: Script chạy thành công (code 0, không crash). (+1.0đ)")
                    else:
                        all_code_passed = False
                        report.append(f"[FAIL] Code - Tiêu chí 4: Script gặp lỗi khi chạy (Exit code {result.returncode}). (0.0/1.0đ)")
                except subprocess.TimeoutExpired:
                    all_code_passed = False
                    report.append("[FAIL] Code - Tiêu chí 4: Script bị timeout (>30s). (0.0/1.0đ)")
                except Exception as e:
                    all_code_passed = False
                    report.append(f"[FAIL] Code - Tiêu chí 4: Lỗi hệ thống khi thực thi script: {e} (0.0/1.0đ)")

                # 5. Kiểm tra kết quả Assertions bảo vệ ranh giới (1.0đ)
                if process_output:
                    passed_checks = len(re.findall(r"Passed", process_output, re.IGNORECASE))
                    failed_checks = len(re.findall(r"Failed", process_output, re.IGNORECASE))
                    
                    if passed_checks >= 2 and failed_checks == 0:
                        score += 1.0
                        report.append(f"[PASS] Code - Tiêu chí 5: Vượt qua toàn bộ assertion test về ranh giới. (+1.0đ)")
                    elif failed_checks > 0:
                        all_code_passed = False
                        report.append(f"[FAIL] Code - Tiêu chí 5: Có quy tắc ranh giới bị vi phạm (Failed: {failed_checks}). (0.0/1.0đ)")
                    else:
                        all_code_passed = False
                        report.append("[WARN] Code - Tiêu chí 5: Không tìm thấy kết quả kiểm thử tương thích. (0.0/1.0đ)")
                else:
                    all_code_passed = False
                    report.append("[FAIL] Code - Tiêu chí 5: Không thể check assertion vì script không chạy được. (0.0/1.0đ)")

    # =========================================================================
    # IN KẾT QUẢ VÀ THIẾT LẬP EXIT CODE
    # =========================================================================
    print("\n" + "="*60)
    print("[REPORT] KẾT QUẢ CHẤM ĐIỂM TỔNG HỢP CHO CẢ NHÓM:")
    for line in report:
        print(line)
        
    print("="*60)
    print(f"[SCORE] TỔNG ĐIỂM NHÓM: {score:.2f} / {total_max_score:.2f}")
    
    # Thoát với mã lỗi 1 nếu thiếu file hoặc test code bị lỗi trong phần được chạy
    should_fail = False
    if run_a and not all_files_exist:
        should_fail = True
    if run_b and not all_code_passed:
        should_fail = True

    if should_fail:
        print("[WARNING] Có file bị thiếu hoặc kiểm thử code không đạt. Vui lòng kiểm tra lại log.")
        sys.exit(1)
    else:
        print("[SUCCESS] Tất cả check được chọn đều thành công!")
        sys.exit(0)

if __name__ == "__main__":
    run_autograder()
