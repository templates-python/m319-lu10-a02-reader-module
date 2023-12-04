from input_reader import read_int, read_float

def test_read_float_valid_input(monkeypatch):
    """ Testet die Funktion 'read_float' mit einer gültigen Eingabe. """
    monkeypatch.setattr('builtins.input', lambda _: "3.14")
    assert read_float("Enter a number: ") == 3.14, "Fehler bei korrekter Gleitkommazahl-Eingabe"

def test_read_float_invalid_then_valid_input(monkeypatch, capsys):
    """ Testet die Funktion 'read_float' erst mit einer ungültigen, dann mit einer gültigen Eingabe. """
    inputs = iter(["no number", "2.718"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Erster Aufruf von read_float, erwartet die ungültige Eingabe, dann die gültige
    assert read_float("Enter a number: ") == 2.718, "Fehler bei korrekter Gleitkommazahl-Eingabe nach ungültiger Eingabe"

    # Überprüfung der Ausgabe nach der ersten, ungültigen Eingabe
    captured = capsys.readouterr()
    assert "Please, enter a real number!" in captured.out, "Fehlermeldung bei ungültiger Eingabe nicht korrekt"

def test_read_int_valid_input(monkeypatch):
    """ Testet die Funktion 'read_int' mit einer gültigen Eingabe. """
    monkeypatch.setattr('builtins.input', lambda _: "42")
    assert read_int("Enter a number: ") == 42, "Fehler bei korrekter Ganzzahl-Eingabe"

def test_read_int_invalid_then_valid_input(monkeypatch, capsys):
    """ Testet die Funktion 'read_int' erst mit einer ungültigen, dann mit einer gültigen Eingabe. """
    inputs = iter(["no number", "100"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Erster Aufruf von read_int, erwartet die ungültige Eingabe, dann die gültige
    assert read_int("Enter a number: ") == 100, "Fehler bei korrekter Ganzzahl-Eingabe nach ungültiger Eingabe"

    # Überprüfung der Ausgabe nach der ersten, ungültigen Eingabe
    captured = capsys.readouterr()
    assert "Please, enter a valid whole number!" in captured.out, "Fehlermeldung bei ungültiger Ganzzahl-Eingabe nicht korrekt"

def test_docstring():
    assert read_int.__doc__ != None, "Docstring is missing"
    assert read_float.__doc__ != None, "Docstring is missing"