# AGENTS.md

硬性约定。本文件只写**代码里看不出来**的约束与验证命令；细则在 `rules/`，任务边界在 `specs/`。
目标：任何一次开工，要读的文件数固定，不随卡片数量增长。

## 命令
| 目的 | 命令 |
|---|---|
| 一键验收（唯一完成信号） | `uv run python scripts/check.py` |
| 单测某个文件 | `cd backend; uv run pytest tests/test_health.py -q` |
| 起服务 | `cd backend; uv run uvicorn app.main:app --reload` ／ `cd frontend; pnpm dev` |
| 重建文件地图 | `uv run python scripts/map.py` |

## 一条会话 = 一张卡
做完一张卡就结束会话，下一张卡开新会话。跨卡累积的上下文是 token 膨胀的最大来源，
比任何文档都大。交接只靠三样东西：`PROGRESS.md`、当前卡的 `spec.md`、`log.md`。

## 开工前读什么（按顺序，读到够用就停）
1. 本文件。
2. `specs/CURRENT` 指向的那张卡的 `spec.md`（要什么、边界在哪）。
3. 同一张卡的 `log.md`（改哪几个文件、每个文件干什么）。
4. `PROGRESS.md`（当前状态、未决问题、下一步）。
5. `rules/` **按需读**：改后端才读 `rules/backend.md`；改前端才读 `rules/frontend.md`；
   写测试读 `rules/testing.md`；要提交读 `rules/git.md`。不相干的不要读。
6. `TROUBLESHOOTING.md` **不要整篇读**：遇到报错时用报错原文 grep 它，命中了再读那一条。

## 开卡（四步，一步别省）
1. 把 `specs/_template/` 复制成 `specs/NNN-短名/`。
2. 填 `spec.md`：DoD 写成可勾选清单；scope 优先写**具体文件路径**，确实整目录才写 glob；
   边界用例至少 3 条。
3. 填 `log.md`：先写**预测**要碰的文件与一句话作用；还没建的文件标 `（待建）`。
4. 把 `specs/CURRENT` 改成 `NNN`。

## 收卡（四步）
1. `git diff --name-only` 核对 `log.md`：把预测改成实际，多退少补。
2. 在 `log.md` 的「本卡消耗」记一行输入 / 输出 token 与工具调用次数。
3. `spec.md` 勾 DoD，把 `check.py` **完整输出**贴进「验收记录」。
4. `check.py` 退出码 0 → 一个 commit。`PROGRESS.md` 只留「当前状态 / 未决问题 / 下一步」。

## 零例外（已机器化，别靠自觉）
1. `check.py` 退出码不是 0 就不算完成；报告完成必须贴完整输出。
2. 禁用 `# type: ignore`、`as any`、`@ts-ignore`、`.skip`、注释掉断言 → `scripts/guards.py` 会拦。
3. 只改当前任务卡 `spec.md` 中 scope 块列出的路径；要动别的先改任务卡。
4. 不准为让测试变绿而改断言；必须改就在 `PROGRESS.md` 写理由。
5. 新增依赖必须写明理由，且同步更新 `uv.lock` / `pnpm-lock.yaml`。
6. 实现 30 分钟仍无法让 `check.py` 退出码为 0：停止编码，在 `PROGRESS.md`「未决问题」
   写清卡在哪一步、报错原文、已试过的两种思路，然后向用户汇报。不准扩大 scope，不准改断言。
7. 文档或代码有歧义：先问，别猜，别先改代码。
8. 指定为管理员时，可豁免非规则类文件的部分限制。
9. `specs/<卡>/tasks.md` 已废弃，进度与验收记录都写在 `spec.md` 里（`guard spec` 会拦）。

## 每份文档只管一件事（互相抄就是重复计费）
| 文件 | 只写 | 不写 |
|---|---|---|
| `PROGRESS.md` | 当前状态、未决问题、下一步；上限 60 行 | 已完成清单、历史 |
| `specs/<卡>/spec.md` | 这张卡要什么、边界、验收记录 | 其它卡的事 |
| `specs/<卡>/log.md` | 这张卡碰了哪些文件、为什么 | 需求讨论 |
| `docs/plan/file-map.md` | 由 `map.py` 自动生成，别手改 | — |
| `TROUBLESHOOTING.md` | 现象 → 原因 → 解决，只增不删 | 进度、计划 |
| `docs/plan/plan.md` | 总计划、里程碑、覆盖矩阵、待拍板；上限 200 行 | 单卡细节 |
| `docs/plan/frontend-plan.md` | 前端 IA、线框、tokens | 实现细节 |

## 参考实现
`backend/src/app/api/health.py`、`backend/tests/test_health.py`、`frontend/src/api/client.ts`。
