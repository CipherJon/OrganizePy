import unittest
from unittest.mock import patch, call
import os
from file_organizer.organizer import organize_files
from file_organizer.config import DUPLICATE_HANDLING

class TestOrganizer(unittest.TestCase):
    @patch('file_organizer.organizer.shutil.move')
    @patch('file_organizer.organizer.os.listdir')
    @patch('file_organizer.organizer.os.path.isfile')  # Added this patch
    @patch('file_organizer.organizer.ensure_dir_exists')
    @patch('file_organizer.organizer.DUPLICATE_HANDLING', {'enabled': False})
    def test_organize_files(self, mock_ensure_dir_exists, mock_isfile, mock_listdir, mock_move):
        base_dir = "/fake/dir"
        file_types = {"images": [".jpg"], "documents": [".pdf"]}

        mock_listdir.return_value = ["test.jpg", "test.pdf"]
        mock_isfile.return_value = True  # Ensure mocked files are treated as files

        # Mock DATE_ORGANIZATION settings
        with patch('file_organizer.organizer.DATE_ORGANIZATION', {'enabled': False}):
            organize_files(base_dir, file_types)

        mock_ensure_dir_exists.assert_has_calls([
            call(os.path.join(base_dir, "images")),
            call(os.path.join(base_dir, "documents"))
        ], any_order=True)

        mock_move.assert_has_calls([
            call(os.path.join(base_dir, "test.jpg"), os.path.join(base_dir, "images", "test.jpg")),
            call(os.path.join(base_dir, "test.pdf"), os.path.join(base_dir, "documents", "test.pdf"))
        ], any_order=True)

if __name__ == '__main__':
    unittest.main()