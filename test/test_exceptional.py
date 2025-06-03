"""
Exception handling tests for the Game Development Utility System.
"""

import unittest
import os
import importlib
import sys
import io
import contextlib
from test.TestUtils import TestUtils

def check_file_exists(filename):
    """Check if a file exists in the current directory."""
    return os.path.exists(filename)

def safely_import_module(module_name):
    """Safely import a module, returning None if import fails."""
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None

def check_function_exists(module, function_name):
    """Check if a function exists in a module."""
    return hasattr(module, function_name) and callable(getattr(module, function_name))

def safely_call_function(module, function_name, *args, **kwargs):
    """Safely call a function, returning the result or None if it fails."""
    if not check_function_exists(module, function_name):
        return None
    try:
        # Suppress stdout to prevent unwanted output
        with contextlib.redirect_stdout(io.StringIO()):
            return getattr(module, function_name)(*args, **kwargs)
    except Exception:
        return None

def check_raises(func, args, expected_exception=Exception):
    """Check if a function raises an expected exception."""
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            func(*args)
        return False
    except expected_exception:
        return True
    except Exception:
        return False

def load_module_dynamically():
    """Load the student's module for testing"""
    module_obj = safely_import_module("game_development_utility_system")
    if module_obj is None:
        module_obj = safely_import_module("solution")
    return module_obj

