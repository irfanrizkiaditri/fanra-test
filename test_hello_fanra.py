#!/usr/bin/env python3
"""
Test for Hello Fanra application
"""
import subprocess
import sys
import json

def test_hello_fanra_simple():
    """Test that hello_fanra.py outputs 'Hello Fanra!' in simple mode"""
    result = subprocess.run([sys.executable, "hello_fanra.py"], capture_output=True, text=True)
    assert result.returncode == 0, f"Exit code {result.returncode}"
    assert result.stdout.strip() == "Hello Fanra!", f"Expected 'Hello Fanra!', got '{result.stdout.strip()}'"
    print("✅ Test passed: simple mode outputs 'Hello Fanra!'")

def test_hello_fanra_formal():
    """Test formal mode"""
    result = subprocess.run([sys.executable, "hello_fanra.py", "formal"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Greetings" in result.stdout
    print("✅ Test passed: formal mode works")

def test_hello_fanra_casual():
    """Test casual mode"""
    result = subprocess.run([sys.executable, "hello_fanra.py", "casual"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hey" in result.stdout
    print("✅ Test passed: casual mode works")

def test_hello_fanra_json():
    """Test JSON mode"""
    result = subprocess.run([sys.executable, "hello_fanra.py", "json"], capture_output=True, text=True)
    assert result.returncode == 0
    data = json.loads(result.stdout.strip())
    assert data["message"] == "Hello Fanra!"
    assert data["project"] == "fanra-test"
    print("✅ Test passed: JSON mode works")

def test_hello_fanra_ascii():
    """Test ASCII mode"""
    result = subprocess.run([sys.executable, "hello_fanra.py", "ascii"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello Fanra!" in result.stdout
    assert "Autonomous Coding" in result.stdout
    print("✅ Test passed: ASCII mode works")

def test_hello_fanra_custom_name():
    """Test custom name"""
    result = subprocess.run([sys.executable, "hello_fanra.py", "simple", "Irfan"], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello Irfan!"
    print("✅ Test passed: custom name works")

if __name__ == "__main__":
    test_hello_fanra_simple()
    test_hello_fanra_formal()
    test_hello_fanra_casual()
    test_hello_fanra_json()
    test_hello_fanra_ascii()
    test_hello_fanra_custom_name()
    print("\n🎉 All tests passed!")