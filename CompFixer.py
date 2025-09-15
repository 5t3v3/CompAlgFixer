import sys
import zipfile
import os

def fix_apk_compression(apk_path, output_path):
    """
    Fixes APK compression flags by re-packing all files with proper compression.
    """
    if not os.path.exists(apk_path):
        print(f"[!] Input file not found: {apk_path}")
        return

    with zipfile.ZipFile(apk_path, 'r') as original_apk:
        with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED) as fixed_apk:
            for item in original_apk.infolist():
                try:
                    data = original_apk.read(item.filename)
                    fixed_apk.writestr(item.filename, data, compress_type=zipfile.ZIP_DEFLATED)
                    print(f"[+] Fixed compression for: {item.filename}")
                except Exception as e:
                    print(f"[!] Failed to extract/write {item.filename}: {e}")

    print(f"\n[+] Fixed APK written to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <input.apk> <output.apk>")
        sys.exit(1)

    input_apk = sys.argv[1]
    output_apk = sys.argv[2]

    fix_apk_compression(input_apk, output_apk)
