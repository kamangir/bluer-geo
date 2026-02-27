# pylint: skip-file

if not QGIS_is_live:
    from ..logger import (
        Q_clear,
        Q_hr,
        Q_log,
        Q_log_error,
        Q_log_warning,
        Q_verbose,
    )


def test_logging():
    Q_clear()

    Q_hr()
    Q_hr(length=5)

    Q_log("some message")
    Q_log("some message", "some note")
    Q_log("some message", "some note", "🔍")

    Q_log_error("this is a test, don't panic! 😁")

    Q_log_warning("this is a test, don't panic! 😁")

    assert isinstance(Q_verbose, bool)
