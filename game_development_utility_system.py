"""
Game Development Utility System (Lambda Functions Focus)

This module demonstrates the use of lambda functions for game development tasks
including player statistics, entity filtering, and game calculations.
"""

def prepare_player_data():
    """
    Prepare player data for processing with lambda functions.
    
    Returns:
        list: A list of player dictionaries for demonstration
    """
    return [
        {"name": "Wizard1", "level": 5, "health": 80, "mana": 100, "score": 2500},
        {"name": "Warrior2", "level": 8, "health": 120, "mana": 40, "score": 3200},
        {"name": "Archer3", "level": 6, "health": 90, "mana": 60, "score": 2800},
        {"name": "Healer4", "level": 4, "health": 70, "mana": 120, "score": 2100},
        {"name": "Tank5", "level": 7, "health": 150, "mana": 30, "score": 2700}
    ]

def prepare_entity_data():
    """
    Prepare game entity data for processing with lambda functions.
    
    Returns:
        list: A list of entity dictionaries for demonstration
    """
    return [
        {"id": "E001", "type": "enemy", "position_x": 100, "position_y": 200, "active": True},
        {"id": "E002", "type": "npc", "position_x": 150, "position_y": 250, "active": True},
        {"id": "E003", "type": "enemy", "position_x": 200, "position_y": 300, "active": False},
        {"id": "E004", "type": "item", "position_x": 120, "position_y": 220, "active": True},
        {"id": "E005", "type": "enemy", "position_x": 180, "position_y": 150, "active": True},
        {"id": "E006", "type": "npc", "position_x": 90, "position_y": 180, "active": False},
        {"id": "E007", "type": "item", "position_x": 210, "position_y": 270, "active": True},
        {"id": "E008", "type": "enemy", "position_x": 160, "position_y": 240, "active": True}
    ]

def prepare_inventory_data():
    """
    Prepare inventory data for processing with lambda functions.
    
    Returns:
        list: A list of item dictionaries for demonstration
    """
    return [
        {"name": "Magic Sword", "type": "weapon", "value": 500, "rarity": "rare", "equipped": False},
        {"name": "Health Potion", "type": "consumable", "value": 50, "rarity": "common", "equipped": False},
        {"name": "Dragon Shield", "type": "armor", "value": 800, "rarity": "epic", "equipped": True},
        {"name": "Mana Crystal", "type": "consumable", "value": 100, "rarity": "uncommon", "equipped": False},
        {"name": "Ancient Bow", "type": "weapon", "value": 600, "rarity": "rare", "equipped": True},
        {"name": "Mystic Robe", "type": "armor", "value": 400, "rarity": "uncommon", "equipped": False}
    ]

def prepare_coordinate_data():
    """
    Prepare coordinate data for processing with lambda functions.
    
    Returns:
        list: A list of coordinate tuples for demonstration
    """
    return [(10, 20), (50, 60), (30, 40), (70, 80), (90, 10)]

def demonstrate_player_transformations(players):
    """
    Demonstrate using lambda functions with map() to transform player data.
    
    Args:
        players (list): List of player dictionaries
    """
    print("\n===== PLAYER TRANSFORMATIONS WITH LAMBDA FUNCTIONS =====")
    
    # Calculate effective health (health + level*10)
    effective_health = list(map(lambda p: {"name": p["name"], "effective_health": p["health"] + p["level"]*10}, players))
    print("Player effective health:")
    for player in effective_health:
        print(f"  {player['name']}: {player['effective_health']}")
    
    # Calculate mana regeneration based on level
    mana_regen = list(map(lambda p: {"name": p["name"], "mana_regen": p["mana"] * 0.1 * p["level"]}, players))
    print("\nPlayer mana regeneration:")
    for player in mana_regen:
        print(f"  {player['name']}: {player['mana_regen']:.1f} per turn")
    
    # Calculate normalized score (based on level)
    normalized_scores = list(map(lambda p: {"name": p["name"], "normalized_score": p["score"] / p["level"]}, players))
    print("\nPlayer normalized scores:")
    for score in normalized_scores:
        print(f"  {score['name']}: {score['normalized_score']:.1f}")
    
    # Calculate power index (custom formula)
    power_index = list(map(lambda p: {"name": p["name"], "power_index": (p["health"] * 0.5 + p["mana"] * 0.3) * p["level"]}, players))
    print("\nPlayer power index:")
    for player in power_index:
        print(f"  {player['name']}: {player['power_index']:.1f}")

