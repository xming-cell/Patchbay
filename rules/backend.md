# 后端规则

技术栈：FastAPI · Python 3.12 · uv。参考实现：`backend/src/app/api/health.py`。

## 分层（不可跨越）
`api/` → `services/` → `repositories/`
- `api/`：只做参数校验 + 转发 service，**不写业务逻辑、不写 SQL、不拼 dict**。
- `services/`：业务规则都在这里，**不写 SQL**，不直接依赖 `fastapi.Request`。
- `repositories/`：只做数据访问，返回领域对象，不做业务判断。

跨层反向 import 一律拒绝：`repositories` 不许 import `services`。

## 接口约定
- 所有 API 输入输出必须是 Pydantic 模型（`schemas/`），禁止裸 `dict` / `Any` 当返回值。
- 金额一律 `Decimal`，禁止 `float`；序列化时用字符串，避免二进制浮点误差。
- 错误统一 `{code, message}`。本骨架还没有 `app/core/errors.py`：
  第一次需要区分错误码时**先建这个文件**（`class AppError(Exception)` + 全局 handler），
  并把它登记进 `PROGRESS.md`；在此之前不要写 `from app.core.errors import ...`。
- 时间统一带时区，禁止裸 `datetime.now()`。需要可注入时钟时先建 `app/core/clock.py`，
  规则同上：先建、先登记，再 import。

## 复用与命名
- 先用后写：`app/core/`（现有 `config.py`）里已有的不再造一遍。
  **AI 最常见的缺陷就是重写一个已有的工具函数**——动手前先 `grep` 一遍。
- 依赖注入用 `Depends`，不要模块级全局单例。

## 禁止
- `# type: ignore`（有病治病，改类型或加断言）。
- 顺手新增 `example/`、`demo_*.py`、`tmp_*.py` 之类演示文件——会被 `check.py` 的范围校验拦下，也确实会把仓库搞脏。