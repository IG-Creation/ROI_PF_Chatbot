from app.chatbot.handler import handle_chat_message
from app.chatbot.intent import classify_intent, extract_entities, IntentType


def test_intent_classification():
    assert classify_intent("hello") == IntentType.GREETING
    assert classify_intent("help") == IntentType.HELP
    assert classify_intent("Calculate ROI for 20k cost and 35k return") == IntentType.CALCULATE_ROI
    assert classify_intent("Profit factor gross profit 50000, gross loss 20000") == IntentType.CALCULATE_PF
    assert classify_intent("Break even: fixed costs 20000, variable 10, price 30") == IntentType.BREAK_EVEN


def test_entity_extraction():
    entities = extract_entities("Calculate ROI on cost $25,000 and return $40,000 over 3 years")
    assert entities.cost == 25000.0
    assert entities.gain == 40000.0
    assert entities.years == 3.0


def test_chat_message_roi():
    resp = handle_chat_message("Calculate ROI on $10,000 cost and $15,000 return", "test_session_1")
    assert resp.intent == "CALCULATE_ROI"
    assert "Return on Investment" in resp.message
    assert resp.data["roi_percent"] == 50.0


def test_chat_message_pricing_factor():
    resp = handle_chat_message("Cost is $40, selling price is $80, calculate pricing factor", "test_session_2")
    assert "Pricing Factor" in resp.message
    assert resp.data["pricing_factor"] == 2.0


def test_chat_message_break_even():
    resp = handle_chat_message("Break even: fixed 10000, variable cost 10, price 20", "test_session_3")
    assert "Break-Even" in resp.message
    assert resp.data["break_even_units"] == 1000.0
