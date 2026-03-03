# ============================================================================
# DLC 模板 - 結局
# ============================================================================

# ============================================================================
# True End: 完美融合
# ============================================================================

label ending_template_true:
    scene bg plaza_evening
    with Fade(3.0, 1.0, 3.0)

    show template_char happy at center
    show cee normal at left
    show jawa normal at right

    narrator "源界的黃昏籠罩著資訊廣場，所有角色聚集在一起。"

    template_char "（看著你）我從沒想過，會有人能同時理解這麼多不同的思維方式。"

    cee "有效率。你的算法知識已經超越了大多數居民。"

    jawa "而且你懂得何時使用哪種方法。這才是真正的智慧。"

    narrator "模板角色走到你面前。"

    template_char "謝謝你。不只是因為你幫了我，而是因為你讓我看到了可能性。"

    template_char "不同的語言、不同的思維，不是障礙，而是力量。"

    narrator "你感到一種深刻的連結——不只是與某個角色，而是與整個源界。"

    scene bg laboratory
    with Dissolve(3.0)

    narrator "現實世界中，阿源看著螢幕上的數據，目瞪口呆。"

    source "這...這些代碼怎麼可能如此完美？每個部分都用了最適合的語言..."

    narrator "【DLC 結局：完美融合】"
    narrator "你成為了連接不同世界的橋樑。"

    $ record_ending("ending_template_true")

    jump ending_final_ack

# ============================================================================
# Good End: 新的朋友
# ============================================================================

label ending_template_good:
    scene bg plaza_noon

    show template_char happy at center

    narrator "你在源界的旅程即將結束。"

    template_char "聽說你要走了？"

    player "嗯，該回去了。"

    template_char "（微笑）那麼，下次再見。"

    template_char "這個世界的大門永遠為你敞開。"

    narrator "你和模板角色握手道別。"

    template_char "對了，如果你在現實世界遇到任何編程問題..."

    template_char "試著用你在這裡學到的思維方式。我會『在這裡』等你的。"

    narrator "【DLC 結局：新的朋友】"
    narrator "你收穫了一段跨越次元的友情。"

    $ record_ending("ending_template_good")

    jump ending_final_ack

# ============================================================================
# Normal End: 匆匆過客
# ============================================================================

label ending_template_normal:
    scene bg plaza_afternoon

    show template_char normal at center

    narrator "你在源界的時間即將結束。"

    template_char "哦，你要走了？"

    player "是的。"

    template_char "好吧。一路順風。"

    narrator "模板角色點點頭，轉身繼續工作。"

    narrator "你感覺你們之間還有很多可以探索的內容..."

    narrator "【DLC 結局：匆匆過客】"
    narrator "你完成了 DLC 的主要內容，但似乎錯過了些什麼。"

    $ record_ending("ending_template_normal")

    jump ending_final_ack

# ============================================================================
# Bad End: 錯過
# ============================================================================

label ending_template_bad:
    scene bg plaza_night

    narrator "你在資訊廣場遊蕩，卻始終沒有找到那個傳說中的角色。"

    narrator "時間就這樣流逝..."

    narrator "當你回到現實時，你只記得模糊的印象——好像有一個人在某處等你。"

    narrator "但你已經不記得是誰，也不記得在哪裡。"

    narrator "【DLC 結局：錯過】"
    narrator "有些相遇，錯過了就是錯過了。"

    $ record_ending("ending_template_bad")

    jump ending_final_ack
