import json
import os
from typing import Optional, Dict, Any


def file_operations_example():
    """Demonstrates file operation errors with proper error handling"""
    file_handle = None
    
    try:
        # Potential FileNotFoundError, PermissionError
        file_handle = open("data.txt", "r")
        content = file_handle.read()
        
        # Potential UnicodeDecodeError
        processed_data = content.upper()
        
    except FileNotFoundError as e:
        print(f"❌ File not found: {e.filename}")
        print("Creating a new file with default content...")
        
        # Create file with default content
        with open("data.txt", "w") as f:
            f.write("Default content for demonstration")
            
    except PermissionError as e:
        print(f"❌ Permission denied: {e.filename}")
        print("Please check file permissions")
        
    except UnicodeDecodeError as e:
        print(f"❌ Encoding error: {e.reason}")
        print("Try opening with different encoding")
        
    except OSError as e:
        print(f"❌ OS Error: {e}")
        
    else:
        # Runs only if no exception occurred
        print("✅ File read successfully")
        print(f"Content length: {len(processed_data)} characters")
        return processed_data
        
    finally:
        # Always runs - cleanup code
        if file_handle and not file_handle.closed:
            file_handle.close()
            print("🔒 File handle closed")


def json_operations_example(data: Optional[str] = None):
    """Demonstrates JSON operation errors"""
    
    try:
        if data is None:
            # Reading from file
            with open("config.json", "r") as file:
                json_data = json.load(file)
        else:
            # Parsing string - potential JSONDecodeError
            json_data = json.loads(data)
            
        # Potential KeyError
        required_field = json_data["required_setting"]
        
        # Potential ValueError/TypeError
        numeric_value = int(json_data["numeric_field"])
        
    except FileNotFoundError:
        print("❌ Config file not found, creating default config...")
        json_data = {"required_setting": "default", "numeric_field": "42"}
        
        # Create default config file
        with open("config.json", "w") as f:
            json.dump(json_data, f, indent=2)
        
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON format: {e.msg} at line {e.lineno}, column {e.colno}")
        return None
        
    except KeyError as e:
        print(f"❌ Missing required field: {e}")
        print("Available fields:", list(json_data.keys()) if 'json_data' in locals() else "None")
        return None
        
    except ValueError as e:
        print(f"❌ Value conversion error: {e}")
        return None
        
    except TypeError as e:
        print(f"❌ Type error: {e}")
        return None
        
    else:
        print("✅ JSON processed successfully")
        print(f"Required setting: {required_field}")
        print(f"Numeric value: {numeric_value}")
        return json_data
        
    finally:
        print("🔍 JSON operation completed")


def mathematical_operations_example(numbers: list):
    """Demonstrates mathematical operation errors"""
    results = []
    
    try:
        for i, num in enumerate(numbers):
            print(f"Processing index {i}: {num}")
            
            # Potential ZeroDivisionError
            result = 100 / num
            
            # Potential IndexError
            try:
                next_num = numbers[i + 1]
                # Potential TypeError
                combined = result + next_num
                results.append(combined)
            except IndexError:
                print(f"⚠️  Last item reached at index {i}")
                results.append(result)
                break
                
    except ZeroDivisionError:
        print(f"❌ Division by zero at index {i} (value: {num})")
        print("Skipping zero values and continuing...")
        
    except TypeError as e:
        print(f"❌ Type error in calculation: {e}")
        print(f"Problem with value: {num} (type: {type(num)})")
        
    else:
        print("✅ All calculations completed successfully")
        
    finally:
        print(f"🧮 Processed {len(results)} calculations")
        print(f"Results: {results}")
        return results


def list_operations_example():
    """Demonstrates list and dictionary operation errors"""
    my_list = [1, 2, 3, 4, 5]
    my_dict = {"name": "John", "age": 30, "city": "New York"}
    
    try:
        # Potential IndexError
        print(f"Accessing index 10: {my_list[10]}")
        
    except IndexError as e:
        print(f"❌ List index error: {e}")
        print(f"List length is {len(my_list)}, valid indices: 0-{len(my_list)-1}")
        
    try:
        # Potential KeyError
        country = my_dict["country"]
        
    except KeyError as e:
        print(f"❌ Dictionary key error: {e}")
        print(f"Available keys: {list(my_dict.keys())}")
        # Provide default value
        country = "Unknown"
        
    else:
        print(f"✅ Country found: {country}")
        
    finally:
        print("🗂️  List/Dictionary operations completed")


