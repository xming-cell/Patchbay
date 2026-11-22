# 001 — 骨架可验收

## 背景与目标
1. 后端能起、`/api/health` 返回 ok，且有 1 个通过的测试。
2. 前端能起、首页显示 `Health: ok`，`type-check` / `lint` / `vitest` 全绿。
3. 一条命令 `uv run python scripts/check.py` 能同时验完后端与前端，且改错范围会被拦住。

## 验收标准（DoD）
- `uv run python scripts/check.py` 退出码 0，输出里能看到 `guard scope`、`guard forbidden`
  以及前后端共 7 道检查，最后一行是 `All checks passed.`。
- `cd backend; uv run uvicorn app.main:app --reload` 后 `/api/health` 返回 `{"status":"ok"}`。
- `cd frontend; pnpm dev` 后首页显示 `Health: ok`。
- `specs/CURRENT` 指向本卡时，在 `scope` 之外新增文件会让 `guard scope` 失败。

## 范围

```scope
.gitattributes
.gitignore
.env.example
README.md
AGENTS.md
PROGRESS.md
TROUBLESHOOTING.md
rules/**
scripts/**
specs/**
docs/**
.github/**
backend/**
frontend/**
```

首次提交前所有文件都处于「未跟踪」状态，`guard scope` 会逐个比对，
所以这张卡的 scope 必须覆盖骨架里的**全部**路径；从 002 开始才收窄到具体模块。

## 边界用例（实现时必须想到）
1. 仓库还没有任何 commit（无 `HEAD`）时，`guard scope` 不能崩。
2. `specs/CURRENT` 写成 `none` 时，`guard scope` 跳过而不是失败。
3. `spec.md` 里没有 scope 块时，`guard scope` 必须失败，不允许「默认全放行」。

## 不做（明确划界）
- 不接数据库、不接鉴权、不做部署脚本。
- 不引入 e2e / Playwright。