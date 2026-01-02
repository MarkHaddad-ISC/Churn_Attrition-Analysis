# Churn_Attrition-Analysis
Scripts for running generative AI on large data sets for semantic reasoning

SETUP:

First step is to run the the requirments.txt file 

if in python:

  subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

Afterwards, go to https://copilot.moodys.com/profile in order to create your own api keys to access Moody's Copilot remotely

FILTERING:

Due to a lack of direct database connections, alot of the work is done in excel sheets, extracting via openpyxl, and manipulitng with pandas.

I have included blank RawInput and Ouputs folders here, this is where the excel files are stored

Some of the data sources are pre filtered, some require scripts to clean to them up
to obtain the data neccesary for this project please reach out to either Xavier Lecomte or Ravi Gupta


PROCESSING:

In order to conduct this processing there are a few key components to consider since every line of data is analyzed one by one leading to somwhere close to 75,000 calls to copilot.

1.) this process will take a long time, currently I do a sumple loop through every line to run an AI analysis on it, you can experiment with sening large batches just under the Moody's rate limit threshold. I was not able to do so reliably so I weent with the simple for loop implimentation

2.) This process should be run on a server ideally if you can provision one, if not you will have to run it locally and execture either a terminal (mac) or shell (windows) command in order to prevent idle sleep for your machine, otherwise the process will stop once the disk sleeps

For Mac Terminal: caffeinate -i

3.) In the case where there is a server timeout, I have created to script with incremntal saves and multiple halucination and error checks to ensure a consistnet output.

4.) when using openPyXl, make sure the page you are writing to closed, if it is open then python will not write the python script outputs to it.


FUTURE CHANGES:

Plan is to incorporate zero shot modeling via open source hugging face model (joeddav/xlm-roberta-large-xnli most likely due to it being multilingual) in order to get consistent results across different runs and an exponentinal speedup

