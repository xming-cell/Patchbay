# 001 — 骨架可验收

> 开卡日期：2026-11-22 ｜ 文件地图：`log.md`

## 背景与目标
1. 后端能起、`/api/health` 返回 ok，且有 1 个通过的测试。
2. 前端能起、首页显示 `Health: ok`，`type-check` / `lint` / `vitest` 全绿。
3. 一条命令 `uv run python scripts/check.py` 能同时验完后端与前端，且改错范围会被拦住。

## 验收标准（DoD）

- [x] `uv run python scripts/check.py` 退出码 0，输出贴进文末「验收记录」
- [x] `/api/health` 返回 `{"status":"ok"}`，且有 `test_health.py` 覆盖
- [x] 前端首页显示 `Health: ok`，`type-check` / `lint` / `vitest` 全绿
- [x] `specs/CURRENT` 指向本卡时，在 `scope` 之外新增文件会让 `guard scope` 失败
- [x] 仓库没有 `HEAD`、`specs/CURRENT` 为 `none`、`spec.md` 无 scope 块三种边界都不崩

## 范围

```scope
# 001 是骨架卡，必须覆盖全部骨架文件；从 002 起收窄到具体文件路径。
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

## 边界用例（实现时必须想到）
1. 仓库还没有任何 commit（无 `HEAD`）时，`guard scope` 不能崩。
2. `specs/CURRENT` 写成 `none` 时，`guard scope` 跳过而不是失败，`guard spec` 同样跳过。
3. `spec.md` 里没有 scope 块时，`guard scope` 必须失败，不允许「默认全放行」。

## 不做（明确划界）
- 不接数据库、不接鉴权、不做部署脚本。
- 不引入 e2e / Playwright。

## 验收记录

### 2026-11-22 骨架首次全绿

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

All checks passed.
```

### 2026-11-25 文档流程 v2

命令：`uv run python scripts/check.py`

```text

=== guard spec ===

=== guard: spec ===
[ok] specs/001-skeleton: spec.md + log.md, 34 file row(s)
[ok] PROGRESS.md 14/60 lines
[ok] TROUBLESHOOTING.md 7 section(s) well formed

[guard] PASS

=== guard scope ===

=== guard: scope ===
task card: specs/001-skeleton (14 path rules)
[ok] 14 changed file(s), all within scope

[guard] PASS

=== guard forbidden ===

=== guard: forbidden ===
[ok] no banned patterns in source

[guard] PASS

=== file map ===
[ok] docs/plan/file-map.md: 34 row(s) from 1 card(s)

=== backend lint ===
All checks passed!

=== backend format ===
5 files already formatted

=== backend types ===
Success: no issues found in 4 source files

=== backend tests ===
.                                                                        [100%]
============================== warnings summary ===============================
.venv\Lib\site-packages\fastapi\testclient.py:1
  D:\MyFiles\projects\project4\backend\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
1 passed, 1 warning in 0.47s

=== frontend types ===
$ vue-tsc --build

=== frontend lint ===
$ run-s "lint:*"
$ oxlint . --fix
Found 0 warnings and 0 errors.
Finished in 18ms on 10 files with 144 rules using 16 threads.
$ eslint . --fix --cache

=== frontend tests ===
$ vitest --run

 RUN  v4.1.12 D:/MyFiles/projects/project4/frontend

 ✓ src/__tests__/App.spec.ts (1 test) 21ms

 Test Files  1 passed (1)
      Tests  1 passed (1)
   Start at  22:17:24
   Duration  1.53s (transform 171ms, setup 0ms, import 364ms, tests 21ms, environment 832ms)


All checks passed.
```
