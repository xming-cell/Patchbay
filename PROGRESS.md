# PROGRESS

> 只写三块，上限 60 行（`guard spec` 会拦）。已完成的事看 `git log` 和各卡的 `spec.md`。

## 当前状态
- 001 骨架已验收：后端 `/api/health` + 1 个测试；前端首页显示 `Health: ok`；`check.py` 全绿；CI 三平台接通。
- v3 计划已重写（2026-11-26）：产品改为「本机开发环境驾驶舱」，范围切成 v1 10 卡 / 约 12.5 人日；
  `plan.md`、`decision-log.md`、`frontend-plan.md`、`README.md` 已同步。**尚未写新功能代码。**
- 最后更新：2026-11-26

## 未决问题
- 002 卡尚未创建，`specs/CURRENT` 仍为 001。
- 第一家国产 Anthropic 兼容厂商尚未选定（002/004 要定）。
- exe 打包方案（PyInstaller 或其他）尚未验证。

## 下一步
- 按 `docs/plan/plan.md` 开 002（CLI + 国产模型 spike）：先复制 `specs/_template/`，填 `spec.md` / `log.md`，
  再把 `specs/CURRENT` 改成 002；不要直接写代码。
- 002 之后：004（Provider Registry + Doctor）依赖 002；003（工具链检测 + 一键安装）只依赖 001，可并行。