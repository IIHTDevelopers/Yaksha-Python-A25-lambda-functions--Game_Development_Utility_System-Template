"""
Exception handling tests for the Game Development Utility System.
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

def check_raises(func, args, expected_exception=Exception):
    """Check if a function raises an expected exception."""
    try:
        func(*args)
        return False
    except expected_exception:
        return True
    except Exception:
        return False

def test_error_handling(test_obj):
    """Test error handling for lambda function operations"""
    errors = []
    
    # Check if module can be imported
    module_obj = safely_import_module("skeleton")
    if module_obj is None:
        module_obj = safely_import_module("solution")
    
    if module_obj is None:
        test_obj.yakshaAssert("TestErrorHandling", False, "exception")
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
        
        # Get valid test data first
        players = safely_call_function(module_obj, "prepare_player_data")
        if players is None:
            players = []
            errors.append("prepare_player_data returned None")
        
        entities = safely_call_function(module_obj, "prepare_entity_data")
        if entities is None:
            entities = []
            errors.append("prepare_entity_data returned None")
        
        inventory = safely_call_function(module_obj, "prepare_inventory_data")
        if inventory is None:
            inventory = []
            errors.append("prepare_inventory_data returned None")
        
        coordinates = safely_call_function(module_obj, "prepare_coordinate_data")
        if coordinates is None:
            coordinates = []
            errors.append("prepare_coordinate_data returned None")
        
        # Test handling of empty data
        empty_players = []
        empty_entities = []
        empty_inventory = []
        empty_coordinates = []
        
        # Test functions handle empty lists gracefully
        if check_function_exists(module_obj, "demonstrate_player_transformations"):
            result = safely_call_function(module_obj, "demonstrate_player_transformations", empty_players)
            if result is False:  # None is ok (void function), False indicates error
                errors.append("demonstrate_player_transformations did not handle empty list gracefully")
        
        if check_function_exists(module_obj, "demonstrate_entity_filtering"):
            result = safely_call_function(module_obj, "demonstrate_entity_filtering", empty_entities)
            if result is False:
                errors.append("demonstrate_entity_filtering did not handle empty list gracefully")
        
        if check_function_exists(module_obj, "demonstrate_item_sorting"):
            result = safely_call_function(module_obj, "demonstrate_item_sorting", empty_inventory)
            if result is False:
                errors.append("demonstrate_item_sorting did not handle empty list gracefully")
        
        if check_function_exists(module_obj, "demonstrate_game_calculations"):
            result = safely_call_function(module_obj, "demonstrate_game_calculations", empty_coordinates, empty_players)
            if result is False:
                errors.append("demonstrate_game_calculations did not handle empty lists gracefully")
        
        # Test with invalid data types
        if check_function_exists(module_obj, "demonstrate_player_transformations"):
            result = safely_call_function(module_obj, "demonstrate_player_transformations", "not a list")
            if result is None:  # Should either handle gracefully or raise TypeError
                # Check if it raises appropriate exception
                func = getattr(module_obj, "demonstrate_player_transformations")
                if not check_raises(func, ("not a list",), (TypeError, AttributeError)):
                    errors.append("demonstrate_player_transformations should handle or reject invalid input type")
        
        if check_function_exists(module_obj, "demonstrate_entity_filtering"):
            result = safely_call_function(module_obj, "demonstrate_entity_filtering", "not a list")
            if result is None:
                func = getattr(module_obj, "demonstrate_entity_filtering")
                if not check_raises(func, ("not a list",), (TypeError, AttributeError)):
                    errors.append("demonstrate_entity_filtering should handle or reject invalid input type")
        
        if check_function_exists(module_obj, "demonstrate_item_sorting"):
            result = safely_call_function(module_obj, "demonstrate_item_sorting", "not a list")
            if result is None:
                func = getattr(module_obj, "demonstrate_item_sorting")
                if not check_raises(func, ("not a list",), (TypeError, AttributeError)):
                    errors.append("demonstrate_item_sorting should handle or reject invalid input type")
        
        # Test with incomplete data (missing required attributes)
        incomplete_players = [{"name": "Incomplete"}]  # Missing level, health, etc.
        incomplete_entities = [{"id": "E999"}]  # Missing type, position, etc.
        incomplete_inventory = [{"name": "Broken Item"}]  # Missing value, type, etc.
        
        if check_function_exists(module_obj, "demonstrate_player_transformations"):
            result = safely_call_function(module_obj, "demonstrate_player_transformations", incomplete_players)
            if result is False:
                errors.append("demonstrate_player_transformations should handle incomplete data gracefully")
        
        if check_function_exists(module_obj, "demonstrate_entity_filtering"):
            result = safely_call_function(module_obj, "demonstrate_entity_filtering", incomplete_entities)
            if result is False:
                errors.append("demonstrate_entity_filtering should handle incomplete data gracefully")
        
        if check_function_exists(module_obj, "demonstrate_item_sorting"):
            result = safely_call_function(module_obj, "demonstrate_item_sorting", incomplete_inventory)
            if result is False:
                errors.append("demonstrate_item_sorting should handle incomplete data gracefully")
        
        # Test entity filtering with invalid player position
        if check_function_exists(module_obj, "demonstrate_entity_filtering") and entities:
            result = safely_call_function(module_obj, "demonstrate_entity_filtering", entities, "not a tuple")
            if result is False:
                errors.append("demonstrate_entity_filtering should handle invalid position gracefully")
        
        # Test game calculations with invalid coordinates
        if check_function_exists(module_obj, "demonstrate_game_calculations"):
            invalid_coords = ["not", "coordinates"]
            result = safely_call_function(module_obj, "demonstrate_game_calculations", invalid_coords, players)
            if result is False:
                errors.append("demonstrate_game_calculations should handle invalid coordinates gracefully")
        
        # Test with mixed valid/invalid data
        mixed_players = [
            {"name": "Valid", "level": 5, "health": 100, "mana": 50, "score": 1000},
            {"name": "Invalid"},  # Missing fields
            "not a dict",
            {"name": "Another Valid", "level": 3, "health": 80, "mana": 40, "score": 800}
        ]
        
        if check_function_exists(module_obj, "demonstrate_player_transformations"):
            result = safely_call_function(module_obj, "demonstrate_player_transformations", mixed_players)
            if result is False:
                errors.append("demonstrate_player_transformations should handle mixed valid/invalid data")
        
        # Final assertion
        if errors:
            test_obj.yakshaAssert("TestErrorHandling", False, "exception")
            pytest.fail("\n".join(errors))
        else:
            test_obj.yakshaAssert("TestErrorHandling", True, "exception")
            
    except Exception as e:
        test_obj.yakshaAssert("TestErrorHandling", False, "exception")
        pytest.fail(f"Error handling test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])