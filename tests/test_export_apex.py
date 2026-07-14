import export_apex


def test_normalize_apex_app_ids_drops_blank_config_values():
    assert export_apex.normalize_apex_app_ids(["", None, "None", "100", " 200, 300 "]) == [
        100,
        200,
        300,
    ]
