# WinVFE (Vault file encryption)

WinVFE is a lightweight, modern encryption utility designed to keep your sensitive files private using AES-256-GCM.

Thank you very much to @Kflone5 for help with development!!

<img width="150" height="100" alt="Снимок экрана 2026-04-10 235136" src="https://github.com/user-attachments/assets/07280b3d-0764-4abb-a914-8a7987525b5d" />
<img width="150" height="100" alt="Снимок экрана 2026-04-10 235129" src="https://github.com/user-attachments/assets/875781bb-137f-4a53-8b0a-2b17fbab2a96" />
<img width="150" height="100" alt="Снимок экрана 2026-04-10 235112" src="https://github.com/user-attachments/assets/9a6d386d-254e-4c77-a5e9-8f44a1b64cc1" />
<img width="150" height="100" alt="Снимок экрана 2026-04-10 235102" src="https://github.com/user-attachments/assets/1451b839-0a78-48e9-a98f-0b9b6af7d837" />
<img width="150" height="100" alt="Снимок экрана 2026-04-10 235050" src="https://github.com/user-attachments/assets/40481b4b-422e-4f71-affe-cd1052d56661" />


Lates version:

**WinVFE v1.5.1**

_06.04.2026_

### New features
WinVFE (Vault) 1.5.2
10.04.2026

Fixed:

    Algorithm button styling (removed circle and bold-text resizing on click)
    UI scaling issues (removed scrolling and adjusted fixed window dimensions)
    General stability when handling large file queues

Removed:

    Legacy Blowfish-CBC encryption support
    Password strength meter (for improved UI performance and clarity)
    Manual algorithm selection for Decryption (now handled by auto-detection)
    Divider lines and subtitles from the Wizard/Start page

Added:

    RAR compression support (requires WinRAR/rar.exe in System PATH)
    Multi-threaded processing for Encryption, Decryption, and Compression
    Secure File Shredding (3-pass overwrite before deletion)
    "Delete archive after decompression" and "Delete .vault after decryption" options
    Normal vs. Best compression level toggles
    Result Dialog popups with "Open Folder" shortcut upon completion
    Footer link buttons for GitHub, Organisation, and Support in the Wizard tab
 
Algorithms:
```
# Encryption

AES-256-GCM
Blowfish-CBC

# Compression

zip
7z
vz
```


Beutiful UI: A clean interface with an easily navigatable and aesthetic UI, includes a wizard.

Portable: Available as a single standalone .exe for Windows.

Encrypt: Select a file, enter a strong password, and click "Encrypt File". This creates a .vault version of your file.
Decrypt: Select your .vault file, enter the original passphrase, and click "Decrypt File" to recover your data.

```
Language: Python 3.10_
Library: Tkinter / Cryptography_
Release Date: 29.03.2026_
```
