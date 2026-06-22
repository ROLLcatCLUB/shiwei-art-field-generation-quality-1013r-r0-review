# 1013R_R0 · Art Generation Quality Standard

## Boundary

```text
quality_standard_only=true
review_draft_only=true
formal_apply_performed=false
database_written=false
memory_written=false
vector_index_written=false
chunks_built=false
feishu_written=false
R36_modified=false
foundation_contracts_modified=false
provider_called=false
model_called=false
runtime_connected=false
```

This standard is used to judge generated candidates later. It does not generate a lesson or modify prompts directly.

## 1. 大单元生成质量

### 合格要求

- 有清楚的单元主题。
- 有大观念或基本问题，最好二者都有。
- 有表现性任务，说明学生最终完成什么作品、方案、展示、说明或应用成果。
- 课时之间不是简单并列，而是有承接、递进、回看。
- 每课有清楚的 `unit_role`。
- 最终有展示、分享、发布、使用或回看终点；若没有，也要说明为什么不需要。
- 能说明学生最终完成什么作品或任务。

### 不合格标签

```text
UNIT_AS_LESSON_LIST
NO_BIG_IDEA
NO_BASIC_QUESTION
NO_PERFORMANCE_TASK
LESSON_CHAIN_WEAK
NO_EXHIBITION_ENDPOINT
GENERIC_UNIT_GOALS
```

## 2. 课时生成质量

### 合格要求

- 说明本课在单元中的位置。
- 说明本课承接上一课、准备下一课的关系；如果没有上下课，也要说明这是单课。
- 说明本课学生可见产出。
- 把材料、技法、观察点放进活动，而不是只放在目标里。
- 不只写“导入 - 新授 - 练习 - 评价”。

### 不合格标签

```text
LESSON_ISOLATED_FROM_UNIT
NO_UNIT_ROLE
NO_STUDENT_OUTPUT
GENERIC_PROCESS
MATERIAL_TECHNIQUE_NOT_IN_ACTIVITY
```

## 3. 教学过程生成质量

### 合格要求

- 每个环节是课堂动作块，而不是大段空泛描述。
- 有教师动作、学生动作、问题、材料或工具、可观察证据。
- 示范环节具体可操作。
- 活动不是泛泛描述，能看出学生在做什么、看什么、说什么、改什么。

### 不合格标签

```text
PROCESS_AS_PARAGRAPH
NO_TEACHER_ACTION
NO_STUDENT_ACTION
NO_OBSERVABLE_EVIDENCE
NO_VISUAL_TASK
```

## 4. 示范与支架生成质量

### 合格要求

- 说明学生卡点。
- 说明教师具体示范动作。
- 有材料工具。
- 有技法步骤。
- 有视觉判断标准。
- 有儿童能记住的口令或短步骤；不是必须花哨，但要可记。
- 有错例与修正。
- 有同龄作品或视觉参照支架；没有现成作品时，也要说明可替代的视觉支架。
- 有防临摹、原创引导。
- 有学生选择空间。
- 有课件屏结构和大屏短文本映射。

### 不合格标签

```text
GENERIC_DEMO
NO_STUDENT_GAP
NO_TECHNIQUE
NO_MANTRA
NO_MISTAKE_FIX
NO_PEER_SCAFFOLD
COPY_RISK
NO_STUDENT_CHOICE
TOO_TEXT_HEAVY
COURSEWARE_IS_LESSON_TEXT
```

## 5. 评价设计生成质量

### 合格要求

- 评价连接学生作品和课堂过程。
- 有作品证据。
- 有过程证据。
- 维度适合任务类型：绘画、设计、手工、综合材料、传统文化表达应不同。
- 不进入正式评分。
- 支持自评、互评、教师观察。

### 不合格标签

```text
ASSESSMENT_AS_REWARD_ONLY
NO_WORK_EVIDENCE
NO_PROCESS_EVIDENCE
GENERIC_RUBRIC
FORMAL_SCORE_RISK
```

## Label Coverage

```text
unit_design_labels_present=true
lesson_design_labels_present=true
teaching_process_labels_present=true
art_demo_labels_present=true
assessment_design_labels_present=true
```

## Quality Upgrade Principle

The goal is not to make generated text longer. The goal is to make it:

```text
field-grounded
teacher-readable
student-actionable
visually mappable
evidence-aware
reviewable by regression labels
```

