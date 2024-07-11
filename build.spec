# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['import.py'],
    pathex=['C:\\Users\\jerome.planken\\Desktop\\Kunder\\Scraper'],
    binaries=[],
    datas=[],
    hiddenimports=[
        'plyer.platforms.win.notification',  # Ensure platform-specific plyer modules are included
        'plyer.platforms.macosx.notification',
        'plyer.platforms.linux.notification',
        'requests',
        'bs4'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='import',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # This line disables the terminal window
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='import'
)
