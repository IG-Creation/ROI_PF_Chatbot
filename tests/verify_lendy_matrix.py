"""
Verification script for Lendy loan pricing & approval matrix logic.
"""

import math

CONFIG = {
    "DTI_LIMIT_PERCENT": 50.0,
    "ROUNDING_TOLERANCE": 1e-6,
    "APPROVERS": {
        "NONE": {"name": "No Approval Needed", "level": 0, "color": "green"},
        "CBO": {"name": "CBO Approval", "level": 1, "color": "blue"},
        "COO": {"name": "COO Approval", "level": 2, "color": "amber"},
        "CEO": {"name": "CEO Approval", "level": 3, "color": "red"},
    },
    "BANDS": {
        "ROI": [
            {"max": 0.0, "approver": "NONE"},
            {"max": 2.0, "approver": "CBO"},
            {"max": 4.0, "approver": "COO"},
            {"max": float("inf"), "approver": "CEO"},
        ],
        "PF": [
            {"max": 0.0, "approver": "NONE"},
            {"max": 1.0, "approver": "CBO"},
            {"max": 1.5, "approver": "COO"},
            {"max": float("inf"), "approver": "CEO"},
        ],
    },
}

# The 56 rows matrix definition
MATRIX = [
    # Regular Secured Business Loan - Upto 5 Lacs
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Documented Income Program", "property": "SORP", "bureau": ">=700 or NTC", "base_roi": 20.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Documented Income Program", "property": "SORP", "bureau": "<700", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Documented Income Program", "property": "Other", "bureau": ">=700 or NTC", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Documented Income Program", "property": "Other", "bureau": "<700", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Assessed Income Program", "property": "SORP", "bureau": ">=700 or NTC", "base_roi": 21.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Hybrid Income Program", "property": "SORP", "bureau": ">=700 or NTC", "base_roi": 21.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Semi Documented Income Program", "property": "SORP", "bureau": ">=700 or NTC", "base_roi": 21.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Assessed Income Program", "property": "SORP", "bureau": "<700", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Hybrid Income Program", "property": "SORP", "bureau": "<700", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Semi Documented Income Program", "property": "SORP", "bureau": "<700", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Assessed Income Program", "property": "Other", "bureau": ">=700 or NTC", "base_roi": 21.5, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Hybrid Income Program", "property": "Other", "bureau": ">=700 or NTC", "base_roi": 21.5, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Semi Documented Income Program", "property": "Other", "bureau": ">=700 or NTC", "base_roi": 21.5, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Assessed Income Program", "property": "Other", "bureau": "<700", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Hybrid Income Program", "property": "Other", "bureau": "<700", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Upto 5 Lacs", "income": "Semi Documented Income Program", "property": "Other", "bureau": "<700", "base_roi": 22.0, "base_pf": 3.0},

    # Regular Secured Business Loan - Above 5 Lacs
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Documented Income Program", "property": "SORP", "bureau": ">=700 or NTC", "base_roi": 18.0, "base_pf": 2.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Documented Income Program", "property": "SORP", "bureau": "<700", "base_roi": 20.0, "base_pf": 2.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Documented Income Program", "property": "Other", "bureau": ">=700 or NTC", "base_roi": 19.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Documented Income Program", "property": "Other", "bureau": "<700", "base_roi": 20.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Assessed Income Program", "property": "SORP", "bureau": ">=700 or NTC", "base_roi": 20.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Hybrid Income Program", "property": "SORP", "bureau": ">=700 or NTC", "base_roi": 20.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Semi Documented Income Program", "property": "SORP", "bureau": ">=700 or NTC", "base_roi": 20.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Assessed Income Program", "property": "SORP", "bureau": "<700", "base_roi": 20.5, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Hybrid Income Program", "property": "SORP", "bureau": "<700", "base_roi": 20.5, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Semi Documented Income Program", "property": "SORP", "bureau": "<700", "base_roi": 20.5, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Assessed Income Program", "property": "Other", "bureau": ">=700 or NTC", "base_roi": 20.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Hybrid Income Program", "property": "Other", "bureau": ">=700 or NTC", "base_roi": 20.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Semi Documented Income Program", "property": "Other", "bureau": ">=700 or NTC", "base_roi": 20.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Assessed Income Program", "property": "Other", "bureau": "<700", "base_roi": 21.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Hybrid Income Program", "property": "Other", "bureau": "<700", "base_roi": 21.0, "base_pf": 3.0},
    {"product": "Regular Secured Business Loan", "ticket": "Above 5 Lacs", "income": "Semi Documented Income Program", "property": "Other", "bureau": "<700", "base_roi": 21.0, "base_pf": 3.0},

    # Secured Working Capital Term Loan - All Ticket Size
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Documented Income Program", "property": "SORP", "bureau": ">=700 or NTC", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Documented Income Program", "property": "SORP", "bureau": "<700", "base_roi": 24.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Documented Income Program", "property": "Other", "bureau": ">=700 or NTC", "base_roi": 24.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Documented Income Program", "property": "Other", "bureau": "<700", "base_roi": 24.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Assessed Income Program", "property": "SORP", "bureau": ">=700 or NTC", "base_roi": 23.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Hybrid Income Program", "property": "SORP", "bureau": ">=700 or NTC", "base_roi": 23.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Semi Documented Income Program", "property": "SORP", "bureau": ">=700 or NTC", "base_roi": 23.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Assessed Income Program", "property": "SORP", "bureau": "<700", "base_roi": 24.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Hybrid Income Program", "property": "SORP", "bureau": "<700", "base_roi": 24.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Semi Documented Income Program", "property": "SORP", "bureau": "<700", "base_roi": 24.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Assessed Income Program", "property": "Other", "bureau": ">=700 or NTC", "base_roi": 24.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Hybrid Income Program", "property": "Other", "bureau": ">=700 or NTC", "base_roi": 24.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Semi Documented Income Program", "property": "Other", "bureau": ">=700 or NTC", "base_roi": 24.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Assessed Income Program", "property": "Other", "bureau": "<700", "base_roi": 24.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Hybrid Income Program", "property": "Other", "bureau": "<700", "base_roi": 24.0, "base_pf": 3.0},
    {"product": "Secured Working Capital Term Loan", "ticket": "All Ticket Size", "income": "Semi Documented Income Program", "property": "Other", "bureau": "<700", "base_roi": 24.0, "base_pf": 3.0},

    # Hypothecation Loans - All Ticket Size
    {"product": "Hypothecation Loans", "ticket": "All Ticket Size", "income": "Documented Income Program", "property": "NA", "bureau": ">=700 or NTC", "base_roi": 20.0, "base_pf": 3.0},
    {"product": "Hypothecation Loans", "ticket": "All Ticket Size", "income": "Documented Income Program", "property": "NA", "bureau": "<700", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Hypothecation Loans", "ticket": "All Ticket Size", "income": "Assessed Income Program", "property": "NA", "bureau": ">=700 or NTC", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Hypothecation Loans", "ticket": "All Ticket Size", "income": "Hybrid Income Program", "property": "NA", "bureau": ">=700 or NTC", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Hypothecation Loans", "ticket": "All Ticket Size", "income": "Semi Documented Income Program", "property": "NA", "bureau": ">=700 or NTC", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Hypothecation Loans", "ticket": "All Ticket Size", "income": "Assessed Income Program", "property": "NA", "bureau": "<700", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Hypothecation Loans", "ticket": "All Ticket Size", "income": "Hybrid Income Program", "property": "NA", "bureau": "<700", "base_roi": 22.0, "base_pf": 3.0},
    {"product": "Hypothecation Loans", "ticket": "All Ticket Size", "income": "Semi Documented Income Program", "property": "NA", "bureau": "<700", "base_roi": 22.0, "base_pf": 3.0},
]


