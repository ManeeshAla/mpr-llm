import os
import sys
import glob
import torch
import torch.optim as optim
from tqdm import tqdm

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from dataset.dataloader import get_dataloader
from model.transformer import MicroLLM, MicroLLMConfig


def get_latest_checkpoint(ckpt_dir="checkpoints"):
    pattern = os.path.join(ckpt_dir, "micro_llm_epoch_*.pt")
    files = glob.glob(pattern)
    if not files:
        return None
    return max(files, key=os.path.getmtime)


def train(epochs=3, batch_size=32, seq_len=128, resume=True):
    device = torch.device("cpu")
    print(f"Training on device: {device}")

    print("Initializing Data Loader...")
    loader, tokenizer = get_dataloader(batch_size=batch_size, seq_len=seq_len)
    vocab_size = tokenizer.n_vocab

    config = MicroLLMConfig(
        vocab_size=vocab_size,
        block_size=seq_len,
        n_layer=4,
        n_head=4,
        n_embd=128,
        dropout=0.1,
        bias=False
    )
    model = MicroLLM(config)
    optimizer = optim.AdamW(model.parameters(), lr=3e-4, weight_decay=1e-2)

    start_epoch = 1
    os.makedirs("checkpoints", exist_ok=True)
    ckpt_path = get_latest_checkpoint("checkpoints")

    if resume and ckpt_path:
        print(f"\n[RESUME] Loading checkpoint: {ckpt_path}")
        checkpoint = torch.load(ckpt_path, map_location=device, weights_only=False)
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        start_epoch = checkpoint['epoch'] + 1
        print(f"[RESUME] Continuing from Epoch {start_epoch}  "
              f"(previous loss: {checkpoint['loss']:.4f})\n")
    else:
        print("\n[NEW] Starting training from scratch...\n")

    model.to(device)
    total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Model: {total_params:,} parameters (~{total_params/1e3:.0f}K)")
    print(f"Running {epochs} epoch(s) starting from Epoch {start_epoch}\n")

    end_epoch = start_epoch + epochs - 1
    for epoch in range(start_epoch, end_epoch + 1):
        model.train()
        total_loss = 0
        progress_bar = tqdm(loader, desc=f"Epoch {epoch}/{end_epoch}")

        for x, y in progress_bar:
            x, y = x.to(device), y.to(device)
            optimizer.zero_grad(set_to_none=True)
            _, loss = model(x, targets=y)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
            total_loss += loss.item()
            progress_bar.set_postfix(loss=f"{loss.item():.4f}")

        avg_loss = total_loss / len(loader)
        print(f"Epoch {epoch} done.  Avg Loss: {avg_loss:.4f}")

        save_path = os.path.join("checkpoints", f"micro_llm_epoch_{epoch}.pt")
        torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': avg_loss,
            'config': config
        }, save_path)
        print(f"Checkpoint saved → {save_path}\n")

    print("Training complete!")


if __name__ == "__main__":
    train(epochs=40, batch_size=32, seq_len=128, resume=True)
