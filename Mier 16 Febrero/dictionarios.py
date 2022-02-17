#  key- value

phone_book = {
    "Batman": 45454,
    "Cersei": 4343,
    1:98
}
print(phone_book)
empty_dict = {}
print(empty_dict)

print(phone_book[1])

empty_dict = dict()
print(empty_dict)

phone_book = dict(Batman=5454, Cersei=86767)
print(phone_book)

phone_book["Godzilla"] =6445
print(phone_book)
phone_book["Godzilla"] =4343
print(phone_book)
del phone_book["Godzilla"]
print(phone_book)
cersei = phone_book.pop("Cersei")
print(cersei)
print(phone_book)
phone_book["Godzilla"] =4343

print(len(phone_book))
print("Batman" in phone_book)

phone_book = {"batman": 2343}
phone_book.update(
    {"email": "aaa@.co"}
)
print(phone_book)