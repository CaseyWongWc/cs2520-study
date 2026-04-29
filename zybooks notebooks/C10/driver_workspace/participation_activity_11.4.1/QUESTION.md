11.4 Executing modules as scripts
An import statement executes the code contained within the imported module. Thus, any statements in the global scope of a module, such as printing or getting user input, will be executed when that module is imported. Execution of those statements may be an unintended side effect of the import. A programmer wants to treat a Python file as both a script executed by the interpreter and as an importable module. When used as an importable module, the file should not produce side effects when imported.

Consider the following Python file WebSearch.py, which contains functions for returning URLs based on a search term. Executing the file as a script produces the following output:

Figure 11.4.1: WebSearch.py: Return up to six unique domain names for a given search term.
# WebSearch.py
from ddgs import DDGS
from urllib.parse import urlparse

def searchTerm(term):
    print('Searching for "', term, '" ...', sep="")
    with DDGS() as ddgs:
        results = [r['href'] for r in ddgs.text(term, max_results=6)]
    return results

def stringifyResult(term, domains, domainString):
    i = 0
    for url in domains:
        domain = urlparse(url).netloc
        if domain and domainString.find(domain) == -1:
            domainString += "
" + domain
            i = i + 1
    if i == 0:
        print("No domains", end="")
    elif i == 1:
        print("One domain", end="")
    elif i == 6:
        print("Search stopped after six domains", end="")
    else:
        print(i, "domains", end="")
    print(' found for search term "', term, '".', sep="")
    return domainString

