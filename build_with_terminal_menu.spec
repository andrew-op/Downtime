# -*- mode: python ; coding: utf-8 -*-
# Build spec for Downtime with Terminal Menu launcher

block_cipher = None

a = Analysis(
    ['terminal_menu.py'],  # Terminal menu as entry point
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['game1_main', 'game_state', 'locations', 'items', 'npcs', 'desktop', 'utils'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Downtime',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Console mode for terminal menu and text game
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None  # Add 'icon.ico' here if you create an icon file
)
