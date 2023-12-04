import pytest
from main import main  # Ersetzen Sie 'your_module' durch den tatsächlichen Modulnamen, der 'main' enthält

def test_main(monkeypatch, capsys):
    """ Testet die 'main'-Funktion mit simulierten Eingaben für 'read_float' und 'read_int'. """
    # Simulierte Eingaben: Zuerst für 'read_float', dann für 'read_int'
    inputs = iter(["3.14", "42"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Aufrufen der main-Funktion
    main()

    # Erfassen und Überprüfen der Ausgabe
    captured = capsys.readouterr()
    expected_output = "3.14\n42\n"
    assert captured.out == expected_output, f"Fehler in der Ausgabe der 'main'-Funktion. Erwartet: {expected_output}, Erhalten: {captured.out}"


def test_main_with_invalid_then_valid_inputs(monkeypatch, capsys):
    """
    Testet die 'main'-Funktion mit zuerst ungültigen und dann gültigen Eingaben
    für 'read_float' und 'read_int'.
    """
    # Simulierte Eingaben: Ungültig, dann gültig für 'read_float', ebenso für 'read_int'
    inputs = iter(["no number", "3.14", "not a number", "42"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Aufrufen der main-Funktion
    main()

    # Erfassen und Überprüfen der Ausgabe
    captured = capsys.readouterr()
    expected_output = ("Please, enter a real number!\n"  # Fehlermeldung von read_float
                       "Please, enter a valid whole number!\n"  # Fehlermeldung von read_int
                       "3.14\n"  # Korrekte Ausgabe von read_float
                       "42\n")  # Korrekte Ausgabe von read_int
    assert captured.out == expected_output, f"Fehler in der Ausgabe der 'main'-Funktion. Erwartet: {expected_output}, Erhalten: {captured.out}"