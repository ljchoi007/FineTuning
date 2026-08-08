# Becoming AI Native — Model Engineering Checklist

A self-directed path from using AI to understanding it: **model internals, training, fine-tuning, evaluation**, plus enough **conceptual fluency** to follow and judge current research. Nothing is assumed — the basics aren't skipped. Checklist, not a calendar.

**Tags:** `P0` must-do · `P1` high-ROI (do after P0 or in training dead time) · `P2` skim (know the word, don't sink time).

**Rules:** end every P0 in code / a loss curve / an eval / a written answer · hand-write the first loops, no copilot where it makes you passive · track tensor shapes (most confusion is shape confusion) · keep a `model-notes.md` with one-line answers to each self-check.

```
COMMON CORE (sequential, first) ── fork ──┬── TRACK A · Fluency   (any-order, read-paced)
                                          └── TRACK B · Hands-On  (strictly sequential)
```

- **Run Track B as the spine; fill its training dead time with Track A reading.** That's the parallelism.
- **Month-one target:** Common Core + Track B §B0–B3 (P0) + Track A P0 vocabulary. Everything else is the tail.

---

# 🟦 COMMON CORE — do first, in order

- [ ] `P0` **3Blue1Brown — Neural Networks (the "Deep Learning" series), in full** — visual intuition for neurons, gradient descent, backprop, and transformers/attention. → [3Blue1Brown](https://www.3blue1brown.com/topics/neural-networks). *Self-check: how can changing one weight lower the loss? For one token, what are Q/K/V doing?*
- [ ] `P0` 🏁 **Karpathy — Neural Networks: Zero to Hero, in full (hand-type the code)** — autograd/backprop, PyTorch tensors, cross-entropy/next-token, training diagnostics, tokenization, and a from-scratch GPT. This is the write-by-hand gate and gives you a raw training loop. → [Zero to Hero](https://karpathy.ai/zero-to-hero.html) · [nanoGPT](https://github.com/karpathy/nanoGPT) · supplement [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) if tensor mechanics feel shaky. *Milestone: a hand-built decoder-only transformer you can explain submodule by submodule, trained to a decreasing loss. (The closing "reproduce GPT-2 (124M)" is the heaviest part and doubles as a later Track B scaling lesson — fine to defer.)*
- [ ] `P0` **Model autopsy** — the one Common Core piece neither series covers: inspect a small HF causal LM as an object, not magic. → [Transformers docs](https://huggingface.co/docs/transformers/index). *Milestone: print `config`, `named_parameters()`, layer/hidden/head/vocab sizes; locate embeddings, attention projections, MLP, layer norms, output head.*

---

# 🟩 TRACK A — Conceptual Fluency

*Parallel to B, mostly any-order. Kept deliberately lean — the goal is recognition-level fluency, not mastery.*

### A1 · Architecture vocabulary
- [ ] `P0` **Why transformers won** — lead with short dependency paths + parallel processing + scaling, *not* just "vanishing gradients." → [Attention Is All You Need](https://arxiv.org/abs/1706.03762). *Self-check: contrast RNN / LSTM / encoder-decoder / decoder-only, and why decoder-only dominates LLMs.*
- [ ] `P1` **Context cost & position** — O(n²) attention, KV cache, FlashAttention; sinusoidal/learned/RoPE/ALiBi. → [RoFormer (RoPE)](https://arxiv.org/abs/2104.09864) · [FlashAttention](https://arxiv.org/abs/2205.14135). *Self-check: why is attention order-agnostic without positional info?*

### A2 · Training & post-training vocabulary
- [ ] `P0` **Mixture of Experts** — router, top-k, sparse activation, total vs active params, expert collapse / load balancing. → [HF MoE explainer](https://huggingface.co/blog/moe) · [Mixtral](https://arxiv.org/abs/2401.04088) · [Switch](https://arxiv.org/abs/2101.03961). *Self-check: why is "1% active" not safe to claim generally? (Mixtral is ~13B/47B ≈ 28%.) How do experts differ from attention heads?*
- [ ] `P0` **Distillation** — teacher/student, soft logits, response vs CoT vs feature distillation, black-box vs white-box. → [Hinton et al.](https://arxiv.org/abs/1503.02531) · [Distilling Step-by-Step](https://arxiv.org/abs/2305.02301). *Self-check: name five variants and the access each needs.*
- [ ] `P0` **SFT / RLHF / preference optimization** — reward model, PPO/GRPO, DPO/KTO/ORPO. → [The RLHF Book](https://rlhfbook.com/) · [DPO](https://arxiv.org/abs/2305.18290) · [TRL](https://huggingface.co/docs/trl/index). *Self-check: SFT vs DPO vs PPO, one line each.*
- [ ] `P0` **Reward hacking + steering** — specification gaming, proxy metrics; steering vectors / representation engineering and where interventions happen. → [Spinning Up RL intro](https://spinningup.openai.com/) · [Representation Engineering](https://arxiv.org/abs/2310.01405). *Self-check: one concrete reward-hacking example; what layer would you intervene on?*

### A3 · Strategy & debate
- [ ] `P0` **The bottleneck** — compute vs data vs algorithms; the synthetic-data flywheel; the "data wall." → [Epoch AI — Will we run out of data?](https://epochai.org/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data). *Self-check: argue each bottleneck; why doesn't synthetic data trivially cause collapse?*
- [ ] `P1` **World models** — predict abstract latent states; work for video/3D/physical-AI, not (yet) language. → [Meta, V-JEPA](https://ai.meta.com/blog/v-jepa-yann-lecun-ai-model-video-joint-embedding-predictive-architecture/). *Self-check: why latent states over pixels — and why is language the hard case?*

### A4 · Skim only (`P2` — one pass, don't go deep)
- [ ] History/UAT (perceptrons, why depth matters) · active vs passive learning · continual learning & catastrophic forgetting ([EWC](https://arxiv.org/abs/1612.00796))
- [ ] Vision: [ViT](https://arxiv.org/abs/2010.11929), [CLIP](https://arxiv.org/abs/2103.00020), [MAE](https://arxiv.org/abs/2111.06377), VLM projector idea · LDA / topic models ([Blei et al.](https://www.jmlr.org/papers/v3/blei03a.html)) · MPC / inverse dynamics / model-based RL · [ARC-AGI](https://arcprize.org/) (humility check, not curriculum)

### A5 · Paper literacy (`P0`, continuous, light)
- [ ] One relevant paper/week, answered against this template:
```
Paper · Problem · Core idea · Why people care · What's actually new ·
Main experiment · Weakest assumption · What I'd ask the author ·
Real result or minor variation? · Relevance to your work
```
First set: [Attention](https://arxiv.org/abs/1706.03762) · [LoRA](https://arxiv.org/abs/2106.09685) · [QLoRA](https://arxiv.org/abs/2305.14314) · [Mixtral](https://arxiv.org/abs/2401.04088) · [DPO](https://arxiv.org/abs/2305.18290) · [CLIP](https://arxiv.org/abs/2103.00020).

---

# 🟧 TRACK B — Hands-On

*Parallel to A, but strictly sequential within. This is the spine.*

### B0 · Compute setup
- [ ] `P0` **Rent and control a GPU** — billing, volumes, images, shutdown. → [RunPod](https://www.runpod.io/) · [Vast](https://vast.ai/) · [Lambda](https://lambdalabs.com/). *Milestone: launch a box, train a toy model, save artifacts, shut down.*

### B1 · First fine-tune gate
- [ ] `P0` **Overfit a tiny batch first** — prove the model can memorize 100–500 examples. *Self-check: if it can't, what's broken?*
- [ ] `P0` **Full fine-tune a small causal LM** — any clean text; start 50–150M if struggling, target ~500M. Goal is a converging loss, not usefulness yet. → [HF training](https://huggingface.co/docs/transformers/training). *Milestone: logged train/val curve, checkpoint, exact config, short postmortem.*
- [ ] `P1` **Repeat with `Trainer`** — earn the framework after the raw loop. → [HF Trainer](https://huggingface.co/docs/transformers/training). *Milestone: same result, compare control vs convenience.*

### B2 · Training mechanics
- [ ] `P0` **Diagnostics** — train vs val, LR too high/low, exploding grads, bad init, data/tokenization bugs, leakage. → [Karpathy, A Recipe for Training NNs](https://karpathy.github.io/2019/04/25/recipe/). *Milestone: a one-page "loss isn't decreasing" checklist.*
- [ ] `P0` **Optimizers & memory** — AdamW, weight decay, grad clipping, warmup, cosine, effective batch; params/grads/optimizer-states/activations/KV-cache. → [CS336](https://cs336.stanford.edu/) · [HF perf guide](https://huggingface.co/docs/transformers/perf_train_gpu_one). *Milestone: estimate VRAM before a run, compare to actual peak.*
- [ ] `P1` **GPU survival** — mixed precision, gradient accumulation, gradient checkpointing, save/resume, sequence packing, W&B logging. → [HF perf guide](https://huggingface.co/docs/transformers/perf_train_gpu_one). *Milestone: same job with/without checkpointing, compare memory/time.*

### B3 · Fine-tuning ladder
- [ ] `P0` **Full fine-tune (all params)** — attention, MLP, layer norms, embeddings, output head all move. *Milestone: converges; inspect what changed.*
- [ ] `P0` **Segmented fine-tune** — freeze most, train one region (final/middle layers, attention projections, or head). *Self-check: what changes when only final layers move?*
- [ ] `P0` **LoRA** — freeze base, train low-rank adapters. → [LoRA](https://arxiv.org/abs/2106.09685) · [PEFT](https://huggingface.co/docs/peft/index). *Milestone: compare trainable params, VRAM, wall-clock, eval vs full FT.*
- [ ] `P0` **QLoRA** — 4-bit frozen base + LoRA. → [QLoRA](https://arxiv.org/abs/2305.14314) · [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes). *Milestone: fine-tune a model too big for comfortable full FT on your GPU.*
- [ ] `P1` **Continued pretraining** — same next-token machinery on unlabeled domain text; mostly semantic vs FT (random vs warm-start weights + more memory). → [HF causal LM](https://huggingface.co/docs/transformers/tasks/language_modeling). *Milestone: held-out domain perplexity improves.*
- [ ] `P1` **Framework pass** — only now: [Unsloth](https://github.com/unslothai/unsloth) / [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) / [Llama-Factory](https://github.com/hiyouga/LLaMA-Factory). *Milestone: reproduce a QLoRA result; compare speed/memory/ergonomics.*

### B4 · Eval & data (the difference between a real result and a fake one)
- [ ] `P0` **Train/val/test discipline + sample inspection** — held-out data, contamination, regression sets; read 20 good/bad generations and label failure modes. *Milestone: every FT has train loss + val loss + one task-level eval.*
- [ ] `P0` **Perplexity ≠ task metric** — lower perplexity can fail the real task. *Milestone: compare perplexity to a small hand-built task eval on one run.*
- [ ] `P1` **Dataset construction** — cleaning, dedup, filtering, packing, split, mixture weights. → [CS336 data lectures](https://cs336.stanford.edu/). *Milestone: a tiny cleaned dataset with a reproducible script + data card.*

### B5 · Joint embeddings & contrastive learning
- [ ] `P0` **Embedding + contrastive basics** — cosine/dot, normalization, NN search, InfoNCE, batch/hard negatives, temperature, collapse. → [Sentence Transformers](https://www.sbert.net/) · [CLIP](https://arxiv.org/abs/2103.00020). *Milestone: tiny embedding search over a small text or code corpus; inspect nearest neighbors.*
- [ ] `P0` **Train a small joint-embedding model** — map two related data types (e.g., queries ↔ code, or questions ↔ documents) into a shared space and retrieve across them. *Milestone: baseline vs trained retrieval, ablate hard negatives, inspect 20 errors. Self-check: when is training a joint embedding worth it over a pretrained, off-the-shelf one?*

### B6 · Inference & serving (the deployment half that's easy to skip)
- [ ] `P0` **Inference basics** — prefill vs decode, KV cache, batching, latency vs throughput. → [vLLM](https://docs.vllm.ai/). *Self-check: why does generation slow as context grows?*
- [ ] `P1` **Quantization for inference** — fp16/bf16/int8/int4, GPTQ/AWQ concepts, quality tradeoffs. → [HF quantization](https://huggingface.co/docs/transformers/quantization/overview). *Self-check: training vs inference quantization?*

---

## VRAM cheat-sheet
| Task | Rough VRAM |
|---|---|
| Full FT, 1B params | ~40 GB (~16 GB/1B: params + AdamW states + grads + activations) |
| LoRA, 8B | ~40 GB |
| QLoRA, 8B | ~12–24 GB |
| QLoRA, 65–70B | single 48–80 GB GPU |
| Pretraining from scratch | terabytes + multi-GPU |

*Drifts with framework/precision — re-check against current tooling.*

## Done when you can
- [ ] Explain a decoder-only transformer end-to-end without "magic."
- [ ] Hand-write a toy LM training loop; make loss converge on a small model.
- [ ] Full / segmented / LoRA / QLoRA the same task and explain what changed in each.
- [ ] Build a toy joint-embedding model and evaluate retrieval.
- [ ] Read a paper and say whether it's meaningful or incremental.
- [ ] Explain when to fine-tune vs continue pretraining vs use retrieval — with reasons, not buzzwords.
