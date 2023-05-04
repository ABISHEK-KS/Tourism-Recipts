'''
This code has been written by K.S.ABISHEK from Sri Sairam Engineering College.
 This section pertains to the documentation of the code.
The objective of this code was to generate a PDF document which automates report-insight consolidation.
Few cases of exception have been caught as key errors. These are shown as "ex" in the output terminal
Do not run this script on desktop as such. I am not responsible for the clutter it would create. 
The script generates 203 images which would be written to the PDF. The PDF may have empty pages. Kindly Ignore

'''
import numpy as np
 

import statistics as s
import seaborn as sb
from collections import OrderedDict
import pandas_profiling as pp
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
from countryinfo import CountryInfo


listwithoutexceptions=['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'French Polynesia', 'Gabon', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Mongolia', 'Morocco', 'Mozambique', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Yemen', 'Zimbabwe']
print('LIST WITHOUT EXCEPTIONS LENGTH IS : '+str(len(listwithoutexceptions)))




pdf = FPDF()
myfile=pd.read_csv('tourism-recipts.csv')
myfilee=pd.DataFrame(myfile)
finaldf=[]
pdf.add_page()
pdf.set_font('Arial','B',14)
pdf.text(80,10,"Tourism Recipts Report")
pdf.text(10,20,'Prepared by : K.S.ABISHEK ')
pdf.text(20,30,'*203 Countries were given in dataset')
pdf.text(20,40,'*172 Countries were analyzed by this script without errors')
pdf.text(20,50,'*31 Countries were not analyzed by this script.')
pdf.text(20,60,'*The names of those countries are attested at ')
pdf.text(20,70,'the last page of this auto-generated PDF')
pdf.text(10,90,'*Prepared by a student from Sri Sairam Engineering College')
pdf.text(10,100,'Please do not duplicate script entirely or claim it as yours')
pdf.text(10,110,'Dashboard for this project has also been hosted at novypro')
pdf.text(10,120,'Please check out the PowerBi dashboard for more details')
pdf.text(10,130,'Disclaimer : ')
pdf.text(20,140,'*Numbers are not in desired format due to unsolvable errors')
pdf.text(20,150,'*Recursive function does not reach limit of recursion (<995 calls)')
pdf.text(20,160,'*Script takes at least 60 seconds to run')
pdf.text(20,170,'*If executed outside of a private directory, parent directory is cluttered')
pdf.text(20,180,'*Kindly run in a separate folder and do not claim it as your own')

exceptionlist=[]


def pdfwrite(name):
    try:
        
    
        pdf.add_page()
        pdf.set_font('Arial', 'B', 10)
        parsearg='Tourism Report for '+name
        pdf.text(80,10,parsearg)
        country= CountryInfo(name)
        r=[]
        interiorlist=[]
        
        r=myfilee.loc[myfilee['name'] == name]
        xaxis=list(r['year'])
        yaxis=list(r['value_$'])
        
            
        plt.plot(xaxis,yaxis)
        
        plt.title(name)
        plt.xlabel('Year')
        plt.ylabel('Value')
        
                
        filename=name+'.png'
        plt.savefig(filename)  
        
        plt.close()
        
        pdf.image(filename,50,10,90,90) 
        s1='The stats for '+name+' is as follows:'
        s2='* The average income from Tourism from '+str(xaxis[0])+' to '+str(xaxis[-1])+' is : '+str(s.mean(yaxis))
        pop=str(country.population())
        s3='*The current population of this country is '+str((pop))
        s4='*The highest income from Tourism stands at '+str((max(yaxis)))
        s5='*The lowest income from Tourism stands at '+str((min(yaxis)))
        s6='All the above mentioned values are in USD'
        val=np.diff(yaxis)
        largestdiff=str((min(val)))
        s7='The largest fall in income stands at '+largestdiff
        s8='The deviation in income for every year is valued at '+str((s.stdev(yaxis)))
        s9='The variance stands at '+str((s.variance(yaxis)))
        interiorlist.append(xaxis[0])
        interiorlist.append(xaxis[-1])
        interiorlist.append(max(yaxis))
        interiorlist.append((min(yaxis)))

        

        

           
        pdf.text(10,120,s1)
        pdf.text(30,130,s2)
        pdf.text(30,140,s3)
        pdf.text(30,150,s4)
        pdf.text(30,160,s5)
        pdf.text(10,170,s6)
        pdf.text(10,180,s7)
        pdf.text(10,190,'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        pdf.text(10,200,s8)
        pdf.text(10,210,s9)
       
        

        


        
        
        
        xaxis=[]
        yaxis=[]
        
        print('No exceptions')
    except: 
        print('exception encountered for name'+name)
        exceptionlist.append(name)    
            


countrieslist=sorted(list(set(myfile['name'])))
print(countrieslist)
for k in listwithoutexceptions: 
    pdfwrite(k)
pdf.add_page()
pdf.set_font('Arial','B',12)    
pdf.text(70,20,'Country names not processed')
a=10
b=30
exceptionlist=[x for x in countrieslist if x not in listwithoutexceptions]
for k in exceptionlist:
    parserarg='*'+k 
    print(parserarg)
    pdf.text(a,b,parserarg)
    b+=10
    if b>297: 
        pdf.add_page()
        pdf.set_font('Arial','B',12)
        b=30
pdf.output('Report.PDF','F')
print('PDF WRITTEN')
print('---------------------------------------------------------------------')
print(exceptionlist)
newlist=[x for x in countrieslist if x not in exceptionlist]
print('*****************************************************************')
print(newlist)

print('+++++++++++++++++++++++++++++++++++++++++')
profrep=pp.ProfileReport(myfile)
profrep.to_file('index.html')
print('HTML REPORT GENERATED')