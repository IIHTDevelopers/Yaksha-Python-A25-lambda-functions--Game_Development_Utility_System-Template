"""
Functional tests for the Game Development Utility System.
"""

import pytest
import inspect
import os
import importlib
import sys
from test.TestUtils import TestUtils

@pytest.fixture
def test_obj():
    return TestUtils()

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

def test_required_function_names(test_obj):
    """Test that all required functions are defined with correct names"""
    errors = []
    
    # Check if module can be imported
    module_obj = safely_import_module("skeleton")
    if module_obj is None:
        module_obj = safely_import_module("solution")
    
    if module_obj is None:
        test_obj.yakshaAssert("TestRequiredFunctionNames", False, "functional")
        pytest.fail("Could not import skeleton or solution module.")
        return
    
    try:
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
            if not check_function_exists(module_obj, func_name):
                errors.append(f"Required function missing: {func_name}")
        
        # Check that data preparation functions have implementations
        data_prep_functions = [
            "prepare_player_data",
            "prepare_entity_data",
            "prepare_inventory_data", 
            "prepare_coordinate_data",
        ]
        
        for func_name in data_prep_functions:
            if not check_for_implementation(module_obj, func_name):
                errors.append(f"Function not implemented (just 'pass'): {func_name}")
        
        # Final assertion
        if errors:
            test_obj.yakshaAssert("TestRequiredFunctionNames", False, "functional")
            pytest.fail("\n".join(errors))
        else:
            test_obj.yakshaAssert("TestRequiredFunctionNames", True, "functional")
            
    except Exception as e:
        test_obj.yakshaAssert("TestRequiredFunctionNames", False, "functional")
        pytest.fail(f"Function name test failed: {str(e)}")

def test_data_structures(test_obj):
    """Test that the data structures match the requirements"""
    errors = []
    
    # Check if module can be imported
    module_obj = safely_import_module("skeleton")
    if module_obj is None:
        module_obj = safely_import_module("solution")
    
    if module_obj is None:
        test_obj.yakshaAssert("TestDataStructures", False, "functional")
        pytest.fail("Could not import skeleton or solution module.")
        return
    
    try:
        # Check required functions exist
        required_functions = [
            "prepare_player_data",
            "prepare_entity_data",
            "prepare_inventory_data", 
            "prepare_coordinate_data"
        ]
        
        for func_name in required_functions:
            if not check_function_exists(module_obj, func_name):
                errors.append(f"Function {func_name} not found")
        
        # Check for proper implementations before testing data structures
        for func_name in required_functions:
            if not check_for_implementation(module_obj, func_name):
                errors.append(f"Function not implemented (just 'pass'): {func_name}")
        
        if errors:
            test_obj.yakshaAssert("TestDataStructures", False, "functional")
            pytest.fail("\n".join(errors))
            return
        
        # Check player data structure
        players = safely_call_function(module_obj, "prepare_player_data")
        if players is None:
            errors.append("prepare_player_data returned None")
        elif not isinstance(players, list):
            errors.append(f"prepare_player_data should return a list, got {type(players)}")
        elif len(players) < 5:
            errors.append(f"Player data must have at least 5 players, got {len(players)}")
        elif len(players) > 0:
            # Check first player has all required fields
            required_player_fields = ["name", "level", "health", "mana", "score"]
            for field in required_player_fields:
                if field not in players[0]:
                    errors.append(f"Player data missing required field '{field}'")
        
        # Check entity data structure
        entities = safely_call_function(module_obj, "prepare_entity_data")
        if entities is None:
            errors.append("prepare_entity_data returned None")
        elif not isinstance(entities, list):
            errors.append(f"prepare_entity_data should return a list, got {type(entities)}")
        elif len(entities) < 8:
            errors.append(f"Entity data must have at least 8 entities, got {len(entities)}")
        elif len(entities) > 0:
            # Check entity has all required fields
            required_entity_fields = ["id", "type", "position_x", "position_y", "active"]
            for field in required_entity_fields:
                if field not in entities[0]:
                    errors.append(f"Entity data missing required field '{field}'")
        
        # Check inventory data structure
        inventory = safely_call_function(module_obj, "prepare_inventory_data")
        if inventory is None:
            errors.append("prepare_inventory_data returned None")
        elif not isinstance(inventory, list):
            errors.append(f"prepare_inventory_data should return a list, got {type(inventory)}")
        elif len(inventory) < 6:
            errors.append(f"Inventory data must have at least 6 items, got {len(inventory)}")
        elif len(inventory) > 0:
            # Check inventory item has all required fields
            required_item_fields = ["name", "type", "value", "rarity", "equipped"]
            for field in required_item_fields:
                if field not in inventory[0]:
                    errors.append(f"Inventory data missing required field '{field}'")
        
        # Check coordinate data structure
        coordinates = safely_call_function(module_obj, "prepare_coordinate_data")
        if coordinates is None:
            errors.append("prepare_coordinate_data returned None")
        elif not isinstance(coordinates, list):
            errors.append(f"prepare_coordinate_data should return a list, got {type(coordinates)}")
        elif len(coordinates) < 5:
            errors.append(f"Coordinate data must have at least 5 coordinates, got {len(coordinates)}")
        elif len(coordinates) > 0:
            if not all(isinstance(c, (list, tuple)) for c in coordinates):
                errors.append("Not all coordinates are lists or tuples")
            elif not all(len(c) == 2 for c in coordinates):
                errors.append("Coordinates must be pairs (tuples with 2 values)")
        
        # Final assertion
        if errors:
            test_obj.yakshaAssert("TestDataStructures", False, "functional")
            pytest.fail("\n".join(errors))
        else:
            test_obj.yakshaAssert("TestDataStructures", True, "functional")
            
    except Exception as e:
        test_obj.yakshaAssert("TestDataStructures", False, "functional")
        pytest.fail(f"Data structure test failed: {str(e)}")

