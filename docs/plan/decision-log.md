# 决策日志

一条决策一条 ADR。只记**为什么**，不记怎么做（怎么做在代码和 `plan.md` 里）。
改主意不删旧条目，在条目末尾加「（已推翻 → ADR-NNN）」。
v3 重写日期：2026-11-26。ADR-005 起是本轮对话的决策；ADR-002 的部分内容已被调整。

## ADR-001 为什么用 uv + pnpm
- 背景：后端与前端各有一套工具链，需要可复现的锁文件与 CI 缓存。
- 决定：后端用 uv 管理 Python 3.12 依赖，前端用 pnpm 管理 Node 依赖。
- 代价：本地需安装 uv 与 pnpm；CI 需维护两套缓存配置。

## ADR-002 v1 纳入对话工作台（原计划不做）
- 背景：上一版把它列为 P2 且做砸了；`plan.md` 初稿的 D-1 默认值是「不做」。
- 决定：纳入 v1，明确「先 spike 真跑 CLI 再定契约」。
- 理由：这是用户明确要求做的功能；且它与环境面板共用同一套本机探测能力，拆开做等于返工。
- 代价：旧版总工期从约 10.5 人日涨到约 18 人日；风险集中在「接别人的 CLI」。
- （已调整 → ADR-005、ADR-011：v1 仍做对话，但不再是 6 张卡，也不再把配置管理作为主线。）

## ADR-003 前端不做设计工具，代码即设计稿
- 背景：上一版在 Penpot 画稿导 PNG，稿与代码是两套产物，最后一次翻译后走形。
- 已否决的方案：设计工具导出前端代码。理由：导出的是单屏像素还原、类名自动生成、无复用无响应式，
  只适合一次性静态页，不适合有状态的 app。
- 决定：IA → 线框 → tokens → 组件，四步都有文件产物，全部落在 `docs/plan/frontend-plan.md`。
  不引组件库，自建 3 个基础组件。
- 代价：视觉上限等于自己的审美；靠 tokens + 参照物 + 截图复盘来兜底，不靠设计灵感。

## ADR-004 总计划改名为 plan.md
- 背景：`test-plan.md` 这个名字与内容不符（内容是路线图，不是测试计划），且与「验收怎么测」混淆。
- 决定：改名 `docs/plan/plan.md`，上限 200 行；前端三个前置产物单独放 `frontend-plan.md`。
- 代价：旧引用需同步（已改 AGENTS.md、PROGRESS.md、001 的 log.md）。

## ADR-005 产品改为「本机开发环境驾驶舱」，不 fork CC Switch
- 背景：原主线是「AI CLI 配置管理器 + 对话」。复核 CC Switch v4.0.42 后确认它已经做了字段级安全写入、
  原子写、自动备份、Session Manager、MCP / Skills / 用量 / 会话等；再抄一遍配置层没有差异化，也不是用户想学的部分。
- 已否决的方案：
  1. fork CC Switch（Tauri 2 + Rust + React）加聊天页——要跟上游同步、维护整个桌面应用，学习目标变成 Rust/React；
  2. 读 `~/.cc-switch/cc-switch.db` 或内部 API 做插件——没有稳定插件 API，schema 会变，耦合脆弱。
- 决定：做独立 app，接口只依赖「CLI + 工具原生配置文件」，不依赖 CC Switch 的代码或数据库；
  产品定位改为「本机开发环境驾驶舱」：工具链、Provider 接入、环境变量、进程/端口/全局包、命令面板、对话。
- 理由：用户真正想要的是「看清本机环境 + 直接跑起来」，不是再做一个 CC Switch；竞品强不妨碍它作为练手项目。
- 代价：原 F-01～F-14、19 卡全部作废；v1 范围重切；进程/端口/包/命令面板推到 v1.1。

## ADR-006 不写工具原生配置，Provider 只注入子进程
- 背景：写 `~/.claude/settings.json` / `~/.codex/config.toml` 需要 diff、备份、原子写、回滚、冲突检测；
  CC Switch 已经做过，且 Codex 0.149 的凭据继承变更证明配置格式会随 CLI 版本漂移。
- 决定：v1 不写任何工具原生配置。用户在 app 里选 Provider，启动 Claude Code 子进程时注入
  `ANTHROPIC_BASE_URL` / `ANTHROPIC_AUTH_TOKEN`（或 `ANTHROPIC_API_KEY`）/ `ANTHROPIC_MODEL`；
  app 自己的 `config.yaml` 只存 Provider Registry 和本机设置。
- 理由：这是「只影响本次对话」的最小侵入方式；不需要写配置的权限，也不会弄坏用户原有环境。
- 代价：app 外启动的终端不会使用这个 Provider；没有「一键切换全局配置」；Provider 选择只对 app 内对话生效。

## ADR-007 CLI 对话优先，不做 API chat
- 背景：用户明确要 VS Code 里 Claude Code 插件式的体验；API chat 要自己重写 agent loop、工具调用、
  权限、diff、会话管理，等于把 CLI 再做一遍。
- 决定：聊天走 Claude Code CLI 的 `-p --output-format stream-json --verbose`；exe 只打包 UI，
  不打包 Claude Code 的安装、登录、账号。v1 先只读 `plan` 模式；v1.1 用 Agent SDK 的 `can_use_tool`
  做逐次允许/拒绝。
