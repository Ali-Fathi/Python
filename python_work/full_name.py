first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(full_name)
print(message)

# format()
full_name = "{} {}".format(first_name, last_name)
print(full_name)