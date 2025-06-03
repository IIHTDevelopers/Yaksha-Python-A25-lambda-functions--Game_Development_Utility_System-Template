"""
Boundary tests for the Game Development Utility System.
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
    
    def test_boundary_scenarios(self):
        """Test boundary scenarios for lambda function operations"""
        try:
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
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
                    self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                    print("TestBoundaryScenarios = Failed")
                    return
            
            # Test data preparation functions
            players = safely_call_function(self.module_obj, "prepare_player_data")
            if players is None:
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            elif not isinstance(players, list):
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            elif len(players) < 5:
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            elif not all(isinstance(p, dict) for p in players):
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            elif players and not all(all(key in p for key in ["name", "level", "health", "mana", "score"]) for p in players):
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            
            entities = safely_call_function(self.module_obj, "prepare_entity_data")
            if entities is None:
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            elif not isinstance(entities, list):
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            elif len(entities) < 8:
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            elif entities and not all(all(key in e for key in ["id", "type", "position_x", "position_y", "active"]) for e in entities):
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            
            inventory = safely_call_function(self.module_obj, "prepare_inventory_data")
            if inventory is None:
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            elif not isinstance(inventory, list):
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            elif len(inventory) < 6:
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            elif inventory and not all(all(key in i for key in ["name", "type", "value", "rarity", "equipped"]) for i in inventory):
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            
            coordinates = safely_call_function(self.module_obj, "prepare_coordinate_data")
            if coordinates is None:
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            elif not isinstance(coordinates, list):
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            elif len(coordinates) < 5:
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            elif coordinates and not all(len(c) == 2 for c in coordinates):
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            
            # Test boundary cases with valid data
            if isinstance(players, list) and len(players) >= 2 and all(isinstance(p, dict) and "level" in p for p in players):
                # Test level boundaries
                try:
                    min_level_player = min(players, key=lambda p: p["level"])
                    max_level_player = max(players, key=lambda p: p["level"])
                    
                    if max_level_player["level"] <= min_level_player["level"]:
                        self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                        print("TestBoundaryScenarios = Failed")
                        return
                except (TypeError, KeyError):
                    self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                    print("TestBoundaryScenarios = Failed")
                    return
            
            if isinstance(entities, list) and len(entities) >= 2 and all(isinstance(e, dict) and "position_x" in e for e in entities):
                # Test position boundaries
                try:
                    min_x_entity = min(entities, key=lambda e: e["position_x"])
                    max_x_entity = max(entities, key=lambda e: e["position_x"])
                    
                    if max_x_entity["position_x"] <= min_x_entity["position_x"]:
                        self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                        print("TestBoundaryScenarios = Failed")
                        return
                except (TypeError, KeyError):
                    self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                    print("TestBoundaryScenarios = Failed")
                    return
            
            if isinstance(inventory, list) and len(inventory) >= 2 and all(isinstance(i, dict) and "value" in i for i in inventory):
                # Test value boundaries
                try:
                    min_value_item = min(inventory, key=lambda i: i["value"])
                    max_value_item = max(inventory, key=lambda i: i["value"])
                    
                    if max_value_item["value"] <= min_value_item["value"]:
                        self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                        print("TestBoundaryScenarios = Failed")
                        return
                except (TypeError, KeyError):
                    self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                    print("TestBoundaryScenarios = Failed")
                    return
            
            # Test demonstration functions don't crash
            if players:
                result = safely_call_function(self.module_obj, "demonstrate_player_transformations", players)
                if result is False:  # None is acceptable (void function), False indicates error
                    self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                    print("TestBoundaryScenarios = Failed")
                    return
            
            if entities:
                result = safely_call_function(self.module_obj, "demonstrate_entity_filtering", entities)
                if result is False:
                    self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                    print("TestBoundaryScenarios = Failed")
                    return
            
            if inventory:
                result = safely_call_function(self.module_obj, "demonstrate_item_sorting", inventory)
                if result is False:
                    self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                    print("TestBoundaryScenarios = Failed")
                    return
            
            if coordinates and players:
                result = safely_call_function(self.module_obj, "demonstrate_game_calculations", coordinates, players)
                if result is False:
                    self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                    print("TestBoundaryScenarios = Failed")
                    return
            
            # Test with empty lists (boundary case)
            if check_function_exists(self.module_obj, "demonstrate_player_transformations"):
                result = safely_call_function(self.module_obj, "demonstrate_player_transformations", [])
                if result is False:
                    self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                    print("TestBoundaryScenarios = Failed")
                    return
            
            if check_function_exists(self.module_obj, "demonstrate_entity_filtering"):
                result = safely_call_function(self.module_obj, "demonstrate_entity_filtering", [])
                if result is False:
                    self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                    print("TestBoundaryScenarios = Failed")
                    return
            
            if check_function_exists(self.module_obj, "demonstrate_item_sorting"):
                result = safely_call_function(self.module_obj, "demonstrate_item_sorting", [])
                if result is False:
                    self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                    print("TestBoundaryScenarios = Failed")
                    return
            
            # All tests passed
            self.test_obj.yakshaAssert("TestBoundaryScenarios", True, "boundary")
            print("TestBoundaryScenarios = Passed")
            
        except Exception as e:
            self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
            print("TestBoundaryScenarios = Failed")

if __name__ == '__main__':
    unittest.main()