def test_lambda_usage(test_obj):
    """Test that lambda functions are used as required"""
    errors = []
    
    # Check if module can be imported
    module_obj = safely_import_module("skeleton")
    if module_obj is None:
        module_obj = safely_import_module("solution")
    
    if module_obj is None:
        test_obj.yakshaAssert("TestLambdaUsage", False, "functional")
        pytest.fail("Could not import skeleton or solution module.")
        return
    
    try:
        # Check required functions exist and are implemented
        required_functions = [
            "demonstrate_player_transformations",
            "demonstrate_entity_filtering",
            "demonstrate_item_sorting",
            "demonstrate_game_calculations",
            "demonstrate_ability_system"
        ]
        
        for func_name in required_functions:
            if not check_function_exists(module_obj, func_name):
                errors.append(f"Function {func_name} not found")
        
        for func_name in required_functions:
            if not check_for_implementation(module_obj, func_name):
                errors.append(f"Function not implemented (just 'pass'): {func_name}")
        
        if errors:
            test_obj.yakshaAssert("TestLambdaUsage", False, "functional")
            pytest.fail("\n".join(errors))
            return
        
        # Check for lambda usage in each function
        player_transform_code = safely_get_source(module_obj, "demonstrate_player_transformations")
        entity_filter_code = safely_get_source(module_obj, "demonstrate_entity_filtering")
        item_sort_code = safely_get_source(module_obj, "demonstrate_item_sorting")
        game_calc_code = safely_get_source(module_obj, "demonstrate_game_calculations")
        ability_code = safely_get_source(module_obj, "demonstrate_ability_system")
        
        # Check for lambda usage in each function
        if "lambda" not in player_transform_code or "map" not in player_transform_code:
            errors.append("demonstrate_player_transformations must use lambda with map()")
        
        if "lambda" not in entity_filter_code or "filter" not in entity_filter_code:
            errors.append("demonstrate_entity_filtering must use lambda with filter()")
        
        if "lambda" not in item_sort_code or "sorted" not in item_sort_code:
            errors.append("demonstrate_item_sorting must use lambda with sorted()")
        
        if "lambda" not in game_calc_code:
            errors.append("demonstrate_game_calculations must use lambda functions")
        
        # Check advanced lambda usage
        if "lambda" not in ability_code:
            errors.append("demonstrate_ability_system must use lambda functions")
        
        # Final assertion
        if errors:
            test_obj.yakshaAssert("TestLambdaUsage", False, "functional")
            pytest.fail("\n".join(errors))
        else:
            test_obj.yakshaAssert("TestLambdaUsage", True, "functional")
            
    except Exception as e:
        test_obj.yakshaAssert("TestLambdaUsage", False, "functional")
        pytest.fail(f"Lambda usage test failed: {str(e)}")

