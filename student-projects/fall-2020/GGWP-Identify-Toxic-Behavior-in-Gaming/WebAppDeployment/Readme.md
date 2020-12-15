# The main components are as below

## The webpage.html holds the UI HTML/CSS/JavaScript necessary for demo functionality

## modelServer.ipynb Holds the python server

## The 8 *.pkl files are described here.

#### gloveModel.pkl loads the Word2Vec Model into memory => Git does not allow upload of files larger than 2 GB. Please find this file here: https://drive.google.com/file/d/1SKpX_5jgS779Q4tK98f9AFIqieDlcSEU/view?usp=sharing
#### vectorizer.pkl loads the vectorizer needed for getting the tf-idf word weights, which are in turn used to get the weighted vector means of a sentence
#### vectorizer2.pkl is used to transform the text into tf-idf features to put into our models
#### The 5 lr_*.pkl files are the various pre-trained logistical regression models that we will use for classification.

## How to get the webapp running on your local?

### Steps:
1. Download the 8 pkl files to your local machine. 7 of these are available in the WebAppDeployment directory and one of them is available at the Google drive link above (due to size limitations.
2. Download the "ModelServer - Test.ipynb" file to the SAME local directory. Make sure these 9 files (8 * pkls and 1* ipynb) are in the same directory.
3. Open the ModelServer Python Notebook on your jupyter notebook interface.
4. Starting from the top, run all the cells. Please note, the last cell with "app.run()" will take a considerable amount of time to run. Please hang tight! You will see some log messages that say "INFO - Running development server on: http://0.0.0.0:5000/" once the run is complete and the server is up.  The backend deployment is now complete!
5. Next, download the webpage.html file onto your local. Please open the HTML file on your browser directly. There is NO deployment required for the front-end. It is a straight HTML file with AngularJS, CSS, and JavaScript embedded in! 
6. On the HTML page, feel free to write down a message and hit "Enter" or "Submit". If you press "F12" on your keyboard, you should be able to see the results from the server on the console logs section of the developer tools. 

NOTE: If you do NOT see the response and instead get a "Cross-Origin Resource Sharing" or "CORS" related error, ir could be because of some setup/configuration of your browser settings. The easiest way steps to follow to get it working is described below. 



### Troubleshooting for CORS (Cross-Origin Resource Sharing) related error:

Please note that I have not developed either of the add-on/extension described below. I have only used them to help simplify the development of my side-projects. Please do disable the add-on/extension and/or uninstall them from your browser add-on/extension settings once you are done with your use. 

If you are using Mozilla Firefox:
1. Please install this add-on: https://addons.mozilla.org/en-US/firefox/addon/cors-everywhere/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search
2. Once installed and basic vanilla set-up is done, please click on the icon that showed up on your Firefox Toolbar. The icon should become green and say "CorsE enabled, CORS rules are bypassed" when you hover your mouse over it.
3. Refresh the webpage.html page.
4. Try to send your message by clicking on "Enter" or "Submit" again. Your request should go through - and you should see the results in the console logs.

5. Once you're done testing, please uninstall the add-on by going to "about:addons" in a new tab. Click on the "More Options" and "Remove".

If you are using Google Chrome:
1. Please install this extension: https://chrome.google.com/webstore/detail/cors-unblock/lfhmikememgdcahcdlaciloancbhjino?hl=en
2. Once installed and basic vanilla set-up is done, please click on the icon that showed up on your Google Chrome extensions toolbar. The icon should now have a colored 'C' and say "Access-Control-Allow-Origin is unblocked" when you hover your mouse over it.
3. Refresh the webpage.html page.
4. Try to send your message by clicking on "Enter" or "Submit" again. Your request should go through - and you should see the results in the console logs.

5. Once you're done testing, please uninstall the add-on by going to "chrome://extensions/" in a new tab. Click on the corresponding "Remove" for the extension.



### The below is just as  FYI for those interested in learning more about CORS. There are no real steps required apart from the troubleshooting steps above.
More info on the CORS issue here:
CORS errors are common in web apps when a cross-origin request is made but the server doesn't return the required headers in the response (is not CORS-enabled). Since this was a Data Science class, we decided to have a simple workaround in place rather than write a full-fledged and deployed server on a remote machine. More info here: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors
