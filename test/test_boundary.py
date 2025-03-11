import pytest
from test.TestUtils import TestUtils
from game_development_utility_system import (
    prepare_player_data,
    prepare_entity_data,
    prepare_inventory_data,
    prepare_coordinate_data,
    demonstrate_player_transformations,
    demonstrate_entity_filtering,
    demonstrate_item_sorting,
    demonstrate_game_calculations
)

class TestBoundary:
    """Boundary tests for game lambda functions."""
    
    def test_boundary_scenarios(self):
        """Consolidated test for boundary scenarios across all functions"""
        try:
            # Test data preparation functions
            players = prepare_player_data()
            assert len(players) >= 5, "Should have at least 5 players"
            assert all(isinstance(p, dict) for p in players), "All players should be dictionaries"
            assert all(all(key in p for key in ["name", "level", "health", "mana", "score"]) for p in players), "Players missing required attributes"
            
            entities = prepare_entity_data()
            assert len(entities) >= 8, "Should have at least 8 entities"
            assert all(all(key in e for key in ["id", "type", "position_x", "position_y", "active"]) for e in entities), "Entities missing required attributes"
            
            inventory = prepare_inventory_data()
            assert len(inventory) >= 6, "Should have at least 6 inventory items"
            assert all(all(key in i for key in ["name", "type", "value", "rarity", "equipped"]) for i in inventory), "Items missing required attributes"
            
            coordinates = prepare_coordinate_data()
            assert len(coordinates) >= 5, "Should have at least 5 coordinate pairs"
            assert all(len(c) == 2 for c in coordinates), "All coordinates should be pairs (tuples with 2 values)"
            
            # Test lambda usage boundary cases
            
            # Find extreme level player (highest and lowest)
            min_level_player = min(players, key=lambda p: p["level"])
            max_level_player = max(players, key=lambda p: p["level"])
            assert max_level_player["level"] > min_level_player["level"], "Should have different player levels"
            
            # Test entities at boundary positions
            min_x_entity = min(entities, key=lambda e: e["position_x"])
            max_x_entity = max(entities, key=lambda e: e["position_x"])
            assert max_x_entity["position_x"] > min_x_entity["position_x"], "Should have entities at different X positions"
            
            # Test item value boundaries
            min_value_item = min(inventory, key=lambda i: i["value"])
            max_value_item = max(inventory, key=lambda i: i["value"])
            assert max_value_item["value"] > min_value_item["value"], "Should have items with different values"
            
            # Test extreme coordinate distances
            max_distance_coordinates = max([(i, j) for i in range(len(coordinates)) for j in range(i+1, len(coordinates))], 
                                        key=lambda pair: ((coordinates[pair[0]][0] - coordinates[pair[1]][0])**2 + 
                                                         (coordinates[pair[0]][1] - coordinates[pair[1]][1])**2)**0.5)
            i, j = max_distance_coordinates
            distance = ((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)**0.5
            assert distance > 0, "Should have coordinates with non-zero distance"
            
            # Test that demonstration functions don't raise exceptions
            demonstrate_player_transformations(players)
            demonstrate_entity_filtering(entities)
            demonstrate_item_sorting(inventory)
            demonstrate_game_calculations(coordinates, players)
            
            TestUtils.yakshaAssert("TestBoundaryScenarios", True, "boundary")
        except Exception as e:
            TestUtils.yakshaAssert("TestBoundaryScenarios", False, "boundary")
            pytest.fail(f"Boundary scenarios test failed: {str(e)}")


if __name__ == '__main__':
    pytest.main(['-v'])