def type_conversion_example():
    """Demonstrates type conversion errors"""
    test_values = ["123", "abc", "45.67", "", None, True, [1, 2, 3]]
    
    for value in test_values:
        try:
            print(f"\nTrying to convert: {value} (type: {type(value).__name__})")
            
            # Potential ValueError, TypeError
            as_int = int(value)
            as_float = float(value)
            
        except ValueError as e:
            print(f"❌ Value conversion error: {e}")
            print("Cannot convert to number")
            
        except TypeError as e:
            print(f"❌ Type error: {e}")
            print("Invalid type for conversion")
            
        else:
            print(f"✅ Converted successfully - Int: {as_int}, Float: {as_float}")
            
        finally:
            print(f"Conversion attempt completed for: {value}")


def custom_exception_example():
    """Demonstrates custom exceptions and exception chaining"""
    
    class CustomValidationError(Exception):
        """Custom exception for validation errors"""
        def __init__(self, message, value=None):
            super().__init__(message)
            self.value = value
    
    def validate_age(age):
        try:
            age_int = int(age)
            if age_int < 0:
                raise CustomValidationError(f"Age cannot be negative: {age_int}", age_int)
            elif age_int > 150:
                raise CustomValidationError(f"Age seems unrealistic: {age_int}", age_int)
            return age_int
        except ValueError as e:
            # Exception chaining - preserve original error
            raise CustomValidationError(f"Invalid age format: {age}") from e
    
    test_ages = ["25", "-5", "200", "abc", "30.5"]
    
    for age in test_ages:
        try:
            valid_age = validate_age(age)
            
        except CustomValidationError as e:
            print(f"❌ Validation error: {e}")
            if hasattr(e, 'value') and e.value is not None:
                print(f"   Invalid value was: {e.value}")
            if e.__cause__:
                print(f"   Original error: {e.__cause__}")
                
        else:
            print(f"✅ Valid age: {valid_age}")
            
        finally:
            print(f"Age validation completed for: {age}")


def comprehensive_error_handling_example():
    """Demonstrates multiple error handling patterns together"""
    
    try:
        print("1. Testing file operations...")
        file_operations_example()
        
        print("\n2. Testing JSON operations...")
        # Test with valid JSON
        json_operations_example('{"required_setting": "production", "numeric_field": "42"}')
        
        # Test with invalid JSON
        print("\n   Testing invalid JSON...")
        json_operations_example('{"invalid": json}')
        
        print("\n3. Testing mathematical operations...")
        mathematical_operations_example([10, 5, 0, 2, "invalid", 3])
        
        print("\n4. Testing list/dict operations...")
        list_operations_example()
        
        print("\n5. Testing type conversions...")
        type_conversion_example()
        
        print("\n6. Testing custom exceptions...")
        custom_exception_example()
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user (Ctrl+C)")
        
    except Exception as e:
        print(f"\n❌ Unexpected error in main execution: {type(e).__name__}: {e}")
        
    else:
        print("\n✅ All examples completed successfully")
        
    finally:
        print("\n🎯 Error handling demonstration finished")


def resource_management_example():
    """Demonstrates proper resource management with context managers"""
    
    # Example 1: File handling with context manager
    try:
        with open("temp_file.txt", "w") as f:
            f.write("Temporary content")
            # File automatically closed even if exception occurs
            
        with open("temp_file.txt", "r") as f:
            content = f.read()
            
    except IOError as e:
        print(f"❌ File operation failed: {e}")
        
    else:
        print(f"✅ File content: {content}")
        
    finally:
        # Cleanup
        try:
            os.remove("temp_file.txt")
            print("🗑️  Temporary file cleaned up")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    print("🐍 Python Error Handling Best Practices Demo")
    print("=" * 50)
    
    comprehensive_error_handling_example()
    
    print("\n" + "=" * 50)
    print("🧹 Testing resource management...")
    resource_management_example()
    
    print("\n" + "=" * 50)
    print("📚 Key Best Practices Demonstrated:")
    print("✓ Specific exception types (not bare except)")
    print("✓ Multiple exception handling with different except blocks")
    print("✓ Proper use of else block (runs only when no exception)")
    print("✓ Proper use of finally block (cleanup code that always runs)")
    print("✓ Meaningful error messages with context")
    print("✓ Exception chaining (raise ... from ...)")
    print("✓ Custom exceptions with additional data")
    print("✓ Resource management with context managers")
    print("✓ Graceful error recovery and fallback behavior")
    print("✓ Nested try-except blocks when appropriate")
