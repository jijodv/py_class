
class nclass():
    def __init__(self, name, domain, company, batch):
        self.name = name
        self.domain = domain
        self.company = company
        self.batch = batch
    def aintro(self):
        print " - {} works in {} domain at {} and studied in {} batch" .format(self.name, self.domain, self.company, self.batch)

kanna = nclass("Kamalakannan Pandian" , "Big Data" , "Great Eastern" , "2nd")
balaji = nclass("Balaji Vellaichamy", "Unix & Cloud" , "Deutsche Bank" , "3rd")

for stu in kanna, balaji:
    stu.aintro()
