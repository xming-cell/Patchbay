# 文件地图（自动生成，勿手改）

> 由 `uv run python scripts/map.py` 从各卡的 `specs/<卡>/log.md` 合并生成。
> 修 bug 的顺序：本表查文件 -> 拿到卡号 -> 读 `specs/<卡>/spec.md`。
> 覆盖 1 张卡、34 行。

| 文件 | 卡 | 动作 | 作用 |
|---|---|---|---|
| .gitattributes | 001 | 新建 | 固定 `* text=auto eol=lf`，避免 CRLF 误报越界 |
| .github/workflows/ci.yml | 001 | 新建 | 三平台 CI：后端 lint / 类型 / 测试 + 前端类型 / lint / 测试 |
| .gitignore | 001 | 新建 | 忽略 `.venv` / `node_modules` / `*.db` / `.env` |
| AGENTS.md | 001 | 新建 | 硬性约定：命令、读取顺序、开卡/收卡、零例外 |
| PROGRESS.md | 001 | 新建 | 当前状态 / 未决问题 / 下一步，上限 60 行 |
| README.md | 001 | 新建 | 项目说明与本地启动方式 |
| TROUBLESHOOTING.md | 001 | 新建 | 现象 → 原因 → 解决，只增不删 |
| backend/pyproject.toml | 001 | 新建 | 后端依赖与 ruff / mypy / pytest 配置 |
| backend/src/app/api/health.py | 001 | 新建 | `GET /api/health` 返回 `{"status":"ok"}` |
| backend/src/app/core/config.py | 001 | 新建 | 应用配置读取 |
| backend/src/app/main.py | 001 | 新建 | FastAPI 应用入口，挂载 `/api` 路由 |
| backend/tests/test_health.py | 001 | 新建 | health 端点测试 |
| backend/uv.lock | 001 | 新建 | 依赖锁文件 |
| docs/plan/decision-log.md | 001 | 新建 | ADR 决策日志 |
| docs/plan/file-map.md | 001 | 新建 | 由 `map.py` 自动生成的总索引，勿手改 |
| docs/plan/test-plan.md | 001 | 新建 | 总计划、里程碑、待拍板清单 |
| frontend/index.html | 001 | 新建 | Vite 入口 HTML |
| frontend/package.json | 001 | 新建 | 前端依赖与脚本（type-check / lint / vitest） |
| frontend/src/App.vue | 001 | 新建 | 根组件 |
| frontend/src/__tests__/App.spec.ts | 001 | 新建 | 首页渲染测试 |
| frontend/src/api/client.ts | 001 | 新建 | 统一请求封装与 `ApiError` 归一 |
| frontend/src/main.ts | 001 | 新建 | 挂载 Vue 应用 |
| frontend/src/router/index.ts | 001 | 新建 | 路由表 |
| frontend/src/style.css | 001 | 新建 | 全局样式 |
| frontend/src/views/HomeView.vue | 001 | 新建 | 首页，显示 `Health: ok` |
| frontend/vite.config.ts | 001 | 新建 | dev server 与 `/api` 代理 |
| frontend/vitest.config.ts | 001 | 新建 | 前端单测配置 |
| rules/backend.md | 001 | 新建 | 后端分层（api → services → repositories）与接口约定 |
| rules/frontend.md | 001 | 新建 | 前端请求 / 状态 / 组件约束 |
| rules/git.md | 001 | 新建 | 提交粒度与消息格式 |
| rules/testing.md | 001 | 新建 | 测试顺序、只测行为、边界必须覆盖 |
| scripts/check.py | 001 | 新建 | 一键验收，串起全部检查 |
| scripts/guards.py | 001 | 新建 | `scope` / `forbidden` / `spec` 三道门禁 |
| scripts/map.py | 001 | 新建 | 合并各卡 `log.md` 生成 `docs/plan/file-map.md`（v2 追加） |
