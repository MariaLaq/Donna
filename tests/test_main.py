from donna.main import main


def test_main_runs(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from Donna!" in captured.out
