# ============================================================================
# DLC 模板 - 角色定義
# ============================================================================

# ============================================================================
# 1. 角色定義
# ============================================================================

define template_char = Character(
    "模板角色",           # 顯示名稱
    color="#00CED1",      # 深青色 - 修改為你角色的主題色
    what_prefix="「",
    what_suffix="」"
)

# ============================================================================
# 2. 角色關係變量
# ============================================================================

# 關係狀態進程
# UNMET → ACQUAINTED → FRIEND → CLOSE → PARTNER
default template_char_relationship = "UNMET"

# 角色專用變量
default template_char_trust = 0        # 信任度 (0-100)
default template_char_unlocked = False # 是否解鎖

# ============================================================================
# 3. 角色語言特性
# ============================================================================

init python:
    template_char_traits = {
        "language": "TemplateLang",     # 語言原型名稱
        "has_gc": True,                 # 是否有垃圾回收
        "strong_typing": True,          # 是否強型別
        "memory_safety": True,          # 是否記憶體安全
        "concurrency_model": "async",   # 並發模型
        "execution_speed": "fast",      # 執行速度
        "learning_curve": "medium",     # 學習曲線

        # 角色性格特點
        "personality": {
            "formal": False,            # 是否正式
            "helpful": True,            # 是否樂於助人
            "cautious": False,          # 是否謹慎
            "efficient": True,          # 是否追求效率
        }
    }

    # 註冊角色到 DLC 系統
    register_dlc_character("template_char", {
        "name": "模板角色",
        "color": "#00CED1",
        "language": "TemplateLang",
        "traits": template_char_traits,
        "relationship_states": ["UNMET", "ACQUAINTED", "FRIEND", "CLOSE", "PARTNER"]
    })

# ============================================================================
# 4. 角色專用函數
# ============================================================================

init python:
    def template_char_update_relationship(new_state):
        """更新模板角色的關係狀態"""
        old_state = store.template_char_relationship
        store.template_char_relationship = new_state

        # 可以在這裡添加狀態變化時的特殊邏輯
        if old_state != new_state:
            if new_state == "FRIEND":
                store.template_char_trust += 20
            elif new_state == "CLOSE":
                store.template_char_trust += 30
            elif new_state == "PARTNER":
                store.template_char_trust = 100

    def template_char_can_interact():
        """檢查是否可以與角色互動"""
        return (
            store.template_char_unlocked and
            store.template_char_relationship != "UNMET"
        )

# ============================================================================
# 5. 角色登場條件
# ============================================================================

init python:
    def template_char_unlock_condition():
        """
        角色解鎖條件

        返回: True 如果角色應該解鎖
        """
        # 示例：需要完成 C_02 後才解鎖
        return store.c_02_status == "completed"

# ============================================================================
# 6. 角色對話風格示例
# ============================================================================

# 根據關係狀態，角色會有不同的對話風格
# 在事件中可以這樣使用：
#
# if template_char_relationship == "UNMET":
#     template_char "（陌生的眼神）...你好。"
# elif template_char_relationship == "ACQUAINTED":
#     template_char "哦，是你。有什麼事嗎？"
# elif template_char_relationship == "FRIEND":
#     template_char "你來了！今天過得怎麼樣？"
# elif template_char_relationship == "CLOSE":
#     template_char "（微笑）看到你真好。"
# elif template_char_relationship == "PARTNER":
#     template_char "我一直都在這裡。"
