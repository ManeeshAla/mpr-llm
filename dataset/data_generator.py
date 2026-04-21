import json
import random
import os

os.makedirs(os.path.dirname(__file__), exist_ok=True)
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "school_business_data.jsonl")

KNOWLEDGE_BASE = {

    # ── GENERAL ──────────────────────────────────────────────────────────
    "General": [
        (
            "When does the new academic year start?",
            "The new academic year begins on June 10th every year. Students are expected to report on the first day with all required stationery and books.",
            [
                "When does school start?", "Academic year start date?", "When will school reopen?",
                "When does the session begin?", "School start date?", "When does new session start?",
                "What is the starting date of the academic year?", "When does school open for new session?",
                "Session start date?", "When do classes start?", "School reopening date?",
                "When does the new term begin?", "First day of school?", "Academic session start?"
            ]
        ),
        (
            "What are the school timings?",
            "School timings are from 8:00 AM to 2:00 PM, Monday to Saturday. Students are advised to arrive by 7:50 AM to avoid being marked late.",
            [
                "What time does school start and end?", "School hours?", "When does school open?",
                "Till what time is school?", "School timing?", "What are the timings?",
                "School schedule timing?", "What time school starts?", "What time does school end?",
                "Morning school timing?", "Tell me the school timings", "School opening time?",
                "School closing time?", "At what time school opens?", "Daily school hours?"
            ]
        ),
        (
            "Is school open tomorrow?",
            "School closure announcements are made through the official school app and SMS alerts. Please check the notice board or contact the school office at +91-XXXXXXXXXX for tomorrow's schedule.",
            [
                "Will there be school tomorrow?", "Is tomorrow a holiday?", "School status tomorrow?",
                "Is school closed tomorrow?", "Does school run tomorrow?", "School tomorrow or not?",
                "Is there school tomorrow?", "Holiday tomorrow?", "Tomorrow school open or closed?",
                "School holiday tomorrow?", "Any holiday tomorrow?"
            ]
        ),
        (
            "How can I get school notifications?",
            "School updates, circulars, and holiday notices are shared via the school's official mobile app, SMS, and WhatsApp group. Please register your mobile number with the admin office.",
            [
                "How to get school updates?", "Where are notices posted?", "How to receive circulars?",
                "School notification system?", "Where to check school announcements?",
                "How do I get updates from school?", "School communication channel?",
                "How to register for alerts?", "School app notification?", "WhatsApp group for school?"
            ]
        ),
        (
            "When is the Parent-Teacher Meeting?",
            "PTM (Parent-Teacher Meeting) is held quarterly, typically after each term exam. Dates are communicated two weeks in advance via the school diary and the official app.",
            [
                "When is PTM?", "Next parent teacher meeting date?", "When can I meet my child's teacher?",
                "PTM schedule?", "Parent teacher meeting schedule?", "When is the next PTM?",
                "PTM dates?", "When do parents meet teachers?", "Parent meeting date?",
                "Teacher parent meeting?", "PTM timing?", "How often is PTM held?"
            ]
        ),
        (
            "What is the school's holiday list?",
            "The annual school holiday calendar is distributed at the beginning of the academic year. It includes national holidays, regional festivals like Diwali, Holi, Dussehra, and school-declared breaks.",
            [
                "Give me the holiday list", "When are school holidays?", "List of holidays this year?",
                "Holiday calendar?", "Annual holiday list?", "Which days are school holidays?",
                "School holiday schedule?", "Festival holidays in school?", "Holidays this academic year?",
                "School closed on which days?", "How many holidays are there?", "Holiday dates?"
            ]
        ),
        (
            "Is there school on Saturday?",
            "Yes, school is open on Saturdays from 8:00 AM to 12:00 PM for regular classes. The second and fourth Saturdays of each month may be declared holidays based on the academic calendar.",
            [
                "Does school run on Saturdays?", "Saturday school timings?", "Is Saturday a working day?",
                "School on Saturday?", "Saturday classes?", "Is school open Saturday?",
                "Saturday school open or closed?", "Do we have school on Saturday?",
                "Saturday school hours?", "Second Saturday holiday?"
            ]
        ),
    ],

    # ── FEES ─────────────────────────────────────────────────────────────
    "Fees": [
        (
            "What is the annual fee for Class 1?",
            "The annual tuition fee for Class 1 is Rs.35,000. This includes tuition, smart class usage, and basic stationery kit. Uniforms and books are charged separately.",
            [
                "Fee for Class 1?", "How much is Class 1 fee?", "1st standard annual fee?",
                "First class fee?", "Class 1 fees?", "What is the fee for 1st class?",
                "Class one fee?", "Fee structure for Class 1?", "How much for Class 1?",
                "1st class annual charges?", "Grade 1 fee?", "Kindergarten to Class 1 fee?"
            ]
        ),
        (
            "What is the annual fee for Class 5?",
            "The annual tuition fee for Class 5 is Rs.42,000. This covers tuition, lab access, and library charges. Books and uniforms are purchased separately.",
            [
                "Fee for Class 5?", "How much does Class 5 cost?", "5th standard fee?",
                "Fee for 5th class?", "Class 5 fees?", "What is the fee for 5th standard?",
                "How much is 5th class fee?", "Annual fee for 5th grade?",
                "5th class annual charges?", "Class five fee?", "Grade 5 fee?"
            ]
        ),
        (
            "What is the annual fee for Class 8?",
            "The annual tuition fee for Class 8 is Rs.50,000. Lab fees, library, and co-curricular activities are included. Books and uniforms are extra.",
            [
                "What is the fee for Class 8?", "8th standard fee?", "Fee for eighth grade?",
                "Class 8 annual charges?", "Class 8 fees?", "Fee for 8th class?",
                "How much is Class 8?", "Annual fee for Class 8?", "8th class fee?",
                "What is 8th standard fee?", "Class eight fee?", "Fees for Class 8?"
            ]
        ),
        (
            "What is the annual fee for Class 10?",
            "The annual fee for Class 10 is Rs.58,000. This includes board exam registration charges, practical lab fees, and pre-board examination fees.",
            [
                "Class 10 fee?", "10th standard annual fee?", "How much is Class 10?",
                "Board class fee?", "Class 10 fees?", "Fee for 10th standard?",
                "10th class charges?", "Annual fee for Class 10?", "Fees for board class?",
                "CBSE Class 10 fee?", "Class ten fee?", "SSC fee?", "Matriculation fee?"
            ]
        ),
        (
            "What is the annual fee for Class 12?",
            "The annual fee for Class 12 is Rs.62,000. It includes CBSE board registration, practicals, and career counselling sessions.",
            [
                "Class 12 fee?", "12th standard fee?", "Senior secondary fee?",
                "Fee for Class 12?", "12th class charges?", "Annual fee for Class 12?",
                "HSC fee?", "Class 12 fees?", "Fee for 12th?", "How much for Class 12?",
                "Board class 12 fee?", "Higher secondary fee?", "Plus two fee?"
            ]
        ),
        (
            "Can I pay fees in installments?",
            "Yes, the school allows fee payment in three installments: the first in April, the second in August, and the third in December. An installment form must be submitted to the accounts office.",
            [
                "Is installment available for fees?", "Can fees be paid in parts?",
                "EMI for school fee?", "Fee in 3 installments?", "Installment option for fees?",
                "Can I pay in installments?", "Fee payment in parts?", "Is installment facility available?",
                "Pay fee in 3 parts?", "Fee installment option?", "Quarterly fee payment?",
                "Can I split the fee?", "Installment plan for fees?", "Pay fees in EMI?"
            ]
        ),
        (
            "What happens if fees are paid late?",
            "A late fee of Rs.100 per day is charged if payment is not made by the due date. After 30 days of non-payment, the student's name may be struck off the rolls.",
            [
                "What is the late fee penalty?", "What happens if fees are late?",
                "Late payment charges?", "Penalty for delayed fee?", "Late fee fine?",
                "What if I miss fee deadline?", "Overdue fee charges?", "Late fee policy?",
                "Fee due date penalty?", "What is late fee?", "Consequences of late fee payment?",
                "Fine for not paying fee on time?", "Penalty for late tuition?"
            ]
        ),
        (
            "What are the payment modes available?",
            "Fees can be paid online via the school portal using UPI, Net Banking, or Debit/Credit card. Cash and cheque payments are accepted at the accounts office between 9:00 AM and 1:00 PM.",
            [
                "How can I pay fees?", "Payment methods accepted?", "Online fee payment?",
                "Can I pay by UPI?", "Fee payment options?", "How to pay school fees?",
                "Payment modes for fees?", "Can I pay online?", "NEFT fee payment?",
                "Cheque payment for fees?", "Cash payment accepted?", "Online fee portal?"
            ]
        ),
        (
            "Is there a fee concession or scholarship?",
            "Yes, the school offers fee concessions for students who score above 90% in the annual exam and for economically weaker sections under the RTE Act. Apply at the admin office before March 31st.",
            [
                "Scholarship available?", "Fee concession?", "Reduction in fees?", "RTE fee waiver?",
                "Do you offer scholarship?", "Fee waiver available?", "Merit scholarship?",
                "EWS fee concession?", "Discount on fees?", "Fee reduction for merit students?",
                "Is there any free admission?", "Scholarship for good students?",
                "How to get fee concession?", "Scholarship criteria?"
            ]
        ),
        (
            "What is the admission fee?",
            "The one-time non-refundable admission registration fee is Rs.1,500. This is separate from the annual tuition fee and covers administrative and documentation charges.",
            [
                "How much is the registration fee?", "Admission form fee?", "Enrolment fee?",
                "One-time admission charges?", "Registration charges?", "Form fee?",
                "How much to register?", "Admission registration cost?", "Application fee?",
                "Form filling charges?", "How much is admission fee?", "Registration form cost?"
            ]
        ),
        (
            "Is the security deposit refundable?",
            "Yes, a refundable caution deposit of Rs.5,000 is collected at the time of admission. It is returned after the student completes their schooling or leaves the school, provided all dues are cleared.",
            [
                "Is security deposit returned?", "Caution money refund?", "Is caution deposit refundable?",
                "Security deposit policy?", "Is deposit refunded?", "Caution deposit amount?",
                "Refund of security deposit?", "Will I get back the deposit?", "Security money returned?"
            ]
        ),
    ],

    # ── ADMISSIONS ───────────────────────────────────────────────────────
    "Admissions": [
        (
            "How can I apply for admission?",
            "Admissions can be done online through the school's official website or in person at the school office. The process involves: (1) Collect or download the application form, (2) Submit it with required documents like birth certificate and previous report card, (3) Appear for the interaction or entrance test, and (4) Pay the admission fee of Rs.1,500 upon selection.",
            [
                "Where to apply for admission?", "Admission process?", "How to enrol my child?",
                "Online admission?", "What is the admission process?", "How does admission work?",
                "Tell me about the admission process", "Steps for admission",
                "How to take admission", "Admission procedure", "Process of admission",
                "How do I get my child admitted", "What is the procedure for admission",
                "Explain the admission process", "How to join the school",
                "Enrollment procedure", "How to get admission in this school",
                "Guide me through admission process", "Admission steps?", "How admission works?",
                "School admission guide?", "How to seek admission?", "Admission requirements?",
                "How to fill admission form?", "Admission application process?"
            ]
        ),
        (
            "When do admissions open?",
            "Admissions open every year in January for the upcoming academic session starting in June. Early applications are encouraged as seats are limited.",
            [
                "Admission start date?", "When can I apply for admission?", "Enrollment date?",
                "When does admission begin?", "When do admissions start?", "Admission opening date?",
                "When to apply?", "Application start date?", "When is admission form available?",
                "Admission season?", "When does registration begin?", "Form availability date?"
            ]
        ),
        (
            "What documents are required for admission?",
            "Required documents include: Birth certificate, last year's report card or Transfer Certificate (TC), Aadhaar card of parent and child, passport-size photographs (4), and caste/income certificate if applying under RTE.",
            [
                "Documents needed for admission?", "What papers to submit?",
                "List of required documents?", "What do I need for enrolment?",
                "Documents for admission?", "Admission documents list?",
                "What certificates are needed?", "Papers required for admission?",
                "Documents to bring for admission?", "What proof is needed?",
                "Admission form documents?", "Required papers for joining school?",
                "What should I submit for admission?", "Documents checklist for admission?"
            ]
        ),
        (
            "Is there an entrance test for admission?",
            "Students seeking admission to Class 1 through Class 5 undergo an oral interaction. For Class 6 and above, a written test in English, Mathematics, and General Knowledge is conducted.",
            [
                "Is there an entrance exam?", "Admission test details?", "Written test for admission?",
                "Admission exam?", "Is there a test for joining?", "Entrance exam details?",
                "Do students have to give a test?", "Selection test for admission?",
                "How is admission test conducted?", "Test subjects for admission?",
                "Admission criteria test?", "Is there an interview for admission?"
            ]
        ),
        (
            "Is admission available mid-year?",
            "Mid-year admissions are considered only in special circumstances such as relocation. A Transfer Certificate from the previous school is mandatory. Contact the admin office for availability.",
            [
                "Can I get admission in the middle of year?", "Mid-session enrolment?",
                "Transfer admission?", "Admission in between session?", "Late admission possible?",
                "January admission available?", "Mid-year transfer admission?",
                "Can I join school in October?", "Admission after June?"
            ]
        ),
        (
            "What is the age criteria for Class 1?",
            "A child must be at least 6 years old as of June 1st of the admission year to be eligible for Class 1 admission, as per CBSE guidelines.",
            [
                "Age limit for Class 1?", "Minimum age for first standard?",
                "How old should my child be for Class 1?", "Age requirement for Class 1?",
                "Eligible age for Class 1?", "What age for Class 1 admission?",
                "Age criteria for admission?", "Minimum age to join school?",
                "Age for LKG admission?", "Age limit for nursery?"
            ]
        ),
        (
            "Are seats available under RTE?",
            "Yes, 25% of seats in Class 1 are reserved under the Right to Education Act for economically weaker section students. Apply with income proof before February 28th.",
            [
                "RTE seats available?", "Free seats under RTE?", "How to apply through RTE?",
                "EWS admission?", "RTE admission process?", "Free admission under RTE?",
                "Right to Education admission?", "Seats for poor students?",
                "RTE quota?", "Government free admission?", "25% RTE seats?"
            ]
        ),
    ],

    # ── ACADEMIC ─────────────────────────────────────────────────────────
    "Academic": [
        (
            "What subjects are taught in Class 10?",
            "Class 10 covers: Mathematics, Science, Social Science, English, Hindi, and one optional subject. Practical examinations are conducted for Science.",
            [
                "Class 10 subjects?", "Which subjects in 10th standard?", "CBSE Class 10 syllabus?",
                "What do 10th students study?", "Subjects for Class 10?", "10th class subjects?",
                "Syllabus for Class 10?", "What is taught in 10th?", "Core subjects in Class 10?",
                "Class 10 curriculum?", "10th subject list?", "Board exam subjects?"
            ]
        ),
        (
            "When are the final exams scheduled?",
            "Annual final examinations for Classes 1 to 9 are held in March. CBSE board examinations for Class 10 and Class 12 begin in February as per the CBSE schedule.",
            [
                "When are exams?", "Exam date?", "Annual exam schedule?", "When do final exams start?",
                "Exam timetable?", "When is the annual exam?", "Final exam date?",
                "Board exam date?", "Exam schedule?", "When are tests?", "Test dates?",
                "End of year exam?", "When do exams begin?", "Examination schedule?"
            ]
        ),
        (
            "How can I access homework?",
            "Homework and class assignments are posted on the school's student portal. Log in with your student ID and password. You can also check the student diary for daily classwork.",
            [
                "Where to find homework?", "How to get homework?", "Student portal for assignments?",
                "Online homework access?", "Where is homework posted?", "How to check homework?",
                "Homework portal?", "Assignment access?", "Student login for homework?",
                "How to see today's homework?", "School app for homework?"
            ]
        ),
        (
            "What is the grading system?",
            "The school follows the CBSE grading system: A1 (91-100), A2 (81-90), B1 (71-80), B2 (61-70), C1 (51-60), C2 (41-50), D (33-40), and E below 33.",
            [
                "How are students graded?", "CBSE grading scale?", "What is A1 grade?",
                "Marks to grade conversion?", "Grading system?", "How is grading done?",
                "Grade criteria?", "Marking scheme?", "Grade A1 marks?", "Pass marks?",
                "What grade is 75%?", "CGPA system?", "Grade calculation?"
            ]
        ),
        (
            "When are results declared?",
            "Results for term exams are declared within two weeks of the last exam. Annual results are published in April. Students can check results on the school portal or collect physical mark sheets from the office.",
            [
                "When will results come?", "Result announcement date?", "Where to check results?",
                "Result date?", "When is result out?", "Exam result date?", "Mark sheet date?",
                "When will I get my result?", "Result portal?", "How to check result?",
                "Result day?", "Report card date?"
            ]
        ),
        (
            "What co-curricular activities are available?",
            "The school offers cricket, football, chess, dance, music, art and craft, debate club, science club, and NCC. Students are encouraged to participate in at least one activity.",
            [
                "Extra-curricular activities?", "Sports available in school?", "Non-academic activities?",
                "Clubs in school?", "What activities does school offer?", "Sports and hobbies?",
                "After school activities?", "School clubs?", "Art and music in school?",
                "NCC in school?", "Dance classes?", "Sports events?"
            ]
        ),
        (
            "What board does the school follow?",
            "The school is affiliated with the Central Board of Secondary Education (CBSE), New Delhi. Our affiliation number is XXXXXXX.",
            [
                "Is the school CBSE?", "Which board?", "CBSE or ICSE?", "School board affiliation?",
                "What board is this school?", "Is it CBSE school?", "School affiliation?",
                "Which curriculum?", "Board of education?", "CBSE affiliated school?"
            ]
        ),
        (
            "Is there a provision for remedial classes?",
            "Yes, remedial and extra support classes are conducted after regular school hours for students who need additional help. These are free of cost and coordinated by the class teacher.",
            [
                "Extra classes for weak students?", "Remedial class available?", "Support classes?",
                "Classes for slow learners?", "Extra help classes?", "Tuition by school?",
                "After school classes?", "Free coaching in school?", "Remedial support?",
                "Special classes for weak students?"
            ]
        ),
    ],

    # ── FACILITIES ───────────────────────────────────────────────────────
    "Facilities": [
        (
            "Is transport available?",
            "Yes, the school provides bus transport covering major routes across the city and nearby localities. A route map is available at the admin office and on the school website.",
            [
                "Does school have buses?", "Is school bus available?", "Transport facility?",
                "Can my child take the school bus?", "Bus service?", "School transport?",
                "Is bus available?", "Does school provide transport?", "School van available?",
                "Pick up and drop service?", "School bus routes?", "Is there a bus service?"
            ]
        ),
        (
            "What is the transport fee?",
            "Transport fees vary by distance: Rs.10,000 per year for routes within 5 km and Rs.20,000 per year for routes between 5 to 15 km. This is payable annually or in two installments.",
            [
                "Bus fee?", "How much is transport?", "School bus charges?",
                "Cost of school transport?", "Transport charges?", "Bus fare?",
                "How much for school bus?", "Transport fee per month?", "Bus fee structure?",
                "Annual transport cost?", "School van charges?"
            ]
        ),
        (
            "Does the school provide lunch?",
            "Yes, a nutritious optional meal plan is available through the school canteen. A monthly meal subscription costs Rs.1,200. Students can also bring home-cooked lunch.",
            [
                "Is mid-day meal available?", "Canteen facility?", "School lunch service?",
                "Does school serve food?", "Meal plan available?", "Food in school?",
                "School canteen?", "Is lunch provided?", "Tiffin service?",
                "Mid-day meal scheme?", "Can students eat in school?"
            ]
        ),
        (
            "Is there a library?",
            "Yes, the school has a well-stocked library with over 10,000 books, including NCERT textbooks, reference books, encyclopaedias, and children's literature. Library cards are issued to all students.",
            [
                "Does school have a library?", "Library facility?", "Can students borrow books?",
                "Library available?", "School library books?", "Are there books to borrow?",
                "Library hours?", "Library card?", "Book borrowing facility?"
            ]
        ),
        (
            "Is there a computer lab?",
            "Yes, the school has a modern computer lab with 60 computers and high-speed internet access. Computer Science is a compulsory subject from Class 6 onwards.",
            [
                "Computer lab available?", "IT lab in school?", "Does school have computers?",
                "Computer room?", "Is there internet?", "Computer class?",
                "IT facility?", "Programming lab?", "Computer education?"
            ]
        ),
        (
            "What sports facilities are available?",
            "The school has a cricket ground, basketball court, volleyball court, and an indoor badminton court. Physical Education is a part of the daily schedule.",
            [
                "Sports grounds?", "Playground available?", "What sports can students play?",
                "Sports infrastructure?", "Cricket ground?", "Basketball court?",
                "Indoor sports?", "PE facilities?", "Playing field?", "Sports complex?"
            ]
        ),
        (
            "Is there a smart classroom?",
            "Yes, all classrooms are equipped with interactive smart boards and projectors connected to the DIKSHA and school's own digital content portal.",
            [
                "Smart board available?", "Digital classroom?", "Does school have projectors?",
                "Smart class?", "Interactive board?", "E-learning in school?",
                "Digital teaching?", "Projector in class?", "Smart teaching tools?"
            ]
        ),
        (
            "Is there CCTV surveillance?",
            "Yes, the entire school campus, including classrooms, corridors, and the main gate, is under 24/7 CCTV surveillance for student safety.",
            [
                "Is the school safe?", "CCTV in school?", "Security cameras?",
                "Campus security?", "Surveillance cameras?", "Is school under CCTV?",
                "Safety measures?", "School security?", "Camera monitoring?"
            ]
        ),
    ],

    # ── STAFF ────────────────────────────────────────────────────────────
    "Staff": [
        (
            "How can I contact the school office?",
            "You can reach the school office at +91-XXXXXXXXXX or email us at info@school.com. Office hours are Monday to Saturday, 8:00 AM to 3:00 PM.",
            [
                "School phone number?", "Contact school?", "Office email?", "How to call school?",
                "School contact details?", "Office number?", "School email id?",
                "How to reach school?", "School address?", "Contact information?",
                "How do I contact school?", "Admin office number?", "School helpline?"
            ]
        ),
        (
            "Who is the principal?",
            "The Principal of the school is Mrs. Sharma. She holds a M.Ed. degree and has over 20 years of experience in education. You can schedule an appointment through the admin office.",
            [
                "Principal name?", "Who is the head of school?", "Meet the principal?",
                "School principal?", "Name of principal?", "Who runs the school?",
                "Headmaster name?", "Principal contact?", "Who is school incharge?",
                "Head teacher name?", "Principal details?"
            ]
        ),
        (
            "How do I contact my child's class teacher?",
            "Class teacher contact details are shared at the start of the academic year. You may also contact them via the school app's messaging feature or request a meeting through the admin desk.",
            [
                "How to reach class teacher?", "Class teacher phone number?", "Contact teacher?",
                "Teacher contact?", "How to speak to teacher?", "Teacher's number?",
                "Reach out to teacher?", "Teacher meeting?", "How to talk to class teacher?"
            ]
        ),
        (
            "Who do I contact for fee-related issues?",
            "For all fee-related queries, contact the Accounts Office directly at accounts@school.com or visit Room 3 on the ground floor between 9:00 AM and 1:00 PM on working days.",
            [
                "Fee department contact?", "Accounts office?", "Who handles fees?",
                "Fee query contact?", "Where to pay fees?", "Fee office?",
                "Billing office contact?", "Accounts department?", "Fee complaint?",
                "Fee correction request?", "Who to ask about fees?"
            ]
        ),
        (
            "How do I report an issue with facilities?",
            "Facility-related complaints can be submitted through the school portal under Support and Grievances or reported directly to the school office. All complaints are addressed within 48 working hours.",
            [
                "Report a problem?", "Complaint for facilities?", "Who to contact for maintenance?",
                "Grievance portal?", "How to complain?", "School complaint process?",
                "Report broken equipment?", "Maintenance request?", "Grievance redressal?"
            ]
        ),
    ],

    # ── POLICIES ─────────────────────────────────────────────────────────
    "Policies": [
        (
            "What is the attendance requirement?",
            "As per CBSE norms, students must maintain a minimum of 75% attendance to be eligible for the annual examinations. Students with less than 75% may be detained.",
            [
                "Minimum attendance needed?", "Attendance policy?", "How many days can I miss school?",
                "75% attendance rule?", "Attendance requirement?", "What is the attendance rule?",
                "Minimum attendance percentage?", "Attendance for exams?", "Can I miss school?",
                "Attendance criteria?", "Mandatory attendance?", "Attendance shortfall consequences?"
            ]
        ),
        (
            "What is the uniform policy?",
            "Students must wear the prescribed school uniform every day. Monday to Thursday: white shirt, navy blue trousers or skirt and school tie. Friday: House-colour PT uniform.",
            [
                "Dress code?", "What uniform should students wear?", "School uniform details?",
                "PT dress policy?", "Uniform rules?", "What clothes to wear?",
                "School dress?", "Uniform color?", "What is the school uniform?",
                "Uniform day wise?", "Friday uniform?", "Sports uniform?"
            ]
        ),
        (
            "What is the mobile phone policy?",
            "Mobile phones are strictly prohibited inside the school premises for students. If a student is found with a phone, it will be confiscated and returned only to parents after a formal meeting.",
            [
                "Can students bring phones?", "Mobile phone rule?", "Phone policy in school?",
                "Cell phone allowed?", "Is phone allowed?", "Mobile in school?",
                "Phone confiscation?", "Can I carry phone to school?", "Phone rules?"
            ]
        ),
        (
            "What is the leave application procedure?",
            "For planned leave, submit an application in the school diary signed by a parent at least one day in advance. For medical leave, a doctor's certificate must be submitted upon return.",
            [
                "How to apply for leave?", "Leave application process?", "Absence procedure?",
                "How to take leave?", "Leave letter format?", "Student leave rules?",
                "Inform school about absence?", "Leave application?", "Sick leave process?"
            ]
        ),
        (
            "What is the homework submission policy?",
            "Homework must be submitted on the date specified by the teacher. Late submissions without prior approval will result in a remark in the student diary and may affect the term grade.",
            [
                "Homework rules?", "Can homework be submitted late?", "Assignment submission policy?",
                "Late homework?", "Homework deadline?", "When to submit homework?",
                "Homework submission rules?", "Penalty for late homework?"
            ]
        ),
        (
            "What is the policy for exam re-tests?",
            "Students who score below 33% in any subject in unit tests are given one re-test opportunity. Re-tests are conducted two weeks after the original exam. For board exams, CBSE compartment exam rules apply.",
            [
                "Re-test available?", "Exam re-attempt policy?", "What if I fail a test?",
                "Compartment exam?", "Remedial exam?", "Second chance in exam?",
                "Retest policy?", "Fail in test?", "Unit test retest?"
            ]
        ),
        (
            "What is the anti-bullying policy?",
            "The school has a zero-tolerance policy for bullying, ragging, or discrimination. Any student found guilty of bullying will face disciplinary action including suspension.",
            [
                "Bullying rules?", "Is ragging allowed?", "Anti-bullying?", "What to do if bullied?",
                "Bullying policy?", "Ragging policy?", "Discipline for bullying?",
                "What if my child is bullied?", "Zero tolerance policy?"
            ]
        ),
        (
            "What is the discipline policy?",
            "Students are expected to maintain respectful behaviour. Repeated misconduct is addressed through: verbal warning, parent meeting, and suspension.",
            [
                "Discipline rules?", "What happens if students misbehave?", "Code of conduct?",
                "Student behaviour policy?", "Misconduct policy?", "Punishment for misbehaviour?",
                "What if student breaks rules?", "Disciplinary action?", "Suspension policy?"
            ]
        ),
    ],

    # ── HR ───────────────────────────────────────────────────────────────
    "HR": [
        (
            "How many casual leaves do PRT teachers get?",
            "PRT (Primary Teachers) are granted 12 Casual Leaves per academic year. Earned Leaves are calculated at 1 per month and can be accumulated up to a maximum of 30 days.",
            [
                "Teacher leave policy?", "How many CLs for primary teachers?", "PRT casual leave?",
                "Teacher CL?", "Leave for teachers?", "How many days leave for teachers?",
                "Teacher leave entitlement?", "Staff leave policy?", "CL for PRT?"
            ]
        ),
        (
            "When are staff salaries credited?",
            "Staff salaries are disbursed on the last working day of every month directly to their salary accounts via NEFT. Payslips are available on the staff portal.",
            [
                "Payday for staff?", "When is the salary credited?", "Salary date for teachers?",
                "When do teachers get paid?", "Staff payment date?", "Salary disbursement date?",
                "When is payroll processed?", "Teacher salary date?", "NEFT salary date?"
            ]
        ),
        (
            "What is the maternity leave policy?",
            "Female staff are entitled to 26 weeks of paid maternity leave as per the Maternity Benefit Act. An application must be submitted at least 60 days before the expected date.",
            [
                "Maternity leave for teachers?", "How many days maternity leave?",
                "Paid maternity leave?", "Maternity benefit?", "Maternity policy?",
                "Pregnancy leave?", "Leave for new mother?", "Maternity leave duration?"
            ]
        ),
        (
            "What is the protocol for summer vacation for non-teaching staff?",
            "Non-teaching staff including peons, lab assistants, and administrative staff operate on a rotational duty schedule during the May-June summer vacation.",
            [
                "Summer holiday for non-teaching staff?", "Do peons get summer vacation?",
                "Admin staff during summer break?", "Non-teaching staff leave?",
                "Office staff summer schedule?", "Support staff summer duty?"
            ]
        ),
        (
            "How do I apply for earned leave?",
            "Earned leave applications must be submitted to the principal's office at least 3 working days in advance through the school's leave management portal or in hard copy via the admin desk.",
            [
                "How to apply for EL?", "Earned leave process?", "EL application?",
                "Leave management?", "How to submit leave application?", "Leave approval process?",
                "Apply for leave?", "Staff leave application?"
            ]
        ),
    ],

    # ── HEALTH & MEDICAL ─────────────────────────────────────────────────
    "Health": [
        (
            "Is there a school nurse or medical room?",
            "Yes, the school has a fully equipped medical room staffed by a trained nurse from 8:00 AM to 2:00 PM on all working days. First aid is available for minor injuries and illnesses.",
            [
                "Medical room in school?", "Is nurse available?", "First aid facility?",
                "School health room?", "Does school have a doctor?", "Medical facility?",
                "Health room?", "School nurse?", "First aid at school?",
                "Who handles emergencies?", "Medical help in school?", "Health care in school?"
            ]
        ),
        (
            "What happens in a medical emergency at school?",
            "In case of a medical emergency, the school nurse is called immediately. Parents are notified within 10 minutes. If required, the student is taken to the nearest empanelled hospital. Emergency contact numbers are on file for every student.",
            [
                "Medical emergency procedure?", "What if student falls sick?", "Emergency protocol?",
                "What if child gets hurt?", "Emergency in school?", "Accident in school?",
                "Child injured at school?", "Emergency contact?", "Medical crisis?",
                "Student health emergency?", "What to do if child is sick in school?"
            ]
        ),
        (
            "Is there a health check-up for students?",
            "Yes, an annual health and dental check-up camp is organized in August for all students in collaboration with a local hospital. Parents receive a health report card for their child.",
            [
                "Annual health check?", "Dental check-up?", "Medical check-up for students?",
                "Health camp in school?", "Doctor visit for students?", "Annual check-up?",
                "Student health check?", "Eye test in school?", "Health screening?"
            ]
        ),
        (
            "What is the policy for sick students attending school?",
            "Students with fever, contagious illness, or Covid-like symptoms must not attend school. A medical certificate is required for absence of more than 3 days. The school reserves the right to send home an unwell student.",
            [
                "Can sick student come to school?", "Sick leave policy?", "Fever policy?",
                "What if student is unwell?", "Corona policy?", "Contagious illness policy?",
                "Should sick child attend school?", "Medical certificate needed?",
                "Student illness rule?", "Sick day policy?"
            ]
        ),
        (
            "Does the school have a tie-up with any hospital?",
            "Yes, the school has a tie-up with City Care Hospital, 2 km from campus. Emergency cases are taken there. The school also has ambulance access on call.",
            [
                "Empanelled hospital?", "School hospital tie-up?", "Nearest hospital?",
                "Ambulance facility?", "Hospital for emergencies?", "Medical tie-up?",
                "Which hospital does school use?", "School ambulance?"
            ]
        ),
    ],

    # ── EVENTS & COMPETITIONS ─────────────────────────────────────────────
    "Events": [
        (
            "When is Annual Day celebrated?",
            "Annual Day is celebrated every year in the month of December. It features cultural performances, prize distribution, and a special address by the principal. All parents are invited.",
            [
                "Annual day date?", "When is school annual function?", "Prize distribution day?",
                "Annual function?", "Varshik utsav?", "When is annual day?",
                "School cultural event?", "Annual day celebration?", "Prize day?"
            ]
        ),
        (
            "When is Sports Day held?",
            "Sports Day is held in January every year on the school grounds. Students from all classes participate in track and field events, relay races, and team sports. Parents are welcome to attend.",
            [
                "Sports day date?", "Annual sports meet?", "School sports event?",
                "Sports week?", "Athletic events?", "Sports competition date?",
                "Running race event?", "Annual sports day?", "Sports meet?"
            ]
        ),
        (
            "Does the school participate in inter-school competitions?",
            "Yes, the school actively participates in inter-school competitions for debate, science, sports, quiz, painting, and dance at the district and state levels. Selected students receive coaching from teachers.",
            [
                "Inter school competitions?", "Does school go for competitions?",
                "External competitions?", "Debate competition?", "Science olympiad?",
                "Quiz competition?", "State level competition?", "District competition?",
                "School representation?", "Can I participate in competitions?"
            ]
        ),
        (
            "Is there a Science Exhibition?",
            "Yes, the school organizes an annual Science and Innovation Exhibition in October. Students from Class 6 to 12 submit projects. Outstanding projects are sent to district-level exhibitions.",
            [
                "Science fair?", "Science exhibition date?", "Innovation day?",
                "Project exhibition?", "Science project event?", "STEM fair?",
                "When is science event?", "Science showcase?", "Annual science exhibition?"
            ]
        ),
        (
            "Does the school celebrate Independence Day and Republic Day?",
            "Yes, Independence Day (August 15) and Republic Day (January 26) are celebrated with great enthusiasm. Flag hoisting, cultural programs, and prizes for patriotic competitions are organized.",
            [
                "Independence day celebration?", "Republic day event?", "National day celebration?",
                "Flag hoisting?", "August 15 program?", "January 26 school event?",
                "Patriotic events?", "National holiday celebration?"
            ]
        ),
        (
            "Is there a farewell for Class 12 students?",
            "Yes, the school organizes a farewell ceremony for Class 12 students in March, hosted by Class 11 students. It includes cultural performances, mementos, and a message from the principal.",
            [
                "Farewell party?", "Class 12 farewell?", "Graduation ceremony?",
                "Passing out ceremony?", "Senior farewell?", "Bidding farewell to seniors?",
                "Farewell for 12th students?", "Last day celebration?"
            ]
        ),
    ],

    # ── PARENT PORTAL & DIGITAL SERVICES ─────────────────────────────────
    "ParentPortal": [
        (
            "How do I access the parent portal?",
            "The parent portal is accessible at portal.school.com. Log in using the credentials provided at the time of admission. You can view attendance, fee receipts, exam results, and school notices.",
            [
                "How to login to parent portal?", "Parent app login?", "School portal access?",
                "How to see child's attendance online?", "Online school portal?",
                "Parent dashboard?", "App for parents?", "School app login?",
                "How to check results online?", "Digital portal?", "Parent login?"
            ]
        ),
        (
            "How do I download my child's fee receipt?",
            "Fee receipts are available on the parent portal under the Payments section. Log in, select your child's profile, click on Fee History, and download the PDF receipt for any payment.",
            [
                "Download fee receipt?", "Get fee payment receipt?", "Fee receipt online?",
                "Fee proof download?", "Payment receipt?", "Where is fee receipt?",
                "How to get fee certificate?", "Fee paid receipt?", "Invoice download?"
            ]
        ),
        (
            "How can I check my child's attendance online?",
            "Attendance records are updated daily on the parent portal and mobile app. Log in and navigate to the Attendance section to view daily, weekly, or monthly attendance for your child.",
            [
                "Check attendance online?", "View attendance?", "Attendance portal?",
                "Online attendance record?", "How many days attended?", "Absent days record?",
                "Attendance check?", "See attendance on app?", "Attendance percentage online?"
            ]
        ),
        (
            "Is there a mobile app for parents?",
            "Yes, the school has an official mobile app available on Android and iOS. It provides real-time notifications, attendance updates, homework, circulars, and fee payment in one place.",
            [
                "School app download?", "Parent mobile app?", "Android app for school?",
                "iOS school app?", "Google Play school app?", "App for parents?",
                "School notification app?", "Mobile app features?", "App name for school?"
            ]
        ),
        (
            "How do I give feedback to the school?",
            "Parents can submit feedback through the parent portal under the Feedback section, by email at feedback@school.com, or by dropping a written note at the admin office.",
            [
                "How to give feedback?", "Complaint to school?", "Parent feedback form?",
                "School feedback?", "Suggestion to school?", "How to complain?",
                "Email feedback?", "Feedback portal?", "Parent suggestion?"
            ]
        ),
    ],

    # ── COUNSELING & CLUBS ────────────────────────────────────────────────
    "Counseling": [
        (
            "Is there a student counselor in school?",
            "Yes, the school has a trained professional counselor available every Tuesday and Thursday from 9:00 AM to 12:00 PM. Students can visit voluntarily or be referred by their class teacher.",
            [
                "Does school have counselor?", "Student counseling?", "Mental health support?",
                "Psychological support?", "Counselor in school?", "Who can students talk to?",
                "Emotional support?", "Student mental health?", "Guidance counselor?"
            ]
        ),
        (
            "How can a student join the Debate Club?",
            "Debate Club selections happen in July every year. Students from Class 8 onwards can apply by submitting a short speech to the English department. Practice sessions happen every Friday.",
            [
                "Join debate club?", "Debate club registration?", "Public speaking club?",
                "Elocution club?", "How to join debate team?", "Debate practice?",
                "Debate competition club?", "English club?"
            ]
        ),
        (
            "Is there an NCC unit in the school?",
            "Yes, the school has an NCC unit open to students from Class 9 onwards. Enrollment happens in June-July. NCC provides leadership, discipline training, and can benefit college admissions.",
            [
                "NCC in school?", "How to join NCC?", "National Cadet Corps?",
                "NCC enrollment?", "NCC benefits?", "Is NCC available?",
                "NCC unit?", "Military training in school?"
            ]
        ),
        (
            "Is there a Student Council?",
            "Yes, the school has an elected Student Council consisting of a Head Boy, Head Girl, and class representatives. Elections are held every July. Any student from Class 9-12 can contest.",
            [
                "Student council?", "Head boy head girl election?", "School elections?",
                "Class representative?", "Student government?", "Council election?",
                "Leadership position?", "Prefect system?", "Student body?"
            ]
        ),
        (
            "What creative clubs does the school have?",
            "The school has Art Club, Music Club, Drama Club, Photography Club, and Coding Club. Each club meets once a week and showcases work at the Annual Day and Science Exhibition.",
            [
                "Art club?", "Music club?", "Drama club?", "Photography club?",
                "Coding club?", "Creative activities?", "Hobby clubs?",
                "What clubs are there?", "Extracurricular clubs?", "After school clubs?"
            ]
        ),
    ],

    # ── SAFETY & INFRASTRUCTURE ───────────────────────────────────────────
    "Safety": [
        (
            "What fire safety measures does the school have?",
            "The school has fire extinguishers on every floor, smoke detectors in labs, and clearly marked emergency exits. Fire safety drills are conducted every semester for all students and staff.",
            [
                "Fire safety?", "Fire drill?", "Emergency exit?", "Fire extinguisher?",
                "Fire safety drill?", "Is school safe from fire?", "Fire emergency?",
                "Safety drill?", "Fire alarm system?"
            ]
        ),
        (
            "Is drinking water safe in school?",
            "The school provides RO-purified drinking water at multiple points across the campus. Water quality is tested monthly by a certified lab. Students are encouraged to carry personal reusable bottles.",
            [
                "Drinking water facility?", "Clean water in school?", "RO water?",
                "Water purifier in school?", "Safe water?", "Water quality?",
                "Is water purified?", "Water filter?", "Drinking water?"
            ]
        ),
        (
            "What is the procedure for student pick-up and drop-off?",
            "Students must be picked up from the school gate only by registered guardians. ID verification is done by security. No child is handed over to an unknown person. Parents must update guardian details in the app.",
            [
                "Pick up procedure?", "Who can pick up child?", "Drop off policy?",
                "Child safety at gate?", "Guardian verification?", "Gate security policy?",
                "Who can collect child?", "Pickup authorization?", "Safety at gate?"
            ]
        ),
        (
            "Does the school have CCTV?",
            "Yes, the entire campus including all classrooms, corridors, labs, canteen, and the main gate is covered by 24/7 CCTV surveillance. Footage is retained for 30 days.",
            [
                "CCTV in school?", "Surveillance cameras?", "Is campus monitored?",
                "Security cameras?", "Camera coverage?", "Is school safe?",
                "CCTV footage?", "Camera monitored?", "24/7 surveillance?"
            ]
        ),
        (
            "What is the school's anti-ragging and bullying policy?",
            "The school has a zero-tolerance policy against ragging, bullying, and discrimination. A dedicated Anti-Bullying Committee meets monthly. Students can report anonymously via the portal or a suggestion box outside the principal's office.",
            [
                "Anti ragging policy?", "Bullying complaint?", "How to report bullying?",
                "Anti bullying?", "Ragging complaint?", "Zero tolerance policy?",
                "Report harassment?", "Bullying helpline?", "Anonymous complaint?"
            ]
        ),
        (
            "Is there a lost and found in school?",
            "Yes, the school maintains a lost and found register at the admin office. Items found on campus are logged and kept for 30 days. Unclaimed items are donated to charity.",
            [
                "Lost and found?", "Where to report lost items?", "Found something in school?",
                "Lost item in school?", "Missing property?", "Where is lost and found?",
                "Misplaced item?", "Lost belongings?"
            ]
        ),
    ],
}



