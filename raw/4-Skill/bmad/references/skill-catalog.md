# BMAD Skill 速查（参考）

执行以各 Skill 安装目录中的 **SKILL.md** 及 <https://docs.bmad-method.org/> 为准。

## 安装与路径

```bash
npx bmad-method install   # 选择 Cursor
```

| 环境 | Skill 目录 |
|------|------------|
| Cursor（BMAD 安装器） | 项目 `.agents/skills/` |
| Cursor（通用） | 也可使用 `.cursor/skills/` |
| 用户级 | `~/.agents/skills/` 或 `~/.cursor/skills/` |

**排错**

- 安装后看不到 Skill：检查 Cursor 是否启用 Agent Skills，重载窗口。
- 缺 Skill：重新运行安装器并确认所选模块；或删除旧 skill 目录后全量重装。
- 卸载模块后残留：手动删除过期的 `bmad-*` 目录。

## Agent 与菜单触发码

加载 Agent：`bmad-agent-analyst` 等。进入角色后输入短码（仅在该 Agent 菜单下有效）。

### Analyst (Mary) — `bmad-agent-analyst`

| 码 | 方向 |
|----|------|
| BP | Brainstorm |
| MR / DR / TR | 市场 / 领域 / 技术调研 |
| TS | Technology selection |
| CR | Competitive teardown（竞品） |
| UV | User-voice research |
| CB | Product brief |
| PC | Project context |
| 等 | 见官方 Agents 页 |

### Product Manager (John) — `bmad-agent-pm`

| 码 | 方向 |
|----|------|
| PRD | 创建/更新/校验 PRD |

### Product Owner (Sofia) — `bmad-agent-po`

| 码 | 方向 |
|----|------|
| SPEC / TICKETS / REFINE / BOARD / VALIDATE / REPLAN / STORE | 需求、切片、精炼、看板、验证、重规划、Tracker |

### Architect (Winston) — `bmad-agent-architect`

| 码 | 方向 |
|----|------|
| CA | Architecture spine |

### Developer (Amelia) — `bmad-agent-dev`

| 码 | 方向 |
|----|------|
| BD | Build（实现） |
| QA | E2E 测试生成（`bmad-qa-generate-e2e-tests`） |
| CR | Code review |
| ER | Epic retrospective |

### UX Designer (Sally) — `bmad-agent-ux-designer`

| 码 | 方向 |
|----|------|
| CU | UX design |

## 推荐流水线（Greenfield 简图）

```text
bmad / bmad-brainstorming / bmad-forge-idea / bmad-deep-recon
  → bmad-product-brief（可选 bmad-prfaq）
  → bmad-prd
  → bmad-ux + bmad-architecture
  → bmad-project-context
  → bmad-agent-po（SPEC / TICKETS …）
  → bmad-build（每项工作）
  → bmad-code-review / bmad-walkthrough
  → bmad-retrospective（Epic 级）
```

小改动或缺陷：可直接 **`bmad-build`** 或 Developer `BD`，不必走全 PRD。

## 核心模块 Skill 一览

| Skill | 一句话 |
|-------|--------|
| `bmad` | 问下一步、setup、status、initiative |
| `bmad-brainstorming` | 100+ idea 头脑风暴 |
| `bmad-forge-idea` | 对谈压测半成型想法 |
| `bmad-deep-recon` | 决策研究 + 代码库 cited 问答 |
| `bmad-advanced-elicitation` | 多方法推挤草稿 |
| `bmad-review` | 多 lens 统一格式 findings |
| `bmad-party-mode` | 多 Agent 圆桌 |
| `bmad-shard-pro` | 长 MD 分片/目录 |
| `bmad-ingest` | 原始记录 → 结构化 note |
| `bmad-customize` | 自然语言写 customize 覆盖 |

## BMad Method 工作流 Skill

| Skill | 一句话 |
|-------|--------|
| `bmad-product-brief` | Brief 创建/更新/校验 |
| `bmad-prfaq` | Working Backwards PRFAQ |
| `bmad-prd` | PRD 创建/更新/校验 |
| `bmad-ux` | DESIGN.md / EXPERIENCE.md |
| `bmad-architecture` | 架构决策记录 |
| `bmad-project-context` | AGENTS/上下文维护 |
| `bmad-build` | 工作项 → 代码 + 内建评审 |
| `bmad-build-auto` | 无人值守开发循环单轮 |
| `bmad-code-review` | 多 reviewer + 分诊 |
| `bmad-walkthrough` | 人工逐块走读 |
| `bmad-qa-generate-e2e-tests` | API/E2E 测试生成 |
| `bmad-retrospective` | Epic 证据与验收 |

## Toolsmith（另装模块）

| Skill | 一句话 |
|-------|--------|
| `bmad-toolsmith` | 编写/维护 Skill 与模块 |
| `bmad-eval` | Skill 效果评估 |

## 已弃用名称（仍可能转发）

`bmad-create-prd`、`bmad-edit-prd`、`bmad-market-research`、`bmad-generate-project-context`、`bmad-checkpoint-preview` 等 → 请改用当前名如 `bmad-prd`、`bmad-deep-recon`、`bmad-project-context`。

## 与本 wiki `4-Skill` 的关系

| 目录 | 作用 |
|------|------|
| `raw/4-Skill/bmad/` | 人类与门户可读的方法索引 |
| 项目 `.agents/skills/bmad-*` | Cursor 实际调用的生成 Skill |
| `raw/4-Skill/superpowers/` | 可并行的另一套工程流 Skill |

在 **personal-knowledge-wiki** 中备份 BMAD 说明；在 **具体产品仓库** 运行 `npx bmad-method install` 后，Agent 才具备完整可执行 Skill 树。
