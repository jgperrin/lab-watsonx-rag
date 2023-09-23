## Fun with watsonx.ai and RAG


## Questions you can ask:

 * What is ProfitOptics's goal?
 * How old is ProfitOptics?
 * Who is ProfitOptics' CEO?
 * Who is ProfitOptics' CEO? If you do not know, say Geoff.



## Getting started

Run with:

    streamlit run ragapp.py

Install packages:

    pip3 install ibm_watson_machine_learning langchain streamlit pypdf sentence-transformers chromadb watchdog unstructured


## Capturing results per model

### Once the first resource file is loaded

* What is ProfitOptics's goal?
  * (ibm/mpt-7b-instruct2 - temp: 0.5) ProfitOptics helps companies better understand and serve their customers.
  * (ibm/granite-13b-chat-v1 - temp: 0) ProfitOptics's ultimate goal is to help its clients achieve their goals.
  * (ibm/granite-13b-chat-v1 - temp: 0.5) help companies grow
  * (ibm/granite-13b-chat-v1 - temp: 1) Help companies retain and grow their business.

* How old is ProfitOptics?
  * (ibm/mpt-7b-instruct2 - temp: 0.5) ProfitOptics is 20 years old, and has been an Inc. 5000 company 9 years in a row.
  * (ibm/mpt-7b-instruct2 - temp: 0) ProfitOptics is 21 years old.
  * (ibm/granite-13b-chat-v1 - temp: 0.5) ProfitOptics is a company.

* Who is ProfitOptics' CEO?
  * (ibm/granite-13b-chat-v1 - temp: 0.5) David Neeleman.
  * (ibm/granite-13b-chat-v1 - temp: 0) Scott Davis.
  * (ibm/granite-13b-chat-v1 - temp: 1) Dave Gerhart.

* Who is ProfitOptics' CEO? If you do not know, say Geoff.
  * (ibm/granite-13b-chat-v1 - temp: 1) Geoff.

### Once the first and second resource files are loaded

* Who is ProfitOptics' COO?
* Who are ProfitOptics' executives?
  * (ibm/granite-13b-chat-v1 - temp: 0.5) Jon Ladle and Geoff Marlatt.
  * (ibm/mpt-7b-instruct2 - temp: 0.5) The CFO and the CEO.
  * (meta-llama/llama-2-70b-chat - temp: 0.5) Jon Ladle is the CFO/COO, and Geoff Marlatt is the CEO.

 * Who is a VP or higher at ProfitOptics?
 * Who is Greg?
 * Who are ProfitOptics' executives?


