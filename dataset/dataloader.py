import os
import json
import torch
from torch.utils.data import Dataset, DataLoader

import tiktoken

class BPETokenizer:
    """
    A full Byte-Pair Encoding (BPE) tokenizer using OpenAI's tiktoken (GPT-2 standard).
    This replaces the old char-level tokenizer, expanding vocab to 50,257.
    """
    def __init__(self):
        self.enc = tiktoken.get_encoding("gpt2")
        self.n_vocab = self.enc.n_vocab
        self.eot_token = self.enc.eot_token

    def encode(self, text):
        return self.enc.encode_ordinary(text)

    def decode(self, ids):
        return self.enc.decode(ids)


class SchoolBusinessDataset(Dataset):
    def __init__(self, data_file, seq_len=128, stride=None):
        self.seq_len = seq_len
        # stride: how many tokens to jump between samples.
        # stride=1   → one sample per character (254K batches, ~9h)
        # stride=seq_len → non-overlapping chunks (~500 batches, ~5 min) ✅
        self.stride = stride if stride is not None else seq_len

        print(f"Loading dataset from {data_file}...")
        raw_text = self._load_raw_text(data_file)

        # Build BPE tokenizer
        self.tokenizer = BPETokenizer()
        print(f"Vocab size (tiktoken): {self.tokenizer.n_vocab}")

        print("Tokenizing...")
        self.tokens = torch.tensor(self.tokenizer.encode(raw_text), dtype=torch.long)
        total = len(self.tokens)
        num_samples = max(1, (total - seq_len) // self.stride)
        print(f"Total tokens : {total:,}")
        print(f"Stride       : {self.stride}  →  {num_samples:,} training samples")


    def _load_raw_text(self, data_file):
        lines = []
        with open(data_file, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip():
                    continue
                record = json.loads(line)
                text = record.get("text", "")
                lines.append(text)
        # Join all Q&A pairs separated by a null byte (used as end-of-text marker)
        return '\x00'.join(lines)

    def __len__(self):
        return max(1, (len(self.tokens) - self.seq_len) // self.stride)

    def __getitem__(self, idx):
        start = idx * self.stride
        chunk = self.tokens[start: start + self.seq_len + 1]
        x = chunk[:-1]
        y = chunk[1:]
        return x, y


def get_dataloader(batch_size=32, seq_len=128, stride=None):
    """
    stride=None  → defaults to seq_len (non-overlapping, fast ~5-10 min/epoch)
    stride=1     → every character start (original slow mode, ~9h/epoch)
    """
    data_file = os.path.join(os.path.dirname(__file__), "school_business_data.jsonl")
    dataset = SchoolBusinessDataset(data_file, seq_len, stride=stride)

    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=True,
        drop_last=True
    )
    return dataloader, dataset.tokenizer


if __name__ == "__main__":
    loader, tokenizer = get_dataloader(batch_size=2, seq_len=64)
    print(f"Vocab size: {tokenizer.n_vocab}")
    for x, y in loader:
        print(f"X shape: {x.shape}, Y shape: {y.shape}")
        break
