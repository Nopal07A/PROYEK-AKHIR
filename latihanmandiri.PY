from tabulate import tabulate
listorang = [
    ["mariska", "18"],
    ["febriyanti", "19"]
]
# for i in enumerate(listorang):
#     head=["No", "nama", "umur"]
#     print(tabulate(i, listorang, headers=head, tablefmt="fancy_grid"))

jumlah = len(listorang)
print("jumlah list orang adalah" , jumlah)