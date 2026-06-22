# 1013R_R0 · Art Field And Generation Quality Upgrade Plan

## Status

```text
stage=1013R_R0_ART_FIELD_AND_GENERATION_QUALITY_UPGRADE_PLAN
status=PASS
review_draft_only=true
formal_apply_performed=false
database_written=false
memory_written=false
vector_index_written=false
chunks_built=false
feishu_written=false
main_project_pushed=false
R36_modified=false
foundation_contracts_modified=false
provider_called=false
model_called=false
runtime_connected=false
formal_frontend_binding_allowed=false
```

Validator result:

```text
PASS_1013R_R0_ART_FIELD_AND_GENERATION_QUALITY_UPGRADE_PLAN
```

## Position

This stage is:

```text
字段体系升级 + 生成质量升级
```

It is not:

```text
UI 主壳升级
正式模型接入
R36 正式回灌
知识库入库
飞象老师网站研究
```

## Inputs

```text
1013P_R3: art_reference_case, art_design_spine, four-module patch proposals
1013M: art_demonstration_and_visual_scaffold contract
1013O: structured expression repair and generation quality review
teacher_uploaded_references: 成长足迹 / 我为文具代言 / 纸卷魔术 / 遇剪美好
external_sample_summary: 飞象老师“理想建筑与温暖家园” sample, reference only
```

## Core Upgrade

The system should move:

```text
from field completeness
to fields that explain art teaching

from one-shot content generation
to layered, reviewable generation

from paragraph process
to classroom action blocks

from activity reward
to work evidence + process evidence
```

## Produced Files

```text
1013R_R0_result.json
1013R_R0_report.md
art_field_upgrade_matrix_1013R_R0.json
art_generation_quality_standard_1013R_R0.md
prompt_upgrade_recommendations_1013R_R0.md
external_and_internal_sample_gap_review_1013R_R0.md
generation_quality_test_case_bank_1013R_R0.json
art_design_spine_to_four_modules_mapping_1013R_R0.json
teacher_review_checklist_1013R_R0.md
validate_1013R_R0_art_field_and_generation_quality_upgrade.py
```

## Field Matrix Decision

The field matrix keeps existing four module boundaries:

```text
unit_design
lesson_design
teaching_process
assessment_design
```

and adds a candidate spine:

```text
art_design_spine_candidate
```

The spine does not replace the four modules. It only maps the art-teaching chain across them:

```text
big idea / basic question
-> unit task chain
-> lesson role
-> material and technique chain
-> demo and visual scaffold
-> support pack
-> evidence-aware assessment
```

## Quality Standard Decision

The quality standard defines five review areas:

```text
unit_design
lesson_design
teaching_process
art_demo_block
assessment_design
```

Each area has failure labels, so later model output can be regression-tested rather than judged only by impression.

## Prompt Patch Decision

Prompt patch recommendations are not applied in this stage.

Recommended order:

```text
1. material_intake_prompt_patch
2. teaching_process_and_demo_prompt_patch
3. assessment_prompt_patch
4. unit_design_prompt_patch
5. lesson_design_prompt_patch
```

## External Sample Boundary

The external sample is useful as comparison:

```text
activity table structure
lesson chain sense
task / situation / teacher-student activity / summary / design intention shape
```

It cannot create required fields and cannot become official evidence.

## Next Stage

```text
preferred_next_stage=1013R_R1_FIELD_PATCH_AND_PROMPT_PATCH_STATIC_FIXTURE
```

R1 still must not formal apply, modify R36, connect model/provider, or write database/memory/vector/chunks.
