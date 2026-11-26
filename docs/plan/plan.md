# 总计划

> 状态：v3 · 2026-11-26。本文件只回答「做什么、为什么这么切、按什么顺序」。
> 单卡细节在 `specs/NNN-*/spec.md`；前端 IA / 线框 / tokens 在 `docs/plan/frontend-plan.md`；
> 决策理由在 `docs/plan/decision-log.md`。
> 计划变更改本文件；决策理由改 decision-log.md；单卡范围改该卡 spec.md。本文件上限 200 行。

## 0. 这一版为什么重写

| 上一版的假设 | 实际情况 | v3 怎么改 |
|---|---|---|
| 主线是「配置管理器」：读配置、预设、切换、回滚 | CC Switch v4.0.42 已做字段级安全写入、原子写、备份、Session Manager；再做一遍是红海 | 配置只读；不写工具原生配置；改为「本机开发环境驾驶舱」 |
| 对话是配置面板的附属功能 | 用户要的是 VS Code 里 Claude Code 插件式的 CLI 对话；API 聊天等于重写 agent loop | CLI 优先；Claude Code 作为第一个运行时；exe 只打包 UI |
| 朋友会自己装 Node/Claude、自己配 key | 朋友不是开发者；没有 Claude 账号；国产模型更现实 | 全局 Node + 全局 Claude + 一键安装 + 国产 Anthropic 兼容 provider + Doctor |
| 危险操作可以在 app 里做 | 删环境变量、杀进程、卸载包都可能弄坏机器；没有回收站 | v1 只读；危险操作给 Windows 原生入口 + 文档；v1.1 再评估 |
| 19 卡 / 18.25 人日 | 范围已换，旧卡表失效 | 重切 10 卡 / 约 12.5 人日；v1.1 backlog 单列 |

## 1. 一句话产品

打开一个本地面板，先看清这台机器上的开发环境：Node / Claude Code 能不能用、AI CLI 接的是哪个模型、
环境变量 / 进程 / 端口 / 全局包是什么状态；再一键运行常用命令，或直接跟 Claude Code 对话。

## 2. 用户与场景

| 用户 | 场景 | v1 要给什么 |
|---|---|---|
| 我自己 | 每天开工前确认环境；改完 PATH 想知道有没有生效；不想记长命令 | 总览 + 环境变量只读 + Provider Doctor + 对话 |
| 朋友（非开发者） | 拿到一个 exe/setup，按向导装好，填国产模型 key，直接聊天 | Setup 向导 + Doctor 绿灯 + 示例仓库 + 5 分钟剧本 |
| 未来的我 | 加进程/端口/全局包/新 provider，不改核心 | ModuleSpec / ModuleDef / CommandSpec 扩展点 |

目标不是做长期产品，是「能自用、能演示、能扩展」。不追求日活、不追求多平台。

## 3. 六条策略

| 策略 | 含义 | 由此砍掉 |
|---|---|---|
| 只读优先 | v1 只看不做；删除/杀进程/卸载只给系统原生入口 + 文档 | app 内注册表写入、进程 kill、包卸载 |
| 全局运行时 | 用全局 Node + 全局 Claude Code；不做私有 runtime | 便携 Node、内置 CLI、运行时版本管理 |
| 不写工具配置 | 不碰 `~/.claude/settings.json` / `~/.codex/config.toml`；provider 只对子进程生效 | 预设 CRUD、diff、备份、原子写、回滚、冲突检测 |
| CLI 优先 | 聊天走 `claude -p --output-format stream-json`；不做 API chat | 自建 agent loop、工具协议、权限系统 |
| 模块化 | 后端 ModuleSpec/Module，前端 ModuleDef；CommandSpec 白名单 + danger | 单体大页面、功能之间直接 import |
| 可演示 | 5 分钟剧本；Doctor 绿灯；示例仓库；两台机器手动验收 | 只在自己机器上能跑的「作品」 |

## 4. 功能清单（编号不复用）

| 编号 | 功能 | 优先级 |
|---|---|---|
| F-01 | 工具链检测：Node / npm / Claude Code 的安装状态、版本、路径 | P0 |
| F-02 | Provider Registry：国产 Anthropic 兼容 provider + 自定义 | P0 |
| F-03 | Doctor：对话 / 流式 / tool use / 长上下文四项探测 | P0 |
| F-04 | CLI 对话：选 provider + 目录 → 流式回复、tool cards、停止/重试 | P0 |
| F-05 | L3 会话历史：本软件会话落盘 + 回放 | P0 |
| F-06 | 环境变量只读：User/Machine、搜索、PATH chips、密钥打码、复制/导出 | P0 |
| F-07 | 打开 Windows 环境变量对话框 + 修改教程 | P0 |
| F-08 | 模块壳 + 总览页 + `/styleguide` | P0 |
| F-09 | 一键安装：全局 Node + 全局 Claude Code + provider 配置 + Doctor | P0 |
| F-10 | exe + Setup 向导 + 5 分钟演示剧本 | P0 |
| F-11 | 进程 / 端口只读 | P1（v1.1） |
| F-12 | 全局 npm / pip 包只读 | P1（v1.1） |
| F-13 | 命令面板：白名单命令一键执行 | P1（v1.1） |
| F-14 | 工具原生配置只读（Claude / Codex） | P2（v1.1） |
| F-15 | 编辑/审批：Agent SDK `can_use_tool` | P2（v1.1） |
| F-16 | 更多 provider / 多工具对话 | P2（v1.2） |

