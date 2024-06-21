import jinja2
import pdfkit
from datetime import datetime


today = datetime.today().strftime('%d %b, %Y')
S_mobile = input("Enter Student Mobile Number\n")
N_installment = input("Next Installment Date:\n")
S_number = input("Student Number:\n")
paidBy = input("Received from:\n")

Describe = input("Program Disciption:\n")
C_name = input("Enter College name of the Student:\n")
P_name = input("Enter Project Name:\n")
Che_name = input("Cheque/DD No.:\n")
Bank = input("Enter The Name of Your Bank:\n")
First_amt = int(input("Enter First Amount:\n"))
Second_amt = int(input("Enter Second Amount:\n"))
tt = First_amt + Second_amt
Amt_word = input("Enter Amount in words:\n")
Course_amt = int( input("Enter the total cost of the Course:\n"))
Paid_amt = int(input("Enter the amount Paid\n"))
Due_amt = Course_amt - Paid_amt


context = {"date":today,
           "sm_no":S_mobile,
           "Ninstall":N_installment,
           "n1":S_number, "s_name":paidBy,
           "D":Describe,
           "Cname":C_name,
           "CAname":First_amt,
           "PAname":Second_amt,
           "Pname":P_name,
           "n2":Che_name,
           "Awords":Amt_word,
           "TAtotal":tt,
           "CAmount":Course_amt,
           "paid":Paid_amt,
           "Due":Due_amt
           }


tloader = jinja2.FileSystemLoader('./')
tevn = jinja2.Environment(loader= tloader)

template = tevn.get_template("invoiceh.html")
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf = r"C:\Users\Jerreh Saidy\OneDrive\Desktop\Desk_All\Jerreh\file2\rapid typing\wkhtmltopdf.exe")
pdfkit.from_string(output_text, "gen.pdf", configuration=config)