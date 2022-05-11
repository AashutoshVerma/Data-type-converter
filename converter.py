from tkinter import ttk
from tkinter import*

root=Tk()
root.title("Conversions")
root.geometry("300x400")
root.configure(bg="Turquoise2")
out=""
num_type='a'
def all_answer(list):
    print("Binary=",list)
    
    label_2=Label(root,text="Binary:").grid(row=8,column=0)
    text_2=Entry(root,bg="light blue")
    text_2.grid(row=9,column=0)
    text_2.insert(0,list)



    # binary to decimal
    binary=list
    ans=0
    k=0
    for i in reversed(range(len(binary))):
        binary[i]=int(binary[i])
        ans=ans+(binary[i]*pow(2,k))
        k=k+1
    print("Decimal=",ans)
    label_1=Label(root,text="Decimal:").grid(row=5,column=0)
    text_1=Entry(root,bg="light blue")
    text_1.grid(row=7,column=0)
    text_1.insert(0,ans)
    #binary to octal
    binary=list
    binary.reverse()
    octal=[]
    k=0
    ans=0
    for i in range(len(binary)):
        if((i+1)%3==0):
            ans=ans+(binary[i]*pow(2,k))
            octal.append(ans)
            k=0
            ans=0
        else:
            if(i==len(binary)-1):
                ans=ans+(binary[i]*pow(2,k))
                octal.append(ans)
            else:
                ans=ans+(binary[i]*pow(2,k))
                k+=1
    octal.reverse()
    print("Octal=",octal)
    label_3=Label(root,text="Octadecimal:").grid(row=11,column=0)
    text_3=Entry(root,bg="light blue")
    text_3.grid(row=13,column=0)
    text_3.insert(0,octal)

    # Binary to Hexadecimal
    
    binary=list
    hexadecimal=[]
    k=0
    ans=0
    for i in range(len(binary)):
        if((i+1)%4==0):
            ans=ans+(binary[i]*pow(2,k))
            hexadecimal.append(ans)
            k=0
            ans=0
        else:
            if(i==len(binary)-1):
                ans=ans+(binary[i]*pow(2,k))
                hexadecimal.append(ans)
            else:
                ans=ans+(binary[i]*pow(2,k))
                k+=1
    hexadecimal.reverse()
    for i in range(len(hexadecimal)):
        if(hexadecimal[i]==10):
            hexadecimal[i]='A'
        elif(hexadecimal[i]==11):
            hexadecimal[i]='B'
        elif(hexadecimal[i]==12):
            hexadecimal[i]='C'
        elif(hexadecimal[i]==13):
            hexadecimal[i]='D'
        elif(hexadecimal[i]==14):
            hexadecimal[i]='E'
        elif(hexadecimal[i]==15):
            hexadecimal[i]='F'
    label_4=Label(root,text="Hexadecimal:").grid(row=14,column=0)
    text_4=Entry(root,bg="light blue")
    text_4.grid(row=15,column=0)
    text_4.insert(0,hexadecimal)

def comboclick(event):
    input.delete(0,"end")
    global out
    out=My_combo.get()

   
    def prin():
        print(decimal_ans.get(1.0,"end-1c"))
        num_type=decimal_ans.get(1.0,"end-1c")
    
        

        if(out=="Decimal"):
            # first decimal to binary
            # and then from binary to all the number type
            input_from_decimal=int(num_type)
            binary=[]
            for i in range(input_from_decimal):
                if(input_from_decimal!=1):
                    b=input_from_decimal%2
                    binary.append(b)
                    input_from_decimal=input_from_decimal//2
                elif(input_from_decimal==1):
                    input_from_decimal=1
                    b=1
                    binary.append(b)
                    break
            binary.reverse()
             #here we got the binary and now we need to convert it to the different number type
            all_answer(binary)

        elif(out=="Binary"):
            a=0
            # from binary to all the number type
            binary=list(num_type)
            all_answer(binary)




        elif(out=="Octadecimal"):
            # first octal to binary
            # and then from binary to all the number type
            input_from_octal=list(num_type)
            ans=[]
            binary=[]
            for i in input_from_octal:
                if(i=='0'):
                    ans=ans+[0,0,0]
                elif(i=='1'):
                    ans=ans+[0,0,1]
                elif(i=='2'):
                    ans=ans+[0,1,0]
                elif(i=='3'):
                    ans=ans+[0,1,1]
                elif(i=='4'):
                    ans=ans+[1,0,0]
                elif(i=='5'):
                    ans=ans+[1,0,1]
                elif(i=='6'):
                 ans=ans+[1,1,0]
                elif(i=='7'):
                    ans=ans+[1,1,1]
            binary=ans   #here we got the binary and now we need to convert it to the different number type



        elif(out=="Hexadecimal"):
            # first hexadecimal to binary
            # and then from binary to all the number type


            input_from_octal=list(num_type)
            binary=[]
            ans=[]
            for i in range(len(input_from_octal)):
                if(input_from_octal[i]=='A'):
                    input_from_octal[i]='10'
                elif(input_from_octal[i]=='B'):
                    input_from_octal[i]='11'
                elif(input_from_octal[i]=='C'): 
                    input_from_octal[i]='12'
                elif(input_from_octal[i]=='D'):
                    input_from_octal[i]='13'
                elif(input_from_octal[i]=='E'):
                    input_from_octal[i]='14'
                elif(input_from_octal[i]=='F'):
                    input_from_octal[i]='15'

            
            for j in input_from_octal:
                if(j=='0'):
                    ans=ans+[0,0,0,0]
                elif(j=='1'):
                    ans=ans+[0,0,0,1]
                elif(j=='2'):
                    ans=ans+[0,0,1,0]
                elif(j=='3'):
                    ans=ans+[0,0,1,1]
                elif(j=='4'):
                    ans=ans+[0,1,0,0]
                elif(j=='5'):
                    ans=ans+[0,1,0,1]
                elif(j=='6'):
                    ans=ans+[0,1,1,0]
                elif(j=='7'):
                    ans=ans+[0,1,1,1]
                elif(j=='8'):
                    ans=ans+[1,0,0,1]
                elif(j=='9'):
                    ans=ans+[1,0,0,1]
                elif(j=='10'):
                    ans=ans+[1,0,1,0]
                elif(j=='11'):
                    ans=ans+[1,0,1,1]
                elif(j=='12'):
                    ans=ans+[1,1,0,0]
                elif(j=='13'):
                    ans=ans+[1,1,0,1]
                elif(j=='14'):
                    ans=ans+[1,1,1,0]
                elif(j=='1'):
                    ans=ans+[1,1,1,1]
            binary=ans         #here we got the binary and now we need to convert it to the different number type
            all_answer(binary)



    decimal=Label(root,text=f"Enter your {out} number",font=("Comic Sans MS", 10, "bold")).grid(row=2,column=0)

    decimal_ans=Text(root,height=1,width=20)
    decimal_ans.grid(row=3,column=0)

    submit=Button(root,text="submit",pady=10,padx=40,command=prin,bd=5,bg="aquamarine")
    submit.grid(row=4,column=0)
    


    


    input.insert(0,My_combo.get())
options = [
    "Decimal",
    "Binary",
    "Octadecimal",
    "Hexadecimal",
    
]

My_combo=ttk.Combobox(root,value=options)
My_combo.current(0)
My_combo.bind("<<ComboboxSelected>>",comboclick)
My_combo.grid(row=0,column=0,columnspan=4,padx=80,pady=10)
input=Entry(root)
input.grid(row=1,column=0,padx=80,pady=10)



root.mainloop()
