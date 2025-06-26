#!/usr/bin/env python3
"""
Python Error Handling Best Practices - Simple Examples
Demonstrates common errors with proper try, except, else, finally blocks
"""

import json
import os


def file_errors_example():
    """Example 1: File Operation Errors"""
    print("\n1️⃣  FILE OPERATION ERRORS")
    print("-" * 40)
    
    file_handle = None
    try:
        # This will cause FileNotFoundError
        file_handle = open("nonexistent_file.txt", "r")
        content = file_handle.read()
        
    except FileNotFoundError as e:
        print(f"❌ FileNotFoundError: {e}")
        print("🔧 Creating the file instead...")
        # Recovery action
        with open("nonexistent_file.txt", "w") as f:
            f.write("File created due to error!")
            
    except PermissionError as e:
        print(f"❌ PermissionError: {e}")
        
    except OSError as e:
        print(f"❌ OSError: {e}")
        
    else:
        # This runs only if NO exception occurred
        print(f"✅ File read successfully: {content}")
        
    finally:
        # This ALWAYS runs - cleanup code
        if file_handle and not file_handle.closed:
            file_handle.close()
        print("🧹 Cleanup completed (finally block)")


def zero_division_example():
    """Example 2: ZeroDivisionError"""
    print("\n2️⃣  ZERO DIVISION ERROR")
    print("-" * 40)
    
    numbers = [10, 5, 0, 15, 20]
    results = []
    
    for i, num in enumerate(numbers):
        try:
            result = 100 / num
            
        except ZeroDivisionError:
            print(f"❌ ZeroDivisionError at index {i}: Cannot divide by {num}")
            result = float('inf')  # Assign infinity as fallback
            
        else:
            print(f"✅ 100 / {num} = {result}")
            
        finally:
            results.append(result)
            print(f"🔄 Processed item {i}: {num}")
    
    print(f"Final results: {results}")


def type_errors_example():
    """Example 3: Type and Value Errors"""
    print("\n3️⃣  TYPE AND VALUE ERRORS")
    print("-" * 40)
    
    test_values = ["123", "abc", "45.67", "", None, [1, 2, 3]]
    
    for value in test_values:
        try:
            print(f"\nTesting: {value} (type: {type(value).__name__})")
            # This can raise ValueError or TypeError
            number = int(value)
            
        except ValueError as e:
            print(f"❌ ValueError: {e}")
            print("Cannot convert to integer")
            number = 0  # Default value
            
        except TypeError as e:
            print(f"❌ TypeError: {e}")
            print("Invalid type for conversion")
            number = 0  # Default value
            
        else:
            print(f"✅ Successfully converted to: {number}")
            
        finally:
            print(f"🔄 Conversion attempt completed")


def json_errors_example():
    """Example 4: JSON Decode Errors"""
    print("\n4️⃣  JSON DECODE ERRORS")
    print("-" * 40)
    
    json_strings = [
        '{"name": "John", "age": 30}',  # Valid JSON
        '{"name": "John", "age": }',    # Invalid JSON
        '{"name": "John" "age": 30}',   # Missing comma
        'not json at all'               # Not JSON
    ]
    
    for i, json_str in enumerate(json_strings):
        try:
            print(f"\nTesting JSON #{i+1}: {json_str}")
            data = json.loads(json_str)
            
            # Try to access a key (potential KeyError)
            name = data["name"]
            
        except json.JSONDecodeError as e:
            print(f"❌ JSONDecodeError: {e}")
            print(f"   Error at position {e.pos}")
            data = {}  # Default empty dict
            
        except KeyError as e:
            print(f"❌ KeyError: Missing key {e}")
            print(f"   Available keys: {list(data.keys())}")
            
        else:
            print(f"✅ Valid JSON parsed successfully")
            print(f"   Name: {name}")
            
        finally:
            print(f"🔄 JSON processing completed")


def index_errors_example():
    """Example 5: Index and Key Errors"""
    print("\n5️⃣  INDEX AND KEY ERRORS")
    print("-" * 40)
    
    my_list = [1, 2, 3, 4, 5]
    my_dict = {"name": "Alice", "age": 25}
    
    # Test IndexError
    try:
        print(f"List: {my_list}")
        value = my_list[10]  # This will raise IndexError
        
    except IndexError as e:
        print(f"❌ IndexError: {e}")
        print(f"   List has {len(my_list)} items, valid indices: 0-{len(my_list)-1}")
        value = None
        
    else:
        print(f"✅ Value at index 10: {value}")
        
    finally:
        print("🔄 List access attempt completed")
    
    # Test KeyError
    try:
        print(f"\nDictionary: {my_dict}")
        country = my_dict["country"]  # This will raise KeyError
        
    except KeyError as e:
        print(f"❌ KeyError: {e}")
        print(f"   Available keys: {list(my_dict.keys())}")
        country = "Unknown"  # Default value
        
    else:
        print(f"✅ Country: {country}")
        
    finally:
        print("🔄 Dictionary access completed")


