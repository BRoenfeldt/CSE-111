

def water_column_height(tower_height, tank_height):
    """
    Calculates the height of the water column in the tank.
    :param tower_height: height of the tower
    :param tank_height: height of the tank
    :return: height of the water column in the tank
    """
    water_column_height = tower_height + (3*tank_height)/4
    return water_column_height

def pressure_gain_from_water_height(height):
    """
    Calculates the pressure gain from the height of the water column.
    :param height: height of the water column
    :return: pressure gain
    """
    pressure = (998.2 * 9.80665 * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculates the pressure loss in the pipe.
    :param pipe_diameter: diameter of the pipe
    :param pipe_length: length of the pipe (meters)
    :param friction_factor: friction factor
    :param fluid_velocity: velocity of the fluid
    :return: pressure loss
    """
    pressure_loss = ((-friction_factor) * pipe_length * 998.2 * (fluid_velocity**2)) / (2000 * pipe_diameter)
    return pressure_loss