class TestAssignment(unittest.TestCase):
    def setUp(self):
        """Standard setup for all test methods"""
        self.test_obj = TestUtils()
        self.module_obj = load_module_dynamically()
    
    def test_error_handling(self):
        """Test error handling for lambda function operations"""
        try:
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                print("TestErrorHandling = Failed")
                return
            
            # Check required functions exist
            required_functions = [
                "prepare_player_data",
                "prepare_entity_data", 
                "prepare_inventory_data",
                "prepare_coordinate_data",
                "demonstrate_player_transformations",
                "demonstrate_entity_filtering",
                "demonstrate_item_sorting",
                "demonstrate_game_calculations"
            ]
            
            for func_name in required_functions:
                if not check_function_exists(self.module_obj, func_name):
                    self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                    print("TestErrorHandling = Failed")
                    return
            
            # Get valid test data first
            players = safely_call_function(self.module_obj, "prepare_player_data")
            if players is None:
                players = []
            
            entities = safely_call_function(self.module_obj, "prepare_entity_data")
            if entities is None:
                entities = []
            
            inventory = safely_call_function(self.module_obj, "prepare_inventory_data")
            if inventory is None:
                inventory = []
            
            coordinates = safely_call_function(self.module_obj, "prepare_coordinate_data")
            if coordinates is None:
                coordinates = []
            
            # Test handling of empty data
            empty_players = []
            empty_entities = []
            empty_inventory = []
            empty_coordinates = []
            
            # Test functions handle empty lists gracefully
            if check_function_exists(self.module_obj, "demonstrate_player_transformations"):
                result = safely_call_function(self.module_obj, "demonstrate_player_transformations", empty_players)
                if result is False:  # None is ok (void function), False indicates error
                    self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                    print("TestErrorHandling = Failed")
                    return
            
            if check_function_exists(self.module_obj, "demonstrate_entity_filtering"):
                result = safely_call_function(self.module_obj, "demonstrate_entity_filtering", empty_entities)
                if result is False:
                    self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                    print("TestErrorHandling = Failed")
                    return
            
            if check_function_exists(self.module_obj, "demonstrate_item_sorting"):
                result = safely_call_function(self.module_obj, "demonstrate_item_sorting", empty_inventory)
                if result is False:
                    self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                    print("TestErrorHandling = Failed")
                    return
            
            if check_function_exists(self.module_obj, "demonstrate_game_calculations"):
                result = safely_call_function(self.module_obj, "demonstrate_game_calculations", empty_coordinates, empty_players)
                if result is False:
                    self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                    print("TestErrorHandling = Failed")
                    return
            
            # Test with invalid data types
            if check_function_exists(self.module_obj, "demonstrate_player_transformations"):
                result = safely_call_function(self.module_obj, "demonstrate_player_transformations", "not a list")
                if result is None:  # Should either handle gracefully or raise TypeError
                    # Check if it raises appropriate exception
                    func = getattr(self.module_obj, "demonstrate_player_transformations")
                    if not check_raises(func, ("not a list",), (TypeError, AttributeError)):
                        self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                        print("TestErrorHandling = Failed")
                        return
            
            if check_function_exists(self.module_obj, "demonstrate_entity_filtering"):
                result = safely_call_function(self.module_obj, "demonstrate_entity_filtering", "not a list")
                if result is None:
                    func = getattr(self.module_obj, "demonstrate_entity_filtering")
                    if not check_raises(func, ("not a list",), (TypeError, AttributeError)):
                        self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                        print("TestErrorHandling = Failed")
                        return
            
            if check_function_exists(self.module_obj, "demonstrate_item_sorting"):
                result = safely_call_function(self.module_obj, "demonstrate_item_sorting", "not a list")
                if result is None:
                    func = getattr(self.module_obj, "demonstrate_item_sorting")
                    if not check_raises(func, ("not a list",), (TypeError, AttributeError)):
                        self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                        print("TestErrorHandling = Failed")
                        return
            
            # Test with incomplete data (missing required attributes)
            incomplete_players = [{"name": "Incomplete"}]  # Missing level, health, etc.
            incomplete_entities = [{"id": "E999"}]  # Missing type, position, etc.
            incomplete_inventory = [{"name": "Broken Item"}]  # Missing value, type, etc.
            
            if check_function_exists(self.module_obj, "demonstrate_player_transformations"):
                result = safely_call_function(self.module_obj, "demonstrate_player_transformations", incomplete_players)
                if result is False:
                    self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                    print("TestErrorHandling = Failed")
                    return
            
            if check_function_exists(self.module_obj, "demonstrate_entity_filtering"):
                result = safely_call_function(self.module_obj, "demonstrate_entity_filtering", incomplete_entities)
                if result is False:
                    self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                    print("TestErrorHandling = Failed")
                    return
            
            if check_function_exists(self.module_obj, "demonstrate_item_sorting"):
                result = safely_call_function(self.module_obj, "demonstrate_item_sorting", incomplete_inventory)
                if result is False:
                    self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                    print("TestErrorHandling = Failed")
                    return
            
            # Test entity filtering with invalid player position
            if check_function_exists(self.module_obj, "demonstrate_entity_filtering") and entities:
                result = safely_call_function(self.module_obj, "demonstrate_entity_filtering", entities, "not a tuple")
                if result is False:
                    self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                    print("TestErrorHandling = Failed")
                    return
            
            # Test game calculations with invalid coordinates
            if check_function_exists(self.module_obj, "demonstrate_game_calculations"):
                invalid_coords = ["not", "coordinates"]
                result = safely_call_function(self.module_obj, "demonstrate_game_calculations", invalid_coords, players)
                if result is False:
                    self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                    print("TestErrorHandling = Failed")
                    return
            
            # Test with mixed valid/invalid data
            mixed_players = [
                {"name": "Valid", "level": 5, "health": 100, "mana": 50, "score": 1000},
                {"name": "Invalid"},  # Missing fields
                "not a dict",
                {"name": "Another Valid", "level": 3, "health": 80, "mana": 40, "score": 800}
            ]
            
            if check_function_exists(self.module_obj, "demonstrate_player_transformations"):
                result = safely_call_function(self.module_obj, "demonstrate_player_transformations", mixed_players)
                if result is False:
                    self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                    print("TestErrorHandling = Failed")
                    return
            
            # All tests passed
            self.test_obj.yakshaAssert("TestErrorHandling", True, "exception")
            print("TestErrorHandling = Passed")
            
        except Exception as e:
            self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
            print("TestErrorHandling = Failed")

if __name__ == '__main__':
    unittest.main()