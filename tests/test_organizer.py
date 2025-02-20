import unittest
from unittest.mock import patch, call
import os
from file_organizer.organizer import organize_files

class TestOrganizer(unittest.TestCase):
    @patch('file_organizer.organizer.shutil.move')
    @patch('file_organizer.organizer.os.listdir')
    @patch('file_organizer.organizer.ensure_dir_exists')
    def test_organize_files(self, mock_ensure_dir_exists, mock_listdir, mock_move):
        base_dir = "/fake/dir"
        file_types = {"images": [".jpg"], "documents": [".pdf"]}

        mock_listdir.return_value = ["test.jpg", "test.pdf"]

        organize_files(base_dir, file_types)

        mock_ensure_dir_exists.assert_has_calls([
            call(os.path.join(base_dir, "images")),
            call(os.path.join(base_dir, "documents"))
        ], any_order=True)

        mock_move.assert_has_calls([
            call(os.path.join(base_dir, "test.jpg"), os.path.join(base_dir, "images", "test.jpg")),
            call(os.path.join(base_dir, "test.pdf"), os.path.join(base_dir, "documents", "test.pdf"))
        ], any_order=True)