import os
import torch
from melo.api import TTS

config_path = "/home/duai/projects/MeloTTS/data/guga/config.json"
ckpt_path = "/home/duai/projects/MeloTTS/melo/G_4000.pth" 

print("🧠 正在載入官方底座 (4語言、11音調)...")
# 2. 初始化
model = TTS(language='ZH', config_path=config_path, ckpt_path=ckpt_path)
print(f"📊 實際的說話人清單: {model.hps.data.spk2id}")

spk_id = model.hps.data.spk2id['Guga']

text = "我天天带着八个充电宝来单位，充不满不走，老板看不下去了，强迫我下班"
output_path = "g4000_base_test.wav"

print(f"🗣️ 準備合成語音: {text}")
model.tts_to_file(text, spk_id, output_path)

print(f"✅ 成功！音檔已儲存至: {os.path.abspath(output_path)}")