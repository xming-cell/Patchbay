# 001 任务清单

状态图例：`[ ]` 待做 · `[x]` 完成并已跑过 check.py · `[~]` 做了但有前提未满足

- [x] T1 前置工具就绪（uv / Node / pnpm / git）
- [x] T2 后端 health 端点 + 1 个通过测试
- [x] T3 前端模板生成，模板文件未被误删
- [x] T4 `src/api/client.ts`、`src/router/index.ts`、`views/HomeView.vue` 建好
- [x] T5 首页显示 `Health: ok`，`pnpm run test:unit --run` 通过
- [x] T6 `scripts/guards.py`、`scripts/check.py`、CI workflow 就位
- [x] T7 规则四份 + 本任务卡 + `PROGRESS.md` + `AGENTS.md` 就位
- [x] T8 首次 `uv run python scripts/check.py` 全绿，输出贴到下面

## 验收记录

命令：`uv run python scripts/check.py`

```text
=== guard scope ===

=== guard: scope ===
task card: specs/001-skeleton (14 path rules)
[ok] 19 changed file(s), all within scope

[guard] PASS

=== guard forbidden ===

=== guard: forbidden ===
[ok] no banned patterns in source

[guard] PASS

=== backend lint ===
All checks passed!

=== backend format ===
5 files already formatted

=== backend types ===
Success: no issues found in 4 source files

=== backend tests ===
.                                                                        [100%]
=============================== warnings summary ===============================
.venv\Lib\site-packages\fastapi\testclient.py:1
  D:\MyFiles\projects\project4\backend\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
1 passed, 1 warning in 0.54s

=== frontend types ===
$ vue-tsc --build

=== frontend lint ===
$ run-s "lint:*"
$ oxlint . --fix
$ eslint . --fix --cache

=== frontend tests ===
$ vitest --run

 RUN  v4.1.12 D:/MyFiles/projects/project4/frontend


 Test Files  1 passed (1)
      Tests  1 passed (1)
   Start at  21:13:33
   Duration  1.71s (transform 119ms, setup 0ms, import 237ms, tests 15ms, environment 1.20s)


All checks passed.
```