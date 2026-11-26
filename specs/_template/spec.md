# NNN — <一句话标题>

> 开卡日期：<YYYY-MM-DD> ｜ 文件地图：`log.md`

## 背景与目标
<为什么做、做完之后什么变了。1-3 条，按优先级。>

## 验收标准（DoD）
做完一项就把 `[ ]` 改成 `[x]`。第一条固定不变。

- [ ] `uv run python scripts/check.py` 退出码 0，输出贴进文末「验收记录」
- [ ] <可被判定的结果，不要写"代码质量好"这种无法验收的话>
- [ ] <每个新行为至少一条>

## 范围

```scope
# 优先写具体文件路径；确实整个目录才写 glob。改这里之外的文件 guard 会拦。
backend/src/app/tools/codex.py
backend/tests/test_codex.py
```

反例（等于没写范围，会被后续卡沿用而失控）：`backend/**`

## 边界用例（实现时必须想到）
1. <空值 / 缺参 / 超长>
2. <重复调用 / 幂等>
3. <权限 / 并发>

## 不做（明确划界）
- <这次明确不碰的东西，防止 AI 顺手扩张>

## 验收记录

命令：`uv run python scripts/check.py`

```text
待填
```
