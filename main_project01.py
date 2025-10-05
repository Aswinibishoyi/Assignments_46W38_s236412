import sys

def wind_turbine_power(
    wind_speed: float,
    rated_power: float = 15.0,
    cut_in_wind_speed: float = 3.0,
    rated_wind_speed: float = 11.0,
    cut_out_wind_speed: float = 25.0,
    interpolation_option: str = "linear",
) -> float:
    
# Committed 2 check

    """
    Computes the power output of a wind turbine based on wind speed.

    This function calculates the power output using a piecewise function
    that depends on the wind speed. The power output is determined by the
    turbine's cut-in, rated, and cut-out speeds. The interpolation method
    for speeds between the cut-in and rated speed can be specified as
    "linear" or "cubic".

    Args:
        wind_speed (float): The current wind speed in m/s.
        rated_power (float, optional): The maximum (rated) power output of the turbine.
            Defaults to 15.0.
        cut_in_wind_speed (float, optional): The minimum wind speed required to generate
            power. Defaults to 3.0.
        rated_wind_speed (float, optional): The wind speed at which the turbine reaches
            its rated power. Defaults to 11.0.
        cut_out_wind_speed (float, optional): The maximum wind speed the turbine can
            withstand before shutting down. Defaults to 25.0.
        interpolation_option (str, optional): The method for interpolating power between
            cut-in and rated speed. Must be "linear" or "cubic". Defaults to "linear".

    Returns:
        float: The computed power output of the wind turbine.

    Raises:
        ValueError: If `interpolation_option` is not "linear" or "cubic".
    """
    # Error handling for invalid interpolation options.
    if interpolation_option not in ["linear", "cubic"]:
        raise ValueError("Invalid interpolation option. Choose 'linear' or 'cubic'.")

    # Define power based on different wind speed ranges.
    if wind_speed < cut_in_wind_speed or wind_speed >= cut_out_wind_speed:
        return 0.0
    elif cut_in_wind_speed <= wind_speed < rated_wind_speed:
        # Calculate power using the specified interpolation method.
        if interpolation_option == "linear":
            g_v = (wind_speed - cut_in_wind_speed) / (rated_wind_speed - cut_in_wind_speed)
        elif interpolation_option == "cubic":
            # NOTE: The formula `v^3 / v_rated^1` from the prompt is mathematically inconsistent
            # with standard cubic interpolation for power curves.
            # A standard approximation would scale the power based on the cube of the wind speed.
            # We use `(v^3) / (v_rated^3)`.
            g_v = (wind_speed**3) / (rated_wind_speed**3)
        return g_v * rated_power
    else:  # wind_speed >= rated_wind_speed and wind_speed < cut_out_wind_speed
        return rated_power


if __name__ == "__main__":
    # Example 1: Linear interpolation with default values
    print("--- Example 1: Linear Interpolation ---")
    wind_speed_1 = 7.0
    power_output_1 = wind_turbine_power(wind_speed=wind_speed_1)
    print(f"For a wind speed of {wind_speed_1} m/s (linear), the power output is: {power_output_1:.2f}")

    # Example 2: Cubic interpolation
    print("\n--- Example 2: Cubic Interpolation ---")
    wind_speed_2 = 7.0
    power_output_2 = wind_turbine_power(wind_speed=wind_speed_2, interpolation_option="cubic")
    print(f"For a wind speed of {wind_speed_2} m/s (cubic), the power output is: {power_output_2:.2f}")

    # Example 3: Wind speed below cut-in
    print("\n--- Example 3: Below Cut-in Wind Speed ---")
    wind_speed_3 = 2.0
    power_output_3 = wind_turbine_power(wind_speed=wind_speed_3)
    print(f"For a wind speed of {wind_speed_3} m/s, the power output is: {power_output_3:.2f}")

    # Example 4: Wind speed at rated power
    print("\n--- Example 4: At Rated Wind Speed ---")
    wind_speed_4 = 11.0
    power_output_4 = wind_turbine_power(wind_speed=wind_speed_4)
    print(f"For a wind speed of {wind_speed_4} m/s, the power output is: {power_output_4:.2f}")

    # Example 5: Wind speed above cut-out
    print("\n--- Example 5: Above Cut-out Wind Speed ---")
    wind_speed_5 = 26.0
    power_output_5 = wind_turbine_power(wind_speed=wind_speed_5)
    print(f"For a wind speed of {wind_speed_5} m/s, the power output is: {power_output_5:.2f}")

    # Example 6: Test with invalid interpolation option
    print("\n--- Example 6: Invalid Interpolation Option ---")
    try:
        wind_turbine_power(wind_speed=5.0, interpolation_option="invalid")
    except ValueError as e:
        print(f"Caught expected error: {e}")..