def demonstrate_entity_filtering(entities, player_position=(100, 100)):
    """
    Demonstrate using lambda functions with filter() to select game entities.
    
    Args:
        entities (list): List of entity dictionaries
        player_position (tuple): Player's x,y position for distance calculations
    """
    print("\n===== ENTITY FILTERING WITH LAMBDA FUNCTIONS =====")
    
    # Filter active enemies
    active_enemies = list(filter(lambda e: e["type"] == "enemy" and e["active"], entities))
    print(f"Active enemies: {len(active_enemies)}")
    for enemy in active_enemies:
        print(f"  {enemy['id']} at position ({enemy['position_x']}, {enemy['position_y']})")
    
    # Filter collectible items
    items = list(filter(lambda e: e["type"] == "item" and e["active"], entities))
    print(f"\nCollectible items: {len(items)}")
    for item in items:
        print(f"  {item['id']} at position ({item['position_x']}, {item['position_y']})")
    
    # Calculate distances from player and filter entities within range
    nearby_entities = list(filter(
        lambda e: ((e["position_x"] - player_position[0])**2 + 
                   (e["position_y"] - player_position[1])**2)**0.5 < 100 and 
                  e["active"],
        entities
    ))
    print(f"\nEntities within 100 units of player: {len(nearby_entities)}")
    for entity in nearby_entities:
        distance = ((entity["position_x"] - player_position[0])**2 + 
                    (entity["position_y"] - player_position[1])**2)**0.5
        print(f"  {entity['id']} ({entity['type']}) at distance {distance:.1f}")
    
    # Filter entities based on multiple criteria
    targets = list(filter(
        lambda e: e["type"] == "enemy" and 
                  e["active"] and 
                  e["position_x"] > 150 and 
                  e["position_y"] > 200,
        entities
    ))
    print(f"\nEnemy targets in northeast quadrant: {len(targets)}")
    for target in targets:
        print(f"  {target['id']} at position ({target['position_x']}, {target['position_y']})")

def demonstrate_item_sorting(inventory):
    """
    Demonstrate using lambda functions with sorted() to order items.
    
    Args:
        inventory (list): List of item dictionaries
    """
    print("\n===== INVENTORY SORTING WITH LAMBDA FUNCTIONS =====")
    
    # Sort by value (ascending)
    value_sorted = sorted(inventory, key=lambda item: item["value"])
    print("Items sorted by value (ascending):")
    for item in value_sorted:
        print(f"  {item['name']}: {item['value']} gold")
    
    # Sort by rarity (custom order)
    rarity_order = {"common": 0, "uncommon": 1, "rare": 2, "epic": 3, "legendary": 4}
    rarity_sorted = sorted(inventory, key=lambda item: rarity_order[item["rarity"]])
    print("\nItems sorted by rarity:")
    for item in rarity_sorted:
        print(f"  {item['name']}: {item['rarity']}")
    
    # Sort by type then value (descending)
    type_value_sorted = sorted(inventory, key=lambda item: (item["type"], -item["value"]))
    print("\nItems sorted by type then value (descending):")
    for item in type_value_sorted:
        print(f"  {item['name']}: {item['type']}, {item['value']} gold")
    
    # Filter equipped items and sort by value
    equipped_sorted = sorted(
        filter(lambda item: item["equipped"], inventory),
        key=lambda item: item["value"]
    )
    print("\nEquipped items sorted by value:")
    for item in equipped_sorted:
        print(f"  {item['name']}: {item['value']} gold")

