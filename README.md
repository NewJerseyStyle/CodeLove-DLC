# CodeLove DLC Template

源界 (Source Realm) 的 DLC 開發模板。使用此模板創建可與主線整合的擴展內容。

## 快速開始

### 1. 使用此模板

點擊 GitHub 頁面上的 **"Use this template"** 按鈕，或：

```bash
# 克隆模板
git clone https://github.com/NewJerseyStyle/CodeLove-DLC.git my-dlc
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

## 打包與安裝

### 方式 1：打包為 ZIP（推薦）

1. 將 DLC 資料夾打包成 ZIP
2. 用戶下載後解壓到主遊戲的 `game/` 目錄

**解壓位置**：

```
SourceRealm/
└── game/        ← 解壓到這個文件夾裡任何位置都可以
    └── CodeLove-YourDLC/      ← 你的 DLC 資料夾
        ├── config.rpy
        ├── characters.rpy
        ├── events/
        └── endings.rpy
```

**重要**：
- 解壓到 `game/` 目錄下的**任何子目錄**都可以
- 不限於 `game/rpy/dlc/`，只要在 `game/` 以下即可
- Ren'Py 會自動加載所有 `.rpy` 檔案

### 方式 2：直接複製開發

如果用戶直接使用原始碼開發，可以直接將資料夾複製到 `game/` 目錄。

### 驗證安裝

1. 啟動遊戲
2. 按開發者控制台鍵（通常是 `Shift+O` 或 `Shift+D`）
3. 輸入 `call debug_dlc_status`
4. 檢查「已安裝 DLC 數量」是否 > 0

## 文件結構

```
your_dlc/
├── README.md           # 說明文件
├── config.rpy          # DLC 配置和區域註冊
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

# 註冊 DLC
register_dlc(your_dlc_config)

# 註冊區域（區域導向設計）
register_dlc_region("your_region", {
    "name": "Your Region",
    "description": "區域描述",
    "dlc_id": "your_dlc",
    "entry_label": "enter_your_region",
    "unlock_condition": lambda: True,  # 解鎖條件
})
```

### 2. 創建角色 (`characters.rpy`)

定義角色、語言特性、關係進程。

```python
# 角色變量（用 default 聲明）
default your_char_relationship = "UNMET"

# 角色定義
define your_char = Character("YourChar", color="#FF6B6B")

# 註冊 DLC 角色
register_dlc_character("your_char", {
    "name": "YourChar",
    "language": "YourLanguage",
    "traits": ["特性1", "特性2"],
})
```

### 3. 編寫事件 (`events/`)

創建區域入口和樞紐菜單：

```renpy
# 區域入口
label enter_your_region:
    scene bg your_region with fade
    narrator "你來到了 Your Region。"
    jump your_region_hub

# 區域樞紐
label your_region_hub:
    show your_char normal at center

    menu:
        "做某事":
            jump your_event

        "返回廣場":
            jump return_to_plaza

# 返回廣場（DLC 必須提供）
label return_to_plaza:
    scene black with fade
    narrator "你返回了廣場。"
    jump time_choice_menu
```

**重要注意**：DLC 必須提供 `return_to_plaza` label，讓玩家返回主遊戲。

### 4. 創建結局 (`endings.rpy`)

定義結局檢查函數：

```python
def your_dlc_check_ending():
    """檢查 DLC 結局條件"""
    if store.your_char_relationship == "PARTNER":
        return "ending_your_char_partner"
    elif store.your_char_relationship == "CLOSE":
        return "ending_your_char_friend"
    return None

# 註冊結局檢查器
your_dlc_config["ending_checker"] = your_dlc_check_ending

# 結局資訊
your_dlc_config["endings"] = {
    "ending_your_char_partner": {
        "name": "YourChar 伴侶結局",
        "condition": lambda: store.your_char_relationship == "PARTNER"
    },
    "ending_your_char_friend": {
        "name": "YourChar 朋友結局",
        "condition": lambda: store.your_char_relationship == "CLOSE"
    }
}
```

## 測試

1. 將 DLC 資料夾放入主遊戲的 `game/` 目錄（任何子目錄都可以）
2. 啟動遊戲
3. 使用 `call debug_dlc_status` 檢查是否已註冊
4. 在廣場選擇「前往其他區域」確認是否出現

## 發布清單

- [ ] 所有檔案使用 UTF-8 編碼
- [ ] 圖片放入 `images/YourLanguage/`
- [ ] 更新 README 說明安裝方法
- [ ] 打包為 ZIP（包含整個資料夾）
- [ ] 在 GitHub 創建 Release
- [ ] 測試全新安裝（從下載到運行）

## 常見問題

### Q: DLC 資料夾應該放在哪裡？

A: `game/` 目錄下的任何位置都可以。例如：
- `game/YourDLC/`
- `game/rpy/dlc/your_dlc/`
- `game/mods/your_dlc/`

只要在 `game/` 以下，Ren'Py 都會找到。

### Q: 為什麼「前往其他區域」選項沒有出現？

A: 檢查以下幾點：
1. DLC 是否已正確註冊（使用 `debug_dlc_status` 檢查）
2. 區域的 `unlock_condition` 是否滿足
3. 主遊戲是否已完成必要章節（例如 C_01）

### Q: 如何在 DLC 中引用主遊戲的變量？

A: 使用 `store.變量名`：
```python
if store.cee_relationship == "FUNCTIONAL":
    # 執行某操作
    pass
```

## 區域導向設計

DLC 採用**區域導向**設計：

```
廣場（主線樞紐）
    ├── 記憶倉庫（Cee）
    ├── 契約局（Jawa）
    └── [前往其他區域]        ← 自動顯示已註冊的 DLC 區域
            ├── Zen Garden（Py-DLC）
            └── 你的區域
```

**優點**：
- DLC 有自己的區域，不干擾主線
- 區域內部自己管理事件和解鎖條件
- 玩家可以自由進出，不強制時間對齊

## 參考範例

完整的可運行範例：[CodeLove-Py-DLC](https://github.com/NewJerseyStyle/CodeLove-Py-DLC)

## 支援

- [DLC_DEVELOPER_GUIDE.md](../DLC_DEVELOPER_GUIDE.md) - 完整開發指南
- [DLC_QUICK_REFERENCE.md](../DLC_QUICK_REFERENCE.md) - 快速參考

## 授權

MIT License（或根據主遊戲授權調整）
