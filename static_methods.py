class TemperatureConvertor:
    num=10
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius*9/5)+32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit-32)*5/9

temp_f=TemperatureConvertor.celsius_to_fahrenheit(25)
temp_c=TemperatureConvertor.fahrenheit_to_celsius(77)
print(f"25C is {temp_f}F")
print(f"77F is {temp_c}C")
    
