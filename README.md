# FastAPI + Vue 骨架

一个带一键验收与规则护栏的 FastAPI + Vue 全栈骨架。

## 开发环境
- 后端：Python 3.12 + uv（`backend/`）
- 前端：Vue 3 + Vite + pnpm（`frontend/`）

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