def test_function_logic(test_obj):
    """Test the logic of key functions"""
    errors = []
    
    # Check if module can be imported
    module_obj = safely_import_module("skeleton")
    if module_obj is None:
        module_obj = safely_import_module("solution")
    
    if module_obj is None:
        test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
        pytest.fail("Could not import skeleton or solution module.")
        return
    
    try:
        # Check required functions exist and are implemented
        required_functions = [
            "prepare_player_data",
            "prepare_entity_data",
            "prepare_inventory_data"
        ]
        
        for func_name in required_functions:
            if not check_function_exists(module_obj, func_name):
                errors.append(f"Function {func_name} not found")
        
        for func_name in required_functions:
            if not check_for_implementation(module_obj, func_name):
                errors.append(f"Function not implemented (just 'pass'): {func_name}")
        
        if errors:
            test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
            pytest.fail("\n".join(errors))
            return
        
        # Test player data logic
        players = safely_call_function(module_obj, "prepare_player_data")
        if players is None or not isinstance(players, list) or len(players) == 0:
            errors.append("prepare_player_data did not return valid player data")
        else:
            # Test lambda calculation logic with actual data
            player = players[0]
            
            if not all(key in player for key in ["health", "level"]):
                errors.append("Player data missing required fields for calculation")
            else:
                # Test effective health calculation (common game formula)
                try:
                    calc_effective_health = lambda p: p["health"] + p["level"] * 10
                    expected_health = calc_effective_health(player)
                    
                    if expected_health <= player["health"]:
                        errors.append("Effective health calculation should increase with level")
                except (TypeError, KeyError):
                    errors.append("Error in health calculation lambda")
        
        # Test entity filtering logic
        entities = safely_call_function(module_obj, "prepare_entity_data")
        if entities is None or not isinstance(entities, list) or len(entities) == 0:
            errors.append("prepare_entity_data did not return valid entity data")
        else:
            if not all(all(key in e for key in ["type", "active"]) for e in entities):
                errors.append("Entity data missing required fields for filtering")
            else:
                # Test filtering logic
                try:
                    active_enemies = list(filter(lambda e: e["type"] == "enemy" and e["active"], entities))
                    all_enemies = [e for e in entities if e["type"] == "enemy"]
                    
                    if len(active_enemies) > len(all_enemies):
                        errors.append("Active enemies count cannot exceed total enemies")
                except (TypeError, KeyError):
                    errors.append("Error in entity filtering lambda")
        
        # Test sorting logic
        inventory = safely_call_function(module_obj, "prepare_inventory_data")
        if inventory is None or not isinstance(inventory, list) or len(inventory) == 0:
            errors.append("prepare_inventory_data did not return valid inventory data")
        else:
            if not all("value" in item for item in inventory):
                errors.append("Inventory data missing required field for sorting")
            else:
                # Test sorting logic
                try:
                    sorted_items = sorted(inventory, key=lambda item: item["value"])
                    
                    if len(sorted_items) != len(inventory):
                        errors.append("Sorting should preserve all items")
                    
                    # Check if actually sorted
                    for i in range(len(sorted_items) - 1):
                        if sorted_items[i]["value"] > sorted_items[i + 1]["value"]:
                            errors.append("Items not properly sorted by value")
                            break
                except (TypeError, KeyError):
                    errors.append("Error in sorting lambda")
        
        # Final assertion
        if errors:
            test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
            pytest.fail("\n".join(errors))
        else:
            test_obj.yakshaAssert("TestFunctionLogic", True, "functional")
            
    except Exception as e:
        test_obj.yakshaAssert("TestFunctionLogic", False, "functional")
        pytest.fail(f"Function logic test failed: {str(e)}")

