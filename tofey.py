# مكتبة تشفير باسم Tofey
import base64
import marshal

class Tofey:
    @staticmethod
    def encrypt_script(input_file: str, output_file: str):
        """
        تشفير ملف بايثون باستخدام Marshal وBase64.
        """
        try:
            with open(input_file, 'r') as file:
                code = file.read()
            
            # تحويل النص البرمجي إلى Bytecode
            compiled_code = compile(code, input_file, 'exec')
            marshalled_code = marshal.dumps(compiled_code)
            encrypted_code = base64.b64encode(marshalled_code)
            
            with open(output_file, 'wb') as file:
                file.write(encrypted_code)
            
            print(f"تم تشفير الملف: {input_file} -> {output_file}")
        except Exception as e:
            print(f"خطأ أثناء التشفير: {e}")

    @staticmethod
    def decrypt_and_execute(encrypted_file: str):
        """
        فك تشفير ملف Python مشفر وتنفيذه.
        """
        try:
            with open(encrypted_file, 'rb') as file:
                encrypted_code = file.read()
            
            # فك التشفير باستخدام Base64 وMarshal
            marshalled_code = base64.b64decode(encrypted_code)
            code_object = marshal.loads(marshalled_code)
            
            # تنفيذ الكود
            exec(code_object)
        except Exception as e:
            print(f"خطأ أثناء فك التشفير أو التنفيذ: {e}")

# أمثلة الاستخدام
if __name__ == "__main__":
    # ملف Python الأصلي
    input_script = "example.py"  # استبدل باسم الملف الخاص بك
    encrypted_script = "example.tofey"

    # تشفير الملف
    Tofey.encrypt_script(input_script, encrypted_script)

    # فك التشفير وتنفيذ الملف
    Tofey.decrypt_and_execute(encrypted_script)