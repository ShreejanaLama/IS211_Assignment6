def convertFahrenheitToCelsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def convertFahrenheitToKelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5/9 + 273.15

def convertKelvinToCelsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def convertKelvinToFahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32