def demonstrate_game_calculations(coordinates, player_data):
    """
    Demonstrate using lambda functions for game mechanic calculations.
    
    Args:
        coordinates (list): List of coordinate tuples
        player_data (list): List of player dictionaries
    """
    print("\n===== GAME CALCULATIONS WITH LAMBDA FUNCTIONS =====")
    
    # Calculate distances between consecutive points
    distances = list(map(
        lambda i: ((coordinates[i][0] - coordinates[i-1][0])**2 + 
                  (coordinates[i][1] - coordinates[i-1][1])**2)**0.5,
        range(1, len(coordinates))
    ))
    print("Distances between consecutive coordinates:")
    for i, distance in enumerate(distances):
        print(f"  From {coordinates[i]} to {coordinates[i+1]}: {distance:.2f} units")
    
    # Calculate total path length
    total_distance = sum(distances)
    print(f"\nTotal path length: {total_distance:.2f} units")
    
    # Create damage calculation lambda
    calculate_damage = lambda attacker, defender: max(0, 
        (attacker["level"] * 5 + attacker["mana"] * 0.2) - (defender["level"] * 2)
    )
    
    print("\nDamage calculations:")
    # Calculate damage between players
    for i in range(len(player_data)):
        for j in range(len(player_data)):
            if i != j:
                damage = calculate_damage(player_data[i], player_data[j])
                print(f"  {player_data[i]['name']} would deal {damage:.1f} damage to {player_data[j]['name']}")
    
    # Create movement speed lambda
    calculate_speed = lambda player: 5 + (player["level"] * 0.5) - (player["health"] * 0.01)
    
    print("\nMovement speeds:")
    for player in player_data:
        speed = calculate_speed(player)
        print(f"  {player['name']}: {speed:.1f} units per second")