# ── Merge expansion facts ─────────────────────────────────────────────
try:
    from dataset.kb_expansion import EXTRA_FACTS
except ImportError:
    from kb_expansion import EXTRA_FACTS

for category, items in EXTRA_FACTS.items():
    if category in KNOWLEDGE_BASE:
        KNOWLEDGE_BASE[category].extend(items)
    else:
        KNOWLEDGE_BASE[category] = items


def generate_dataset(num_samples=15000):
    intros = [
        "Can you tell me, ", "I want to know: ", "Please explain: ",
        "", "Question: ", "Query: ", "Sir/Madam, ", "Hello, ", "Hi, "
    ]
    outros = [
        " Thank you.", " Please be specific.", "", " Thanks!",
        " Kindly advise.", " Please help.", " Urgent please."
    ]

    all_items = []
    for category, items in KNOWLEDGE_BASE.items():
        for item in items:
            all_items.append(item)

    print(f"Total unique Q&A facts: {len(all_items)}")
    print(f"Generating {num_samples} training samples...")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for _ in range(num_samples):
            base_q, base_a, variations = random.choice(all_items)
            q_text  = random.choice([base_q] + variations)
            q_final = random.choice(intros) + q_text + random.choice(outros)
            prompt  = f"User: {q_final.strip()}\nAssistant: {base_a}"
            f.write(json.dumps({"text": prompt}, ensure_ascii=False) + "\n")

    print(f"Dataset saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_dataset(15000)
