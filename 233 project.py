print('Hello this is a program that will generate a 233.')
print()

time = str(input('When did the inmate get palced in confinement? '))

charge = int(input('What is the charge? '))

name = str(input('What is the name of the Inmate? '))

DC = str(input('What is the DC number of the Inmate? '))

summary = str(input('Give a brief summary? '))

OIC = str(input('Who is the OIC that locked them up? '))

location = str(input('Where did the Inmate recieve his pre-confinement? '))

nurse = str(input('Who was the nurse that did the pre-confinement? '))

psy_grade  = str(input('What is thier psy grade? '))

staff = str(input('What dorm did the property? '))

def get_first_word(s): 
    return s.split()[0] if s else ''
def get_first_word(s): 
    return s.split()[0] if s else ','


first_name = name.split()

first_word = first_name[0]


from datetime import date

# Get the current date
current_date = date.today()

if charge == 13:
       code = '1-3 Spoken, written or gestured threats'		
if charge == 14:
       code = '1-4  Disrespect to officials, employees, or other persons of constituted authority expressed by means of words, gestures, and the like'	
	
if charge == 15:
       code = '1-5  Sexual Battery or attempted sexual battery'	
	
if charge == 16:
       code = '1-6  Lewd or lascivious exhibition by intentionally masturbating, intentionally exposing genitals in a lewd or lascivious manner, or intentionally committing any other sexual act in the presence of a staff member, contracted staff member or visitor.'	
	
if charge == 17:
       code = '1-7  Aggravated battery or attempted aggravated battery on a correctional officer'	
	
if charge == 18:
       code = '1-8  Aggravated battery or attempted aggravated battery on staff other than correctional officer'		
if charge == 19:
       code = '1-9  Aggravated battery or attempted aggravated battery on someone other than staff or inmates (vendor, etc.)' 		

if charge == 110:
       code = '1-10 Aggravated battery or attempted aggravated battery on an inmate'	
	
if charge == 111:
       code = '1-11 Aggravated assault or attempted aggravated assault on a correctional officer'
		
if charge == 112:
       code = '1-12 Aggravated assault or attempted aggravated assault on staff other than correctional officer'

if charge == 113:
       code = '1-13 Aggravated assault or attempted aggravated assault on someone other than staff or inmates (vendor, etc.)'		

if charge == 114:
       code = '1-14 Aggravated assault or attempted aggravated assault on an inmate'
	
if charge == 115:
       code = '1-15 Battery or attempted battery on a correctional officer'	
	
if charge == 116:
       code = '1-16 Battery or attempted battery on staff other than correctional officer'	
	
if charge == 117:
       code = '1-17 Battery or attempted battery on someone other than staff or inmates (vendor, etc.)' 	
	
if charge == 118:
       code = '1-18 Battery or attempted battery on an inmate'	
	
if charge == 119:
       code = '1-19 Assault or attempted assault on a correctional officer'
		
if charge == 120:
       code = '1-20 Assault or attempted assault on staff other than correctional officer'		

if charge == 121:
       code = '1-21 Assault or attempted assault on someone other than staff or inmates (vendor, etc.)'	
	
if charge == 122:
       code = '1-22 Assault or attempted assault on an inmate'		

if charge == 21:
       code = '2-1  Participating in riots, strikes, mutinous acts or disturbances'	
	
if charge == 22:
       code = '2-2  Inciting or attempting to incite riots, strikes, mutinous acts or disturbances—Conveying any inflammatory, riotous, or mutinous communication by word of mouth, in writing or by sign, symbol or gesture' 	
	
if charge == 23:
       code = '2-3  Creating participating in or inciting a minor disturbance'	
	
if charge == 24:
       code = '2-4  Fighting'		

if charge == 31:
       code = '3-1  Possession or manufacture of weapons, ammunition, or explosives'
	
if charge == 32:
       code = '3-2  Possession of escape paraphernalia'		

if charge == 33:
       code = '3-3  Possession of narcotics, unauthorized drugs and drug paraphernalia' 
		
if charge == 34:
       code = '3-4  Trafficking in drugs or unauthorized beverages'
	
if charge == 35:
       code = '3-5  Manufacture of drugs or unauthorized beverages'	
	
if charge == 36:
       code = '3-6  Possession of unauthorized beverages'	
	
if charge == 37:
       code = '3-7  Possession of aromatic stimulants or depressants, such as paint thinner, glue, toluene, etc.'		

if charge == 38:
       code = '3-8  Possession of negotiables—unauthorized amounts of cash where cash is permitted, cash where cash is not permitted, other inmate’s canteen coupons, other inmate’s cashless canteen or identification cards or gift certificates, checks, credit cards or any other negotiable item which is not authorized'		

