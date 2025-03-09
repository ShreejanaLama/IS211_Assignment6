import unittest
from conversions import (
    convertCelsiusToKelvin, convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius, convertFahrenheitToKelvin,
    convertKelvinToCelsius, convertKelvinToFahrenheit
)

class TestTemperatureConversions(unittest.TestCase):
    """Tests for temperature conversion functions."""

    # Celsius to Kelvin and Fahrenheit tests are already defined

    def test_convertFahrenheitToCelsius(self):
        """Test Fahrenheit to Celsius conversions."""
        self.assertAlmostEqual(convertFahrenheitToCelsius(32), 0)
        self.assertAlmostEqual(convertFahrenheitToCelsius(212), 100)
        self.assertAlmostEqual(convertFahrenheitToCelsius(-40), -40)
        self.assertAlmostEqual(convertFahrenheitToCelsius(77), 25)
        self.assertAlmostEqual(convertFahrenheitToCelsius(-58), -50)

    def test_convertFahrenheitToKelvin(self):
        """Test Fahrenheit to Kelvin conversions."""
        self.assertAlmostEqual(convertFahrenheitToKelvin(32), 273.15)
        self.assertAlmostEqual(convertFahrenheitToKelvin(212), 373.15)
        self.assertAlmostEqual(convertFahrenheitToKelvin(-40), 233.15)
        self.assertAlmostEqual(convertFahrenheitToKelvin(77), 298.15)
        self.assertAlmostEqual(convertFahrenheitToKelvin(-58), 223.15)

    def test_convertKelvinToCelsius(self):
        """Test Kelvin to Celsius conversions."""
        self.assertAlmostEqual(convertKelvinToCelsius(273.15), 0)
        self.assertAlmostEqual(convertKelvinToCelsius(373.15), 100)
        self.assertAlmostEqual(convertKelvinToCelsius(233.15), -40)
        self.assertAlmostEqual(convertKelvinToCelsius(298.15), 25)
        self.assertAlmostEqual(convertKelvinToCelsius(223.15), -50)

    def test_convertKelvinToFahrenheit(self):
        """Test Kelvin to Fahrenheit conversions."""
        self.assertAlmostEqual(convertKelvinToFahrenheit(273.15), 32)
        self.assertAlmostEqual(convertKelvinToFahrenheit(373.15), 212)
        self.assertAlmostEqual(convertKelvinToFahrenheit(233.15), -40)
        self.assertAlmostEqual(convertKelvinToFahrenheit(298.15), 77)
        self.assertAlmostEqual(convertKelvinToFahrenheit(223.15), -58)

if __name__ == '__main__':
    unittest.main()
