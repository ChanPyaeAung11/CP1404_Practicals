"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Lindsay Ward'

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    final_km = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculate(self, text):
        """ handle calculation (could be button press or other call), output result to label widget """
        print("handle calc")
        miles = self.convert_to_num(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """
        handle up/down button press, update the text input with new value, call calculation function
        """
        print("handle inc")
        miles = self.convert_to_num(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        output_km = str(miles * MILES_TO_KM)
        self.root.ids.output_label.text = str(output_km)

    @staticmethod
    def convert_to_num(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            value = float(text)
            return value
        except ValueError:
            return 0.0


MilesConverterApp().run()