if charge == 39:
       code = '3-9  Possession of unauthorized or altered identification-driver’s license, social security card, cashless canteen identification card, etc.'		

if charge == 310:
       code = '3-10 Possession of unauthorized clothing or linen—State or personal'
	
if charge == 311:
       code = '3-11 Possession of stolen property—State or personal'
		
if charge == 312:
       code = '3-12 Possession of any other contraband'		

if charge == 313:
       code = '3-13 Introduction of any contraband'	
	
if charge == 314:
       code = '3-14 Possession or use of a cellular telephone or any other type of wireless communication device'

if charge == 315:
       code = '3-15 Possession of gang related paraphernalia or related material, gang symbols, logos, gang colors, drawings, hand signs, or gang related documents'	

if charge == 41:
       code = '4-1  Escape or escape attempt'	
	
if charge == 42:
       code = '4-2  Unauthorized absence from assigned area, including housing, job or any other assigned or designated area'		

if charge == 43:
       code = '4-3  Being in unauthorized area, including housing, job, or any other assigned or designated area'	

if charge == 51:
       code = '5-1  Missing Count'		

if charge == 52:
       code = '5-2  Failure to comply with count procedure'

if charge == 61:
       code = '6-1  Disobeying verbal or written order—any order given to an inmate or inmates by a staff member or other authorized person'
	
if charge == 62:
       code = '6-2  Disobeying institutional regulations'		

if charge == 71:
       code = '7-1  Destruction of State property or property belonging to another'
		
if charge == 72:
       code = '7-2  Altering or defacing State property or property belonging to another'
		
if charge == 73:
       code = '7-3  Destruction of State property or property belonging to another due to gross negligence'
	
if charge == 74:
       code = '7-4  Misuse of State property or property belonging to another- use for purpose other than the intended purpose'		

if charge == 75:
       code = '7-5  Willfully wasting State property or property belonging to another—any waste of edible or usable property'		

if charge == 76:
       code = '7-6  Arson or attempted arson'		

if charge == 81:
       code = '8-1  Failure to maintain personal hygiene or appearance'	
	
if charge == 82:
       code = '8-2  Failure to maintain acceptable hygiene or appearance of housing area'		

if charge == 92:
       code = '9-1  Obscene or profane act, gesture, or statement—oral, written or signified'	
	
if charge == 92:
       code = '9-2  Bribery or attempted bribery'		

if charge == 93:
       code = '9-3  Breaking and entering or attempted breaking' 
	
if charge == 94:
       code = '9-4  Attempt, conspiracy, or attempted conspiracy to commit any crime or violation of the Rule of Prohibited Conduct'		

if charge == 95:
       code = '9-5  Theft of property under $50.00 in value'
	
if charge == 96:
       code = '9-6  Bartering with others'		

if charge == 97:
       code = '9-7  Sex acts or unauthorized physical contact involving inmates'
	    
if charge == 99:
       code = '9-9  Tattooing, being tattooed, or body art to include body piercing, scarring or other non- life threatening acts.'	

if charge == 910:
       code = '9-10 Lying to staff member or others in official capacity, or falsifying records'	
	
if charge == 911:
       code = '9-11 Feigning illness or malingering as determined by a physician or medical authority'	
	
if charge == 912:
       code = '9-12 Gambling or possession of gambling paraphernalia'		

if charge == 913:
       code = '9-13 Insufficient work: This constitutes an inmate not working up to expectation, taking into consideration the inmate’s physical condition, the degree of difficulty of assignment, and the average performance by fellow inmates assigned to the same task.'

if charge == 914:
       code = '9-14 Mail regulation violations'	
	
if charge == 915:
       code = '9-15 Visiting regulation violations'	
	
if charge == 916:
       code = '9-16 Refusing to work or participate in mandatory programs'	
	
if charge == 917:
       code = '9-17 Disorderly conduct'		

if charge == 918:
       code = '9-18 Unauthorized physical contact involving non-inmates' 
		
if charge == 919:
       code = '9-19 Presenting false testimony or information before Disciplinary Team, Hearing Officer, or Investigating Officer'		

if charge == 920:
       code = '9-20 Extortion or attempted extortion'	
	
if charge == 921:
       code = '9-21 Fraud or attempted fraud'	
	
if charge == 922:
       code = '9-22 Robbery or attempted robber'	
	
if charge == 923:
       code = '9-23 Theft of property exceeding $50 in value'	
	
if charge == 924:
       code = '9-24 Loaning or borrowing money or other valuables'	
	
