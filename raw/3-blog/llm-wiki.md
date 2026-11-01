---
title: 打造个人 LLM Wiki：从 0 到 1 的实践
description: 将 Markdown、Git、PARA 与 Agent Skills 组合成可持续迭代的个人知识系统。
category: 知识管理
date: 2026-05-28
readTime: 16 分钟
icon: ⌘
featured: true
draft: false
---


##  LLM Wiki

传统 Wiki 强调链接与协作；个人场景更常见的问题是 **记录分散、版本不清、AI 对话无法沉淀**。LLM Wiki 把三者接起来：

- **Wiki 层**：Markdown 文件 + Git，服务检索、 diff 与长期存档。
- **LLM 层**：摘要、重组、提问、对照多份笔记生成大纲——输入输出都尽量落盘，而不是只留在聊天里。
- **边界层**：明确哪些目录是私人草稿，哪些是可引，可发表，避免一键同步把内部信息带到公开页。

它不要求一开始就建完整知识图谱；先跑通 **记录 → 整理 → 选用途** 的闭环，再慢慢加链接与分类。

## 1. 让知识保持可迁移

**默认格式选 Markdown。** 标题、列表、代码块、表格、公式（若需要）都有成熟工具链；任何文本编辑器都能打开，不依赖单一 SaaS 的导出能力。

**版本用 Git 管理。** 一次学习、一次项目复盘，对应一次或多次 commit；以后能回答这段结论是什么时候、在什么上下文里写下的。比专有笔记的同步记录，更适合和 CI、静态站、Agent 脚本配合。

**媒体文件集中管理。** 图片、附件放在约定目录，正文用相对路径引用。搬家、换构建工具时，只需重写路径规则，不必手工找散落的截图。

**阅读用静态站或本地预览生成。** 渲染站点是只读视图，不是第二份真源。换 Hugo、Astro、MkDocs 时，Markdown 仓可原样保留。

和 LLM 协作时，养成习惯：**探索在对话里，结论在文件里**；对话窗口适合试错，文件适合承诺。

## 2. 用 PARA 组织行动

PARA（Projects / Areas / Resources / Archives）的价值不在于文件夹必须叫这四个名字，而在于 **按下一步行动决定放哪**：

| 类型 | 含义 | 典型内容 |
|------|------|----------|
| Projects | 有终点、有交付 | 正在写的系列文章、季度学习计划、某个产品方案 |
| Areas | 长期标准 | 某技术栈深度、写作习惯、健康管理 |
| Resources | 待用资料 | 书单、课程笔记、论文摘要 |
| Archives | 已结束 | 旧项目复盘、不再维护的主题 |

落地时可以只用 **编号或语义化目录**（如「日常笔记 / 外部材料 / 成稿 / 公开副本」），不必机械复制 PARA 字母。

**决策顺序**比目录名更重要：

1. 新内容先进 **可随意写的层**（允许口语、未验证）。
2. 结构清晰、愿意负责后，再进入 **审核公开层** 或 **博客成稿层**。
3. 反复执行的流程（发布检查、写作模板、代码审查要点）写成 **Skill**，而不是每次重新口述给 AI。

Archive 用归档目录、分支或「不再更新」的标记即可，无需单独系统。

## 3. 四层内容：raw、publish、博客、Skill

建议在概念上拆分四类存储角色（物理上可以是不同目录或不同仓库）：

```text
raw      → 真源：学习笔记、踩坑、碎片想法
publish  → 审核后可对外引用的副本（不与 raw 自动同步）
blog     → 叙事成稿：背景、取舍、过程（可用 draft 控制未完工）
Skill    → Agent 操作说明：步骤、边界、输出格式
```

**raw 与 publish 必须分离。** 自动同步笔记到公开页，极易泄露内部用语或未核实判断。publish 层应有显式规则：仅人工迁入；检查隐私与事实；在 frontmatter 中标记审核状态与日期。

**博客层** 回答「为什么、怎么选」；**知识库式 publish** 更接近「是什么、怎么用」——二者可以主题相关，但文体不同。

**Skill 层** 使用 Agent 可读的说明文件（如带 `name`、`description` 的 YAML 头 + Markdown 正文），描述 **何时触发、做什么、禁止什么**。把稳定规则从聊天 prompt 里抽出来，才能版本化与复用；详细清单、范例放在 skill 目录的子文件夹，与主说明区分。

## 4. 内容仓与展示站分离

长期维护建议 **内容 Git 仓** 与 **站点 Git 仓** 分开（或 monorepo 内边界清晰）：

- 内容仓：Markdown、图片、Skill、publish 副本。
- 站点仓：主题、导航、构建配置、个人品牌页。

