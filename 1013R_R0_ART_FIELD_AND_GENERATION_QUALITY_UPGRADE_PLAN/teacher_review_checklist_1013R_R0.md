# 1013R_R0 · Teacher Review Checklist

## Boundary

```text
teacher_review_checklist_only=true
formal_apply_performed=false
R36_modified=false
foundation_contracts_modified=false
provider_called=false
model_called=false
```

## A. 字段体系是否合理

- `big_idea / basic_question / performance_task / lesson_chain` 是否真的能帮助你看清一个美术单元？
- `unit_role / connects_from_previous_lesson / prepares_for_next_lesson` 是否会让课时之间更连贯？
- `materials_and_tools / technique_chain / visual_criteria / safety_note / student_choice_point` 是否是美术示范前必须考虑的东西？
- `composition_or_layout / technique_use / creative_expression / evidence_type` 是否比普通“优秀/良好/合格”更适合美术评价？

## B. 哪些字段不该强制填写

请重点确认这些字段是否只能 optional：

```text
culture_context
exhibition_or_share_endpoint
learning_sheet
board_plan
resource_cards
presentation_script
classroom_use_guide
safety_and_cleanliness
```

## C. 生成质量标准是否可用

请判断这些不合格标签是否能帮助你快速指出问题：

```text
UNIT_AS_LESSON_LIST
LESSON_ISOLATED_FROM_UNIT
PROCESS_AS_PARAGRAPH
GENERIC_DEMO
COPY_RISK
COURSEWARE_IS_LESSON_TEXT
ASSESSMENT_AS_REWARD_ONLY
NO_WORK_EVIDENCE
FORMAL_SCORE_RISK
```

## D. 示范环节是否够具体

一条合格的美术示范候选应该能回答：

```text
学生卡在哪里？
老师具体示范什么动作？
用什么材料和工具？
学生看什么？
分几步做？
容易错在哪里？
怎么修正？
怎样避免照抄？
学生有哪些选择？
大屏或课件该显示什么？
评价看什么证据？
```

## E. 页面下一步是否要做

R0 不改页面。若后续进入 R1/R2，请先判断：

```text
是否先做字段/Prompt fixture？
是否再做 R36 参考案例卡静态预览？
是否仍不接模型？
是否仍不正式回灌正文？
```

## F. 最小通过标准

教师审核可按下面方式判定：

```text
字段能解释美术教学=true/false
生成质量标签能用于回归测试=true/false
prompt_patch方向合理=true/false
允许进入1013R_R1静态fixture=true/false
允许进入R36页面预览=true/false
```