非功能约束：N-1 仅 Windows；N-2 无数据库；N-3 不在仓库/日志里存明文 key；N-4 只绑定 localhost，不对外。

## 5. 范围

**v1 做**：F-01～F-10。一个 Claude Code runtime；Anthropic 兼容 provider；环境变量只读；全局 Node/Claude；exe + Setup；L3 历史。

**v1.1 做**：F-11～F-15。进程/端口/全局包只读、命令面板、工具配置只读、Agent SDK 编辑审批。

**v1.2 做**：F-16，以及杀进程/卸载包/环境变量删除的安全操作；先有备份/撤销/审计再开。

**v1 不做**：写工具原生配置；预设 CRUD/切换/回滚；L2 原生历史；Gemini/OpenCode；API chat；私有 Node runtime；多工具同时对话。

## 6. 领域模型与命名

    Toolchain : node, npm, claude; status, version, path
    Provider  : id, name, protocol=anthropic, base_url, model, key_ref, auth_style, docs_url
    Doctor    : provider_id, checks[{name,status,detail,latency_ms}], overall
    Chat      : id, provider_id, cwd, cli_session_id, status, messages
    EnvVar    : name, value_masked, scope(user|machine), kind, is_secret
    Module    : id, title, route, commands[], status
    Command   : id, argv[], danger(safe|caution|danger), timeout, cwd_policy

命名先定死：

| 词 | 只指 | 不指 |
|---|---|---|
| Provider | 一个 Anthropic 兼容 API 端点 + key 引用 + model | 工具厂商 / 模型厂商抽象层 |
| Toolchain | 全局 Node / npm / Claude Code | app 自带运行时 |
| Doctor | 对 provider 做兼容性探测 | 安装器 |
| Module | 一个可独立开关的功能单元 | Python module |
| Command | 白名单里的一个可执行动作 | 任意 shell 字符串 |
| Preset | **v1 不再使用**；旧计划的概念 | 现在的 Provider |

## 7. 状态矩阵

| 对象 | 状态 | UI | 下一步 |
|---|---|---|---|
| Toolchain | Node 缺失 / 过旧 / 正常 | 红 / 黄 / 绿 | 安装 / 升级 / 继续 |
| Toolchain | Claude 缺失 / 版本不兼容 / 正常 | 红 / 黄 / 绿 | 安装 / 升级 / 继续 |
| Provider | 未配置 / 未测试 / 测试中 / 通过 / 失败 | 灰 / 黄 / 蓝 / 绿 / 红 | 添加 / 测试 / 进 chat |
| Chat | 无 provider / 无目录 / 空闲 / 流式 / 退出 / 异常 | 禁用 / 禁用 / 可用 / 停止 / 可重试 / 红条 | 选 provider / 选目录 / 发送 |
| Env | 加载 / 空 / 错误 | 骨架 / 说明 / 红条 | 重试 / 打开系统对话框 |
| Env 打开对话框 | 成功 / 失败 | 提示 / 回退教程 | — |

## 8. 前端策略

不引组件库；IA → 线框 → tokens → 组件，全部在 `docs/plan/frontend-plan.md`。
v1 六个路由：`/` 总览、`/providers` 模型接入、`/chat` 对话、`/history` 历史、`/env` 环境变量、`/styleguide`。
`/system`（进程/端口/包）是 v1.1 预留，不进 v1 导航。
每张前端卡用 Playwright 截图存 `docs/design/shots/NNN-*.png`；`/styleguide` 是活规范。

## 9. 里程碑与任务卡

已完成：**001 骨架**。