构建时站点 **读取** 内容仓的指定路径；线上部署通过 submodule、包版本或 CI 拉取 **锁定内容版本**，避免「本地最新、线上过期」。

好处：内容仓可私有；公开站只挂载允许的路径；换前端框架不动内容。

## 5. 四种阅读契约

若读者从网站进入，应对每个入口说明 **粒度与可信度**：

| 入口 | 内容性质 | 读者预期 |
|------|----------|----------|
| 笔记 | 原始、可能冗长 | 作者自用，可能过时 |
| 知识库 | 审核后的专题 | 可引用、相对严谨 |
| 博客 | 观点与叙事 | 有上下文、有取舍 |
| Skill | 流程与规范 | 指导人与 Agent 如何执行 |

同一主题可以 **只存在于笔记**，也可以 **提炼为知识库条目**，再 **写博客讲决策过程**——这是分层而非重复劳动。

## 6. LLM 与 Agent：加速，不越权

**适合自动化**：生成大纲、统一术语、补全 frontmatter、批量修正链接、按 Skill 跑发布前检查、从多篇笔记归纳对比表。

**必须人工决定**：是否对外、是否含敏感信息、结论是否与原始数据一致、审核副本是否达标。

操作建议：

1. 重要判断 **写进文件**，并附来源、日期。
2. 模型输出默认进入 raw；进入 publish 或发博客前 **固定一道人工 review**。
3. 重复协作模式 **沉淀为 Skill**，减少每次从零描述规则。


## 7. 一条想法如何变成可分享页面

1. 在 raw 层快速记录（结构差没关系）。
2. 用 LLM + Skill 整理层级、交叉链接、摘要（仍留在 raw）。
3. 值得对外：改写为 publish 条目，做隐私与事实自检。
4. 需要讲故事：在博客目录写成稿，关闭 draft 后构建发布。
5. 内容仓更新后，触发站点所用版本的更新与部署。

若 publish 更新频繁，可用 CI 在内容 push 后 **自动重建站点**，保持网页与仓库一致。

## 8. 最小闭环与常见坑

**建议的第一周目标**（小于「完美知识图谱」）：

- 一个常写主题目录；
- 一篇博客成稿；
- 一条 raw → publish 的人工审核习惯；
- 一个 Skill（如写作结构或发布清单）。

**常见坑**：

- 只信在线笔记，导出与自动化困难。
- raw 与公开目录混放，部署误发草稿。
- 图片路径混乱，迁移或构建大量失效。
- 开发环境与生产构建读取不同路径，线上内容为空。
- 过度依赖对话，不更新文件与 Skill，每次重 prompt。

## 小结

个人 LLM Wiki = **Markdown + Git 的真源** + **PARA 式的行动分类** + **raw / publish / 博客 / Skill 的分层** + **LLM 辅助整理、人工把关发布**。不必一次做对；先让 **写得随意、发得谨慎、找得到、换得了** 四件事成立，系统就会随使用时间自然变厚。

## 实践

下面是我本地工作区 **`11-Profile-Web`** 里两个仓库的落地方式：**`personal-knowledge-wiki` 存内容与流程，`personal-tech-portal` 负责静态站呈现**。可作为上文方法的参考实例，而非通用标准。

### 仓库初始化

**1. 工作区布局**

两个 Git 仓库并列放置（也可只 clone 门户，用 submodule 拉 wiki）：

```text
11-Profile-Web/
├── personal-knowledge-wiki/     # 内容真源
└── personal-tech-portal/      # Astro 个人站（GitHub: boyang167.github.io）
```

**2. 克隆门户并拉取 wiki 子模块**

```bash
git clone https://github.com/boyang167/boyang167.github.io.git personal-tech-portal
cd personal-tech-portal
git submodule update --init --recursive
npm install
```

子模块路径为 `external/personal-knowledge-wiki`，用于 **CI / GitHub Pages** 构建时锁定 wiki 版本。本地若另有 sibling 目录 `../personal-knowledge-wiki`，门户在 dev/build 时会 **优先读 sibling**（内容更全的一侧），便于日常改 wiki 立刻在站点预览。

**3. 内容仓（personal-knowledge-wiki）要点**