def derive_ticket_size(product: str, loan_amount: float) -> str:
    if product == "Regular Secured Business Loan":
        if loan_amount <= 500000.0:
            return "Upto 5 Lacs"
        else:
            return "Above 5 Lacs"
    return "All Ticket Size"


def lookup_base_rates(product: str, ticket_size: str, income_program: str, property_type: str, bureau: str):
    for row in MATRIX:
        if (
            row["product"] == product
            and row["ticket"] == ticket_size
            and row["income"] == income_program
            and row["property"] == property_type
            and row["bureau"] == bureau
        ):
            return row["base_roi"], row["base_pf"]
    return None, None


def get_approver_for_deviation(deviation: float, band_type: str) -> str:
    eps = CONFIG["ROUNDING_TOLERANCE"]
    if deviation <= eps:
        return "NONE"

    bands = CONFIG["BANDS"][band_type]
    for b in bands:
        if deviation <= b["max"] + eps:
            return b["approver"]
    return "CEO"


def determine_final_approval(base_roi: float, req_roi: float, base_pf: float, req_pf: float):
    roi_dev = round(base_roi - req_roi, 4)
    pf_dev = round(base_pf - req_pf, 4)

    roi_appr = get_approver_for_deviation(roi_dev, "ROI")
    pf_appr = get_approver_for_deviation(pf_dev, "PF")

    levels = {"NONE": 0, "CBO": 1, "COO": 2, "CEO": 3}
    final_key = roi_appr if levels[roi_appr] >= levels[pf_appr] else pf_appr
    return {
        "roi_deviation": roi_dev,
        "pf_deviation": pf_dev,
        "roi_approver": roi_appr,
        "pf_approver": pf_appr,
        "final_approver": final_key,
        "requires_approval": final_key != "NONE",
    }


def calculate_reducing_emi(principal: float, annual_rate_pct: float, tenure_months: int) -> float:
    if tenure_months <= 0:
        return 0.0
    if annual_rate_pct <= 0:
        return principal / tenure_months

    r = annual_rate_pct / 12.0 / 100.0
    factor = (1.0 + r) ** tenure_months
    emi = principal * r * factor / (factor - 1.0)
    return emi


def calculate_dti(existing_emis: float, new_emi: float, monthly_income: float):
    if monthly_income <= 0:
        return 0.0, 0.0, False
    curr_dti = (existing_emis / monthly_income) * 100.0
    upd_dti = ((existing_emis + new_emi) / monthly_income) * 100.0
    warning = upd_dti > CONFIG["DTI_LIMIT_PERCENT"]
    return curr_dti, upd_dti, warning


if __name__ == "__main__":
    assert len(MATRIX) == 56, f"Expected 56 rows, got {len(MATRIX)}"
    print("Matrix has exactly 56 rows.")
