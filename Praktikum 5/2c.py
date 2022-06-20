# versi 1

dict1 = {"a":"Anggie", "b":"Eka", "c":"Berkuliah di UMG", "d":"Teknik Industry"}
print("Sebelum di hapus dalam dictionary:\n")
print(str(dict1))
dict1.clear()
print("\nSesudah di hapus dalam dictionary:")
print(str(dict1))

# versi 2 

dict1 = {"a":"Anggie", "b":"Eka", "c":"Berkuliah di UMG", "d":"Teknik Industry"}
print("Sebelum di hapus dalam dictionary:\n")
print(str(dict1))
pop_item = dict1.pop("a")
print("\nKata yang dihapus dari dictionary :")
print(str(pop_item))
print("\nSesudah di hapus dalam dictionary:")
print(str(dict1))

