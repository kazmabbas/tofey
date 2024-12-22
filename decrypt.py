import base64
import marshal

def decrypt_and_execute(encrypted_code: str):
    """
    فك تشفير الكود المشفر وتنفيذه.
    """
    marshalled_code = base64.b64decode(encrypted_code)
    code_object = marshal.loads(marshalled_code)
    exec(code_object)

def run_encrypted_file(file_path: str):
    """
    قراءة ملف مشفر، فك تشفيره وتنفيذه.
    """
    with open(file_path, 'r') as file:
        encrypted_code = file.read()
    decrypt_and_execute(encrypted_code)
