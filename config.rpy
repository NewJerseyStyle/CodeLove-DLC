# ============================================================================
# DLC 模板 - 配置文件
# ============================================================================
#
# 這是一個完整的 DLC 模板，展示如何創建可與主線整合的擴展內容。
# 複製此目錄並修改以創建你自己的 DLC。
#
# 使用步驟：
# 1. 複製 rpy/dlc/template_dlc/ 目錄
# 2. 重命名為你的 DLC ID（如 rpy/dlc/my_story/）
# 3. 修改所有文件中的 "template" 為你的 DLC ID
# 4. 編輯角色、事件、結局
# 5. 測試並發布
# ============================================================================

init python:
    # ============================================================================
    # DLC 元數據
    # ============================================================================

    template_dlc_info = {
        "id": "template_dlc",           # DLC 唯一標識符（必須與目錄名一致）
        "name": "模板 DLC",              # 顯示名稱
        "version": "1.0.0",             # 版本號
        "author": "你的名字",            # 作者
        "description": "一個展示 DLC 結構的模板",  # 描述
        "dependencies": [],             # 依賴的其他 DLC ID
        "conflicts": [],                # 衝突的 DLC ID
        "min_main_version": "0.1.0",    # 最低主線版本要求
    }

    # ============================================================================
    # DLC 選項
    # ============================================================================

    template_dlc_options = {
        # 是否禁用主線結局的強制觸發
        # True = DLC 可以延後主線結局到 custom_ending_threshold
        "disable_main_ending": False,

        # 自定義結局觸發時間
        # 只有當 disable_main_ending = True 時有效
        "custom_ending_threshold": 42,

        # 是否使用獨立時間線
        # True = DLC 有自己的時間系統，不影響主線
        "independent_timeline": False,

        # 是否與主線整合
        # True = DLC 角色可以出現在主線事件中
        "integrate_with_main": True,
    }

    # ============================================================================
    # 結局檢查函數
    # ============================================================================

    def template_dlc_check_ending():
        """
        檢查 DLC 結局條件

        返回: 結局 ID 或 None
        """
        # 獲取相關狀態
        rel = getattr(store, 'template_char_relationship', 'UNMET')
        st = store.source_time
        completed = getattr(store, 'template_dlc_completed', False)

        # True End: 完成所有內容 + 最高關係
        if completed and rel == "PARTNER":
            return "ending_template_true"

        # Good End: 完成主要內容 + 高關係
        if completed and rel in ["CLOSE", "PARTNER"]:
            return "ending_template_good"

        # Normal End: 完成主要內容
        if completed:
            return "ending_template_normal"

        # Bad End: 超時但沒完成
        if st >= 45 and rel == "UNMET":
            return "ending_template_bad"

        return None

    # ============================================================================
    # 時間線擴展
    # ============================================================================

    template_dlc_timeline = {
        "ST_38-40": {
            "available_lines": ["template_dlc"],
            "template_dlc_event": "TEMPLATE_01",
            "is_holiday": False
        },
        "ST_40-42": {
            "available_lines": ["template_dlc", "cee"],
            "template_dlc_event": "TEMPLATE_02",
            "is_holiday": False
        },
        "ST_42-45": {
            "available_lines": ["template_dlc"],
            "template_dlc_event": "TEMPLATE_03",
            "is_holiday": True,
            "holiday_id": "holiday_template"
        },
    }

    # ============================================================================
    # 結局定義
    # ============================================================================

    template_dlc_endings = {
        "ending_template_true": {
            "name": "模板 True End",
            "condition": lambda: (
                getattr(store, 'template_dlc_completed', False) and
                getattr(store, 'template_char_relationship', '') == "PARTNER"
            )
        },
        "ending_template_good": {
            "name": "模板 Good End",
            "condition": lambda: getattr(store, 'template_dlc_completed', False)
        },
        "ending_template_normal": {
            "name": "模板 Normal End",
            "condition": lambda: True
        },
        "ending_template_bad": {
            "name": "模板 Bad End",
            "condition": lambda: getattr(store, 'template_char_relationship', '') == "UNMET"
        },
    }

    # ============================================================================
    # 註冊 DLC
    # ============================================================================

    # 構建完整的 DLC 信息
    template_dlc_full_info = dict(template_dlc_info)
    template_dlc_full_info["ending_checker"] = template_dlc_check_ending
    template_dlc_full_info["timeline_data"] = template_dlc_timeline
    template_dlc_full_info["endings"] = template_dlc_endings
    template_dlc_full_info["options"] = template_dlc_options

    # 註冊到系統
    register_dlc(template_dlc_full_info)

    # 如果需要禁用主線結局
    if template_dlc_options["disable_main_ending"]:
        store.dlc_disable_main_ending = True
        store.dlc_custom_ending_threshold = template_dlc_options["custom_ending_threshold"]