def custom_exception_example():
    """Example 6: Custom Exceptions with Exception Chaining"""
    print("\n6️⃣  CUSTOM EXCEPTIONS")
    print("-" * 40)
    
    class ValidationError(Exception):
        """Custom exception for validation errors"""
        def __init__(self, message, value=None):
            super().__init__(message)
            self.value = value
    
    def validate_email(email):
        try:
            if not isinstance(email, str):
                raise TypeError("Email must be a string")
            if "@" not in email:
                raise ValidationError("Email must contain @", email)
            if len(email) < 5:
                raise ValidationError("Email too short", email)
            return email.lower()
        except TypeError as e:
            # Exception chaining - preserve original error
            raise ValidationError(f"Invalid email type: {email}") from e
    
    test_emails = ["user@example.com", "invalid", "", 123, None]
    
    for email in test_emails:
        try:
            valid_email = validate_email(email)
            
        except ValidationError as e:
            print(f"❌ ValidationError: {e}")
            if hasattr(e, 'value'):
                print(f"   Invalid value: {e.value}")
            if e.__cause__:
                print(f"   Caused by: {e.__cause__}")
                
        else:
            print(f"✅ Valid email: {valid_email}")
            
        finally:
            print(f"🔄 Email validation completed for: {email}")


def nested_exceptions_example():
    """Example 7: Nested Try-Except Blocks"""
    print("\n7️⃣  NESTED EXCEPTION HANDLING")
    print("-" * 40)
    
    data = [
        {"numbers": [1, 2, 3], "operation": "divide"},
        {"numbers": [10, 0], "operation": "divide"},
        {"numbers": "invalid", "operation": "divide"},
        {"numbers": [5, 2], "operation": "unknown"}
    ]
    
    for i, item in enumerate(data):
        try:
            print(f"\nProcessing item {i}: {item}")
            numbers = item["numbers"]
            operation = item["operation"]
            
            # Nested try block for specific operations
            try:
                if operation == "divide":
                    result = numbers[0] / numbers[1]
                else:
                    raise ValueError(f"Unknown operation: {operation}")
                    
            except ZeroDivisionError:
                print(f"❌ Inner: Cannot divide {numbers[0]} by zero")
                result = float('inf')
                
            except TypeError as e:
                print(f"❌ Inner: Type error in calculation: {e}")
                result = None
                
            except IndexError as e:
                print(f"❌ Inner: Not enough numbers for operation: {e}")
                result = None
                
        except KeyError as e:
            print(f"❌ Outer: Missing key in data: {e}")
            result = None
            
        except TypeError as e:
            print(f"❌ Outer: Invalid data structure: {e}")
            result = None
            
        except Exception as e:
            print(f"❌ Outer: Unexpected error: {type(e).__name__}: {e}")
            result = None
            
        else:
            print(f"✅ Operation successful: {result}")
            
        finally:
            print(f"🔄 Processing completed for item {i}")


def main():
    """Run all error handling examples"""
    print("🐍 PYTHON ERROR HANDLING BEST PRACTICES")
    print("=" * 50)
    
    try:
        # Run all examples
        file_errors_example()
        zero_division_example()
        type_errors_example()
        json_errors_example()
        index_errors_example()
        custom_exception_example()
        nested_exceptions_example()
        
    except KeyboardInterrupt:
        print("\n❌ Program interrupted by user (Ctrl+C)")
        
    except Exception as e:
        print(f"\n❌ Unexpected error in main: {type(e).__name__}: {e}")
        
    else:
        print("\n✅ All examples completed successfully!")
        
    finally:
        print("\n🎯 Error handling demonstration finished")
        
        # Cleanup any created files
        try:
            os.remove("nonexistent_file.txt")
            print("🗑️  Cleaned up temporary files")
        except FileNotFoundError:
            pass
    
    print("\n" + "=" * 50)
    print("📚 BEST PRACTICES DEMONSTRATED:")
    print("✓ Specific exception types (avoid bare 'except:')")
    print("✓ Multiple except blocks for different error types")
    print("✓ 'else' block runs only when no exceptions occur")
    print("✓ 'finally' block always runs (cleanup code)")
    print("✓ Exception chaining with 'raise ... from ...'")
    print("✓ Custom exceptions with additional data")
    print("✓ Nested try-except for complex error handling")
    print("✓ Meaningful error messages with context")
    print("✓ Graceful error recovery and fallback values")
    print("✓ Resource cleanup in finally blocks")


if __name__ == "__main__":
    main() 