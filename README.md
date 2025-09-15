# 🔧 APK Compression Fixer

A Python-based utility for malware analysts and reverse engineers to repair **tampered or corrupted ZIP compression flags** in malicious APK files.  
This tool allows you to make APKs with broken compression headers readable again — so they can be decompiled with `jadx`, `apktool`, or other reverse engineering tools.

---

## 📌 Why This Tool?

In the wild, some malware authors intentionally **tamper with the ZIP compression flags** in APK files to break static analysis tools.  
When you try to unzip or decompile such APKs, you may see errors like:

- `unzip: invalid compression method`
- `apktool: cannot extract file`
- `bad CRC or file corrupt`

This tool:
- Reads the APK as a raw ZIP,
- Iterates over each file entry,
- Rebuilds correct local file headers and central directory records,
- Outputs a **repaired APK** with standard ZIP compression flags.

---

## ⚡ Features
✅ Automatically detects and fixes corrupted compression flags  
✅ Preserves all original files and directory structure  
✅ Produces a valid APK that can be opened by common tools (`apktool`, `jadx`, `zipalign`)  
✅ Works with **deflate**, **stored**, and mixed compression methods  
✅ Minimal dependencies — pure Python

---

## 🛠️ Installation

No installation required — just clone or download the script.

## Syntax

python3 CompFixer.py test.apk testfixout.apk  
