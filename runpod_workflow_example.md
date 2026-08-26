## Setup
Rent an RTX 3090 instance from [RunPod](https://www.runpod.io).
```
Specs:
GPU: RTX 3090 24GB
Template: Runpod PyTorch 2.1.0（Python 3.10，CUDA 11.8.0)
```

```bash
pip install e .
pip install onnx --break-system-packages
pip install "fishaudio[utils]" --break-system-packages
apt update && apt install unzip && apt install -y wget
cd /workspace
wget https://huggingface.co/drewThomasson/unidic_3.1.0_backup/resolve/main/unidic-3.1.0.zip
unzip -j /workspace/unidic-3.1.0.zip -d /usr/local/lib/python3.10/dist-packages/unidic/dicdir
touch /usr/local/lib/python3.10/dist-packages/unidic/dicdir/mecabrc
pip install matplotlib==3.7.3
```
## Prepare data
- prepare training data from fish audio use your API Key, VOICE_ID and SENTENCES
```bash
cd melo
python fish_audio.py
```
- preprocess text
```bash
python preprocess_text.py --metadata data/guga/metadata.list 
```
- prepare pretrained weights
```bash
wget -O G_zh.pth https://huggingface.co/myshell-ai/MeloTTS-Chinese/resolve/main/checkpoint.pth

```

## Fine tune base on G_zh.pth
```bash
torchrun --nproc_per_node=1 train.py \
  -c data/guga/config.json \
  -m guga \
  --pretrain_G G_zh.pth
```
## Export onnx
original code: https://github.com/k2-fsa/sherpa-onnx/blob/master/scripts/melo-tts/export-onnx.py
```bash
python export_onnx.py \
  --checkpoint ./logs/guga/G_4000.pth \
  --config ./logs/guga/config.json \
  --output ./guga.onnx
```