if charge == 925:
       code = '9-25 Telephone regulation violations'	
	
if charge == 926:
       code = '9-26 Refusing to submit to substance abuse testing'
		
if charge == 927:
       code = '9-27 Use of unauthorized drugs- as evidence by positive results from urinalysis test or observable behavior'
	
if charge == 928:
       code = '9-28 Canteen Shortage under $50.00'
		
if charge == 929:
       code = '9-29 Canteen Shortage over $50.00'	
	
if charge == 931:
       code = '9-31 Use of Alcohol—as evidenced by positive results from authorized tests, or by observable behavior'

if charge == 932:
       code = '9-32 In accordance with s. 944.279 (1), F.S., is found by the court to have brought a frivolous or malicious suit, action, claim, proceeding or appeal in any court, or to have brought a frivolous or malicious collateral criminal proceeding or is found by the court to have knowingly or with reckless disregard for the truth brought false information or evidence before the court.' 	
	
if charge == 933:
       code = '9-33 Tampering with, defeating or depriving staff of any security device. Security devices include: locks; locking devices; electronic detection; personal body alarm transmitters and receivers; handheld radios; restraint devices such as handcuffs, waist chains, leg irons and handcuff covers; keys; video and audio monitoring and recording devices; security lighting; weapons; and any other device utilized to ensure the security of the institution.'	
	
if charge == 934:
       code = '9-34 Tampering with or defeating any fire or other safety device. Safety devices include: fire, smoke, and carbon dioxide detection devices; alarm systems; fire suppression systems and devices such as fire sprinklers, fire extinguishers, and dry  chemical systems; safety and emergency lighting; exit lights; evacuation route and warning placards; self-contained breathing apparatuses; personal protective equipment; first aid kits; eye wash stations; and any other device utilized to ensure the safety of the institutions, staff and inmates.'
		
if charge == 935:
       code = '9-35 Establishes or attempts to establish a personal or business relationship with any staff member'

if charge == 936:
       code = '9-36 Gang related activities, including recruitment; organizing; display of symbols, groups, or group photos; promotion or participation'		

if charge == 101:
       code = '10-1 Failure to directly and promptly proceed to and return from designated area by approved method'	

if charge == 102:
       code = '10-2 Failure to remain within designated area of release plan'	

if charge == 103:
       code = '10-3 Failure to return if plan terminated prior to scheduled time'	

if charge == 104:
       code = '10-4 Making unauthorized contact, personal, telephone or otherwise, with any individual in behalf of another inmate'	

if charge == 105:
       code = '10-5 Deviating from or changing approved plan without permission'

if charge == 106:
       code = '10-6 Making purchase or contract without approval'	

if charge == 107:
       code = '10-7 Failure to deposit entire earnings, less authorized deductions, each pay period'

if charge == 108:
       code = '10-8 Failure to repay advancement of monies at stipulated in the inmate’s financial plan'

if charge == 111:
       code = '11-1 Violation of the terms and conditions of the Supervised Community Release Agreement'	
	
if charge == 112:
       code = '11-2 Absconding from the Supervised Community Release Program'


if current_date.month == 1:
    month = 'January '
if current_date.month == 2:
    month = 'February '
if current_date.month == 3:
    month = 'March '
if current_date.month == 4:
    month = 'April '
if current_date.month == 5:
    month = 'May'
if current_date.month == 6:
    month = 'June'
if current_date.month == 7:
    month = 'July'
if current_date.month == 8:
    month = 'August'
if current_date.month == 9:
    month = 'September'
if current_date.month == 10:
    month = 'October'
if current_date.month == 11:
    month = 'November'
if current_date.month == 12:
    month = 'December'

print(f'On {month} {current_date.day}, { current_date.year}, at approximately {time}hrs. Inmate {name} DC#{DC}  was placed in Confinement pending Disciplinary Charges, A7, per Captain {OIC} for {code}. {summary}. Confinement placement was deemed necessary at this time because Inmate {first_word} posed a threat to the security, safety, and orderly operations of the facility. Due to Inmate {first_word} actions and behavior, no alternative housing options were appropriate. Inmate {first_word} was escorted to {location} and received a pre-confinement assessment by Nurse {nurse}.  Inmate {first_word} has a mental health grade of a ({psy_grade}).  It was determined, at this time, that there would be no negative impact on Inmate {first_word} ’s medical or mental health by this placement. Inmate {first_word} was afforded the opportunity to call and notify at least (3) approved visitors. His ID Card was deactivated by Captain {OIC} and his property was inventoried by {staff}-Dorm Staff.')