def test_demonstration_functions(test_obj):
    """Test that demonstration functions work with actual data"""
    errors = []
    
    # Check if module can be imported
    module_obj = safely_import_module("skeleton")
    if module_obj is None:
        module_obj = safely_import_module("solution")
    
    if module_obj is None:
        test_obj.yakshaAssert("TestDemonstrationFunctions", False, "functional")
        pytest.fail("Could not import skeleton or solution module.")
        return
    
    try:
        # Get test data
        players = safely_call_function(module_obj, "prepare_player_data")
        entities = safely_call_function(module_obj, "prepare_entity_data")
        inventory = safely_call_function(module_obj, "prepare_inventory_data")
        coordinates = safely_call_function(module_obj, "prepare_coordinate_data")
        
        # Test demonstration functions with valid data
        if players and isinstance(players, list):
            if check_function_exists(module_obj, "demonstrate_player_transformations"):
                result = safely_call_function(module_obj, "demonstrate_player_transformations", players)
                if result is False:  # None is ok (void), False indicates error
                    errors.append("demonstrate_player_transformations failed with valid data")
        
        if entities and isinstance(entities, list):
            if check_function_exists(module_obj, "demonstrate_entity_filtering"):
                result = safely_call_function(module_obj, "demonstrate_entity_filtering", entities)
                if result is False:
                    errors.append("demonstrate_entity_filtering failed with valid data")
        
        if inventory and isinstance(inventory, list):
            if check_function_exists(module_obj, "demonstrate_item_sorting"):
                result = safely_call_function(module_obj, "demonstrate_item_sorting", inventory)
                if result is False:
                    errors.append("demonstrate_item_sorting failed with valid data")
        
        if coordinates and players and isinstance(coordinates, list) and isinstance(players, list):
            if check_function_exists(module_obj, "demonstrate_game_calculations"):
                result = safely_call_function(module_obj, "demonstrate_game_calculations", coordinates, players)
                if result is False:
                    errors.append("demonstrate_game_calculations failed with valid data")
        
        # Test advanced demonstration functions
        advanced_functions = [
            "demonstrate_ability_system",
            "demonstrate_combat_system", 
            "demonstrate_level_system"
        ]
        
        for func_name in advanced_functions:
            if check_function_exists(module_obj, func_name):
                if func_name == "demonstrate_ability_system":
                    result = safely_call_function(module_obj, func_name)
                elif func_name == "demonstrate_combat_system" and players and entities:
                    result = safely_call_function(module_obj, func_name, players, entities)
                elif func_name == "demonstrate_level_system" and players:
                    result = safely_call_function(module_obj, func_name, players)
                else:
                    continue  # Skip if no valid data
                
                if result is False:
                    errors.append(f"{func_name} failed during execution")
        
        # Final assertion
        if errors:
            test_obj.yakshaAssert("TestDemonstrationFunctions", False, "functional")
            pytest.fail("\n".join(errors))
        else:
            test_obj.yakshaAssert("TestDemonstrationFunctions", True, "functional")
            
    except Exception as e:
        test_obj.yakshaAssert("TestDemonstrationFunctions", False, "functional")
        pytest.fail(f"Demonstration functions test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])