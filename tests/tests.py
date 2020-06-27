import unittest
import rasa_plus.__main__ as rasa_plus
import os
import shutil


class TestRasaPlus(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.t_domain = "tests/test_files/domain"
        return super().setUp()

    def test_get_files_path_not_provided(self):
        with self.assertRaises(TypeError):
            rasa_plus._get_files()

    def test_get_files_path_does_not_exist(self):
        self.assertEqual(len(rasa_plus._get_files(path="random")), 0)

    def test_file_finder(self):
        self.assertEqual(len(rasa_plus._get_files(path=f"{self.t_domain}/original")), 1)

    def test_file_finder_multiple_files(self):
        self.assertEqual(len(rasa_plus._get_files(path=f"{self.t_domain}/2_split/")), 2)

    def test_file_finder_multiple_folders(self):
        self.assertEqual(
            len(rasa_plus._get_files(path=f"{self.t_domain}/multiple_folders")), 7
        )

    def test_path_correct(self):
        self.assertEqual(
            rasa_plus._get_files(path=f"{self.t_domain}/original"),
            rasa_plus._get_files(path=f"{self.t_domain}/original/"),
        )

    def test_unify_domain_without_path(self):
        with self.assertRaises(TypeError):
            rasa_plus._unify_domain()

    def test_simple_unification(self):
        expected = open(f"{self.t_domain}/expected/domain-2-split.yml", "r").read()
        self.assertEqual(
            rasa_plus._unify_domain(path=f"{self.t_domain}/2_split/"), expected
        )

    def test_complicated_unification(self):
        expected = open(
            f"{self.t_domain}/expected/domain-multiple-folders.yml", "r"
        ).read()
        self.assertEqual(
            rasa_plus._unify_domain(path=f"{self.t_domain}/multiple_folders/"), expected
        )

    def test_file_generation_path_does_not_exist(self):
        content = "test domain"
        path = "random"
        filename = "test.yml"
        with self.assertRaises(FileNotFoundError):
            rasa_plus._generate_file(path=path, filename=filename, content=content)

    def test_file_generation_path_does_not_exist(self):
        content = "test domain"
        path = "random"
        filename = "test.yml"
        with self.assertRaises(FileNotFoundError):
            rasa_plus._generate_file(path=path, filename=filename, content=content)

    def test_file_generation(self):
        content = "test domain"
        path = "tests/test_files/temp/"
        filename = "test.yml"
        fpath= f"{path}{filename}"

        if not os.path.exists(path):
            os.mkdir(path)

        self.assertFalse(os.path.exists(fpath) and os.path.isfile(fpath))
        rasa_plus._generate_file(path=path, filename=filename, content=content)
        self.assertTrue(os.path.exists(fpath) and os.path.isfile(fpath))

        shutil.rmtree(path, ignore_errors=True)
        



if __name__ == "__main__":
    unittest.main()
