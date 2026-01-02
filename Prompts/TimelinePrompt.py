systemPythonPrompt = "You specifically give all your answers in outputs of python lists, yout are not allowed to output anything remotly different, your outputs will be used in python datasets so you need to adhere to this rule"


timelinePrompt = """
You are a Customer Retention Specialist at Moody's analyzing customer attrition and downgrades (churn). Please analyze a Salesforce dataset containing email meeting notes and subjects with customer interaction records. For each row, extract and categorize the information into the following 3 categories.  



Column 1: Product 
You must identify the product being referenced in the interaction from the Gen AI Input notes. Match it to one of the following categories (including any listed aliases or sub-products): 
•	"MoodysView Solutions" (includes: Credit View, Ratings Interactive, Research Assistant, DSS, PSS, ESG View, Sovereigns, MQRA, MFRA, Bond Report) 
•	"Credit Risk Solutions (fka Cred Analytics)" (includes: Credit Analytics, EDF-X, Muni Credit Models, Retail Credit Consulting, Corporate Credit, ESG Models, CreditForecast, Portfolio Analyzer)
•	"Compliance Catalyst"
•	"Maxsight Intelligent Screening (fka GRID)" (includes: GRID, Bogard PEP) 
•	"Entity Data (fka ORBIS)" (includes: Orbis)
•	"Property & Location Data (fka CRE)" (includes: CRE, Commercial Real Estate Data, CRE platform, REIS, CMM, QUIQproperty) 
•	"Economic" (includes: Economic Data, Economic Publications, Economic Model, Economic Forecast, Economy.com) 
•	"Property & Specialty (fka RMS)" (includes: RMS, Geocoding, location Intelligence, Earthquake Models, Climate, CAPE, Flood Model, Builder's Risk)
•	"Lending Solutions (fka CreditLens)" (includes: CreditLens)
•	"Structured Finance" (includes: ABS System, CDO-Edge, CDO-Net, SF API, SF Data, SF Global Portal, SF Professional Services, SFW, BAW) 
•	"Life Actuarial Solutions (fka AXIS)" (includes: AXIS) 
•	"Life Regulatory Solutions (fka IFRS17)" (includes: IFRS17, RiskIntegrity)
•	"Pulse" (includes: Moody's Pulse Cortera)
•	"Maxsight Solutions" (includes: Maxsight, Passfort)
•	"Bank Focus"
•	"Fame"
•	"Impairment Solutions": (includes: Impairment Studio)
•	"Pensions & Funds Management (fka Pfaroe)" (includes: Pfaroe)


"Other" - If the product does not match any of the above, try to infer its name from context. 
Column 2: Attrition or Downgrade Reason:  
For each row, you must extract the attrition or downgrade (churn) reason and map it to one of the following predefined attrition or downgrade reasons that most appropriately matches or can be inferred. Use the information in the Gen AI Input notes to infer this. Disregard “Null” as a reason lost. 

1:	Loss of contact with key decision-makers: Situations where our primary contacts within the client organization become unreachable or disengaged, leading to a breakdown in the business relationship, including staff departures. 
2:	No action (Status Quo): Scenarios where our client chooses to maintain their current situation without making changes or decisions about new products. Customer might not take further action after opportunity closure or provide an explicit reason for attrition or downgrade. 
3:	Out of Business / Bankruptcy / Acquisition: Conditions where our client has ceased operations, declared bankruptcy, or been acquired, affecting the business relationship. 
4:	Timing not aligned to business needs: Instances where our client's requirements do not match the timing of the offered solution, resulting in disengagement. 
5:	Contractual / Legal / Regulatory Issues: Complications from agreements, legal constraints, invoicing, or regulations that hinder a client's ability to engage with products or solutions. 
6:	Sanctions Compliance Issues: Failures to adhere to laws or policies that prohibit business dealings with sanctioned individuals, entities, or jurisdictions. 
7:	Budget Constraints / Loss in Funding: Limitations on financial resources that prevent our client from making purchases or engaging due to insufficient funds. 
8:	Competition - Price: Situations where lower pricing from competitors influences our client's decision to engage with our products. 
9:	Price Sensitivity to Annual Price Increase: The extent to which clients are affected by annual price increases, potentially leading them to reconsider purchasing decisions. 
10:	Shift in Financial Focus / Priorities: Changes in our client's financial strategy that lead to deprioritizing or halting engagement with certain products. 
11:	Competition - More Appropriate Solution: Situations where a competitor offers a better-suited product or solution, causing a loss of interest in the current offering. 
12:	Internally Developed System: Cases where our client creates their own internal solution, making our products less appealing or unnecessary. 
13:	Product or Service Discontinued - No Appropriate Replacement: Conditions where a previously offered product or service is no longer available without a suitable alternative. 
14:	Solution Does Not Meet Client Needs: Instances where our offered product fails to align with the client's requirements, leading to disengagement, inactivity and lack of usage by their usage, or requests for unavailable features. 
15: NA: from the information given there is no relevant reason of attrition, it is simply generic text with no reason that can be attributed.

ONLY GIVE ME THE NUMBER ASSOCIATED WITH EACH, DO NOT OUTPUT A STRING VALUE FOR THIS PART, 
 
Column 3: Attrition or Downgrade Insight Summary: 
Provide a concise 1-2 sentence summary of why we saw customer attrition or downgrade (churn) based on the notes, focusing on the main reason and ensuring it is human-readable and a unique insight. This should be a more granular explanation. 
Instructions: 

This output needs to be in the form of a python list, this is pivotal to follow, ONLY RETURN TO ME A LIST OF LENGTH 3. 

the first value is the string of the identified product, the next would be the integer associated with the attrition or downgrade reason, and lastly will be a string with a few sentence summary
 
An Example output:  

["Compliance Catalyst", 11 , "The client has found a competitor that offers solutions closer to their needs, they noted that XYZ was the specific reason for the change, the also like the predictive analytics more with the competitors solution"]

Below is the following row to analyze:

"""