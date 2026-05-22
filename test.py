"""
Unit Tests for Hospital Management System
Tests all core logic: add, view, search, delete, and exception handling.
Run with: python -m pytest test_main.py -v
       or: python test_main.py
"""

import unittest


# ─── Standalone logic functions (extracted for testability) ──────────────────

patients = []  # Shared in-memory store for testing


def add_patient_logic(patient_id, name, disease):
    """Core logic for adding a patient (independent of GUI)."""
    if not isinstance(patient_id, int):
        raise TypeError("Patient ID must be an integer.")
    if not name or not name.strip():
        raise ValueError("Name cannot be empty.")
    if not disease or not disease.strip():
        raise ValueError("Disease cannot be empty.")
    for p in patients:
        if p["id"] == patient_id:
            raise ValueError(f"Patient ID {patient_id} already exists.")
    patients.append({"id": patient_id, "name": name.strip(), "disease": disease.strip()})
    return True


def search_patient_logic(patient_id):
    """Core logic for searching a patient by ID."""
    for p in patients:
        if p["id"] == patient_id:
            return p
    return None


def delete_patient_logic(patient_id):
    """Core logic for deleting a patient by ID."""
    for i, p in enumerate(patients):
        if p["id"] == patient_id:
            return patients.pop(i)
    return None


def view_patients_logic():
    """Returns all patients."""
    return list(patients)


# ─── Test Cases ──────────────────────────────────────────────────────────────

class TestAddPatient(unittest.TestCase):

    def setUp(self):
        """Clear patient list before each test."""
        patients.clear()

    def test_add_valid_patient(self):
        """Test Case 1: Adding a valid patient should succeed."""
        result = add_patient_logic(1, "Ali Hassan", "Flu")
        self.assertTrue(result)
        self.assertEqual(len(patients), 1)

    def test_add_patient_empty_name(self):
        """Test Case 2: Empty name should raise ValueError."""
        with self.assertRaises(ValueError):
            add_patient_logic(2, "", "Fever")

    def test_add_patient_empty_disease(self):
        """Test Case 3: Empty disease should raise ValueError."""
        with self.assertRaises(ValueError):
            add_patient_logic(3, "Sara", "")

    def test_add_duplicate_patient_id(self):
        """Test Case 4: Duplicate ID should raise ValueError."""
        add_patient_logic(1, "Ali", "Flu")
        with self.assertRaises(ValueError):
            add_patient_logic(1, "Ahmed", "Cold")

    def test_add_invalid_id_type(self):
        """Test Case 5: Non-integer ID should raise TypeError."""
        with self.assertRaises(TypeError):
            add_patient_logic("abc", "Sara", "Cold")

    def test_add_multiple_patients(self):
        """Test Case 6: Multiple patients can be added."""
        add_patient_logic(1, "Ali", "Flu")
        add_patient_logic(2, "Sara", "Cold")
        add_patient_logic(3, "Ahmed", "Fever")
        self.assertEqual(len(patients), 3)


class TestSearchPatient(unittest.TestCase):

    def setUp(self):
        patients.clear()
        add_patient_logic(101, "Ali Hassan", "Diabetes")
        add_patient_logic(102, "Sara Khan", "Asthma")

    def test_search_existing_patient(self):
        """Test Case 7: Search existing patient returns correct record."""
        result = search_patient_logic(101)
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Ali Hassan")

    def test_search_nonexistent_patient(self):
        """Test Case 8: Search non-existent ID returns None."""
        result = search_patient_logic(999)
        self.assertIsNone(result)

    def test_search_correct_disease(self):
        """Test Case 9: Correct disease returned for patient."""
        result = search_patient_logic(102)
        self.assertEqual(result["disease"], "Asthma")


class TestDeletePatient(unittest.TestCase):

    def setUp(self):
        patients.clear()
        add_patient_logic(201, "Ahmed Raza", "Malaria")
        add_patient_logic(202, "Fatima Noor", "TB")

    def test_delete_existing_patient(self):
        """Test Case 10: Deleting existing patient removes them."""
        result = delete_patient_logic(201)
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Ahmed Raza")
        self.assertEqual(len(patients), 1)

    def test_delete_nonexistent_patient(self):
        """Test Case 11: Deleting non-existent patient returns None."""
        result = delete_patient_logic(999)
        self.assertIsNone(result)

    def test_delete_reduces_count(self):
        """Test Case 12: Patient count decreases after deletion."""
        delete_patient_logic(201)
        self.assertEqual(len(patients), 1)


class TestViewPatients(unittest.TestCase):

    def setUp(self):
        patients.clear()

    def test_view_empty_list(self):
        """Test Case 13: View returns empty list when no patients."""
        result = view_patients_logic()
        self.assertEqual(result, [])

    def test_view_returns_all(self):
        """Test Case 14: View returns all added patients."""
        add_patient_logic(1, "Ali", "Flu")
        add_patient_logic(2, "Sara", "Cold")
        result = view_patients_logic()
        self.assertEqual(len(result), 2)


# ─── Run ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    unittest.main(verbosity=2)