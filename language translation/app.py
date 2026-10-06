from deep_translator import GoogleTranslator

print("========================================")
print("        LANGUAGE TRANSLATOR")
print("========================================")

text = input("Enter text to translate: ")

print("\nAvailable languages:")
print("1. Hindi")
print("2. Telugu")
print("3. Tamil")
print("4. French")
print("5. Spanish")

choice = input("\nEnter your choice: ")

if choice == "1":
    language = "hi"
elif choice == "2":
    language = "te"
elif choice == "3":
    language = "ta"
elif choice == "4":
    language = "fr"
elif choice == "5":
    language = "es"
else:
    print("Invalid choice!")
    exit()

try:
    translated_text = GoogleTranslator(
        source="auto",
        target=language
    ).translate(text)

    print("\n----------------------------------------")
    print("Original Text:")
    print(text)

    print("\nTranslated Text:")
    print(translated_text)

    print("----------------------------------------")

except Exception as e:
    print("\nTranslation failed.")
    print("Please check your internet connection.")