# GPT SOP Generator

This is a simple tool that uses GPT-3.5 or GPT-4 to convert raw meeting notes or intake form data into structured Standard Operating Procedures (SOPs).

---

## What It Does

- Takes unstructured notes or bullet points as input  
- Sends them to OpenAI's GPT API  
- Returns a clean, formal SOP ready to use or edit  

---

## Technologies Used

- Python  
- OpenAI API  

---

## Sample Input
Meeting notes:

   - ID must be submitted within 24 hours

   - Accounts setup takes 2 days

   - Assign buddy for 1st week


---

## Sample Output

Standard Operating Procedure – Employee Onboarding

Step 1: New employees must submit a valid national ID within 24 hours of joining.  
Step 2: IT will create user accounts within two business days.  
Step 3: Each new hire is assigned a buddy for their first week to assist with onboarding.

---

## Use Cases

- HR and People Operations  
- Small Business Owners  
- Freelancers or consultants writing SOPs for clients  

---

## Notes

- Requires an OpenAI API key to run.  
- Can be extended with a simple UI (Streamlit or Flask) for internal use.




