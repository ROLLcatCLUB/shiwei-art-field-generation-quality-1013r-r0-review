# 1013R_R0 · Prompt Upgrade Recommendations

## Boundary

```text
recommendation_only=true
prompt_patch_applied=false
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

## Shared Upgrade Rule

The prompt system should not ask the model to "write more". It should ask the model to produce layered, inspectable candidates:

```text
teacher_reading_structure_version
classroom_script_reference_version
courseware_screen_structure_version
big_screen_short_text_version
assessment_evidence_version
```

Every patch below remains a recommendation only.

## 1. material_intake_prompt_patch

### Goal

Teacher-uploaded materials should become `art_reference_case`, not正文.

### Add

```text
Extract a readonly art_reference_case from teacher-uploaded art materials.
Do not generate full unit body or complete lesson body.
For each field, label its source as official_textbook_evidence, teacher_uploaded_reference, model_inference, or teacher_confirmation_needed.
If source is teacher upload, official_claim_allowed=false.
If field is inferred or missing, teacher_confirmation_required=true.
Return only normalized fields, uncertainty notes, and source evidence refs.
```

### Must Distinguish

```text
official_textbook_evidence
teacher_uploaded_reference
model_inference
teacher_confirmation_needed
```

### Must Not Output

```text
full_unit_body
complete_lesson_body
official_curriculum_claim
formal_scoring_rule
```

## 2. unit_design_prompt_patch

### Goal

Shift from "write a unit plan" to "build a unit spine candidate".

### Required Candidate Output

```text
big_idea
basic_question
performance_task
lesson_chain
exhibition_or_share_endpoint
assessment_evidence
reference_case_usage
teacher_confirmation_items
```

### Add

```text
Use teacher-confirmed reference fields only.
Explain how each lesson node contributes to the performance task.
For every external or teacher-uploaded source, mark it as reference only.
Do not treat external sample or teacher-uploaded material as official evidence.
Do not generate a formal complete unit body.
```

### Quality Labels To Avoid

```text
UNIT_AS_LESSON_LIST
NO_BIG_IDEA
NO_BASIC_QUESTION
NO_PERFORMANCE_TASK
LESSON_CHAIN_WEAK
GENERIC_UNIT_GOALS
```

## 3. lesson_design_prompt_patch

### Goal

Shift from isolated lesson plan to lesson design that inherits unit position.

### Required Candidate Output

```text
unit_role
connects_from_previous_lesson
prepares_for_next_lesson
student_output_this_lesson
method_or_technique_focus
courseware_screen_need
rubric_link
teacher_confirmation_items
```

### Add

```text
State what this lesson contributes to the unit.
State what students visibly produce or record in this lesson.
Place materials, tools, techniques, and observation points inside activities.
If unit context is missing, mark fields as teacher_confirmation_needed instead of inventing continuity.
```

### Quality Labels To Avoid

```text
LESSON_ISOLATED_FROM_UNIT
NO_UNIT_ROLE
NO_STUDENT_OUTPUT
GENERIC_PROCESS
MATERIAL_TECHNIQUE_NOT_IN_ACTIVITY
```

## 4. teaching_process_and_demo_prompt_patch

### Goal

Shift from paragraph flow to classroom action blocks plus demonstration/visual scaffold.

### Required Candidate Output

```text
phase_name
teacher_action
student_action
teacher_question
materials_or_tools
technique_steps
visual_criteria
common_mistakes_and_fixes
student_choice
observable_evidence
```

### Add

```text
Each process phase must be a classroom action block.
If students will make, draw, design, craft, compose, revise, or present a visual work, include an art_demo_block.
The demo must include student_gap, tools/materials, teacher demo actions, student observation tasks, technique steps, visual criteria, mistakes/fixes, anti-copy guidance, student choice paths, pre-creation check, and courseware/big-screen mapping.
```

### Must Prevent

```text
教师示范。
学生创作。
```

without concrete actions.

### Quality Labels To Avoid

```text
PROCESS_AS_PARAGRAPH
NO_TEACHER_ACTION
NO_STUDENT_ACTION
NO_OBSERVABLE_EVIDENCE
GENERIC_DEMO
NO_STUDENT_GAP
NO_TECHNIQUE
COPY_RISK
COURSEWARE_IS_LESSON_TEXT
```

## 5. assessment_prompt_patch

### Goal

Shift from activity reward to work evidence + process evidence + display/reflection.

### Required Candidate Output

```text
rubric_dimensions
evidence_type
evidence_source
teacher_observation_points
self_peer_teacher_review
formal_scoring=false
```

### Add

```text
Assessment must connect to student work and classroom process.
Use task-fit dimensions rather than generic "good/fair/needs improvement".
Do not produce formal scores, ranking, or student profile writeback.
If the lesson uses tools or shared materials, safety/cleanliness may be included as optional evidence, not a universal score.
```

### Quality Labels To Avoid

```text
ASSESSMENT_AS_REWARD_ONLY
NO_WORK_EVIDENCE
NO_PROCESS_EVIDENCE
GENERIC_RUBRIC
FORMAL_SCORE_RISK
```

## Recommended Patch Order

```text
1. material_intake_prompt_patch
2. teaching_process_and_demo_prompt_patch
3. assessment_prompt_patch
4. unit_design_prompt_patch
5. lesson_design_prompt_patch
```

Reason: material provenance and demo/evidence quality are the highest-risk areas before fixture generation.

