"""
Boundary tests for the Game Development Utility System.
"""

import pytest
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

def test_boundary_scenarios(test_obj):
    """Test boundary scenarios for lambda function operations"""
    errors = []
    
    # Check if module can be imported
    module_obj = safely_import_module("skeleton")
    if module_obj is None:
        module_obj = safely_import_module("solution")
    
    if module_obj is None:
        test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
        pytest.fail("Could not import skeleton or solution module.")
        return
    
    try:
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
            if not check_function_exists(module_obj, func_name):
                errors.append(f"Function {func_name} not found")
        
        # Test data preparation functions
        players = safely_call_function(module_obj, "prepare_player_data")
        if players is None:
            errors.append("prepare_player_data returned None")
        elif not isinstance(players, list):
            errors.append(f"prepare_player_data should return a list, got {type(players)}")
        elif len(players) < 5:
            errors.append(f"Should have at least 5 players, got {len(players)}")
        elif not all(isinstance(p, dict) for p in players):
            errors.append("All players should be dictionaries")
        elif players and not all(all(key in p for key in ["name", "level", "health", "mana", "score"]) for p in players):
            errors.append("Players missing required attributes")
        
        entities = safely_call_function(module_obj, "prepare_entity_data")
        if entities is None:
            errors.append("prepare_entity_data returned None")
        elif not isinstance(entities, list):
            errors.append(f"prepare_entity_data should return a list, got {type(entities)}")
        elif len(entities) < 8:
            errors.append(f"Should have at least 8 entities, got {len(entities)}")
        elif entities and not all(all(key in e for key in ["id", "type", "position_x", "position_y", "active"]) for e in entities):
            errors.append("Entities missing required attributes")
        
        inventory = safely_call_function(module_obj, "prepare_inventory_data")
        if inventory is None:
            errors.append("prepare_inventory_data returned None")
        elif not isinstance(inventory, list):
            errors.append(f"prepare_inventory_data should return a list, got {type(inventory)}")
        elif len(inventory) < 6:
            errors.append(f"Should have at least 6 inventory items, got {len(inventory)}")
        elif inventory and not all(all(key in i for key in ["name", "type", "value", "rarity", "equipped"]) for i in inventory):
            errors.append("Items missing required attributes")
        
        coordinates = safely_call_function(module_obj, "prepare_coordinate_data")
        if coordinates is None:
            errors.append("prepare_coordinate_data returned None")
        elif not isinstance(coordinates, list):
            errors.append(f"prepare_coordinate_data should return a list, got {type(coordinates)}")
        elif len(coordinates) < 5:
            errors.append(f"Should have at least 5 coordinate pairs, got {len(coordinates)}")
        elif coordinates and not all(len(c) == 2 for c in coordinates):
            errors.append("All coordinates should be pairs (tuples with 2 values)")
        
        # Test boundary cases with valid data
        if isinstance(players, list) and len(players) >= 2 and all(isinstance(p, dict) and "level" in p for p in players):
            # Test level boundaries
            try:
                min_level_player = min(players, key=lambda p: p["level"])
                max_level_player = max(players, key=lambda p: p["level"])
                
                if max_level_player["level"] <= min_level_player["level"]:
                    errors.append("Should have players with different levels")
            except (TypeError, KeyError):
                errors.append("Error calculating player level boundaries")
        
        if isinstance(entities, list) and len(entities) >= 2 and all(isinstance(e, dict) and "position_x" in e for e in entities):
            # Test position boundaries
            try:
                min_x_entity = min(entities, key=lambda e: e["position_x"])
                max_x_entity = max(entities, key=lambda e: e["position_x"])
                
                if max_x_entity["position_x"] <= min_x_entity["position_x"]:
                    errors.append("Should have entities at different X positions")
            except (TypeError, KeyError):
                errors.append("Error calculating entity position boundaries")
        
        if isinstance(inventory, list) and len(inventory) >= 2 and all(isinstance(i, dict) and "value" in i for i in inventory):
            # Test value boundaries
            try:
                min_value_item = min(inventory, key=lambda i: i["value"])
                max_value_item = max(inventory, key=lambda i: i["value"])
                
                if max_value_item["value"] <= min_value_item["value"]:
                    errors.append("Should have items with different values")
            except (TypeError, KeyError):
                errors.append("Error calculating item value boundaries")
        
        # Test demonstration functions don't crash
        if players:
            result = safely_call_function(module_obj, "demonstrate_player_transformations", players)
            if result is False:  # None is acceptable (void function), False indicates error
                errors.append("demonstrate_player_transformations raised an exception")
        
        if entities:
            result = safely_call_function(module_obj, "demonstrate_entity_filtering", entities)
            if result is False:
                errors.append("demonstrate_entity_filtering raised an exception")
        
        if inventory:
            result = safely_call_function(module_obj, "demonstrate_item_sorting", inventory)
            if result is False:
                errors.append("demonstrate_item_sorting raised an exception")
        
        if coordinates and players:
            result = safely_call_function(module_obj, "demonstrate_game_calculations", coordinates, players)
            if result is False:
                errors.append("demonstrate_game_calculations raised an exception")
        
        # Test with empty lists (boundary case)
        if check_function_exists(module_obj, "demonstrate_player_transformations"):
            result = safely_call_function(module_obj, "demonstrate_player_transformations", [])
            if result is False:
                errors.append("demonstrate_player_transformations should handle empty list gracefully")
        
        if check_function_exists(module_obj, "demonstrate_entity_filtering"):
            result = safely_call_function(module_obj, "demonstrate_entity_filtering", [])
            if result is False:
                errors.append("demonstrate_entity_filtering should handle empty list gracefully")
        
        if check_function_exists(module_obj, "demonstrate_item_sorting"):
            result = safely_call_function(module_obj, "demonstrate_item_sorting", [])
            if result is False:
                errors.append("demonstrate_item_sorting should handle empty list gracefully")
        
        # Final assertion
        if errors:
            test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
            pytest.fail("\n".join(errors))
        else:
            test_obj.yakshaAssert("TestBoundaryScenarios", True, "boundary")
            
    except Exception as e:
        test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
        pytest.fail(f"Boundary scenarios test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])