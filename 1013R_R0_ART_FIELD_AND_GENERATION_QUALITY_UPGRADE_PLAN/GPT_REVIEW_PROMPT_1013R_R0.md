# GPT Review Prompt · 1013R_R0

请审核本包：

```text
STAGE=1013R_R0_ART_FIELD_AND_GENERATION_QUALITY_UPGRADE_PLAN
POSITION=字段体系升级 + 生成质量升级
REVIEW_DRAFT_ONLY=true
FORMAL_APPLY_ALLOWED=false
R36_CHANGE_ALLOWED=false
PROVIDER_MODEL_RUNTIME=false
```

## Read Order

1. `1013R_R0_result.json`
2. `1013R_R0_report.md`
3. `art_field_upgrade_matrix_1013R_R0.json`
4. `art_generation_quality_standard_1013R_R0.md`
5. `prompt_upgrade_recommendations_1013R_R0.md`
6. `generation_quality_test_case_bank_1013R_R0.json`
7. `external_and_internal_sample_gap_review_1013R_R0.md`
8. `art_design_spine_to_four_modules_mapping_1013R_R0.json`
9. `teacher_review_checklist_1013R_R0.md`
10. `validate_1013R_R0_art_field_and_generation_quality_upgrade.py`

## Review Questions

请重点判断：

1. 字段矩阵是否能表达美术真实备课链，而不是只增加字段数量。
2. `art_design_spine_candidate` 是否适合作为四模块之间的串联主干。
3. 生成质量标签是否能支持后续模型回归测试。
4. prompt patch 是否仍保持 recommendation-only，没有越界成正式应用。
5. 测试课例库是否覆盖大单元、课时、材料技法、传统文化、设计应用五类场景。
6. 是否存在把教师上传资料误升格为官方依据的风险。
7. 是否存在把外部样例字段直接设为 required 的风险。
8. 是否存在把情境包装词变成稳定字段的风险。

## Boundary To Check

必须保持：

```text
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

## Expected Review Output

请按以下格式返回：

```text
REVIEW_DECISION=ACCEPT | ACCEPT_WITH_NOTES | REVISE
STAGE=1013R_R0_ART_FIELD_AND_GENERATION_QUALITY_UPGRADE_PLAN
VALIDATOR=PASS | FAIL | NOT_RUN
R36_MODIFIED=false
PROVIDER_MODEL_RUNTIME=false
NEXT=UPLOAD_REVIEW_ONLY_OR_ENTER_R1_STATIC_FIXTURE
```

并补充：

```text
1. 通过点
2. 风险点
3. R1 是否允许进入
4. R1 如果进入，只允许做哪些 fixture
5. 是否仍禁止 formal apply / R36 修改 / provider-model-runtime 接入
```

