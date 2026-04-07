import sys
from ui import VaultApp

_FLAG_TO_TAB = {
    "--encrypt":    0,
    "--decrypt":    1,
    "--compress":   2,
    "--decompress": 3,
}

if __name__ == "__main__":
    flag     = sys.argv[1] if len(sys.argv) > 1 else None
    filepath = sys.argv[2] if len(sys.argv) > 2 else None

    tab = _FLAG_TO_TAB.get(flag)

    app = VaultApp(startup_tab=tab, startup_file=filepath)
    app.mainloop()