| 路径 | 用途 |
|------|------|
| `raw/1-Note/` | 原始 Markdown 笔记（门户「笔记」模块直接读取） |
| `raw/2-StudyMaterials/` | 大块外部资料、PDF 等，不全量上站 |
| `raw/3-blog/` | 技术博客源文件（YAML frontmatter + 正文） |
| `raw/4-Skill/` | Cursor Agent Skill（`<name>/SKILL.md`） |
| `wiki/` | 结构化知识、MOC、LLM 索引（Agent 维护，见 `AGENTS.md`） |
| `publish/` | **人工审核**后可对外分享的知识副本 |
| `scripts/` | 索引构建、raw ingest 等维护脚本 |
| `.cursor/rules/`、`.cursor/skills/` | Agent 行为约束与项目级 Skill |

`publish/` 规则见仓库内 `publish/README.md`：**不得从 raw 自动同步**；迁入前确认无隐私，建议标记 `status: reviewed`。

**4. 门户仓（personal-tech-portal）本地跑起来**

```bash
cd personal-tech-portal
npm run dev    # 内部会先执行 prepare:notes，再启动 Astro（默认 http://localhost:4321）
npm run build
npm run preview
```

**5. 双仓联动（可选自动化）**

- wiki 的 `publish/**` push 到 `main` 后，可通过 Actions + **`PORTAL_REPO_TOKEN`** 向门户发 `repository_dispatch`，触发门户重新部署（见门户 `.github/KNOWLEDGE_WIKI_SETUP.md`）。
- 未配置 Token 时，需在门户更新 submodule 指针或手动 push 门户，线上知识库才会更新。

### 前端架构

门户是 **Astro 5 静态站**（`output: 'static'`），无后端 API；个人品牌页与构建配置在 portal，**正文 Markdown 尽量留在 wiki**。

**1. 页面与导航**

主导航对应四类内容入口（另含首页、关于我等）：

| 站点路径 | 数据来源（wiki 内） | 说明 |
|----------|---------------------|------|
| `/notes/` | `raw/1-Note/**/*.md` | 原始笔记，可含 draft 态 frontmatter |
| `/knowledge/` | `publish/**/*.md` | 仅审核副本 |
| `/blog/` | `raw/3-blog/**/*.md` | `draft: true` 不发布；`featured: true` 可上首页 |
| `/skills/` | `raw/4-Skill/**/SKILL.md` | 展示 Skill 正文与目录 |

**2. 构建时如何读 wiki**

- **博客**：`src/content.config.ts` 使用 `glob` loader，`base` 指向 `resolveBlogRoot()`（`raw/3-blog`）。
- **笔记**：`src/lib/wiki-notes.ts` 扫描 `raw/1-Note`；构建前 `scripts/prepare-note-assets.mjs` 把笔记引用的图片复制到 `public/notes-media/`，页面内重写为 `/notes-media/img/...`。
- **知识库**：`src/lib/knowledge-publish.ts` 只读 `publish/`（submodule 或 sibling）。
- **Skill**：`src/lib/wiki-skills.ts` 递归查找 `SKILL.md`；开发模式每次请求重新扫描，避免新增 Skill 后列表不刷新。

路径解析统一模式：候选为 **`../personal-knowledge-wiki/...`** 与 **`external/personal-knowledge-wiki/...`**，按目录内 Markdown / Skill 数量选更全的一侧。

**3. 渲染与交互**

- Markdown：`marked` 渲染；笔记/长文支持目录提取、KaTeX、Mermaid（`MermaidInit` 组件）。
- 布局：`BaseLayout.astro` + `Header.astro`；中英切换为客户端字典替换（非 i18n 路由）。
- 样式：卡片 + 低饱和背景 + 蓝色强调；笔记/知识库/Skill 列表共用 sidebar + 卡片网格布局。

**4. 发布**

- 门户 push `main` → `.github/workflows/deploy.yml` 构建并部署到 **`gh-pages`**，用户站根域 `https://boyang167.github.io/`（`astro.config.mjs` 中 `site`，无 `base` 前缀）。
- 博客与 Skill 要在线上可见，需 wiki 已 push 且门户 submodule **指向含这些文件的 commit**；仅本地 sibling 有而 submodule 未更新时，线上仍会缺内容。

**5. 日常写稿位置速查**

- 记笔记 → `personal-knowledge-wiki/raw/1-Note/`
- 写博客 → `personal-knowledge-wiki/raw/3-blog/`（可复制门户 `docs/blog-article-template.md`）
- 对外知识页 → 审核后写入 `personal-knowledge-wiki/publish/`
- 固化 Agent 流程 → `personal-knowledge-wiki/raw/4-Skill/<name>/SKILL.md`

这样，方法篇里的分层在工程上变成 **两个仓库 + 四条读取规则 + 一条 publish 审核线**；扩展新模块时，优先新增「wiki 子目录 + portal 一个 lib + 一组 pages」，而不是把正文 copy 进 portal 仓库。

