# CC Hub

本机开发环境驾驶舱：看清 Node / npm / Claude Code 和 Provider 状态，在浏览器里直接和 Claude Code 对话。
不写工具原生配置；Provider 只注入本次 CLI 子进程；环境变量只读，修改交给 Windows 原生对话框。

> 当前状态：v3 计划已重写，**尚未实现新功能**。仓库里目前只有 001 骨架（后端 `/api/health` + 前端首页）。
> 计划见 `docs/plan/plan.md`，决策见 `docs/plan/decision-log.md`，前端三章见 `docs/plan/frontend-plan.md`。

## v1 目标

- 工具链检测：Node / npm / Claude Code 的版本、路径、缺失项。
- Provider 接入：只接原生 Anthropic 兼容端点，保存 `base_url` / `model` / `key_ref`，Doctor 测对话、流式、tool use、长上下文。
- 对话：选 Provider + 目录，启动 Claude Code CLI，流式展示，可停止；v1 先只读 `plan` 模式。
- 环境变量：User / Machine 只读列表，PATH 拆条，密钥打码；提供「打开 Windows 环境变量」按钮和教程。
- 历史：本软件自己的 L3 会话记录，只读回放。
- 交付：Windows 上可双击的 exe + Setup 向导 + 手动 E2E。

v1 不做：写工具原生配置、杀进程/卸载、进程/端口/全局包面板、API 直连聊天、逐次权限审批。
这些在 `plan.md` 的 v1.1 / v1.2 里。

## 开发环境

- 后端：Python 3.12 + uv（`backend/`）
- 前端：Vue 3 + Vite + pnpm（`frontend/`）
- 运行时前置（v1 目标，不是当前骨架的要求）：Windows 10/11、Node.js 20+、全局 Claude Code
  （`npm install -g @anthropic-ai/claude-code`）。安装器尚未实现。

## 本地启动

```powershell
# 终端 1：后端
cd backend
uv sync
uv run uvicorn app.main:app --reload --port 8000

# 终端 2：前端
cd frontend
pnpm install
pnpm dev
```

后端接口文档：`http://127.0.0.1:8000/docs`；前端：`http://localhost:5173`。

## 验收

```powershell
uv run python scripts/check.py
```

退出码 0 才算完成。规则见 `rules/`，任务卡见 `specs/`，交接状态见 `PROGRESS.md`。

Agent 的读取顺序写在 `AGENTS.md`：`specs/CURRENT` → 该卡 `spec.md` → 该卡 `log.md`
→ `PROGRESS.md` → 按需读 `rules/`。要查某个功能改了哪些文件，看自动生成的
`docs/plan/file-map.md`（`uv run python scripts/map.py` 重建）。