def demonstrate_ability_system():
    """
    Demonstrate lambda functions for a game ability system.
    """
    print("\n===== ABILITY SYSTEM WITH LAMBDA FUNCTIONS =====")
    
    # Define abilities using lambda functions
    abilities = {
        "fireball": lambda level: {"damage": 20 + level * 5, "mana_cost": 10 + level * 2},
        "heal": lambda level: {"healing": 15 + level * 5, "mana_cost": 15 + level * 3},
        "shield": lambda level: {"defense": 10 + level * 3, "duration": 2 + level // 2},
        "lightning": lambda level: {"damage": 15 + level * 7, "mana_cost": 20 + level * 4}
    }
    
    # Show ability stats at different levels
    ability_levels = [1, 3, 5]
    for ability_name, ability_func in abilities.items():
        print(f"\n{ability_name.capitalize()} ability stats:")
        for level in ability_levels:
            stats = ability_func(level)
            stats_str = ", ".join([f"{k}: {v}" for k, v in stats.items()])
            print(f"  Level {level}: {stats_str}")
    
    # Create an ability usage system
    can_use_ability = lambda player, ability_name, ability_level: (
        player["mana"] >= abilities[ability_name](ability_level)["mana_cost"]
    )
    
    # Test ability usage
    test_player = {"name": "TestWizard", "level": 4, "health": 70, "mana": 50, "score": 0}
    print("\nAbility usage test for player with 50 mana:")
    for ability_name in abilities:
        level = 3
        usable = can_use_ability(test_player, ability_name, level)
        mana_cost = abilities[ability_name](level)["mana_cost"]
        print(f"  Can use {ability_name} (level {level}, cost {mana_cost}): {usable}")

def demonstrate_combat_system(players, entities):
    """
    Demonstrate lambda functions for a game combat system.
    
    Args:
        players (list): List of player dictionaries
        entities (list): List of entity dictionaries
    """
    print("\n===== COMBAT SYSTEM WITH LAMBDA FUNCTIONS =====")
    
    # Create a player position for simulating combat
    player = players[0]
    player_position = (100, 100)
    
    # Get enemies within attack range (using filter with lambda)
    attack_range = 150
    enemies_in_range = list(filter(
        lambda e: e["type"] == "enemy" and 
                 e["active"] and 
                 ((e["position_x"] - player_position[0])**2 + 
                 (e["position_y"] - player_position[1])**2)**0.5 <= attack_range,
        entities
    ))
    
    print(f"Enemies in attack range ({attack_range} units) of {player['name']}:")
    for enemy in enemies_in_range:
        distance = ((enemy["position_x"] - player_position[0])**2 + 
                   (enemy["position_y"] - player_position[1])**2)**0.5
        print(f"  {enemy['id']} at distance {distance:.1f}")
    
    # Define combat calculation lambdas
    calculate_hit_chance = lambda distance: max(0, min(100, 100 - distance * 0.5))
    calculate_damage = lambda player, distance: max(1, (player["level"] * 5 + player["mana"] * 0.2) * (1 - distance/attack_range))
    calculate_xp_reward = lambda enemy_distance: 50 - enemy_distance * 0.2
    
    # Simulate attacks on enemies in range
    print("\nSimulated combat results:")
    for enemy in enemies_in_range:
        distance = ((enemy["position_x"] - player_position[0])**2 + 
                   (enemy["position_y"] - player_position[1])**2)**0.5
        
        hit_chance = calculate_hit_chance(distance)
        damage = calculate_damage(player, distance)
        xp_reward = calculate_xp_reward(distance)
        
        print(f"  Attack on {enemy['id']}:")
        print(f"    Distance: {distance:.1f} units")
        print(f"    Hit chance: {hit_chance:.1f}%")
        print(f"    Potential damage: {damage:.1f}")
        print(f"    XP reward: {xp_reward:.1f}")

def demonstrate_level_system(players):
    """
    Demonstrate lambda functions for a game leveling system.
    
    Args:
        players (list): List of player dictionaries
    """
    print("\n===== LEVEL SYSTEM WITH LAMBDA FUNCTIONS =====")
    
    # Define level system lambdas
    calculate_xp_required = lambda level: 100 * (level ** 1.5)
    calculate_stats_at_level = lambda base_stats, level: {
        "health": base_stats["health"] + level * 10,
        "mana": base_stats["mana"] + level * 5
    }
    
    # Show XP requirements for different levels
    print("XP required for next level:")
    for level in range(1, 11):
        xp_required = calculate_xp_required(level)
        print(f"  Level {level} -> {level+1}: {xp_required:.0f} XP")
    
    # Show player stats progression
    print("\nStat progression for players:")
    for player in players:
        base_stats = {"health": player["health"] - player["level"] * 10, 
                     "mana": player["mana"] - player["level"] * 5}
        
        print(f"\n  {player['name']} (currently level {player['level']}):")
        print(f"    Current stats: Health={player['health']}, Mana={player['mana']}")
        
        # Show progression for next 3 levels
        for future_level in range(player["level"] + 1, player["level"] + 4):
            future_stats = calculate_stats_at_level(base_stats, future_level)
            print(f"    At level {future_level}: Health={future_stats['health']}, Mana={future_stats['mana']}")

def main():
    """
    Main function demonstrating lambda functions for game development.
    """
    print("===== GAME DEVELOPMENT UTILITY SYSTEM =====")
    
    # Prepare game data
    players = prepare_player_data()
    entities = prepare_entity_data()
    inventory = prepare_inventory_data()
    coordinates = prepare_coordinate_data()
    
    # Demonstrate various lambda function applications
    demonstrate_player_transformations(players)
    demonstrate_entity_filtering(entities)
    demonstrate_item_sorting(inventory)
    demonstrate_game_calculations(coordinates, players)
    demonstrate_ability_system()
    demonstrate_combat_system(players, entities)
    demonstrate_level_system(players)
    
    print("\n===== DEMONSTRATION COMPLETED =====")

if __name__ == "__main__":
    main()