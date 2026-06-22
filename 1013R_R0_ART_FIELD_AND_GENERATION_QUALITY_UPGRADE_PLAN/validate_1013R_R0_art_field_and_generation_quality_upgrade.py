import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "1013R_R0_result.json",
    "1013R_R0_report.md",
    "art_field_upgrade_matrix_1013R_R0.json",
    "art_generation_quality_standard_1013R_R0.md",
    "prompt_upgrade_recommendations_1013R_R0.md",
    "external_and_internal_sample_gap_review_1013R_R0.md",
    "generation_quality_test_case_bank_1013R_R0.json",
    "art_design_spine_to_four_modules_mapping_1013R_R0.json",
    "teacher_review_checklist_1013R_R0.md",
    "validate_1013R_R0_art_field_and_generation_quality_upgrade.py",
]

TRUE_BOUNDARY_KEYS = [
    "review_draft_only",
]

FALSE_BOUNDARY_KEYS = [
    "formal_apply_performed",
    "database_written",
    "memory_written",
    "vector_index_written",
    "chunks_built",
    "feishu_written",
    "main_project_pushed",
    "R36_modified",
    "foundation_contracts_modified",
    "provider_called",
    "model_called",
    "runtime_connected",
    "formal_frontend_binding_allowed",
    "full_unit_body_generated",
    "complete_lesson_body_generated",
    "official_claim_from_teacher_reference",
    "external_sample_fields_required",
    "scenario_packaging_as_required_field",
    "prompt_patch_applied",
]

QUALITY_CATEGORIES = [
    "unit_design",
    "lesson_design",
    "teaching_process",
    "art_demo_block",
    "assessment_design",
]

SCENARIO_WORDS = [
    "时光机",
    "昆虫特工队",
    "色彩魔法",
    "建筑勋章",
    "小小讲解员",
]

FORBIDDEN_REQUIRED_FIELDS = {
    "full_unit_body",
    "complete_lesson_body",
    "official_curriculum_claim",
    "formal_scoring_rule",
    "scenario_text",
    "activity_reward_label",
    "external_sample_phrase",
}


def load_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def fail_if(condition, message, failures):
    if condition:
        failures.append(message)


def iter_fields(matrix):
    groups = matrix.get("field_groups", {})
    for group_name, group in groups.items():
        if isinstance(group, dict) and "fields" in group:
            for field in group["fields"]:
                if isinstance(field, dict):
                    yield group_name, field
        elif isinstance(group, dict):
            for subgroup_name, subgroup in group.items():
                if isinstance(subgroup, dict) and "fields" in subgroup:
                    for field in subgroup["fields"]:
                        if isinstance(field, dict):
                            yield f"{group_name}.{subgroup_name}", field


