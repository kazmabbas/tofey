import base64
import marshal

def encrypt_code(source_code: str) -> str:
    """
    تشفير كود Python باستخدام marshal و base64.
    """
    compiled_code = compile(source_code, '<string>', 'exec')
    marshalled_code = marshal.dumps(compiled_code)
    encrypted_code = base64.b64encode(marshalled_code).decode('utf-8')
    return encrypted_code

def save_encrypted_file(input_file: str, output_file: str):
    """
    قراءة ملف Python وتشفيره وحفظه.
    """
    with open(input_file, 'r') as file:
        source_code = file.read()
    encrypted_code = encrypt_code(source_code)
    with open(output_file, 'w') as file:
        file.write(encrypted_code)
