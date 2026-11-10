"""Driver-session-specific exclusions from predictive qualifying pace history.

These are evidence-quality annotations, not alterations of original results.
Entries require external, attributable incident provenance; do not add entries
based solely on a disappointing finishing or qualifying position.
"""

QUALIFYING_PACE_EXCLUSIONS = {
    (2026, 15, "Q", "ANT"): {
        "reason": "Antonelli crashed at Turn 1 in Q1 and could not run Q2/Q3; his saved lap is not representative of maximum qualifying pace.",
        "source": "https://www.formula1.com/en/latest/article/a-good-way-to-come-back-to-earth-antonelli-rues-very-stupid-mistake-during-azerbaijan-grand-prix-qualifying.2XUXR2KRfYXq5W76q4ibkd",
        "scope": "prediction_only",
    },
}
