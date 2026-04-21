import torch, glob
ckpts = sorted(glob.glob('checkpoints/micro_llm_epoch_*.pt'))
for ckpt in ckpts:
    c = torch.load(ckpt, map_location='cpu', weights_only=False)
    print(f"Epoch {c['epoch']:>2}  |  Loss: {c['loss']:.4f}")
