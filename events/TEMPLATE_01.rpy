# ============================================================================
# DLC 模板 - 事件第一章
# ============================================================================
#
# 這是一個完整的事件模板，展示標準的事件結構。
# ============================================================================

# ============================================================================
# TEMPLATE_01: 初次相遇
# ============================================================================

label template_TEMPLATE01_start:
    # ===== 前置條件檢查 =====
    if not template_char_unlock_condition():
        narrator "這個區域目前無法進入..."
        jump time_choice_menu

    # ===== 場景設置 =====
    scene bg plaza_afternoon
    with Fade(1.0)

    # ===== 角色登場 =====
    show template_char normal at center

    # ===== 開場敘述 =====
    narrator "你在資訊廣場的角落發現了一個從未見過的身影。"

    narrator "那個人似乎正在專注地處理一些數據流，動作輕快而流暢。"

    # ===== 初次接觸 =====
    template_char "（注意到你）嗯？你是..."

    narrator "對方停下手中的工作，打量著你。"

    template_char "沒見過的型別。你是新來的？"

    # ===== 玩家回應 =====
label template_TEMPLATE01_response:
    menu:
        "自我介紹":
            jump template_TEMPLATE01_introduce

        "詢問對方是誰":
            jump template_TEMPLATE01_ask

        "保持沉默":
            jump template_TEMPLATE01_silent

# ===== 分支 A：自我介紹 =====
label template_TEMPLATE01_introduce:
    player "我是從現實世界來的，不小心進入了這個地方..."

    template_char "現實世界？你是說『那邊』？"

    narrator "對方的表情變得感興趣。"

    template_char "有意思。我是模板角色，負責處理這一區的數據轉換工作。"

    template_char "你可以叫我模板角色，或者隨便什麼你喜歡的稱呼。"

    $ template_char_relationship = "ACQUAINTED"
    $ track_affection("template_char", 10)

    jump template_TEMPLATE01_continue

# ===== 分支 B：詢問對方 =====
label template_TEMPLATE01_ask:
    player "你是誰？在這裡做什麼？"

    template_char "問得直接。我喜歡。"

    narrator "對方微微點頭。"

    template_char "我是模板角色，這一區的數據轉換工程師。你又是誰？"

    player "我...我是從外面來的。"

    template_char "外面？哦，現實世界。稀客。"

    $ template_char_relationship = "ACQUAINTED"
    $ track_affection("template_char", 5)

    jump template_TEMPLATE01_continue

# ===== 分支 C：保持沉默 =====
label template_TEMPLATE01_silent:
    narrator "你沒有說話，只是靜靜地看著對方。"

    template_char "...不說話嗎？也行。"

    narrator "對方聳聳肩，繼續手頭的工作。"

    template_char "我是模板角色。如果你改變主意想聊聊，隨時可以來找我。"

    $ template_char_relationship = "ACQUAINTED"
    $ track_affection("template_char", 0)

    jump template_TEMPLATE01_continue

# ===== 繼續劇情 =====
label template_TEMPLATE01_continue:
    scene bg plaza_afternoon

    show template_char normal at center

    narrator "模板角色似乎對你產生了一些興趣。"

    template_char "既然你是從現實來的，應該還不熟悉這裡的運作方式。"

    template_char "需要幫忙的話，可以來找我。不過..."

    narrator "對方停頓了一下。"

    template_char "我這裡也有一些工作需要人手。如果你有興趣的話。"

    # ===== 結束選項 =====
label template_TEMPLATE01_end_choice:
    menu:
        "答應幫忙":
            jump template_TEMPLATE01_help

        "先考慮一下":
            jump template_TEMPLATE01_consider

# ===== 結束 A：答應幫忙 =====
label template_TEMPLATE01_help:
    player "好啊，我可以幫什麼忙？"

    template_char "（露出一絲微笑）爽快。下次來的時候再詳細說。"

    $ track_affection("template_char", 5)
    $ store.template_char_trust += 10

    jump template_TEMPLATE01_end

# ===== 結束 B：考慮 =====
label template_TEMPLATE01_consider:
    player "讓我先考慮一下..."

    template_char "當然。不著急。"

    narrator "模板角色點點頭，轉身繼續工作。"

    jump template_TEMPLATE01_end

# ===== 章節結束 =====
label template_TEMPLATE01_end:
    $ complete_chapter("template_01")
    $ store.template_char_unlocked = True

    narrator "你與模板角色的初次相遇就這樣結束了。"

    narrator "這個源界似乎還有很多你不知道的事物..."

    jump end_time_period

# ============================================================================
# TEMPLATE_02: 第一次合作
# ============================================================================

label template_TEMPLATE02_start:
    # 檢查前置條件
    if template_char_relationship == "UNMET":
        narrator "你還沒有見過這個人..."
        jump time_choice_menu

    scene bg plaza_noon
    show template_char normal at center

    narrator "你再次遇到了模板角色。"

    template_char "哦，是你。考慮得怎麼樣了？"

    # ===== 核心互動 =====
label template_TEMPLATE02_main:
    template_char "我這裡有一個問題需要解決..."

    narrator "模板角色指向一組正在運行的數據流。"

    template_char "這些數據需要按照特定的規則進行排序，但我目前用的方法太慢了。"

    narrator "你觀察了一會兒，發現模板角色正在用最直觀的方式逐一比較每個數據。"

    # ===== 玩家選擇 =====
    menu:
        "建議使用更高效的排序方法":
            jump template_TEMPLATE02_optimal

        "詢問數據的特點":
            jump template_TEMPLATE02_analyze

        "讓他繼續用原方法":
            jump template_TEMPLATE02_brute

# ===== 分支 A：最優解 =====
label template_TEMPLATE02_optimal:
    player "這些數據有什麼特點嗎？如果是部分有序的，可以用優化的方法..."

    template_char "（眼睛一亮）你懂這個？"

    narrator "你簡單解釋了更高效的算法。"

    template_char "原來可以這樣...讓我試試。"

    narrator "模板角色快速執行了你的方案，效率提升了數倍。"

    template_char "不錯。非常不錯。"

    $ template_char_relationship = "FRIEND"
    $ track_affection("template_char", 20)
    $ store.template_char_trust += 20

    jump template_TEMPLATE02_end_good

# ===== 分支 B：分析 =====
label template_TEMPLATE02_analyze:
    player "能告訴我更多關於這些數據的信息嗎？"

    template_char "這些是從不同來源收集的日誌數據，需要按時間戳排序..."

    narrator "經過討論，你們一起找到了一個還不錯的解決方案。"

    template_char "這樣效率確實提高了。謝了。"

    $ track_affection("template_char", 10)
    $ store.template_char_trust += 10

    jump template_TEMPLATE02_end_neutral

# ===== 分支 C：暴力 =====
label template_TEMPLATE02_brute:
    player "繼續用你現在的方法應該也行吧..."

    template_char "是沒問題，就是慢了點。"

    narrator "模板角色繼續用原方法處理，花了很長時間才完成。"

    template_char "完成了。不過下次有更好的方法記得告訴我。"

    $ track_affection("template_char", 5)

    jump template_TEMPLATE02_end_neutral

# ===== 結局 =====
label template_TEMPLATE02_end_good:
    narrator "這次合作讓你和模板角色的關係更近了一步。"

    $ complete_chapter("template_02")

    jump end_time_period

label template_TEMPLATE02_end_neutral:
    narrator "任務完成了，但你覺得可以做得更好。"

    $ complete_chapter("template_02")

    jump end_time_period