| 编号 | 卡名 | 产出 / DoD | 依赖 | 预估 |
|---|---|---|---|---|
| **M0 验证** | | | | |
| 002 | CLI + 国产模型 spike | 干净 Windows：全局 Node + 全局 Claude + Anthropic 兼容端点（Node/Claude 可手工装，003 再自动化）；无 Claude 登录；stream-json 事件、tool use、resume、取消、中文编码；产出 `docs/spikes/chat-runtime.md` | 001 | 1.5d |
| **M1 环境与接入** | | | | |
| 003 | 工具链检测 + 一键安装 | Node/npm/Claude 检测；`install.bat` 全局安装 Node + Claude；版本/路径/错误归一；假 PATH 测试 | 001 | 1.5d |
| 004 | Provider Registry + Doctor | `provider.yaml` schema；对话/流式/tool use/长上下文测试；API + 页面；失败可读 | 002 | 1.5d |
| 005 | 环境变量只读 + 原生入口 | User/Machine 列表、PATH chips、密钥打码、复制/导出；`open-editor` 调 `rundll32`；教程 | 001 | 1d |
| 006 | 模块壳 + 总览 | ModuleSpec/ModuleDef；顶栏；总览卡；`/styleguide` 骨架 | 004、005 | 1d |
| **M2 对话** | | | | |
| 007 | CLI chat 后端 A | spawn Claude、stream-json 解析、事件归一、假 CLI 测试 | 002、004 | 1.5d |
| 008 | CLI chat 后端 B | SSE、取消/进程树终止、超时、错误归一 | 007 | 1.5d |
| 009 | Chat 前端 | 消息流、tool cards、上下文条、停止/重试、空/错状态 | 008 | 1.5d |
| 010 | L3 历史 | 会话落盘 + 历史页回放 | 009 | 1d |
| **M3 收口** | | | | |
| 011 | exe + Setup + 手动 E2E | PyInstaller、setup 向导、README、5 分钟剧本；两台机器验收 | 003、006、010 | 1d |

合计约 **12.5 人日**（±2）。每张卡 ≤ 1.5 天；超了就拆。

## 10. 需求覆盖矩阵

| 功能 | 落点卡 | 可观察的验收锚点 |
|---|---|---|
| F-01 | 003 | 删掉假 PATH 后总览显示「未安装 Node」，不是报错 |
| F-02 | 004 | 加一个 provider，重启后还在；key 不以明文回显 |
| F-03 | 004 | 四项探测各有 pass/fail；失败显示具体检查项 |
| F-04 | 007、008、009 | 发一句话，字符逐段出现；停止后进程树里查不到子进程 |
| F-05 | 010 | 重开 app，历史页能看到上次会话并回放 |
| F-06 | 005 | User/Machine 两个 scope 正确；密钥默认打码；PATH 拆成条目 |
| F-07 | 005 | 点按钮打开 Windows 环境变量对话框；失败回退教程 |
| F-08 | 006 | 六个路由可达；`/styleguide` 显示所有 tokens |
| F-09 | 003、004、011 | 干净 Windows 上双击 setup，Doctor 绿灯 |
| F-10 | 011 | 朋友按剧本 5 分钟跑通一次对话 |

## 11. 依赖顺序

```text
001 → 002 → 004 → {006, 007}
001 → 003 → 011
001 → 005 → 006
007 → 008 → 009 → 010
{003, 006, 010} → 011
```

关键路径：002 → 004 → 007 → 008 → 009 → 010 → 011。

## 12. 每张卡的节奏

1. 开工前：把 `spec.md` 的 scope + DoD 写成 5 行摘要发给你，你点头才开工。
2. 做完：贴 `uv run python scripts/check.py` 完整输出 + 「这张卡你应该能解释的 3 个问题」。
3. 你过了才提交：一张卡一个 commit，`specs/CURRENT` 同步更新。
4. 30 分钟搞不定就停，按 `AGENTS.md` 第 6 条写 `PROGRESS.md`「未决问题」。

## 13. 待拍板

| 编号 | 问题 | 默认 | 改动影响 |
|---|---|---|---|
| D-1 | 第一家国产 Anthropic 兼容 provider | 先选一家明确支持 Messages API 的 | 不支持则加 LiteLLM，+2 卡 |
| D-2 | v1 做只读 plan 还是可编辑 | 只读 plan | 可编辑走 Agent SDK，+2 卡 |
| D-3 | key 存哪 | app 的 `config.yaml` 只存引用；明文只在本机 settings，不进 git | 存明文要加加密/脱敏卡 |
| D-4 | exe 打包工具 | PyInstaller | 换 Tauri/Electron 则前端重做 |
| D-5 | 进程/端口/包/命令面板 | v1.1 | 提前则 +4 卡 / +4 人日 |
| D-6 | L2 原生历史 | 不做 | 做则 +1.5 卡 |
| D-7 | UI 语言 | 中文 | — |

## 14. 风险与对策

| 风险 | 对策 |
|---|---|
| 国产 provider 的「兼容」只兼容普通对话，tool use 不可用 | 002 先测；Doctor 四项分级；tool use 失败降级为只读聊天 |
| Claude Code 对第三方端点仍要登录/onboarding | 002 在干净 Windows 验证；不行换 Codex CLI + OpenAI 兼容端点 |
| 全局 Node 版本冲突 / PATH 污染 | 003 只检测不静默升级；环境变量页展示 PATH；文档写清 |
| `.cmd` shim、进程树、UTF-8 | 007/008 用 `cmd /c` + psutil 进程树 + 显式 encoding；假 CLI 测试 |
| exe 打包后路径/参数变化 | 011 用打包产物跑 5 分钟剧本，不用开发模式验收 |
| 计划再次膨胀 | 新需求先进第 13 节；本文件超 200 行就砍 |