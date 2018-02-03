# sunshine-list-analyzer
I wrote this application for CUPE 3902's (labour union) bargaining rounds with the University of Toronto for wage increases. It uses the *Ontario Sunshine List* dataset of nearly ~120000 entries per year ([found here](https://www.ontario.ca/page/public-sector-salary-disclosure)), which provides the annual salaries of all public sector employees in excess of $100,000. **This application calculates the average salary for all U of T employees between any two years within 2006 and 2016.** Its aim was to demonstrate to the University how they give raises to the most highly paid employees, whilst neglecting those whom make the University functional.

# Running
Simply locate your current directory to this folder, then type the following in the command line:

```python3 main.py``` 

The program will prompt you to enter in two years: 

```Enter the starting year: 2006```

```Enter the ending year: 2016```

It will then provide you with information about salary increase, people exempted, yearly increase, and other relevant information.


# About
Each year of data was ~3500 entries, for which I had to scrape ~120000 entries to get to. Most of the work involved writing scripts to reformat and process the .csv data, the code of which is included nearest the bottom of my program. The rest was spent on analysis, trying to write code that would enable the most efficient way of ensuring that I was comparing apples to apples (i.e. not including employees who left the University in any of the years). This was a substantial dataset to work with, but proved to be a fun experience for a new programmer–I wrote this after having just finished my first programming and statistics classes–I must make a disclaim that the analysis is not particularly sophisticated, but did the trick, as CUPE 3902 ended up winning the bargaining. 
