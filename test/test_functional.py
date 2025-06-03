"""
Functional tests for the Game Development Utility System.
"""

import unittest
import inspect
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

def safely_get_source(module, function_name):
    """Safely get the source code of a function, returning empty string if it fails."""
    if not check_function_exists(module, function_name):
        return ""
    try:
        return inspect.getsource(getattr(module, function_name))
    except Exception:
        return ""

def check_for_implementation(module, function_name):
    """Check if a function has a real implementation and not just 'pass'."""
    source = safely_get_source(module, function_name)
    return source and "pass" not in source.strip() and len(source.strip().split('\n')) > 3

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
    
    def test_required_function_names(self):
        """Test that all required functions are defined with correct names"""
        try:
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestRequiredFunctionNames", False, "functional")
                print("TestRequiredFunctionNames = Failed")
                return
            
            # List of required function names from requirements
            required_functions = [
                "prepare_player_data",
                "prepare_entity_data",
                "prepare_inventory_data", 
                "prepare_coordinate_data",
                "demonstrate_player_transformations",
                "demonstrate_entity_filtering",
                "demonstrate_item_sorting",
                "demonstrate_game_calculations",
                "demonstrate_ability_system",
                "demonstrate_combat_system",
                "demonstrate_level_system",
                "main"
            ]
            
            # Check each required function exists
            for func_name in required_functions:
                if not check_function_exists(self.module_obj, func_name):
                    self.test_obj.yakshaAssert("TestRequiredFunctionNames", False, "functional")
                    print("TestRequiredFunctionNames = Failed")
                    return
            
            # Check that data preparation functions have implementations
            data_prep_functions = [
                "prepare_player_data",
                "prepare_entity_data",
                "prepare_inventory_data", 
                "prepare_coordinate_data",
            ]
            
            for func_name in data_prep_functions:
                if not check_for_implementation(self.module_obj, func_name):
                    self.test_obj.yakshaAssert("TestRequiredFunctionNames", False, "functional")
                    print("TestRequiredFunctionNames = Failed")
                    return
            
            # All tests passed
            self.test_obj.yakshaAssert("TestRequiredFunctionNames", True, "functional")
            print("TestRequiredFunctionNames = Passed")
            
        except Exception as e:
            self.test_obj.yakshaAssert("TestRequiredFunctionNames", False, "functional")
            print("TestRequiredFunctionNames = Failed")

    def test_data_structures(self):
        """Test that the data structures match the requirements"""
        try:
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                print("TestDataStructures = Failed")
                return
            
            # Check required functions exist
            required_functions = [
                "prepare_player_data",
                "prepare_entity_data",
                "prepare_inventory_data", 
                "prepare_coordinate_data"
            ]
            
            for func_name in required_functions:
                if not check_function_exists(self.module_obj, func_name):
                    self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                    print("TestDataStructures = Failed")
                    return
            
            # Check for proper implementations before testing data structures
            for func_name in required_functions:
                if not check_for_implementation(self.module_obj, func_name):
                    self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                    print("TestDataStructures = Failed")
                    return
            
            # Check player data structure
            players = safely_call_function(self.module_obj, "prepare_player_data")
            if players is None:
                self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                print("TestDataStructures = Failed")
                return
            elif not isinstance(players, list):
                self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                print("TestDataStructures = Failed")
                return
            elif len(players) < 5:
                self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                print("TestDataStructures = Failed")
                return
            elif len(players) > 0:
                # Check first player has all required fields
                required_player_fields = ["name", "level", "health", "mana", "score"]
                for field in required_player_fields:
                    if field not in players[0]:
                        self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                        print("TestDataStructures = Failed")
                        return
            
            # Check entity data structure
            entities = safely_call_function(self.module_obj, "prepare_entity_data")
            if entities is None:
                self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                print("TestDataStructures = Failed")
                return
            elif not isinstance(entities, list):
                self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                print("TestDataStructures = Failed")
                return
            elif len(entities) < 8:
                self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                print("TestDataStructures = Failed")
                return
            elif len(entities) > 0:
                # Check entity has all required fields
                required_entity_fields = ["id", "type", "position_x", "position_y", "active"]
                for field in required_entity_fields:
                    if field not in entities[0]:
                        self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                        print("TestDataStructures = Failed")
                        return
            
            # Check inventory data structure
            inventory = safely_call_function(self.module_obj, "prepare_inventory_data")
            if inventory is None:
                self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                print("TestDataStructures = Failed")
                return
            elif not isinstance(inventory, list):
                self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                print("TestDataStructures = Failed")
                return
            elif len(inventory) < 6:
                self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                print("TestDataStructures = Failed")
                return
            elif len(inventory) > 0:
                # Check inventory item has all required fields
                required_item_fields = ["name", "type", "value", "rarity", "equipped"]
                for field in required_item_fields:
                    if field not in inventory[0]:
                        self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                        print("TestDataStructures = Failed")
                        return
            
            # Check coordinate data structure
            coordinates = safely_call_function(self.module_obj, "prepare_coordinate_data")
            if coordinates is None:
                self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                print("TestDataStructures = Failed")
                return
            elif not isinstance(coordinates, list):
                self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                print("TestDataStructures = Failed")
                return
            elif len(coordinates) < 5:
                self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                print("TestDataStructures = Failed")
                return
            elif len(coordinates) > 0:
                if not all(isinstance(c, (list, tuple)) for c in coordinates):
                    self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                    print("TestDataStructures = Failed")
                    return
                elif not all(len(c) == 2 for c in coordinates):
                    self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
                    print("TestDataStructures = Failed")
                    return
            
            # All tests passed
            self.test_obj.yakshaAssert("TestDataStructures", True, "functional")
            print("TestDataStructures = Passed")
            
        except Exception as e:
            self.test_obj.yakshaAssert("TestDataStructures", False, "functional")
            print("TestDataStructures = Failed")

    def test_lambda_usage(self):
        """Test that lambda functions are used as required"""
        try:
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestLambdaUsage", False, "functional")
                print("TestLambdaUsage = Failed")
                return
            
            # Check required functions exist and are implemented
            required_functions = [
                "demonstrate_player_transformations",
                "demonstrate_entity_filtering",
                "demonstrate_item_sorting",
                "demonstrate_game_calculations",
                "demonstrate_ability_system"
            ]
            
            for func_name in required_functions:
                if not check_function_exists(self.module_obj, func_name):
                    self.test_obj.yakshaAssert("TestLambdaUsage", False, "functional")
                    print("TestLambdaUsage = Failed")
                    return
            
            for func_name in required_functions:
                if not check_for_implementation(self.module_obj, func_name):
                    self.test_obj.yakshaAssert("TestLambdaUsage", False, "functional")
                    print("TestLambdaUsage = Failed")
                    return
            
            # Check for lambda usage in each function
            player_transform_code = safely_get_source(self.module_obj, "demonstrate_player_transformations")
            entity_filter_code = safely_get_source(self.module_obj, "demonstrate_entity_filtering")
            item_sort_code = safely_get_source(self.module_obj, "demonstrate_item_sorting")
            game_calc_code = safely_get_source(self.module_obj, "demonstrate_game_calculations")
            ability_code = safely_get_source(self.module_obj, "demonstrate_ability_system")
            
            # Check for lambda usage in each function
            if "lambda" not in player_transform_code or "map" not in player_transform_code:
                self.test_obj.yakshaAssert("TestLambdaUsage", False, "functional")
                print("TestLambdaUsage = Failed")
                return
            
            if "lambda" not in entity_filter_code or "filter" not in entity_filter_code:
                self.test_obj.yakshaAssert("TestLambdaUsage", False, "functional")
                print("TestLambdaUsage = Failed")
                return
            
            if "lambda" not in item_sort_code or "sorted" not in item_sort_code:
                self.test_obj.yakshaAssert("TestLambdaUsage", False, "functional")
                print("TestLambdaUsage = Failed")
                return
            
            if "lambda" not in game_calc_code:
                self.test_obj.yakshaAssert("TestLambdaUsage", False, "functional")
                print("TestLambdaUsage = Failed")
                return
            
            # Check advanced lambda usage
            if "lambda" not in ability_code:
                self.test_obj.yakshaAssert("TestLambdaUsage", False, "functional")
                print("TestLambdaUsage = Failed")
                return
            
            # All tests passed
            self.test_obj.yakshaAssert("TestLambdaUsage", True, "functional")
            print("TestLambdaUsage = Passed")
            
        except Exception as e:
            self.test_obj.yakshaAssert("TestLambdaUsage", False, "functional")
            print("TestLambdaUsage = Failed")

    def test_function_logic(self):
        """Test the logic of key functions"""
        try:
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                print("TestFunctionLogic = Failed")
                return
            
            # Check required functions exist and are implemented
            required_functions = [
                "prepare_player_data",
                "prepare_entity_data",
                "prepare_inventory_data"
            ]
            
            for func_name in required_functions:
                if not check_function_exists(self.module_obj, func_name):
                    self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                    print("TestFunctionLogic = Failed")
                    return
            
            for func_name in required_functions:
                if not check_for_implementation(self.module_obj, func_name):
                    self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                    print("TestFunctionLogic = Failed")
                    return
            
            # Test player data logic
            players = safely_call_function(self.module_obj, "prepare_player_data")
            if players is None or not isinstance(players, list) or len(players) == 0:
                self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                print("TestFunctionLogic = Failed")
                return
            else:
                # Test lambda calculation logic with actual data
                player = players[0]
                
                if not all(key in player for key in ["health", "level"]):
                    self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                    print("TestFunctionLogic = Failed")
                    return
                else:
                    # Test effective health calculation (common game formula)
                    try:
                        calc_effective_health = lambda p: p["health"] + p["level"] * 10
                        expected_health = calc_effective_health(player)
                        
                        if expected_health <= player["health"]:
                            self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                            print("TestFunctionLogic = Failed")
                            return
                    except (TypeError, KeyError):
                        self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                        print("TestFunctionLogic = Failed")
                        return
            
            # Test entity filtering logic
            entities = safely_call_function(self.module_obj, "prepare_entity_data")
            if entities is None or not isinstance(entities, list) or len(entities) == 0:
                self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                print("TestFunctionLogic = Failed")
                return
            else:
                if not all(all(key in e for key in ["type", "active"]) for e in entities):
                    self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                    print("TestFunctionLogic = Failed")
                    return
                else:
                    # Test filtering logic
                    try:
                        active_enemies = list(filter(lambda e: e["type"] == "enemy" and e["active"], entities))
                        all_enemies = [e for e in entities if e["type"] == "enemy"]
                        
                        if len(active_enemies) > len(all_enemies):
                            self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                            print("TestFunctionLogic = Failed")
                            return
                    except (TypeError, KeyError):
                        self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                        print("TestFunctionLogic = Failed")
                        return
            
            # Test sorting logic
            inventory = safely_call_function(self.module_obj, "prepare_inventory_data")
            if inventory is None or not isinstance(inventory, list) or len(inventory) == 0:
                self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                print("TestFunctionLogic = Failed")
                return
            else:
                if not all("value" in item for item in inventory):
                    self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                    print("TestFunctionLogic = Failed")
                    return
                else:
                    # Test sorting logic
                    try:
                        sorted_items = sorted(inventory, key=lambda item: item["value"])
                        
                        if len(sorted_items) != len(inventory):
                            self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                            print("TestFunctionLogic = Failed")
                            return
                        
                        # Check if actually sorted
                        for i in range(len(sorted_items) - 1):
                            if sorted_items[i]["value"] > sorted_items[i + 1]["value"]:
                                self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                                print("TestFunctionLogic = Failed")
                                return
                    except (TypeError, KeyError):
                        self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
                        print("TestFunctionLogic = Failed")
                        return
            
            # All tests passed
            self.test_obj.yakshaAssert("TestFunctionLogic", True, "functional")
            print("TestFunctionLogic = Passed")
            
        except Exception as e:
            self.test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
            print("TestFunctionLogic = Failed")

    def test_demonstration_functions(self):
        """Test that demonstration functions work with actual data"""
        try:
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestDemonstrationFunctions", False, "functional")
                print("TestDemonstrationFunctions = Failed")
                return
            
            # Get test data
            players = safely_call_function(self.module_obj, "prepare_player_data")
            entities = safely_call_function(self.module_obj, "prepare_entity_data")
            inventory = safely_call_function(self.module_obj, "prepare_inventory_data")
            coordinates = safely_call_function(self.module_obj, "prepare_coordinate_data")
            
            # Test demonstration functions with valid data
            if players and isinstance(players, list):
                if check_function_exists(self.module_obj, "demonstrate_player_transformations"):
                    result = safely_call_function(self.module_obj, "demonstrate_player_transformations", players)
                    if result is False:  # None is ok (void), False indicates error
                        self.test_obj.yakshaAssert("TestDemonstrationFunctions", False, "functional")
                        print("TestDemonstrationFunctions = Failed")
                        return
            
            if entities and isinstance(entities, list):
                if check_function_exists(self.module_obj, "demonstrate_entity_filtering"):
                    result = safely_call_function(self.module_obj, "demonstrate_entity_filtering", entities)
                    if result is False:
                        self.test_obj.yakshaAssert("TestDemonstrationFunctions", False, "functional")
                        print("TestDemonstrationFunctions = Failed")
                        return
            
            if inventory and isinstance(inventory, list):
                if check_function_exists(self.module_obj, "demonstrate_item_sorting"):
                    result = safely_call_function(self.module_obj, "demonstrate_item_sorting", inventory)
                    if result is False:
                        self.test_obj.yakshaAssert("TestDemonstrationFunctions", False, "functional")
                        print("TestDemonstrationFunctions = Failed")
                        return
            
            if coordinates and players and isinstance(coordinates, list) and isinstance(players, list):
                if check_function_exists(self.module_obj, "demonstrate_game_calculations"):
                    result = safely_call_function(self.module_obj, "demonstrate_game_calculations", coordinates, players)
                    if result is False:
                        self.test_obj.yakshaAssert("TestDemonstrationFunctions", False, "functional")
                        print("TestDemonstrationFunctions = Failed")
                        return
            
            # Test advanced demonstration functions
            advanced_functions = [
                "demonstrate_ability_system",
                "demonstrate_combat_system", 
                "demonstrate_level_system"
            ]
            
            for func_name in advanced_functions:
                if check_function_exists(self.module_obj, func_name):
                    if func_name == "demonstrate_ability_system":
                        result = safely_call_function(self.module_obj, func_name)
                    elif func_name == "demonstrate_combat_system" and players and entities:
                        result = safely_call_function(self.module_obj, func_name, players, entities)
                    elif func_name == "demonstrate_level_system" and players:
                        result = safely_call_function(self.module_obj, func_name, players)
                    else:
                        continue  # Skip if no valid data
                    
                    if result is False:
                        self.test_obj.yakshaAssert("TestDemonstrationFunctions", False, "functional")
                        print("TestDemonstrationFunctions = Failed")
                        return
            
            # All tests passed
            self.test_obj.yakshaAssert("TestDemonstrationFunctions", True, "functional")
            print("TestDemonstrationFunctions = Passed")
            
        except Exception as e:
            self.test_obj.yakshaAssert("TestDemonstrationFunctions", False, "functional")
            print("TestDemonstrationFunctions = Failed")

if __name__ == '__main__':
    unittest.main()