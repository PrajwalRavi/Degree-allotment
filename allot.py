import csv
branch = {'1':7,'2':8,'3':13,'4':10,'7':22,'8':5,'A':13,'B':5}
cutoff = {'1':10,'2':10,'3':10,'4':10,'7':10,'8':10,'A':10,'B':10}

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""
    f=open(raw_file,"r+")
    reader=csv.reader(f)
    parsed_data = []
    g=0
    csv_data=[]
    for row in reader:
        if(g==0):
            fields=row
            g=5
        else:
            csv_data.append(row)
    
    for row in csv_data:
        # Figure out what dict() and zip() do. Read the documentation. Links are in the post.
        parsed_data.append(dict(zip(fields, row)))

    f.close()

    return parsed_data


def allot(new_data):
    """Function to allot branch based on preferences you get from the parsed_data"""
    for i in range(len(new_data)):
        prefcount='1'
        for j in range(len(new_data[i])):
            x=new_data[i][prefcount]
            b=x[1:]            
            if(branch[b]>0):
                branch[b]-=1
                new_data[i]['alloted']=x
                cutoff[b]=new_data[i]['CG Year 1']
                break
            else:
                prefcount=ord(prefcount)-48
                prefcount+=49
                prefcount=chr(prefcount)


def addnew(new_data):
    """Writes back alloted stuff into csv file"""
    fieldnames=["ID","CG Year 1","1","2","3","4","5","6","7","8","9","alloted"]
    f=open("result.csv","w")
    writer=csv.DictWriter(f,delimiter=',', fieldnames=fieldnames)
    writer.writeheader()
    for row in new_data:
        writer.writerow(row)

def main():
    new_data = parse("file.csv", ",")
    allot(new_data)
    print(cutoff)
    addnew(new_data)

if __name__ == "__main__":
    main()
