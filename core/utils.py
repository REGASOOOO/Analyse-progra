def grid_to_iso(x, y, tile_width, tile_height):
    """Convertit coordonnées grille → coordonnées écran"""
    screen_x = (x - y) * (tile_width // 2)
    screen_y = (x + y) * (tile_height // 2)
    return screen_x, screen_y