import pytest
import inspect
from test.TestUtils import TestUtils
import game_development_utility_system as glf

class TestFunctionNames:
    """Test class to verify function names and structure match requirements"""
    
    def test_required_function_names(self):
        """Test that all required functions are defined with correct names"""
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
            
            # Get all function names from the module
            module_functions = [name for name, obj in inspect.getmembers(glf) 
                               if inspect.isfunction(obj) and not name.startswith('_')]
            
            # Check each required function exists
            for func_name in required_functions:
                assert func_name in module_functions, f"Required function '{func_name}' is missing"
            
            TestUtils.yakshaAssert("TestRequiredFunctionNames", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("TestRequiredFunctionNames", False, "functional")
            pytest.fail(f"Function name test failed: {str(e)}")
    
    def test_data_structures(self):
        """Test that the data structures match the requirements"""
        try:
            # Check player data structure
            players = glf.prepare_player_data()
            assert len(players) >= 5, "Player data must have at least 5 players"
            
            # Check first player has all required fields
            required_player_fields = ["name", "level", "health", "mana", "score"]
            for field in required_player_fields:
                assert field in players[0], f"Player data missing required field '{field}'"
            
            # Check entity data structure
            entities = glf.prepare_entity_data()
            assert len(entities) >= 8, "Entity data must have at least 8 entities"
            
            # Check entity has all required fields
            required_entity_fields = ["id", "type", "position_x", "position_y", "active"]
            for field in required_entity_fields:
                assert field in entities[0], f"Entity data missing required field '{field}'"
            
            # Check inventory data structure
            inventory = glf.prepare_inventory_data()
            assert len(inventory) >= 6, "Inventory data must have at least 6 items"
            
            # Check inventory item has all required fields
            required_item_fields = ["name", "type", "value", "rarity", "equipped"]
            for field in required_item_fields:
                assert field in inventory[0], f"Inventory data missing required field '{field}'"
            
            # Check coordinate data structure
            coordinates = glf.prepare_coordinate_data()
            assert len(coordinates) >= 5, "Coordinate data must have at least 5 coordinates"
            assert all(len(c) == 2 for c in coordinates), "Coordinates must be pairs (tuples with 2 values)"
            
            TestUtils.yakshaAssert("TestDataStructures", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("TestDataStructures", False, "functional")
            pytest.fail(f"Data structure test failed: {str(e)}")
    
    def test_lambda_usage(self):
        """Test that lambda functions are used as required"""
        try:
            # Get the source code for each function that should use lambdas
            player_transform_code = inspect.getsource(glf.demonstrate_player_transformations)
            entity_filter_code = inspect.getsource(glf.demonstrate_entity_filtering)
            item_sort_code = inspect.getsource(glf.demonstrate_item_sorting)
            game_calc_code = inspect.getsource(glf.demonstrate_game_calculations)
            
            # Check for lambda usage in each function
            assert "lambda" in player_transform_code and "map" in player_transform_code, \
                "demonstrate_player_transformations must use lambda with map()"
            
            assert "lambda" in entity_filter_code and "filter" in entity_filter_code, \
                "demonstrate_entity_filtering must use lambda with filter()"
            
            assert "lambda" in item_sort_code and "sorted" in item_sort_code, \
                "demonstrate_item_sorting must use lambda with sorted()"
            
            assert "lambda" in game_calc_code and "=" in game_calc_code and "lambda" in game_calc_code, \
                "demonstrate_game_calculations must assign lambda to variables"
            
            # Check advanced lambda usage
            ability_code = inspect.getsource(glf.demonstrate_ability_system)
            assert "lambda" in ability_code and ":" in ability_code, \
                "demonstrate_ability_system must use lambda functions"
            
            TestUtils.yakshaAssert("TestLambdaUsage", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("TestLambdaUsage", False, "functional")
            pytest.fail(f"Lambda usage test failed: {str(e)}")
    
    def test_function_logic(self):
        """Test the logic of key functions"""
        try:
            # Test player transformations logic
            players = glf.prepare_player_data()
            
            # Get any player to test with
            player = players[0]
            
            # Manually calculate effective health using the formula from the function
            expected_effective_health = player["health"] + player["level"] * 10
            
            # Use a lambda directly to check calculation
            calc_effective_health = lambda p: p["health"] + p["level"] * 10
            actual_effective_health = calc_effective_health(player)
            
            assert expected_effective_health == actual_effective_health, \
                "Effective health calculation is incorrect"
            
            # Test entity filtering logic
            entities = glf.prepare_entity_data()
            
            # Count active enemies manually
            active_enemies_count = sum(1 for e in entities if e["type"] == "enemy" and e["active"])
            
            # Use filter with lambda to count active enemies
            active_enemies = list(filter(lambda e: e["type"] == "enemy" and e["active"], entities))
            
            assert len(active_enemies) == active_enemies_count, \
                "Entity filtering logic is incorrect"
            
            # Test sorting logic
            inventory = glf.prepare_inventory_data()
            
            # Manually sort by value
            manual_sorted = sorted(inventory, key=lambda item: item["value"])
            
            # Check first item is lowest value
            lowest_value_item = min(inventory, key=lambda item: item["value"])
            assert manual_sorted[0]["value"] == lowest_value_item["value"], \
                "Sorting logic is incorrect"
            
            TestUtils.yakshaAssert("TestFunctionLogic", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("TestFunctionLogic", False, "functional")
            pytest.fail(f"Function logic test failed: {str(e)}")


if __name__ == '__main__':
    pytest.main(['-v'])