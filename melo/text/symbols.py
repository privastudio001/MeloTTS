# 官方標準標點符號
punctuation = ["!", "?", "…", ",", ".", "'", "-"]
pu_symbols = punctuation + ["SP", "UNK"]
pad = "_"

# 這裡只保留 ZH, JP, EN 的符號，徹底砍掉韓文、法文、德文、俄文
zh_symbols = ["E", "En", "a", "ai", "an", "ang", "ao", "b", "c", "ch", "d", "e", "ei", "en", "eng", "er", "f", "g", "h", "i", "i0", "ia", "ian", "iang", "iao", "ie", "in", "ing", "iong", "ir", "iu", "j", "k", "l", "m", "n", "o", "ong", "ou", "p", "q", "r", "s", "sh", "t", "u", "ua", "uai", "uan", "uang", "ui", "un", "uo", "v", "van", "ve", "vn", "w", "x", "y", "z", "zh", "AA", "EE", "OO"]
ja_symbols = ["N", "a", "a:", "b", "by", "ch", "d", "dy", "e", "e:", "f", "g", "gy", "h", "hy", "i", "i:", "j", "k", "ky", "m", "my", "n", "ny", "o", "o:", "p", "py", "q", "r", "ry", "s", "sh", "t", "ts", "ty", "u", "u:", "w", "y", "z", "zy"]
en_symbols = ["aa", "ae", "ah", "ao", "aw", "ay", "b", "ch", "d", "dh", "eh", "er", "ey", "f", "g", "hh", "ih", "iy", "jh", "k", "l", "m", "n", "ng", "ow", "oy", "p", "r", "s", "sh", "t", "th", "uh", "uw", "V", "w", "y", "z", "zh"]

# 合併符號 (這會精確等於 112 個)
normal_symbols = sorted(set(zh_symbols + ja_symbols + en_symbols))
symbols = [pad] + normal_symbols + pu_symbols

# 鎖定維度 (對齊 G_zh.pth)
num_zh_tones = 6
num_ja_tones = 1
num_en_tones = 4
num_tones = num_zh_tones + num_ja_tones + num_en_tones # 剛好 11

# 鎖定語言數
language_id_map = {"ZH": 0, "JP": 1, "EN": 2, "ZH_MIX_EN": 3}
num_languages = len(language_id_map.keys()) # 剛好 4

# 偏移量地圖
language_tone_start_map = {
    "ZH": 0,
    "ZH_MIX_EN": 0,
    "JP": num_zh_tones,
    "EN": num_zh_tones + num_ja_tones,
}