def main():
    failures = []

    for name in REQUIRED_FILES:
        fail_if(not (ROOT / name).exists(), f"missing required file: {name}", failures)

    if failures:
        print(json.dumps({"status": "FAIL", "failures": failures}, ensure_ascii=False, indent=2))
        raise SystemExit(1)

    result = load_json("1013R_R0_result.json")
    matrix = load_json("art_field_upgrade_matrix_1013R_R0.json")
    test_bank = load_json("generation_quality_test_case_bank_1013R_R0.json")
    mapping = load_json("art_design_spine_to_four_modules_mapping_1013R_R0.json")

    boundary = result.get("boundary", {})
    for key in TRUE_BOUNDARY_KEYS:
        fail_if(boundary.get(key) is not True, f"boundary {key} must be true", failures)
    for key in FALSE_BOUNDARY_KEYS:
        fail_if(boundary.get(key) is not False, f"boundary {key} must be false", failures)

    produced = set(result.get("outputs", []))
    for name in REQUIRED_FILES:
        fail_if(name not in produced, f"result outputs missing {name}", failures)

    fail_if(result.get("preferred_next_stage") != "1013R_R1_FIELD_PATCH_AND_PROMPT_PATCH_STATIC_FIXTURE",
            "preferred_next_stage must be 1013R_R1_FIELD_PATCH_AND_PROMPT_PATCH_STATIC_FIXTURE", failures)

    categories = result.get("quality_label_categories", {})
    for category in QUALITY_CATEGORIES:
        labels = categories.get(category, [])
        fail_if(not labels, f"quality labels missing for {category}", failures)

    quality_md = (ROOT / "art_generation_quality_standard_1013R_R0.md").read_text(encoding="utf-8")
    for label in [
        "UNIT_AS_LESSON_LIST",
        "LESSON_ISOLATED_FROM_UNIT",
        "PROCESS_AS_PARAGRAPH",
        "GENERIC_DEMO",
        "ASSESSMENT_AS_REWARD_ONLY",
    ]:
        fail_if(label not in quality_md, f"quality standard missing label {label}", failures)

    fail_if(matrix.get("source_rules", {}).get("external_sample_can_make_required_field") is not False,
            "external_sample_can_make_required_field must be false", failures)
    fail_if(matrix.get("source_rules", {}).get("scenario_text_can_be_stable_required_field") is not False,
            "scenario_text_can_be_stable_required_field must be false", failures)
    fail_if(matrix.get("source_rules", {}).get("teacher_uploaded_reference_official_claim_allowed") is not False,
            "teacher_uploaded_reference_official_claim_allowed must be false", failures)

    for group_name, field in iter_fields(matrix):
        field_name = field.get("field", "")
        level = field.get("level")
        source_basis = field.get("source_basis", [])
        fail_if(level == "required" and "external_sample" in source_basis,
                f"external sample field must not be required: {group_name}.{field_name}", failures)
        fail_if(level == "required" and field_name in FORBIDDEN_REQUIRED_FIELDS,
                f"forbidden field is required: {group_name}.{field_name}", failures)
        for word in SCENARIO_WORDS:
            fail_if(level == "required" and word in field_name,
                    f"scenario packaging word appears in required field: {word}", failures)

    forbidden = set(matrix.get("field_groups", {}).get("forbidden_as_required", {}).get("fields", []))
    fail_if(not FORBIDDEN_REQUIRED_FIELDS.issubset(forbidden),
            "forbidden_as_required must include full body, official claim, scoring, scenario fields", failures)

    prompt_md = (ROOT / "prompt_upgrade_recommendations_1013R_R0.md").read_text(encoding="utf-8")
    fail_if("recommendation_only=true" not in prompt_md, "prompt patch must be recommendation only", failures)
    fail_if("prompt_patch_applied=false" not in prompt_md, "prompt patch must not be applied", failures)

    external_md = (ROOT / "external_and_internal_sample_gap_review_1013R_R0.md").read_text(encoding="utf-8")
    fail_if("external_sample_is_reference_only=true" not in external_md,
            "external sample must be reference only", failures)
    fail_if("official_claim_allowed=false" not in external_md,
            "external sample must not allow official claims", failures)

    fail_if(test_bank.get("test_case_count") != 5, "test case bank must contain 5 cases", failures)
    for case in test_bank.get("test_cases", []):
        for key in [
            "grade",
            "topic",
            "lesson_or_unit_type",
            "expected_big_idea",
            "expected_student_output",
            "expected_materials",
            "expected_technique_chain",
            "expected_demo_need",
            "expected_assessment_evidence",
            "expected_courseware_screen_types",
            "known_risks",
        ]:
            fail_if(key not in case, f"test case {case.get('case_id')} missing {key}", failures)

    fail_if(mapping.get("art_design_spine_candidate", {}).get("replaces_existing_modules") is not False,
            "spine must not replace existing modules", failures)
    fail_if(mapping.get("art_design_spine_candidate", {}).get("generates_formal_body") is not False,
            "spine must not generate formal body", failures)

    html_files = list(ROOT.glob("*.html"))
    fail_if(bool(html_files), f"R0 must not create HTML/page files: {html_files}", failures)

    combined_text = "\n".join((ROOT / name).read_text(encoding="utf-8") for name in REQUIRED_FILES if name.endswith((".md", ".json")))
    fail_if("formal_apply_performed=true" in combined_text, "formal apply must not be true", failures)
    fail_if("provider_called=true" in combined_text, "provider_called must not be true", failures)
    fail_if("model_called=true" in combined_text, "model_called must not be true", failures)
    fail_if("R36_modified=true" in combined_text, "R36_modified must not be true", failures)
    fail_if("foundation_contracts_modified=true" in combined_text, "foundation_contracts_modified must not be true", failures)

    if failures:
        print(json.dumps({"status": "FAIL", "failures": failures}, ensure_ascii=False, indent=2))
        raise SystemExit(1)

    print(json.dumps({
        "status": "PASS",
        "stage": result["stage"],
        "checked_files": REQUIRED_FILES,
        "boundary_checked": True,
        "quality_categories_checked": QUALITY_CATEGORIES,
        "test_case_count": test_bank.get("test_case_count"),
        "external_sample_required_field_blocked": True,
        "scenario_required_field_blocked": True,
        "prompt_patch_recommendation_only": True
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
