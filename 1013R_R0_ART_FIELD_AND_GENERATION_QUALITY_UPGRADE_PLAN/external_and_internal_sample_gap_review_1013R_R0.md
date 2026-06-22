# 1013R_R0 · External And Internal Sample Gap Review

## Boundary

```text
gap_review_only=true
external_sample_is_reference_only=true
official_claim_allowed=false
formal_apply_performed=false
provider_called=false
model_called=false
R36_modified=false
```

This review compares sample patterns. It does not fetch, study, or integrate an external website in this stage.

## 1. 新上传教师资料

### Review Use

The newly collected teacher-uploaded unit materials are strongest as field-discovery evidence.

### Useful Patterns

```text
成长足迹:
big_idea
basic_question
lesson_chain
share_endpoint

我为文具代言:
learning_handbook
performance_task
classroom_use_guide
student_recording_slots

纸卷魔术:
materials_and_tools
technique_chain
classroom_process
assessment_clues

遇剪美好:
culture_context
technique_chain
meaning
rubric_sheet
safety_and_cleanliness
```

### Gap

These materials are not official evidence and are not universal templates. They need source labels and teacher confirmation.

## 2. 1013M / 1013O Demonstration Samples

### Review Use

1013M and 1013O are strongest as generation-quality evidence.

### Useful Patterns

```text
art_demonstration_and_visual_scaffold
student_gap
teacher_demo_actions
student_observation_tasks
technique_steps
process_mantra
common_mistakes_and_fixes
anti_copy_guidance
student_choice_paths
courseware_screen_seeds
big_screen_short_text
assessment_evidence
```

### Gap

The model language can be useful, but it needs structure. A single generated paragraph should be split into:

```text
teacher_reading_structure_version
classroom_script_reference_version
courseware_screen_structure_version
big_screen_short_text_version
assessment_evidence_version
```

## 3. 飞象老师样例

### Review Use

The external sample is a comparison reference only. It is not official curriculum evidence and must not directly create required fields.

### Reported Strengths

```text
generation_speed_fast
unit_theme_present
content_and_literacy_analysis_present
activity_table_structure_present
lesson_chain_can_link_three_lessons
```

The activity table shape is useful as a reference:

```text
任务
情境创设
师生活动
归纳提升
设计意图
```

The sample also reportedly connects:

```text
老房子
我造的小房子
漂亮的房间
```

into a "回望 -> 创造 -> 入驻 / 美化" chain.

### Reported Gaps

```text
big_idea_not_explicit_enough
basic_question_not_explicit_enough
performance_task_not_explicit_enough
assessment_tends_to_activity_reward
technique_demo_not_expanded
scenario_packaging_heavy
source_evidence_requires_teacher_confirmation
```

### Absorption Rule

Useful:

```text
activity_table_as_process_reference
lesson_chain_sense
task_situation_activity_intention_breakdown
```

Do not absorb as stable required fields:

```text
时光机
建筑勋章
小小讲解员
specific_external_scenario_packaging
external_sample_official_claim
```

## Combined Upgrade Direction

The three sample groups suggest this upgrade:

```text
fields must explain art teaching
generation must become layered
process must become action blocks
demo must become method and visual scaffold
assessment must use work/process evidence
courseware must map design intent, not paste lesson text
```

