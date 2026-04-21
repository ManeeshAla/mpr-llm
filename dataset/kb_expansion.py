"""
kb_expansion.py  — Extra Q&A facts added on top of the base KNOWLEDGE_BASE.
Run data_generator.py which imports and merges these automatically.
"""

EXTRA_FACTS = {

    # ── GENERAL ──────────────────────────────────────────────────────────
    "General": [
        ("What is the school's motto?",
         "The school's motto is 'Knowledge, Discipline, Service'. It reflects the three pillars of holistic education we follow — academic excellence, personal discipline, and community service.",
         ["School motto?", "What is the school vision?", "Mission of school?", "School slogan?",
          "School tagline?", "School philosophy?", "What does the school stand for?"]),

        ("When was the school established?",
         "The school was established in 1998 and has been serving the community for over 25 years. It started with 120 students and has grown to over 2,000 students today.",
         ["School founding year?", "How old is the school?", "Year school was started?",
          "When was school founded?", "School history?", "How many years old is school?"]),

        ("What is the total student strength?",
         "The school currently has over 2,000 students enrolled from Nursery to Class 12, spread across 65 sections.",
         ["How many students in school?", "Total enrollment?", "School student count?",
          "How many children study here?", "Student strength?", "Total number of students?"]),

        ("What is the morning assembly schedule?",
         "Morning assembly takes place from 7:55 AM to 8:10 AM daily in the school ground. It includes the national anthem, prayer, thought of the day, news headlines, and important announcements.",
         ["Assembly time?", "What happens in morning assembly?", "Prayer time?",
          "Morning prayer schedule?", "Assembly routine?", "When is assembly?"]),

        ("Does the school offer Nursery, LKG, and UKG?",
         "Yes, the school has a Pre-Primary section with Nursery (age 3+), LKG (age 4+), and UKG (age 5+). The Pre-Primary section has a dedicated building with child-friendly infrastructure.",
         ["Is nursery available?", "LKG UKG admission?", "Pre primary classes?",
          "Kindergarten available?", "Does school have playgroup?", "Pre-school classes?"]),

        ("What streams are available in Class 11 and 12?",
         "The school offers three streams in Class 11 and 12: Science (PCM and PCB), Commerce (with and without Maths), and Humanities/Arts. Stream selection is done in April after Class 10 results.",
         ["Science stream available?", "Commerce stream?", "Arts stream?", "Humanities in school?",
          "PCM PCB available?", "Which stream can I choose?", "Stream selection process?"]),

        ("What is the student-teacher ratio?",
         "The school maintains a student-teacher ratio of 30:1 to ensure adequate individual attention. Each class has a dedicated class teacher and subject specialists.",
         ["How many students per teacher?", "Teacher student ratio?", "Class size?",
          "How many students per class?", "Students per teacher?", "Class strength?"]),

        ("Does the school publish an annual magazine?",
         "Yes, the school publishes an annual magazine called 'Expressions' every March. It features student articles, poetry, artwork, and the year's achievements. A copy is included in the school fee.",
         ["School magazine?", "Annual magazine?", "Student publication?",
          "School journal?", "Does school have a magazine?", "Annual school book?"]),

        ("What languages are taught in the school?",
         "The school offers English and Hindi as compulsory languages. Sanskrit and French are available as third language options from Class 6 onwards. German is available as an elective in Class 11-12.",
         ["Which languages?", "Is French taught?", "Sanskrit in school?", "German language?",
          "Third language options?", "Foreign language?", "Which language subjects?"]),

        ("What is the school's address?",
         "The school is located at 12, Education Avenue, near City Park, Mumbai - 400001. Nearest landmark: City Mall. You can also find us on Google Maps as 'City School Mumbai'.",
         ["School address?", "Where is the school located?", "School location?",
          "How to reach school?", "School directions?", "School map?"]),

        ("How many classrooms does the school have?",
         "The school has 65 well-ventilated classrooms spread across 4 floors, including smart classrooms on all floors, 3 science labs, a computer lab, art room, music room, and a library.",
         ["Number of classrooms?", "School infrastructure?", "How many rooms?",
          "School building details?", "How big is the school?", "School facilities count?"]),

        ("Is there a school uniform inspection?",
         "Yes, school captains and prefects conduct a weekly uniform inspection every Monday. Students found in improper uniform are noted and a remark is given in the diary.",
         ["Uniform check?", "Who checks uniform?", "Dress inspection?",
          "Uniform inspection day?", "Prefect duties?", "How is uniform checked?"]),

        ("What are the school's key achievements?",
         "The school has won the Best School Award by the State Government 3 times. Our students have won National Science Olympiad, State Debate Championship, and Inter-District Sports Meet consecutively for 5 years.",
         ["School awards?", "School achievements?", "School recognition?",
          "Awards won by school?", "School reputation?", "Is school well known?",
          "Famous achievements of school?"]),

        ("Does the school have a WhatsApp group for parents?",
         "Yes, each class has an official parent WhatsApp group managed by the class teacher. Only school-related updates are shared. Joining details are provided at the start of the year.",
         ["Parent WhatsApp group?", "Class WhatsApp group?", "School WhatsApp?",
          "Parent group for updates?", "How to join parent group?", "WhatsApp notifications?"]),

        ("Is there a school canteen?",
         "Yes, the school canteen is open from 8:00 AM to 2:30 PM. It serves hot meals, snacks, and beverages. The menu is reviewed monthly and approved by a nutritionist.",
         ["Canteen timing?", "Canteen menu?", "School cafeteria?", "Food available in school?",
          "Snacks available?", "School tuck shop?", "Where to eat in school?"]),

        ("What is the fee for Class 9?",
         "The annual tuition fee for Class 9 is Rs.54,000. This includes lab access, library charges, and co-curricular fees. Books and uniforms are purchased separately.",
         ["Class 9 fee?", "9th standard fee?", "Fee for ninth grade?",
          "Class 9 annual charges?", "How much is Class 9?", "9th class fees?"]),
    ],

    # ── FEES ─────────────────────────────────────────────────────────────
    "Fees": [
        ("What is the annual fee for Class 2?",
         "The annual tuition fee for Class 2 is Rs.36,500. This covers tuition and basic activity charges. Books and uniforms are separate.",
         ["Fee for Class 2?", "2nd standard fee?", "Class 2 annual fee?",
          "How much is Class 2?", "Second class fee?", "Class two fee?"]),

        ("What is the annual fee for Class 3?",
         "The annual tuition fee for Class 3 is Rs.37,500. This includes tuition and library access. Books and uniforms are charged separately.",
         ["Fee for Class 3?", "3rd standard fee?", "Class 3 fee?",
          "Third class fee?", "Class three annual charges?", "Grade 3 fee?"]),

        ("What is the annual fee for Class 4?",
         "The annual tuition fee for Class 4 is Rs.39,000. Books and uniforms are purchased separately.",
         ["Fee for Class 4?", "4th standard fee?", "Class 4 fee?",
          "Fourth class fee?", "Grade 4 fee?", "Class four annual charges?"]),

        ("What is the annual fee for Class 6?",
         "The annual tuition fee for Class 6 is Rs.44,000. This includes the science lab access and library. Books and uniforms are extra.",
         ["Fee for Class 6?", "6th standard fee?", "Class 6 fee?",
          "Sixth class fee?", "Class 6 annual charges?", "Grade 6 fee?"]),

        ("What is the annual fee for Class 7?",
         "The annual tuition fee for Class 7 is Rs.46,000. Lab access and co-curricular fees are included. Books and uniforms are extra.",
         ["Fee for Class 7?", "7th standard fee?", "Class 7 fee?",
          "Seventh class fee?", "Class 7 charges?", "Grade 7 fee?"]),

        ("What is the annual fee for Class 11?",
         "The annual fee for Class 11 is Rs.60,000. It varies slightly by stream: Science stream students pay an additional Rs.3,000 for lab fees. Commerce and Arts fees are the same.",
         ["Fee for Class 11?", "11th standard fee?", "Class 11 fee?",
          "Eleventh class fee?", "Junior college fee?", "Class 11 annual charges?"]),

        ("What is the annual fee for LKG?",
         "The annual fee for LKG is Rs.28,000. It includes tuition, activities, and a stationery kit. Uniforms are purchased separately.",
         ["LKG fee?", "Lower kindergarten fee?", "Fee for LKG?",
          "LKG annual charges?", "How much is LKG?", "Kindergarten fee?"]),

        ("What is the annual fee for UKG?",
         "The annual fee for UKG is Rs.29,500. It includes tuition, activity material, and basic stationery. Uniforms are separate.",
         ["UKG fee?", "Upper kindergarten fee?", "Fee for UKG?",
          "UKG annual charges?", "How much is UKG?", "Senior kindergarten fee?"]),

        ("What is the annual fee for Nursery?",
         "The annual fee for Nursery is Rs.25,000. It includes play-based learning activities and a basic stationery kit.",
         ["Nursery fee?", "Fee for nursery class?", "Pre-nursery fee?",
          "Nursery annual charges?", "How much for nursery?", "Play school fee?"]),

        ("Is there a development fee charged?",
         "Yes, a one-time development fee of Rs.10,000 is collected at the time of admission. This goes toward school infrastructure upgrades such as smart boards and lab equipment.",
         ["Development fee?", "Infrastructure fee?", "Building fund?",
          "Development charges?", "One time school charge?", "Capital fee?"]),

        ("What is the examination fee?",
         "The internal exam fee of Rs.500 per term is included in the annual fee. For CBSE board exam registration, Class 10 and 12 students pay an additional Rs.1,500 directly to the school which is forwarded to CBSE.",
         ["Exam fee?", "Examination charges?", "Board exam fee?",
          "Test fee?", "CBSE registration fee?", "Exam registration cost?"]),

        ("Is there any sibling discount on fees?",
         "Yes, the school offers a 10% tuition fee concession for the second sibling and 15% for the third sibling onwards. Submit a sibling declaration form at the accounts office.",
         ["Sibling fee discount?", "Fee reduction for siblings?", "Concession for second child?",
          "Brother sister fee discount?", "Second child fee?", "Family discount?"]),

        ("What is the fine for a lost library book?",
         "If a library book is lost or damaged beyond repair, the student must pay twice the current market price of the book. Report lost books immediately to the librarian to avoid additional penalty.",
         ["Lost library book fine?", "Damaged book charges?", "Library book penalty?",
          "Book replacement cost?", "Lost book policy?", "Library fine?"]),

        ("Is there a fee for sports activities?",
         "Sports equipment usage and coaching for cricket, football, basketball, and athletics are included in the annual co-curricular fee of Rs.2,000 per year.",
         ["Sports fee?", "Games fee?", "Sports charges?", "Cricket coaching fee?",
          "Football coaching charges?", "Athletic coaching fee?", "Activity fee?"]),

        ("How do I get a fee certificate for income tax?",
         "Fee certificates for income tax purposes (Section 80C) are available on the parent portal under 'Documents'. You can also request a physical copy at the accounts office with 2 working days' notice.",
         ["Fee certificate for income tax?", "80C fee proof?", "Tax exemption certificate?",
          "Income tax fee document?", "Tuition fee receipt for tax?", "Fee document for IT return?"]),
    ],

    # ── ADMISSIONS ───────────────────────────────────────────────────────
    "Admissions": [
        ("What is the re-admission process?",
         "If a student has taken a TC and wishes to re-join, they must apply fresh with all original documents plus the TC from the school where they went. Re-admission is subject to seat availability.",
         ["Re-admission process?", "Can a student come back after TC?", "Rejoining the school?",
          "Re-enrollment?", "Can I re-admit my child?", "Rejoining after leaving?"]),

        ("Is there a sibling concession on admission fees?",
         "Yes, siblings of current students get a waiver on the Rs.1,500 registration fee and priority consideration in admissions.",
         ["Sibling priority admission?", "Is sibling given preference?",
          "Brother or sister already in school admission?", "Family admission priority?"]),

        ("How do I complete the online admission process?",
         "Step 1: Visit the school website and click 'Apply Online'. Step 2: Fill the form with student and parent details. Step 3: Upload scanned documents. Step 4: Pay the Rs.1,500 registration fee online. Step 5: You will receive a confirmation email and interview date within 3 working days.",
         ["Online admission steps?", "How to fill online form?", "Online application process?",
          "Steps to apply online?", "Digital admission?", "How to register online?"]),

        ("Can I visit the school before applying?",
         "Yes, open house visits are available every Saturday from 9:00 AM to 11:00 AM during the admission season (January to March). No prior appointment is needed. Speak to the Admissions Coordinator directly.",
         ["School visit before admission?", "Open house visit?", "Can I tour the school?",
          "School campus visit?", "Pre-admission visit?", "Visit school before applying?"]),

        ("Is there a waiting list for admissions?",
         "Yes, if seats are full, eligible applicants are placed on a waiting list in order of application date and entrance test score. Parents are notified if a seat becomes available.",
         ["Admission waiting list?", "What if seats are full?", "Waitlist for admission?",
          "Is there a queue for admission?", "When will seat be available?"]),

        ("How is admission confirmed after selection?",
         "After selection, parents must pay the first installment of fees and submit original documents within 7 days to confirm the seat. Failure to do so will result in the seat being offered to the next applicant.",
         ["Admission confirmation process?", "How to secure seat?", "When is seat confirmed?",
          "Fee to confirm admission?", "Deposit to confirm seat?"]),

        ("What is the age criteria for Nursery admission?",
         "A child must be at least 3 years old as of June 1st to be admitted to Nursery. For LKG, the minimum age is 4 years and for UKG it is 5 years.",
         ["Age for nursery?", "Nursery age limit?", "Minimum age for nursery admission?",
          "Age requirement for LKG?", "UKG age criteria?", "Kindergarten age?"]),

        ("What if a document is missing at the time of admission?",
         "Provisional admission may be granted for up to 30 days to allow time to submit missing documents. However, all documents must be submitted before the final confirmation.",
         ["Missing document admission?", "Incomplete documents?", "Can I submit documents later?",
          "Provisional admission?", "What if I don't have all papers?"]),

        ("How do I get a Transfer Certificate (TC) if my child is leaving?",
         "To obtain a TC, submit a written application to the principal's office at least 15 days in advance. Clear all dues, return library books, and the TC will be issued within 7 working days.",
         ["How to get TC?", "Transfer certificate process?", "Leaving school TC?",
          "TC issuing procedure?", "Process for TC?", "School leaving certificate?"]),

        ("How do I get a bonafide certificate?",
         "A bonafide certificate can be requested at the admin office with a written application. It is issued within 2 working days and is free of charge. Required for bank accounts, scholarships, etc.",
         ["Bonafide certificate?", "Studying certificate?", "School bonafide?",
          "Student certificate?", "Proof of enrollment certificate?", "Bonafide request?"]),

        ("How do I get a character certificate?",
         "Character certificates are issued upon written request to the admin office. They are available to students who have completed at least one full academic year at the school.",
         ["Character certificate?", "Conduct certificate?", "Good character proof?",
          "Certificate for character?", "Character testimonial?"]),

        ("Can admission be cancelled after confirmation?",
         "Yes, a parent may withdraw admission before June 1st. The registration fee of Rs.1,500 is non-refundable. The development fee and first term tuition fees are refundable after deducting a processing fee of Rs.2,000.",
         ["Cancel admission?", "Withdrawal of admission?", "Refund on cancellation?",
          "Can I cancel school admission?", "Admission refund policy?"]),

        ("Is the school open for NRI/OCI admissions?",
         "Yes, NRI and OCI students can apply directly. They must submit their passport, visa, and last school report as part of the application. An online interview may be arranged if the student is abroad.",
         ["NRI admission?", "OCI card admission?", "Foreign student admission?",
          "Admission from abroad?", "Is NRI child eligible?"]),

        ("Are there seats reserved for differently-abled students?",
         "Yes, the school has a 3% reservation for students with disabilities as per the RTE Act. Special accommodations including ramps, separate seating, and extra time in exams are provided.",
         ["Disabled student admission?", "Differently abled admission?", "Special needs admission?",
          "Handicapped student seats?", "Wheelchair accessible school?", "Special education seats?"]),
    ],

    # ── ACADEMIC ─────────────────────────────────────────────────────────
    "Academic": [
        ("What subjects are available in the Science stream (Class 11-12)?",
         "Science stream students choose between PCM (Physics, Chemistry, Mathematics) or PCB (Physics, Chemistry, Biology). Computer Science or Informatics Practices can be taken as a 5th subject.",
         ["Science stream subjects?", "PCM subjects?", "PCB subjects?",
          "Physics chemistry maths?", "Biology stream?", "Science subjects 11th?",
          "Class 11 science subjects?", "What is in science stream?"]),

        ("What subjects are in the Commerce stream (Class 11-12)?",
         "Commerce stream includes: Accountancy, Business Studies, Economics, English, and either Mathematics or Informatics Practices as the 5th subject.",
         ["Commerce stream subjects?", "Accountancy in school?", "Business studies?",
          "Class 11 commerce subjects?", "Commerce subjects?", "Economics subject?"]),

        ("What subjects are in the Humanities/Arts stream (Class 11-12)?",
         "Humanities includes: History, Political Science, Geography or Psychology, English, and one elective subject such as Sociology, Fine Arts, or Home Science.",
         ["Arts stream subjects?", "Humanities subjects?", "History Geography in school?",
          "Class 11 arts?", "Humanities stream?", "Political science in school?"]),

        ("How many periods are there in a school day?",
         "There are 8 periods per day, each of 40 minutes. Periods 4 and 5 are separated by a lunch break from 12:00 PM to 12:30 PM.",
         ["Number of periods?", "How many classes per day?", "Period duration?",
          "Length of a class?", "How long is each period?", "Class duration in school?"]),

        ("What is the internal assessment (IA) weightage?",
         "Internal assessment carries 20% of the total marks for all subjects. It includes periodic tests (10%), student enrichment activities (5%), and portfolio/practical (5%).",
         ["Internal assessment marks?", "IA percentage?", "Internal marks?",
          "How much is internal assessment?", "Term marks weightage?", "Formative assessment?"]),

        ("When are pre-board exams held?",
         "Pre-board exams for Class 10 and Class 12 are held in December-January. A second pre-board may be conducted in February for students who need additional practice.",
         ["Pre-board exam date?", "Mock board exam?", "Practice board exam?",
          "Pre-board schedule?", "When is pre-board?", "Trial exam?"]),

        ("Does the school conduct Olympiads?",
         "Yes, the school participates in Science Olympiad Foundation (SOF) exams including IMO (Maths), NSO (Science), and IEO (English). Enrollment is done in August every year.",
         ["Olympiad exams?", "Math olympiad?", "Science olympiad?", "IMO registration?",
          "SOF olympiad?", "English olympiad?", "IEO exam?"]),

        ("Is Sanskrit available as a subject?",
         "Yes, Sanskrit is offered as a third language option from Class 6 to Class 10. It can also be taken as an elective in Class 11-12 Humanities stream.",
         ["Sanskrit subject?", "Is Sanskrit taught?", "Sanskrit in school?",
          "Can I take Sanskrit?", "Sanskrit language option?"]),

        ("Is French available as a subject?",
         "Yes, French is available as a third language option from Class 6 onwards and as a full elective in Class 11-12. Classes are conducted by a trained French language teacher.",
         ["French in school?", "Is French taught?", "French language subject?",
          "Can I study French?", "French option available?"]),

        ("What is the holiday homework policy?",
         "Holiday homework is given during summer and winter breaks. It is designed to be creative and activity-based rather than rote writing. Submission is on the first day of reopening.",
         ["Holiday homework?", "Summer vacation homework?", "Vacation assignments?",
          "Holiday project?", "Break homework?", "Are there holiday assignments?"]),

        ("How many times are exams conducted in a year?",
         "The school conducts three periodic tests and two major term examinations per academic year. Class 10 and 12 students also have pre-board exams. Total: 5-6 assessments per subject per year.",
         ["How many exams per year?", "Exam frequency?", "Number of tests in year?",
          "How often are exams?", "Exam schedule overview?", "Tests in a year?"]),

        ("When is the result for Class 10 Board declared?",
         "CBSE Class 10 board results are typically declared in May. Students can check results on the CBSE official website cbseresults.nic.in and also on the school portal.",
         ["Class 10 board result date?", "CBSE 10th result?", "When is 10th result?",
          "Board result announcement?", "Matric result date?", "10th marks when?"]),

        ("What is the minimum marks to pass?",
         "The minimum passing marks is 33% in each subject for Classes 1 to 12 as per CBSE norms. In practical subjects, passing separately in theory and practical is mandatory.",
         ["Passing marks?", "Minimum marks to pass?", "Pass percentage?",
          "What is passing score?", "How many marks to pass?", "Fail marks?"]),

        ("Is there a topper recognition program?",
         "Yes, class toppers are felicitated at the Annual Day ceremony with merit certificates, trophies, and a full tuition fee waiver for the next academic year for the school topper.",
         ["Merit scholarship for topper?", "Reward for topper?", "Who gets topper prize?",
          "Recognition for rank 1?", "School topper award?", "Academic prize?"]),
    ],

    # ── FACILITIES ───────────────────────────────────────────────────────
    "Facilities": [
        ("Are there separate science labs?",
         "Yes, the school has three separate labs: Physics Lab, Chemistry Lab, and Biology Lab, each equipped for Class 9-12 practicals. Class 6-8 share a combined Junior Science Lab.",
         ["Physics lab?", "Chemistry lab?", "Biology lab?", "Science lab available?",
          "Lab facility?", "Practical lab?", "Laboratory in school?"]),

        ("Is there an art room?",
         "Yes, the school has a dedicated Art Room equipped with easels, drawing boards, painting supplies, and a kiln for pottery. Art is a compulsory subject up to Class 8.",
         ["Art room?", "Art studio?", "Drawing room?", "Painting facility?",
          "Craft room?", "Is art taught?", "Where are art classes held?"]),

        ("Is there a music room?",
         "Yes, the school has a fully equipped Music Room with both Indian and Western instruments including tabla, harmonium, keyboard, guitar, and a set of drums. Music classes are held daily.",
         ["Music room?", "Musical instruments?", "Keyboard guitar in school?",
          "Tabla harmonium?", "Where are music classes?", "School band room?"]),

        ("Is there an auditorium?",
         "Yes, the school has a 500-seat air-conditioned auditorium used for Annual Day, PTMs, seminars, and inter-school competitions. It has a stage, sound system, and projection setup.",
         ["School auditorium?", "Seminar hall?", "Stage facility?",
          "Event hall?", "Is there a hall?", "School theater?"]),

        ("Is there a parking facility for parents?",
         "Yes, there is a designated parent parking area on the east side of the school gate with a capacity for 100 vehicles. Parking is free during school hours.",
         ["Parking available?", "Parent parking?", "Car parking?",
          "Where to park?", "Parking facility?", "Bike parking?"]),

        ("Is there a generator backup in school?",
         "Yes, the school has a 100KVA diesel generator that automatically kicks in during power cuts, ensuring uninterrupted classes and computer lab sessions.",
         ["Generator in school?", "Power backup?", "Electricity backup?",
          "Power cut issue?", "UPS facility?", "School power supply?"]),

        ("Are there separate washrooms for boys and girls?",
         "Yes, the school has separate washrooms for boys and girls on every floor, maintained hygienically by dedicated sanitation staff. Staff washrooms are also separate.",
         ["Separate toilets?", "Girls washroom?", "Boys toilet?",
          "Washroom facility?", "Hygiene in school toilets?", "Bathroom in school?"]),

        ("Is the school Wi-Fi enabled?",
         "Yes, the school campus has high-speed Wi-Fi coverage in all classrooms, the library, computer lab, and staff rooms. Student access is filtered and monitored.",
         ["Wi-Fi in school?", "Internet in school?", "Wireless internet?",
          "School internet connection?", "Campus Wi-Fi?", "Is there internet?"]),

        ("Are there lockers for students?",
         "Lockers are available for Class 9-12 students in the corridor. A refundable locker deposit of Rs.500 is required. One locker is shared between two students.",
         ["Student lockers?", "Storage facility?", "Is there a locker?",
          "Locker availability?", "Can I get a locker?", "Bag storage?"]),

        ("Does the school have solar panels?",
         "Yes, the school installed a 50KW rooftop solar panel system in 2022 as part of its Green Campus initiative. It meets approximately 40% of the school's electricity requirement.",
         ["Solar energy?", "Green school?", "Solar panels?", "Renewable energy?",
          "Eco-friendly school?", "Solar power in school?"]),

        ("Is there a school garden or nature area?",
         "Yes, the school has a nature garden tended by students as part of environmental education. It has medicinal plants, a small vegetable patch, and a compost pit.",
         ["School garden?", "Nature area?", "Plant area?", "Ecology garden?",
          "Does school have plants?", "Green area in school?"]),

        ("Are classrooms air-conditioned?",
         "Smart classrooms for Class 9-12 are air-conditioned. Classes 1-8 have ceiling fans and good cross-ventilation. The computer lab, library, and auditorium are air-conditioned.",
         ["AC classrooms?", "Air conditioned rooms?", "Are rooms cool?",
          "Cooling in classrooms?", "Fan or AC?", "AC in school?"]),

        ("Is there a school dispensary or first aid room?",
         "Yes, the school has a medical room with a trained nurse, basic medicines, first aid kits, a stretcher, and a wheelchair. The room is open throughout school hours.",
         ["First aid room?", "School dispensary?", "Medical room?",
          "Sick room?", "Is nurse there?", "First aid facility?"]),
    ],

    # ── STAFF ────────────────────────────────────────────────────────────
    "Staff": [
        ("How can I apply for a teaching job at this school?",
         "Job openings are posted on the school's website under 'Careers'. Send your updated resume and a covering letter to hr@school.com. Shortlisted candidates are called for a demo class and interview.",
         ["Job in school?", "How to apply for teacher job?", "Teaching vacancy?",
          "School recruitment?", "HR email for job?", "Career in school?"]),

        ("What qualifications are required to become a teacher here?",
         "Teachers must hold a relevant graduation degree and a B.Ed or D.El.Ed qualification as per NCTE norms. Subject specialists for Class 11-12 must have a postgraduate degree.",
         ["Teacher qualification?", "Requirement to teach here?",
          "BEd required?", "Teacher eligibility?", "Educational qualification for teacher?"]),

        ("Who is the Vice Principal?",
         "The Vice Principal is Mr. Verma, who oversees academics and student discipline. You can meet him during office hours from 9:00 AM to 12:00 PM on working days.",
         ["Vice principal name?", "Who is VP?", "Second in charge?",
          "Assistant principal?", "VP contact?", "Who handles academics?"]),

        ("Who handles the academics coordination?",
         "The Academic Coordinator, Ms. Joshi, manages curriculum, exam schedules, and teacher trainings. She can be reached at coordinator@school.com.",
         ["Academic coordinator?", "Who manages curriculum?", "Academics in charge?",
          "Curriculum coordinator contact?", "Who plans academics?"]),

        ("How can I update my contact details with the school?",
         "To update your mobile number, email ID, or home address, fill the 'Contact Update Form' available at the admin office or on the parent portal under 'My Profile'.",
         ["Update phone number?", "Change address in school record?",
          "Update contact info?", "How to change contact details?", "Edit parent details?"]),

        ("Who is the sports teacher?",
         "The Physical Education department is led by Mr. Raj, who has 15 years of experience in coaching cricket and athletics. He also coordinates all inter-school sports events.",
         ["Sports teacher name?", "PE teacher?", "Physical education teacher?",
          "Who coaches cricket?", "Sports department?", "PT teacher?"]),

        ("What are the office hours for parent queries?",
         "The admin office is open for parent queries from 8:30 AM to 2:30 PM on all working days. For urgent matters, call the school helpline at +91-XXXXXXXXXX.",
         ["Admin office timing?", "When can I visit school office?", "Query timing?",
          "Office hours?", "When is admin open?", "Office availability?"]),

        ("Is career guidance available for students?",
         "Yes, the school has a dedicated Career Counselor who helps Class 10, 11, and 12 students with stream selection, college choices, entrance exam guidance, and scholarship applications.",
         ["Career counseling?", "College guidance?", "Stream selection help?",
          "Entrance exam guidance?", "Career advice in school?", "Who guides for college?"]),

        ("Is there a suggestion box in school?",
         "Yes, a suggestion box is placed outside the principal's office. Students and parents can drop anonymous suggestions or complaints, which are reviewed every week.",
         ["Suggestion box?", "Anonymous feedback?", "Where to give complaints?",
          "Suggestion drop box?", "Complaint box?", "Student suggestion?"]),
    ],

    # ── POLICIES ─────────────────────────────────────────────────────────
    "Policies": [
        ("Is weekend homework given?",
         "Light revision exercises may be given over the weekend, but heavy homework loads are avoided to allow students rest. Projects requiring research may have weekend components.",
         ["Weekend homework?", "Saturday Sunday homework?", "Work on weekends?",
          "Homework on Sunday?", "Is homework given for weekend?"]),

        ("What items are not allowed in school?",
         "Prohibited items include: mobile phones, smart watches, Bluetooth earphones, chewing gum, playing cards, energy drinks, and any electronic gadgets not authorized by the teacher.",
         ["Banned items in school?", "What can't students bring?", "Prohibited things?",
          "Not allowed in school?", "Forbidden items?", "What is banned?"]),

        ("Can parents enter the school premises during class hours?",
         "Parents may enter the school only with prior appointment and a visitor's pass issued at the gate. Random entry is not permitted during class hours to avoid disruption.",
         ["Can parents come in?", "Parent entry policy?", "Can I enter school?",
          "Parent visit during class?", "Visitor policy?", "Gate entry for parents?"]),

        ("What is the birthday celebration policy?",
         "Students may celebrate birthdays by distributing small snacks like chocolates or biscuits during the lunch break. Cake cutting during class time is not permitted. Expensive gifts are discouraged.",
         ["Birthday party in school?", "How to celebrate birthday?", "Can I bring cake?",
          "Birthday policy?", "Can students celebrate?", "Birthday distribution?"]),

        ("Are students allowed to leave school early?",
         "Students may leave early only with a written request from parents submitted at the admin office. The student is released into the care of an authorized adult after verification.",
         ["Early leave?", "Leave school before time?", "Can child leave early?",
          "Permission to leave early?", "Mid-day pickup?", "Early dismissal?"]),

        ("What is the academic integrity policy?",
         "Plagiarism, copying in exams, or submitting others' work is treated as a serious misconduct. First offence: zero marks. Second offence: parent meeting. Third offence: suspension.",
         ["Plagiarism policy?", "Copying in exam?", "Academic cheating policy?",
          "What if student cheats?", "Integrity in exams?", "Exam misconduct?"]),

        ("Are water bottles and tiffin boxes allowed?",
         "Yes, students are encouraged to bring their own water bottles and home-cooked tiffin. Sharing food with other students is discouraged due to hygiene and allergy concerns.",
         ["Water bottle allowed?", "Can students bring tiffin?", "Food from home?",
          "Lunch box allowed?", "Home food in school?", "Bring water?"]),

        ("What is the re-checking of exam papers policy?",
         "Students can apply for re-checking of their answer sheet within 7 days of result declaration. Submit the application at the admin office with a fee of Rs.100 per paper.",
         ["Paper re-checking?", "Recount marks?", "Apply for re-evaluation?",
          "Check answer sheet again?", "Review exam marks?", "Re-examination of paper?"]),

        ("Does the school provide student insurance?",
         "Yes, all enrolled students are covered under a group student accident insurance policy of Rs.1,00,000 at no extra cost. This covers accidents within the school premises and during school-approved events.",
         ["Student insurance?", "Accident insurance?", "School insurance policy?",
          "Is student insured?", "Coverage for accidents?", "Medical insurance in school?"]),

        ("What is the inter-school field trip policy?",
         "Educational trips require written consent from parents and are subject to principal approval. Students below Class 6 are accompanied by a parent volunteer. Trip fees are announced separately.",
         ["School trip policy?", "Field trip rules?", "Educational excursion?",
          "Trip permission?", "Picnic rules?", "School outing policy?"]),

        ("What is the social media policy for students?",
         "Students are prohibited from posting school content, photos of classmates, or school events on social media without explicit written permission from the school. Cyberbullying is treated as a serious offence.",
         ["Social media rules?", "Can students post online?", "Instagram school photos?",
          "Photo policy?", "Cyber rules for students?", "Posting school pictures?"]),
    ],

    # ── HR ───────────────────────────────────────────────────────────────
    "HR": [
        ("What are the working hours for teaching staff?",
         "Teachers are required to be present from 7:45 AM to 2:30 PM on working days. Beyond school hours, teachers may be called for PTMs, events, and training programs.",
         ["Teacher working hours?", "Staff timing?", "How long do teachers work?",
          "Work hours for teachers?", "Teacher shift?", "School timing for teachers?"]),

        ("Is there a staff lunch break?",
         "Yes, teachers get a 30-minute lunch break from 12:00 PM to 12:30 PM. The staff canteen provides subsidised meals for all teaching and non-teaching staff.",
         ["Staff lunch break?", "Teacher lunch time?", "Food for staff?",
          "Staff cafeteria?", "Teacher mess?", "Lunch facility for teachers?"]),

        ("What is the staff dress code?",
         "Teaching staff are expected to dress professionally. Formals or traditional Indian attire (saree/kurta) are preferred. Jeans, shorts, and casual t-shirts are not permitted on teaching days.",
         ["Staff uniform?", "Teacher dress code?", "What should teachers wear?",
          "Teachers attire?", "Staff clothing policy?", "Dress for teachers?"]),

        ("Is there health insurance for school staff?",
         "Yes, the school provides a group medical insurance of Rs.3,00,000 per annum for all permanent staff and their immediate family members.",
         ["Staff health insurance?", "Medical insurance for teachers?",
          "Employee insurance?", "Teacher medical coverage?", "Staff hospital cover?"]),

        ("Does the school offer PF/EPF benefits?",
         "Yes, Provident Fund (PF) contributions are made as per the EPF Act — 12% of basic salary by the employee and matched by the school. Staff can access their PF details on the EPFO portal.",
         ["PF for teachers?", "EPF benefit?", "Provident fund?",
          "Retirement benefit?", "PF contribution?", "Staff pension?"]),

        ("What is the notice period for resignation?",
         "A 30-day written notice is required for resignation. If leaving mid-session (June to March), a 60-day notice or payment in lieu is required to ensure students are not affected.",
         ["Resignation notice period?", "How to resign?", "Leaving job notice?",
          "Notice for teachers?", "Quit job process?", "Staff resignation policy?"]),

        ("Is there an annual increment for staff?",
         "Yes, teaching staff receive an annual increment of 5–10% based on performance appraisal conducted in March every year. Non-teaching staff follow the pay commission scales.",
         ["Salary increment?", "Annual raise?", "Hike in salary?",
          "Pay increment?", "Salary increase?", "Teacher pay raise?"]),

        ("Is there a staff training program?",
         "Yes, the school conducts in-service teacher training workshops at least twice a year. Topics include new pedagogy techniques, technology in classrooms, and mental health first aid.",
         ["Teacher training?", "In-service training?", "Staff development?",
          "Professional development?", "Workshop for teachers?", "Training program?"]),

        ("Is gratuity provided to staff?",
         "Yes, staff who complete 5 or more years of continuous service are entitled to gratuity as per the Payment of Gratuity Act, calculated as 15 days of salary per year of service.",
         ["Gratuity policy?", "Gratuity for teachers?", "Long service benefit?",
          "Retirement gratuity?", "Staff gratuity amount?", "Gratuity calculation?"]),

        ("How to raise a staff grievance?",
         "Staff grievances should be first discussed with the HOD or principal. If unresolved, a written grievance can be submitted to the HR department. All grievances are addressed within 10 working days.",
         ["Staff complaint?", "Teacher grievance?", "Employee complaint?",
          "HR complaint?", "Staff problem?", "How to raise issue at school?"]),
    ],

    # ── HEALTH ───────────────────────────────────────────────────────────
    "Health": [
        ("Is there an eye testing camp in school?",
         "Yes, the school organizes a free eye testing camp every September in collaboration with an eye care NGO. Students who need glasses are referred to an empanelled optician at discounted rates.",
         ["Eye camp?", "Vision testing?", "Eye checkup?", "Free eye test?",
          "Eyesight check?", "Glasses for students?", "Eye care camp?"]),

        ("Is there a dental check-up in school?",
         "Yes, an annual dental awareness and check-up camp is held in August. A dentist visits the school and screens all students. Parents receive a dental report card.",
         ["Dental camp?", "Teeth check?", "Dental checkup in school?",
          "Dentist visit?", "Oral health check?", "Dental hygiene camp?"]),

        ("What is the allergy policy in school?",
         "Parents must inform the school nurse of any known allergies at the beginning of the year. An allergy action plan is filed for each student. Nut-free zones are maintained near food areas.",
         ["Allergy policy?", "Food allergy?", "Nut allergy?",
          "Is allergy managed in school?", "Child allergy?", "Allergy action plan?"]),

        ("Can students take medicines during school hours?",
         "Students must not self-medicate. Prescription medicines can be given by the school nurse with a written note from parents and the prescription. Medicines are stored in the medical room.",
         ["Medicines in school?", "Can nurse give medicine?", "Prescription medicine?",
          "Student medication?", "Medicine during school?", "Can child take tablet?"]),

        ("Does the school conduct mental health sessions?",
         "Yes, the school observes Mental Health Awareness Week every October. Class sessions on stress management, exam anxiety, and emotional health are conducted by the school counselor.",
         ["Mental health in school?", "Stress management?", "Exam anxiety?",
          "Emotional wellbeing?", "Mental health week?", "Counseling sessions?"]),

        ("Is yoga or meditation practiced in school?",
         "Yes, a 10-minute guided breathing and mindfulness exercise is part of the daily morning assembly. Dedicated Yoga sessions are held every Friday during PE periods.",
         ["Yoga in school?", "Meditation?", "Mindfulness?",
          "Breathing exercise?", "Friday yoga?", "Yoga classes?"]),

        ("Does the school maintain student health records?",
         "Yes, each student has a health card maintained by the school nurse. It records height, weight, blood group, allergies, immunization history, and annual medical check-up results.",
         ["Health record?", "Student medical file?", "Blood group record?",
          "Immunization record?", "Child health card?", "Medical history in school?"]),

        ("What is the Covid safety protocol?",
         "Symptomatic students must stay home. Sanitizers are placed at all entry and exit points. The medical room has an isolation area. A thermal scanner is used at the school gate.",
         ["Covid policy?", "Fever in school?", "Sanitizer in school?",
          "Corona safety?", "Health safety post covid?", "Covid isolation?"]),

        ("Does the school have a physical fitness program?",
         "Yes, the school conducts an annual Physical Fitness Test each October assessing speed, strength, and flexibility. Results are shared with parents and tracked over time.",
         ["Fitness test?", "Physical test in school?", "Sports fitness check?",
          "Annual fitness?", "PE assessment?", "Fitness program?"]),
    ],

    # ── EVENTS ───────────────────────────────────────────────────────────
    "Events": [
        ("Does the school celebrate Teachers' Day?",
         "Yes, Teachers' Day on September 5th is celebrated with cultural performances by students, a special assembly, and a token of appreciation for each teacher.",
         ["Teachers day celebration?", "September 5 event?", "How is teachers day celebrated?",
          "Teacher appreciation day?", "Is teachers day observed?"]),

        ("Does the school celebrate Children's Day?",
         "Yes, Children's Day on November 14th is celebrated with fun activities, games, a cultural program by teachers for students, and distribution of sweets.",
         ["Children's day event?", "November 14 celebration?", "Kids day?",
          "How is children's day celebrated?", "Bal diwas?"]),

        ("Does the school celebrate Environment Day?",
         "Yes, World Environment Day (June 5) is observed with tree-planting drives, poster competitions, eco-pledges, and a Green Campus awareness quiz.",
         ["Environment day?", "World environment day?", "Tree planting?",
          "Eco day?", "Earth day?", "Green day celebration?"]),

        ("Does the school observe Yoga Day?",
         "Yes, International Yoga Day on June 21st is celebrated with a school-wide yoga session led by the PE department. Students in all classes participate at the grounds.",
         ["Yoga day?", "June 21 event?", "International yoga day?",
          "Mass yoga session?", "Yoga celebration?"]),

        ("Is there a Talent Show in school?",
         "Yes, the school holds an annual 'Spark' Talent Show in November. Students perform dance, music, comedy, and magic acts. Judged by teachers and open to parent audience.",
         ["Talent show?", "Student performance?", "Cultural show?",
          "Spark event?", "Performance show?", "Is there a talent competition?"]),

        ("Does the school hold a Diwali celebration?",
         "Yes, the school holds a Diwali Mela two days before Diwali vacation. Students set up stalls, wear traditional attire, and participate in rangoli, lamp decoration, and folk performances.",
         ["Diwali mela?", "Diwali celebration in school?", "Festival mela?",
          "Traditional day?", "Cultural festival?", "Diwali event?"]),

        ("Does the school celebrate Christmas?",
         "Yes, the school celebrates Christmas with carol singing, a Christmas tree decoration competition, and Secret Santa gift exchange on December 24th before winter break.",
         ["Christmas in school?", "December 24 event?", "Christmas celebration?",
          "Carol singing?", "Santa gift exchange?", "Xmas celebration?"]),

        ("Are there any inter-school debate competitions?",
         "Yes, the school hosts an annual inter-school debate competition 'WordWars' inviting 15+ schools every August. Our school also sends students to external competitions throughout the year.",
         ["Debate competition?", "Inter school debate?", "WordWars?",
          "Debate event?", "School speeches?", "Debate tournament?"]),

        ("Is there a Winter Carnival in school?",
         "Yes, the school holds a Winter Carnival in December with food stalls, games, cultural performances, and a craft fair organized by students of Class 8-12.",
         ["Winter carnival?", "December event?", "School fair?",
          "Annual mela?", "Winter fest?", "Fun fair in school?"]),
    ],

    # ── PARENT PORTAL ─────────────────────────────────────────────────────
    "ParentPortal": [
        ("How do I reset my parent portal password?",
         "Click on 'Forgot Password' on the portal login page. Enter your registered email and a reset link will be sent. If the issue persists, call the IT helpdesk at it@school.com.",
         ["Forgot portal password?", "Reset password?", "Can't login to portal?",
          "Portal password reset?", "Login issue?", "Lost password?"]),

        ("Can I link multiple children to one parent account?",
         "Yes, if you have more than one child enrolled, they can all be linked to a single parent account. Contact the admin office to raise a linking request with both admission numbers.",
         ["Multiple children portal?", "Two children one account?", "Sibling accounts?",
          "Link kids to portal?", "Two students one login?", "Family account?"]),

        ("Can I view my child's timetable on the portal?",
         "Yes, the class timetable is available under 'Academics > Timetable' on the parent portal and mobile app. It is updated each term.",
         ["Timetable online?", "Class schedule on portal?", "View timetable?",
          "Check schedule online?", "Period timetable?", "Daily schedule?"]),

        ("Can I download the Transfer Certificate from the portal?",
         "No, the TC is a physical document issued by the school office. You must apply in person. A digital copy can be shared via email upon request after the original has been issued.",
         ["TC from portal?", "Download TC online?", "Online TC?",
          "Transfer certificate download?", "Is TC available digitally?"]),

        ("Is the school calendar available online?",
         "Yes, the full academic calendar — including holidays, exam dates, PTM dates, and event schedule — is available on the parent portal under 'Calendar' and on the school website.",
         ["School calendar online?", "Holiday list online?", "Academic calendar portal?",
          "Exam dates online?", "Event schedule?", "Year planner online?"]),

        ("Can I view my child's exam marks online?",
         "Yes, term exam mark sheets and periodic test scores are published on the parent portal under 'Results' within 2 weeks of the exam. Report cards are also downloadable.",
         ["Marks on portal?", "Check marks online?", "Result online?",
          "Exam score portal?", "Progress card?", "Mark sheet online?"]),

        ("Is the parent portal available 24/7?",
         "Yes, the portal is available 24/7 except during scheduled maintenance windows, usually Sunday 1:00 AM to 4:00 AM. Planned maintenance is communicated via SMS.",
         ["Portal always available?", "Portal downtime?", "Access portal anytime?",
          "Is portal 24 hours?", "Night portal access?"]),

        ("How do I submit a leave application online?",
         "Login to the parent portal, go to 'Leave Application', fill in the date range and reason, and submit. The class teacher will approve it. You'll receive a confirmation SMS.",
         ["Leave application online?", "Apply leave through portal?", "Online leave form?",
          "Absence application?", "Submit leave portal?", "Leave via app?"]),

        ("How do I opt in for SMS alerts from school?",
         "SMS alerts are enabled by default. If you are not receiving them, go to 'Notification Settings' on the portal and enable SMS. Ensure your registered mobile number is correct.",
         ["SMS alerts?", "Enable SMS?", "How to get text from school?",
          "SMS notification?", "Text message from school?", "Mobile alerts?"]),

        ("Are event photos shared on the portal?",
         "Yes, a photo gallery of school events is uploaded to the parent portal and the school website within 3 days of each event. Parents can download photos of their children.",
         ["Event photos?", "School photo gallery?", "Pictures from events?",
          "Photo download?", "Can I see school event photos?", "Gallery on portal?"]),
    ],

    # ── COUNSELING ────────────────────────────────────────────────────────
    "Counseling": [
        ("Is there a Science Club?",
         "Yes, the Science Club meets every Wednesday after school. Students conduct experiments, participate in science fairs, and build models. It is open to Class 6-12 students.",
         ["Science club?", "Join science club?", "Lab activities club?",
          "Science experiments?", "Sci club?", "STEM club?"]),

        ("Is there a Math Club?",
         "Yes, the Math Club holds weekly problem-solving sessions every Thursday. It helps students prepare for Math Olympiads and competitive exams. Open to Class 5-12.",
         ["Math club?", "Maths activities?", "Math olympiad prep?",
          "Numbers club?", "Mathematics group?", "Math competition prep?"]),

        ("Is there an Eco/Environment Club?",
         "Yes, the Eco Club runs environmental awareness drives, organizes the school garden, leads the No Plastic campaign, and participates in World Environment Day events.",
         ["Eco club?", "Environment club?", "Green club?", "Nature club?",
          "Environmental activities?", "Save earth club?"]),

        ("Is there an NSS unit?",
         "Yes, the school has a registered NSS (National Service Scheme) unit for Class 11-12. Activities include community service, blood donation camps, and rural awareness drives.",
         ["NSS in school?", "National Service Scheme?", "Community service program?",
          "NSS enrollment?", "Social work program?", "Volunteer program?"]),

        ("Are Scouts and Guides available in school?",
         "Yes, the school has both Scouts (for boys) and Guides (for girls) units, open to Class 6-10 students. Meetings are held every Saturday. National level participation is possible.",
         ["Scouts in school?", "Girl guides?", "Boy scouts?",
          "Scouting activity?", "How to join scouts?", "Scouts and guides?"]),

        ("Is there a Robotics Club?",
         "Yes, the Robotics Club meets every Tuesday. Students build and program robots using Arduino and Lego Mindstorms kits. The club participates in national robotics competitions.",
         ["Robotics club?", "Robot building?", "Arduino in school?",
          "STEM robotics?", "Coding robots?", "Robotics competition?"]),

        ("Is there a Reading/Literature Club?",
         "Yes, the Reading Club meets fortnightly in the library. Members read and discuss books, write reviews, and organize the annual Book Fair in February.",
         ["Reading club?", "Book club?", "Literature club?",
          "Library club?", "Book discussion?", "Reading group?"]),

        ("Does the school have a school band?",
         "Yes, the school has a marching band and a cultural orchestra. Students can audition in June. The band performs at Annual Day, Republic Day, and Independence Day.",
         ["School band?", "Marching band?", "Orchestra?",
          "Music performance?", "Band audition?", "School music group?"]),

        ("Are career counseling sessions held?",
         "Yes, career counseling sessions are held every month for Class 10, 11, and 12 students. Guest speakers from various professions are invited. Session schedule is on the portal.",
         ["Career session?", "Career talk?", "Profession guidance?",
          "Career planning?", "Future career advice?", "What career to choose?"]),
    ],

    # ── SAFETY ────────────────────────────────────────────────────────────
    "Safety": [
        ("Are earthquake/disaster drills conducted?",
         "Yes, earthquake and fire evacuation drills are conducted twice a year. Students are trained to follow the 'Drop, Cover, Hold' protocol. Exit routes are clearly marked.",
         ["Earthquake drill?", "Disaster drill?", "Evacuation drill?",
          "Emergency practice?", "Safety drill?", "Natural disaster protocol?"]),

        ("Is first aid training given to students?",
         "Yes, Class 9 and 10 students receive 3-hour first aid training sessions by certified instructors organized in collaboration with the Red Cross. This includes CPR and bandaging.",
         ["First aid training?", "CPR training?", "Red Cross training?",
          "Emergency first aid?", "Basic life support?", "First aid for students?"]),

        ("Is there a school safety committee?",
         "Yes, the school has a Safety Committee comprising the principal, two teachers, two parent representatives, and two senior students. It meets quarterly and reviews safety incidents.",
         ["Safety committee?", "School safety team?", "Who manages safety?",
          "Safety review?", "School safety board?", "Safety governance?"]),

        ("What safety measures are in place on school buses?",
         "School buses are fitted with GPS tracking, speed limiters (max 40 km/h), CCTV, and a lady attendant. Emergency contact details are displayed inside the bus. Fire extinguisher on board.",
         ["Bus safety?", "GPS on bus?", "Safe school bus?", "Lady attendant in bus?",
          "Speed limiter?", "School bus CCTV?"]),

        ("Is there a cyber safety program?",
         "Yes, the school conducts Cyber Safety workshops for students every January. Topics include online privacy, cyberbullying, screen time management, and safe social media use.",
         ["Cyber safety?", "Internet safety?", "Online safety?",
          "Digital safety?", "Cyberbullying awareness?", "Safe internet use?"]),

        ("Is there a security guard at the gate?",
         "Yes, the main gate is staffed by two security guards 24/7. During school hours, an additional guard manages visitor entry and exit. Visitor IDs are scanned at entry.",
         ["Guard at gate?", "Security at school?", "Is school gated?",
          "Watchman?", "Gate security?", "Security personnel?"]),

        ("Does the school have a boundary wall?",
         "Yes, the school campus is enclosed by a 10-foot compound wall with CCTV cameras mounted at regular intervals. Entry and exit is only through the main gate.",
         ["Boundary wall?", "Compound wall?", "Is school enclosed?",
          "School campus security?", "Fencing?", "Campus boundary?"]),

        ("What happens if an unauthorized person tries to pick up a student?",
         "No student is released to an unauthorized person. The school only releases students to verified individuals listed in the student's guardian record. Police are alerted for suspicious persons.",
         ["Stranger pickup?", "Unauthorized person?", "Who can take child from school?",
          "Child protection?", "Kidnapping prevention?", "Unauthorized pickup?"]),

        ("Is there night security at school?",
         "Yes, two security guards are on duty through the night (2:30 PM to 8:00 AM) patrolling the campus, checking CCTV feeds, and securing labs and the server room.",
         ["Night security?", "After hours security?", "Night guard?",
          "School at night?", "Evening security?", "24 hour security?"]),

        ("Does the school have a student ID card policy?",
         "Yes, every student is issued a photo ID card at the start of the year. It must be worn as a lanyard during school hours. Lost cards are replaced for Rs.100.",
         ["Student ID card?", "ID card policy?", "School ID?",
          "Identity card?", "Lost ID card?", "ID card replacement?"]),
    ],
}
