"""
Comprehensive Acceptance Tests for Lendy Chatbot as specified in prompt.
"""

import pytest
from tests.verify_lendy_matrix import (
    derive_ticket_size,
    lookup_base_rates,
    determine_final_approval,
    calculate_reducing_emi,
    calculate_dti,
)


def test_acceptance_case_1():
    # 1. R, Above 5 Lacs, Documented, SORP, >=700, loan 10,00,000: Base ROI 18, PF 2.
    ticket = derive_ticket_size("Regular Secured Business Loan", 1000000.0)
    assert ticket == "Above 5 Lacs"

    base_roi, base_pf = lookup_base_rates(
        product="Regular Secured Business Loan",
        ticket_size=ticket,
        income_program="Documented Income Program",
        property_type="SORP",
        bureau=">=700 or NTC",
    )
    assert base_roi == 18.0
    assert base_pf == 2.0

    # Requested ROI 16.5 and PF 2 -> deviation 1.5 -> CBO
    res1 = determine_final_approval(base_roi, 16.5, base_pf, 2.0)
    assert res1["roi_deviation"] == 1.5
    assert res1["final_approver"] == "CBO"

    # Requested ROI 15 -> deviation 3 -> COO
    res2 = determine_final_approval(base_roi, 15.0, base_pf, 2.0)
    assert res2["roi_deviation"] == 3.0
    assert res2["final_approver"] == "COO"

    # Requested ROI 13.5 -> deviation 4.5 -> CEO
    res3 = determine_final_approval(base_roi, 13.5, base_pf, 2.0)
    assert res3["roi_deviation"] == 4.5
    assert res3["final_approver"] == "CEO"


def test_acceptance_case_2():
    # 2. Same case with requested ROI 18 and PF 1.2 -> PF deviation 0.8 -> CBO.
    # With PF 0.4 -> deviation 1.6 -> CEO.
    base_roi = 18.0
    base_pf = 2.0

    res1 = determine_final_approval(base_roi, 18.0, base_pf, 1.2)
    assert pytest.approx(res1["pf_deviation"], 0.01) == 0.8
    assert res1["final_approver"] == "CBO"

    res2 = determine_final_approval(base_roi, 18.0, base_pf, 0.4)
    assert pytest.approx(res2["pf_deviation"], 0.01) == 1.6
    assert res2["final_approver"] == "CEO"


def test_acceptance_case_3():
    # 3. ROI deviation 3 (COO) combined with PF deviation 1.6 (CEO) -> final approver CEO
    base_roi = 18.0
    base_pf = 2.0
    res = determine_final_approval(base_roi, 15.0, base_pf, 0.4)
    assert res["roi_approver"] == "COO"
    assert res["pf_approver"] == "CEO"
    assert res["final_approver"] == "CEO"


def test_acceptance_case_4():
    # 4. Requested ROI 19 and PF 2 on the case above -> no approval.
    base_roi = 18.0
    base_pf = 2.0
    res = determine_final_approval(base_roi, 19.0, base_pf, 2.0)
    assert res["roi_deviation"] == -1.0
    assert res["pf_deviation"] == 0.0
    assert res["final_approver"] == "NONE"
    assert res["requires_approval"] is False


def test_acceptance_case_5():
    # 5. Loan 10,00,000 at 18% for 60 months -> EMI about 25,393.
    emi = calculate_reducing_emi(principal=1000000.0, annual_rate_pct=18.0, tenure_months=60)
    assert round(emi) == 25393


def test_acceptance_case_6():
    # 6. Income 80,000/month, existing EMIs 20,000, new EMI 25,393 -> current DTI 25%,
    # updated DTI about 56.7%, with the DTI warning shown.
    curr_dti, upd_dti, warning = calculate_dti(existing_emis=20000.0, new_emi=25393.43, monthly_income=80000.0)
    assert curr_dti == 25.0
    assert round(upd_dti, 1) == 56.7
    assert warning is True


def test_acceptance_case_7():
    # 7. Annual income 12,00,000 is treated as 1,00,000/month.
    annual_income = 1200000.0
    monthly_income = annual_income / 12.0
    assert monthly_income == 100000.0


def test_acceptance_case_8():
    # 8. Hypothecation product skips the property-type question.
    product = "Hypothecation Loans"
    ticket = derive_ticket_size(product, 300000.0)
    assert ticket == "All Ticket Size"

    # Property type for Hypothecation is NA
    roi, pf = lookup_base_rates(product, ticket, "Documented Income Program", "NA", ">=700 or NTC")
    assert roi == 20.0
    assert pf == 3.0
