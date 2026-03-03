# CodeLove DLC Template

源界 (Source Realm) 的 DLC 開發模板。使用此模板創建可與主線整合的擴展內容。

## 快速開始

### 1. 使用此模板

點擊 GitHub 頁面上的 **"Use this template"** 按鈕，或：

```bash
# 克隆模板
git clone https://github.com/YOUR_USERNAME/CodeLove-DLC.git my-dlc
cd my-dlc
rm -rf .git && git init  # 重新初始化為你的專案
```

### 2. 重命名

```bash
# 全局替換（建議使用編輯器）
# template_dlc → your_dlc_name
# template_char → your_char_id
# TEMPLATE → YOUR_CHAPTER_PREFIX
```

### 3. 打包為 RPA

DLC 不需要完整的 Ren'Py 專案。只需將 `.rpy` 檔案打包：

```bash
# 在主遊戲目錄下，使用 Ren'Py 的 RPA 打包工具
# 或手動建立目錄結構後壓縮
```

### 4. 安裝

將打包好的 RPA 檔案放入主遊戲的 `game/` 目錄即可。

## 文件結構

```
your_dlc/
├── README.md           # 說明文件
├── config.rpy          # DLC 配置和註冊
├── characters.rpy      # 角色定義
├── events/             # 事件文件
│   └── YOUR_01.rpy
└── endings.rpy         # 結局定義
```

## 開發步驟

### 1. 配置 (`config.rpy`)

更新基本資訊：

```python
your_dlc_config = {
    "id": "your_dlc",
    "name": "Your DLC Name",
    "author": "Your Name",
    "version": "1.0.0",
    "description": "DLC 描述",
}
```

### 2. 創建角色 (`characters.rpy`)

定義角色、語言特性、關係進程。

### 3. 編寫事件 (`events/`)

按照模板結構編寫章節，使用：
- `complete_chapter()` 標記完成
- `track_affection()` 追蹤好感度

### 4. 創建結局 (`endings.rpy`)

定義至少一個結局，使用 `record_ending()` 記錄。

## 測試

1. 將 DLC 資料夾放入主遊戲的 `game/rpy/dlc/` 目錄
2. 啟動遊戲
3. 檢查 `debug_dlc_status` 確認已註冊

## 發布清單

- [ ] 所有檔案使用 UTF-8 編碼
- [ ] 圖片放入 `images/YourLanguage/`
- [ ] 更新 README 說明安裝方法
- [ ] 打包為 RPA 或 ZIP

## 支援

- [DLC_DEVELOPER_GUIDE.md](../DLC_DEVELOPER_GUIDE.md) - 完整開發指南
- [DLC_QUICK_REFERENCE.md](../DLC_QUICK_REFERENCE.md) - 快速參考

## 授權

MIT License（或根據主遊戲授權調整）
