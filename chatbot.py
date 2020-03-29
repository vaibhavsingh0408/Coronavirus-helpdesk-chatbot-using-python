from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["hello %1, How are you today"]
    ],
    [
        r"hi",
        ["""
        Namaste 🙏
        This is the Government of 
        India's Coronavirus (COVID-19) 
        Helpdesk to create awareness and 
        help you and your family stay safe. 

        For any emergency 👇 
        📞 Helpline: 011-23978046 | Toll-Free Number: 1075
        ✉️ Email: ncov2019@gov.in


        Please choose from the following options 👇

        1. Latest Update on Coronavirus in India
        2. What is Coronavirus and what are its symptoms?
        3. How does Coronavirus spread?
        4. How to reduce the risk of Coronavirus? 
        5. Professional advice by AIIMS
        6. State and language specific chatbots (Gujarat, Maharashtra)
        7. Where to get help?

        💡Tip: You can type 1, 2, 3, 4, 5, 6, 7 to make a selection of the menu options.
         """]
    ],
    [
        r"1",
        ["""
        Hon'ble Prime Minister addressed the nation on 24 March 2020 at 8 PM. Check the video here 👇
https://youtu.be/4napLmFM5BA

COVID-19 updates as on 27.03.2020 at 11 AM 👇
▪️ Active Cases: 640
▪️ Cured/Discharged/Migrated cases: 67
▪️ Death cases: 17

Lockdown announced across the country for 21 days (Starting from 25.03.2020 to 14.04.2020)

Useful Alerts 👇
▪️  Doorstep delivery of drugs to consumers allowed: Health Ministry
▪️  ₹1.70 lakh crore Relief package announced under PM Gareeb Kalyan Yojana
▪️  ₹50 lakh/ person insurance cover for healthcare professionals dealing with COVID-19
▪️  Government conducting Contact Tracing as per infectious disease containment strategy
▪️  Get NCERT e-Book on UMANG. To download give a missed call on 📞 9718397183
▪️  FACT: COVID-19 spreads through droplets and human contact, when people touch their mouths, noses and eyes with contaminated 🤲

Testing Facilities for COVID-19 in the Country 👇
▪️ Operational Govt. Laboratories: 109
▪️ Govt. Laboratories (being operationalized): +12 
▪️ Authorized Private Laboratories: 35

For detailed information on coronavirus, please check the link below 👇
https://www.mygov.in/covid-19
https://www.mohfw.gov.in

👉 Type 2 for Symptoms
👉 Type 3, 4, 5, 6, 7 to see other options
👉 Type Menu to view the Main Menu        

        """]
    ],
    [
        r"2",
        ["""
        Coronaviruses are a large family of viruses, some causes illness in people. Its symptoms in humans are

 🤒 Fever
 😐 Breathing problem
 🤧 Coughing
 😫 Tightness of chest
 👃 Running Nose
 😨 Headache
 🌡️ Feeling unwell
 😷 Pneumonia
 💉 Kidney Failure

It can be difficult to identify the disease based on symptoms alone. Check when you should get tested 👇
https://www.mohfw.gov.in/FINAL_14_03_2020_ENg.pdf

You can also view the video on symptoms by Director,AIIMS-Delhi 👇
https://youtu.be/E8-UoeWewFI

👉 Type 3 to know more on How does Coronavirus spread? 
👉 Type 1, 4, 5, 6, 7 to see other options
👉 Type Menu to view the Main Menu
        """]
    ],
    [
        r"3",
        ["""
        Coronavirus spreads from an infected person through 👇

♦️ Small droplets from the nose or mouth which are spread when a person coughs or sneezes 

♦️ Touching an object or surface with these droplets on it and then touching your mouth, nose, or eyes before washing your hands

♦️ Close personal contact, such as touching or shaking hands

Please watch the video for more information 👇
https://youtu.be/0MgNgcwcKzE

👉 Type 4 to check the Preventive Measures 
👉 Type 1, 2, 5, 6, 7 to see other options
👉 Type Menu to view the Main Menu
        """]
    ],
    [
        r"4",
        ["""
        Coronavirus infection can be prevented through the following means 👇

✔️ Clean hand with soap and water or alcohol-based hand rub 
https://youtu.be/EJbjyo2xa2o

✔️ Cover nose and mouth when coughing & sneezing with a tissue or flexed elbow
https://youtu.be/f2b_hgncFi4

✔️ Avoid close contact & maintain 1-meter distance with anyone who is coughing or sneezing
https://youtu.be/mYyNQZ6IdRk

✔️ Isolation of persons traveling from affected countries or places for at least 14 days
https://www.mohfw.gov.in/AdditionalTravelAdvisory1homeisolation.pdf

✔️ Quarantine if advised
https://www.mohfw.gov.in/Guidelinesforhomequarantine.pdf

👉 Type 5 to check the Professional Advice By AIIMS 
👉 Type 1, 2, 3, 6, 7 to see other options
👉 Type Menu to view the Main Menu
        """]
    ],
    [
        r"5",
        ["""
        Please watch the videos by Director, AIIMS - Delhi to learn and clear your doubts on Coronavirus 👇

https://youtu.be/JXobDg2Fpn4

https://youtu.be/E8-UoeWewFI

https://youtu.be/5wCZdcAsvE8

https://youtu.be/mYyNQZ6IdRk

https://youtu.be/08ryxbcT3-o

👉 Type 6 to check the State and language specific chatbots
👉 Type 1, 2, 3, 4, 7 to see other options
👉 Type Menu to view the Main Menu
        """]
    ],
    [
        r"6",
        ["""
        You can start chatting with the state-specific chat bot by tapping the links below 👇

Gujarat State Chat Bot (Language-Gujarati)
https://wa.me/917433000104?text=Hi

Maharashtra State Chat Bot
 https://wa.me/912026127394?text=Hi

👉 Type 7 for any kind of Medical Help
👉 Type 1, 2, 3, 4, 5 to see other options
👉 Type Menu to view the Main Menu
        """]
    ],
    [
        r"7",
        ["""
        For medical help in India please reach out to the 24/7 Control Room.

📞 Phone: +91-11-23978046
☎️ Toll-Free Number: 1075
✉️ Email: ncov2019@gov.in

MyGov Corona Chatbot is also available 👇 

WhatAapp: https://wa.me/919013151515?text=Hi 
Telegram: https://t.me/MyGovCoronaNewsdesk
Facebook Messenger: https://m.me/MyGovIndia?ref=Hi

For queries from a person outside India. Please contact Ministry of External Affairs(MEA), GOI

📞 1800118797
✉️ covid19@mea.gov.in

For Visa related queries

📞 01124300666
✉️ support.covid19-boi@gov.in

👉 Type Menu to view the Main Menu
👉 To check the helpline number of your state. Please type the name of your state below 👇

For eg. Maharashtra
        """]
    ],
    [
        r"Maharastra",
        ["""
        The helpline number for Maharashtra is 020-26127394

Please check the PDF given below to check the helpline numbers of other states 👇

https://www.mohfw.gov.in/coronvavirushelplinenumber.pdf

💡 Type Menu to view the main menu.
        """]
    ],
    [
        r"Menu",
        ["""
        Please choose from the following options 👇

1. Latest Update on Coronavirus in India
2. What is Coronavirus and what are its symptoms?
3. How does Coronavirus spread?
4. How to reduce the risk of Coronavirus? 
5. Professional advice by AIIMS
6. State and language specific chatbots (Gujarat, Maharashtra)
7. Where to get help?

💡Tip: You can type 1, 2, 3, 4, 5, 6, 7 to make a selection of the menu options.
        """]
    ]
]


def chatty():
    print("hello dear, I m Coronavirus Helpdesk\nmy creator name is vaibhav singh")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    chatty()