contacts={     
"Alice": "555-1234",
"Bob": "555-5678",
"Charlie": "555-9012"
}
contacts["Diana"] = "555-3456"
contacts["Bob"] = "555-7777"
existing_contact = contacts.get("Alice", "Contact not found")
missing_contact = contacts.get("Eve", "Contact not found")
print(" Contact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
print("\n Safe Lookups:")
print(f"Alice: {existing_contact}")
print(f"Eve: {missing_contact}")
