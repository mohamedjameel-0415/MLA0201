def decision_tree(weather, temperature, humidity):

    # Root node: Weather
    if weather == "Sunny":

        # Next node: Humidity
        if humidity == "High":
            return "Don't Play"
        else:
            return "Play"

    elif weather == "Rainy":

        # Next node: Wind
        if temperature == "Cold":
            return "Don't Play"
        else:
            return "Play"

    else:  # Cloudy or others
        return "Play"


# Example inputs
print("Case 1:", decision_tree("Sunny", "Hot", "High"))
print("Case 2:", decision_tree("Rainy", "Cold", "Low"))
print("Case 3:", decision_tree("Cloudy", "Hot", "Normal"))