import os
import json

class Election:

    def __init__(self, n_code, name, family, elec):
        self.n_code = n_code
        self.name = name
        self.family = family
        self.elec = elec

    def __str__(self):
        return f"{self.name} {self.family} (کدملی: {self.n_code}) → رأی به شماره {self.elec}"

    def to_dict(self):
        #
        return {
            'name': self.name,
            'family': self.family,
            'n_code': self.n_code,
            'vote': self.elec
        }

class Nm_election:
    #
    def __init__(self):
        self.candid = []  

    def insert(self):

        while True:

            print("\nAmin = 1 , Farpor = 2 , Hadad = 3")
            name = input("Enter your name : ").strip().lower()
            if name.lower() == "q":
                break

            else:
                family = input("Enter your family name: ").strip().lower()
                n_code = input("Enter your national code: ").strip()
            
            file_name = '/home/am/Documents/python/code.json'
        
            try:
                with open(file_name, 'r') as f_obj:
                    data = json.load(f_obj)
            except:
                print("Error: Invalid JSON format.")
                continue

               
            found = False
            for record in data:
                if (record["name"].lower() == name and 
                    record["family"].lower() == family and 
                    record["n_code"] == n_code):
                    print("Record found. OK, let's go.")
                    found = True
                    break

            if not found:
                print("No matching record found.")
                continue

            if self.submit(n_code):
                print("but,You have already voted.")
                continue
            
            elec = input("Enter your vote: ")   
            self.candid.append(Election(n_code, name, family, elec))


            file_submit = '/home/am/Documents/python/sub.json'
            try:
                with open(file_submit, 'w') as f_o:
                    json.dump(a.get_all_votes(), f_o, indent=4)
                print("Your vote was successfully registered.")
            except:
                print("Something went wrong while saving.")


    def submit(self, n_code):

        file_submit = '/home/am/Documents/python/sub.json'
        try:
            with open(file_submit, 'r') as f_o:
                votes = json.load(f_o)

            for vote in votes:
                if vote["n_code"] == n_code:
                    return True  # یعنی قبلاً رأی داده
        except:
            return False  # اگر فایل وجود نداشت یا خطا داشت، یعنی رأی نداده

        return False
    
    def get_all_votes(self):

        x = [person.to_dict() for person in self.candid]
        return x


class Numeration(Nm_election):
    #
    def __init__(self):
        super().__init__()

    def num(self):

        counts = {}
        for d in a.get_all_votes():
            v = d["vote"]
            if v in counts :
                counts[v] += 1
            else:
                counts[v] = 1

        print("\nguide : (Amin = 1 , Farpor = 2 , Hadad = 3)")
        print("Election result :")
        print(counts)

class All(Nm_election):
    #
    def __init__(self):
        super().__init__()

    def all(self):

        file_submit = '/home/am/Documents/python/sub.json'
        try:
            with open (file_submit, 'r') as f_o:
                vo = json.load(f_o)
                n = "Total number of voters: " + str(len(vo))
                print(n)

        except SyntaxError:
            print("something wrong")
            




a = Nm_election()
a.insert()

votes_list = a.get_all_votes()
for v in votes_list:
    print(v)

b = Numeration()
b.num()
c = All()
c.all()