print("Welcome to Web Search")
term  = input("Enter search term: ")
result = searchTerm(term)
resultString = ""
resultString = stringifyResult(term, result, resultString)
print(resultString)
print("
End of Web Search")
Welcome to Web Search
Enter search term: Funny pictures of cats
Searching for "Funny pictures of cats" ...
Search stopped after six domains found for search term "Funny pictures of cats".

cats.com
articles.hepper.com
tenor.com
unsplash.com
pixabay.com
www.rd.com

End of Web Search
Note that the above program imports and uses the ddgs module, which provides functions for fetching URLs using the DuckDuckGo.com search engine. To run the program, the package ddgs (Ex: pip install ddgs) must be installed.


Feedback?
If another script imports WebSearch.py to use the searchTerm() function, the statements at the bottom of WebSearch.py will also execute. WebSearchMultiple.py enables the user to enter more than one search term and have results from all search terms returned. However, importing WebSearch.py causes an unwanted prompt for and search of a single term, because that search is in the global scope of WebSearch.py.

Figure 11.4.2: MultipleWebSearch.py: Importing WebSearch.py causes an unintended search to occur.
# MultipleWebSearch.py
import WebSearch as ws  # Causes unintended search

print("Welcome to Multiple Web Search")
term = input('Enter search term ("q" to quit): ')
terms = 0
resultString = ""
while term != "q":
    terms = terms + 1
    result = ws.searchTerm(term)
    resultString = ws.stringifyResult(term, result, resultString)
    term  = input('Enter search term ("q" to quit): ')
if terms == 0:
    print("No search terms entered.")
else:
    if terms == 1:
        print("Results for the one search term entered:")
    else:
        print("Results for the", terms, "search terms entered:")
    print(resultString)
print("
End of Multiple Web Search")
Welcome to Web Search
Enter search term: Music videos
Searching for "Music videos" ...
Search stopped after six domains found for search term "Music videos".

en.wikipedia.org
grokipedia.com
www.youtube.com
vimeo.com
music.apple.com
www.npr.org

End of Web Search
Welcome to Multiple Web Search
Enter search term ("q" to quit): Statue of Liberty
Searching for "Statue of Liberty" ...
5 domains found for search term "Statue of Liberty".
Enter search term ("q" to quit): Mount Rushmore
Searching for "Mount Rushmore" ...
3 domains found for search term "Mount Rushmore".
Enter search term ("q" to quit): q
Results for the 2 search terms entered:

en.wikipedia.org
grokipedia.com
www.nps.gov
whc.unesco.org
www.statueofliberty.org
share.america.gov
www.worldatlas.com
www.britannica.com

End of Multiple Web Search

Feedback?
A file can better support execution as both a script and an importable module by utilizing the __name__ special variable. __name__ is a global string variable automatically added to every module that contains the name of the module. Ex: my_funcs.__name__ would have the value "my_funcs", and WebSearch.__name__ would have the value "WebSearch". (Note that __name__ has two underscores before name and two underscores after.) However, the value of __name__ for the executing script is always set to "__main__" to differentiate the script from imported modules. The following comparison can be performed:

Figure 11.4.3: Checking if a file is the executing script or an imported module.
if __name__ == "__main__":
    # File executed as a script

Feedback?
If if __name__ == "__main__" is true, then the file is being executed as a script and the branch is taken. Otherwise, the file was imported and thus __name__ is equal to the module name, e.g., "WebSearch".

The contents of the branch typically include a user interface to functions or class definitions within the file. A user can execute the file as a script and interact with the user interface, or another script can import the file just to use the definitions. The WebSearch.py file is modified below to fix the unintentional search.

Figure 11.4.4: WebSearch.py modified to run as either a script (left) or imported module (right).
Each file below is executed as a script.

WebSearch.py
# WebSearch.py
from ddgs import DDGS
from urllib.parse import urlparse

def searchTerm(term):
    # ...

def stringifyResult(term, domains, domainString):
    # ...

if __name__ == "__main__":
    print("Welcome to Web Search")
    term  = input("Enter search term: ")
    result = searchTerm(term)
    resultString = ""
    resultString = stringifyResult(term, result, resultString)
    print(resultString)
    print("
End of Web Search")
MultipleWebSearch.py
# MultipleWebSearch.py
import WebSearch as ws

print("Welcome to Multiple Web Search")
term = input('Enter search term ("q" to quit): ')
terms = 0
resultString = ""
while term != "q":
    terms = terms + 1
    result = ws.searchTerm(term)
    resultString = ws.stringifyResult(term, result, resultString)
    term  = input('Enter search term ("q" to quit): ')
if terms == 0:
    print("No search terms entered.")
else:
    if terms == 1:
        print("Results for the one search term entered:")
    else:
        print("Results for the", terms, "search terms entered:")
    print(resultString)
print("
End of Multiple Web Search")
Welcome to Web Search
Enter search term: Music videos
Searching for "Music videos" ...
Search stopped after six domains found for search term "Music videos".

en.wikipedia.org
grokipedia.com
www.youtube.com
music.apple.com
vimeo.com
www.npr.org

End of Web Search
Welcome to Multiple Web Search
Enter search term ("q" to quit): Statue of Liberty
Searching for "Statue of Liberty" ...
Search stopped after six domains found for search term "Statue of Liberty".
Enter search term ("q" to quit): Mount Rushmore
Searching for "Mount Rushmore" ...
3 domains found for search term "Mount Rushmore".
Enter search term ("q" to quit): q
Results for the 2 search terms entered:

en.wikipedia.org
grokipedia.com
www.nps.gov
www.statueofliberty.org
whc.unesco.org
www.statueoflibertytickets.com
share.america.gov
www.worldatlas.com
www.britannica.com

End of Multiple Web Search

Feedback?
The WebSearch.py file has been modified to compare __name__ to "__main__". When the file is executed as a script, a single search request is made and the results are displayed. Executing MultipleWebSearch.py imports WebSearch, which now does not perform the initial search because __name__ is equal to "WebSearch".

participation activity
11.4.1: Executing modules as scripts.
1)
Importing a module executes the statements contained within the imported module.
2)
The value of the __name__ variable of the executing script is always "__main__".
3)
If a module is imported with the statement import MyMod, then MyMod.__name__ is equal to "__main__".

Feedback?
How was this section?

|


Provide section feedback