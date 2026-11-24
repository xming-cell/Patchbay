# TROUBLESHOOTING.md

记录实际踩过的坑；只写「现象 → 原因 → 解决办法」。

## 问题列表

### guard scope 报 specs/001-skeleton/spec.md not found
- **原因**：`specs/CURRENT` 已经指向 001，但任务卡文件还没建。
- **解决**：按 4.7 建 `spec.md`（scope 块不能为空），或把 `CURRENT` 临时改成 `none`。

### guard scope 把 frontend/.eslintcache 列为越界文件
- **原因**：`pnpm run lint` 带 `--cache`，会生成 `.eslintcache`；根 `.gitignore` 的规则不覆盖它。
- **解决**：保留 create-vue 生成的 `frontend/.gitignore`（里面已有 `.eslintcache`），不要用根目录那份覆盖它。

### pnpm run test:unit 看起来卡住不退出
- **原因**：`test:unit` 是 vitest 的 watch 模式。
- **解决**：单次执行用 `pnpm run test:unit --run`；脚本里没有 `test:unit:run` 这个命令。

### 2.12 报 TS1294 / ESLint couldn't find eslint.config.* / location is not defined
- **原因**：2.1 用了 `pnpm create vite`（create-vite 极简模板），缺少 create-vue 才有的 vitest / eslint / tsconfig 配置。
- **解决**：按 2.1 改用 `pnpm create vue@latest frontend --ts --router --pinia --vitest --eslint --prettier` 重新生成；只补文件的话，需要补 `vitest.config.ts`、`eslint.config.ts`、`.oxlintrc.json`、`tsconfig.vitest.json`、`env.d.ts`，并把 `tsconfig.*.json` 换成 create-vue 版本。

### pnpm create vue@latest . 停在「请输入包名称」
- **原因**：`.` 不是合法包名，create-vue 进入交互模式。
- **解决**：在仓库根执行 `pnpm create vue@latest frontend ...`，不要先 `cd frontend`。

### corepack: command not found（Node 25+）
- **原因**：Node 25 起不再自带 corepack。
- **解决**：`npm install -g pnpm@9`。

### 前端显示 Health: error
- **原因**：后端没起、端口不是 8000，或 `vite.config.ts` 的代理路径与 `/api` 不一致。
- **解决**：先确认 `http://127.0.0.1:8000/api/health` 可访问，再检查代理配置。