import pytest
from unittest import mock

import todo


def test_exit(capsys):
    with mock.patch('builtins.input', side_effect=['exit']):
        # This test is entering 'exit' and should therefor just stop the main function
        todo.main()


def test_add(capsys):
    with mock.patch('builtins.input', side_effect=['add WDIC Hausübung', 'list', 'exit']):
        # This test is adding one item and "list" it on the stdout
        todo.main()
        output_lines = capsys.readouterr().out.splitlines()
        assert 'WDIC Hausübung' in output_lines[0], 'Added item was not found in "list" output'
        assert '1.' in output_lines[0], 'Index "1" was not found in "list" output'
        assert len(output_lines) == 1, 'Only one line should be on output of "list"'


def test_add_and_remove(capsys):
    with mock.patch('builtins.input', side_effect=['add WDIC Hausübung', 'add Äpfel einkaufen', 'list', 'add "Krieg und Frieden" lesen', 'remove 2', 'list', 'exit']):
        # This test is adding and removing items
        todo.main()
        output_lines = capsys.readouterr().out.splitlines()

        # Checking first "list"
        assert 'WDIC Hausübung' in output_lines[0], 'Added item was not found in "list" output'
        assert '1.' in output_lines[0], 'Index "1" was not found in "list" output (or not at the expected line)'
        assert 'Äpfel einkaufen' in output_lines[1], 'Added item was not found in "list" output'
        assert '2.' in output_lines[1], 'Index "2" was not found in "list" output (or not at the expected line)'

        # "list" after removing second entry
        assert 'WDIC Hausübung' in output_lines[2], 'Added item was not found in "list" output'
        assert '1.' in output_lines[2], 'Index "1" was not found in "list" output (or not at the expected line)'
        assert 'Krieg und Frieden' in output_lines[3], 'Added item was not found in "list" output'
        assert '2.' in output_lines[3], 'Index "2" was not found in "list" output (or not at the expected line)'

        assert len(output_lines) == 4, 'Only four line should be on output of "list"'


def test_help(capsys):
    with mock.patch('builtins.input', side_effect=['help', 'wrong', 'exit']):
        # This test is testing for various wrong input to remove
        todo.main()

        output = capsys.readouterr().out

        assert 'add' in output, 'A help text for "add" should be available in output'
        assert 'remove' in output, 'A help text for "remove" should be available in output'
        assert 'list' in output, 'A help text for "list" should be available in output'
        assert 'help' in output, 'A help text for "help" should be available in output'
        assert 'exit' in output, 'A help text for "exit" should be available in output'

        output_lines = output.splitlines()
        assert output_lines[0] == output_lines[len(output_lines) // 2], 'A wrong command chould lead to the help text'


def test_invalid_remove(capsys):
    with mock.patch('builtins.input', side_effect=['add WDIC Hausübung', 'remove 0', 'remove 2', 'remove -1', 'remove WDIC Hausübung', 'remove', 'list', 'exit']):
        # This test is testing for various wrong input to remove
        todo.main()

        output_lines = capsys.readouterr().out.splitlines()

        assert 'WDIC Hausübung' in output_lines[0], 'Added item was not found in "list" output'
        assert '1.' in output_lines[0], 'Index "1" was not found in "list" output (or not at the expected line)'
        assert len(output_lines) == 1, 'Only one line should be on output of "list"'


def test_invalid_arguments(capsys):
    with mock.patch('builtins.input', side_effect=['add Sentinel', 'list add', 'help help', 'list', 'exit test', 'exit']):
        # This test is testing for various wrong input to commands
        todo.main()

        output_lines = capsys.readouterr().out.splitlines()

        assert 'Sentinel' in output_lines[-1], 'Item "Sentinel" should be the only added item'
