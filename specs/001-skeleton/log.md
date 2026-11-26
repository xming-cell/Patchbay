# 001 文件地图

> 骨架卡，登记的是建仓时落地的文件。

| 文件 | 动作 | 作用（一句话） |
|---|---|---|
| AGENTS.md | 新建 | 硬性约定：命令、读取顺序、开卡/收卡、零例外 |
| README.md | 新建 | 项目说明与本地启动方式 |
| PROGRESS.md | 新建 | 当前状态 / 未决问题 / 下一步，上限 60 行 |
| TROUBLESHOOTING.md | 新建 | 现象 → 原因 → 解决，只增不删 |
| .gitattributes | 新建 | 固定 `* text=auto eol=lf`，避免 CRLF 误报越界 |
| .gitignore | 新建 | 忽略 `.venv` / `node_modules` / `*.db` / `.env` |
| rules/backend.md | 新建 | 后端分层（api → services → repositories）与接口约定 |
| rules/frontend.md | 新建 | 前端请求 / 状态 / 组件约束 |
| rules/testing.md | 新建 | 测试顺序、只测行为、边界必须覆盖 |
| rules/git.md | 新建 | 提交粒度与消息格式 |
| scripts/guards.py | 新建 | `scope` / `forbidden` / `spec` 三道门禁 |
| scripts/check.py | 新建 | 一键验收，串起全部检查 |
| scripts/map.py | 新建 | 合并各卡 `log.md` 生成 `docs/plan/file-map.md`（v2 追加） |
| docs/plan/plan.md | 新建 | 总计划、里程碑、覆盖矩阵、待拍板（替代 test-plan.md） |
| docs/plan/frontend-plan.md | 新建 | 前端 IA / 线框 / tokens 三章 |
| docs/plan/decision-log.md | 新建 | ADR 决策日志 |
| docs/plan/file-map.md | 新建 | 由 `map.py` 自动生成的总索引，勿手改 |
| backend/pyproject.toml | 新建 | 后端依赖与 ruff / mypy / pytest 配置 |
| backend/uv.lock | 新建 | 依赖锁文件 |
| backend/src/app/main.py | 新建 | FastAPI 应用入口，挂载 `/api` 路由 |
| backend/src/app/api/health.py | 新建 | `GET /api/health` 返回 `{"status":"ok"}` |
| backend/src/app/core/config.py | 新建 | 应用配置读取 |
| backend/tests/test_health.py | 新建 | health 端点测试 |
| frontend/package.json | 新建 | 前端依赖与脚本（type-check / lint / vitest） |
| frontend/vite.config.ts | 新建 | dev server 与 `/api` 代理 |
| frontend/vitest.config.ts | 新建 | 前端单测配置 |
| frontend/index.html | 新建 | Vite 入口 HTML |
| frontend/src/main.ts | 新建 | 挂载 Vue 应用 |
| frontend/src/App.vue | 新建 | 根组件 |
| frontend/src/style.css | 新建 | 全局样式 |
| frontend/src/router/index.ts | 新建 | 路由表 |
| frontend/src/api/client.ts | 新建 | 统一请求封装与 `ApiError` 归一 |
| frontend/src/views/HomeView.vue | 新建 | 首页，显示 `Health: ok` |
| frontend/src/__tests__/App.spec.ts | 新建 | 首页渲染测试 |
| .github/workflows/ci.yml | 新建 | 三平台 CI：后端 lint / 类型 / 测试 + 前端类型 / lint / 测试 |

## 本卡消耗

| 项 | 值 |
|---|---|
| 输入 / 输出 token | 未记录（v2 之前的卡没有记账） |
| 工具调用次数 | 未记录 |
| 会话数 | 多 |