- 理由：agent 能力由 CLI 提供，app 专注「接入、展示、控制、记录」；这也是最容易做出 demo 的路径。
- 代价：朋友仍需安装 Claude Code；纯 CLI `-p` 的权限只能选 mode，做不到逐次审批；Windows 上要处理
  `.cmd` shim、进程树、UTF-8、SmartScreen。

## ADR-008 全局 Node + 全局 Claude Code，不做私有 runtime
- 背景：用户的机器已有全局 Node；产品定位是「看清本机环境」，私有 runtime 反而把环境藏起来；
  便携 Node + 本地 npm 安装会增加打包、升级、许可和路径维护成本。
- 决定：v1 使用全局 Node 与全局 Claude Code；安装器只负责检测、提示、调用 `winget`/MSI 和
  `npm install -g @anthropic-ai/claude-code`；不做内置 Node、不做私有 runtime。
- 理由：与「驾驶舱」定位一致；朋友装完后，其他终端也能用同一个 Node/Claude；卸载简单。
- 代价：需要 UAC/管理员；全局 Node 版本冲突和 PATH 污染要由 app 展示和文档兜底；不能保证隔离。

## ADR-009 国产模型只接 Anthropic 兼容端点，先不做通用转换
- 背景：朋友没有 Claude 账号；国产模型更现实。Claude Code 说 Anthropic Messages API；
  部分国产厂商提供原生 Anthropic 兼容端点，另一些只有 OpenAI 兼容。
- 决定：v1 只支持原生 Anthropic 兼容的 Provider；Provider Registry 记录
  `base_url / model / auth_style / key_ref / docs_url`；Doctor 测对话、流式、tool use、长上下文。
  OpenAI-only 的厂商先不做通用代理；需要时 v1.1 接 LiteLLM 或 claude-code-router。
- 理由：通用转换层会引入新的失败面（协议差异、tool call、流式、错误格式），不适合第一版。
- 代价：可选厂商变少；仍需要厂商 API key；「不用 Claude 账号」不等于「不用账号」；tool use 可能失败，
  失败时只能降级为只读聊天。

## ADR-010 环境变量 UI 只读，修改交给 Windows 原生对话框
- 背景：用户想要「查看环境变量，顺便删除」。但环境变量没有回收站；删错 `PATH` / `SystemRoot`
  会让 Node、npm、Claude 甚至 Windows 工具找不到；`setx` 有 1024 字符截断；已打开的进程不会更新；
  系统变量还要 UAC。
- 决定：v1 只做只读列表 + 搜索 + PATH chips + 密钥打码 + 复制/导出；提供
  「打开 Windows 环境变量」按钮（`rundll32.exe sysdm.cpl,EditEnvironmentVariables`）和教程；
  app 不写注册表、不提供删除按钮。PATH 条目清理也放到 v1.1 再评估。
- 理由：把「看清」和「修改」分开，责任边界清楚；与用户对杀进程「危险操作先给文档」的原则一致。
- 代价：用户要跳到系统对话框操作；app 不能校验、不能撤销；教程必须写清备份和生效范围。

## ADR-011 范围重切：v1 10 卡 / 约 12.5 人日
- 背景：旧计划 19 卡 / 18.25 人日是按「配置管理器 + 对话」估的；新定位和只读策略改变了工作量。
- 决定：v1 只做 F-01～F-10：CLI/Provider spike、工具链检测与安装、Provider Registry + Doctor、
  环境变量只读、模块壳、CLI chat 后端/前端、L3 历史、exe + Setup + 手动 E2E。
  进程/端口/全局包/命令面板/工具配置只读/编辑审批放 v1.1；更多 provider 放 v1.2。
- 理由：先把「朋友能装、能测、能聊」这条主链路打通；环境驾驶舱的其余模块用同一套 Module 机制增量加。
- 代价：v1 不包含用户最初提的进程/端口/全局包/命令面板；这些要在 v1.1 补，不能假装 v1 已覆盖。

## ADR-012 模块注册表 + CommandSpec 作为扩展点
- 背景：用户明确「可扩展性是最重要的」；后续要加进程、端口、包、命令、更多 provider。
- 决定：后端 `ModuleSpec` / `Module`，前端 `ModuleDef`；功能模块只注册路由、命令、导航和状态；
  `CommandSpec` 用白名单 argv + `danger(safe|caution|danger)`，不接受任意 shell 字符串。
- 理由：加模块不改核心；危险等级在注册表里显式声明，UI 和文档可以统一处理。
- 代价：要先定接口，v1 只能用 3～4 个模块验证；接口设计错了会返工。

## ADR-013 演示优先：5 分钟剧本是 v1 的验收标准
- 背景：用户担心「别人没法用，我就白做了」；朋友不是开发者，不会看文档自己配环境。
- 决定：v1 的最终验收不是「功能列表全勾」，而是朋友按 `docs/guides/demo.md` 在 5 分钟内完成：
  双击 setup → Doctor 绿灯 → 选示例仓库 → 发一句话 → 看到流式/tool cards → 停止 → 重开能看到历史。
- 理由：这个剧本同时覆盖安装、Provider、Doctor、CLI 进程、流式、L3 历史，是最小可演示闭环。
- 代价：安装器和打包必须进 v1；不能只交一个开发模式能跑的仓库；需要两台机器手动验收。