# Ex02 Time Table
## Date: 07-02-2026

## AIM
To write a html webpage page to display your slot timetable.

## ALGORITHM
### STEP 1
Create a Django-admin Interface.

### STEP 2
Create a static folder and insert HTML code.

### STEP 3
Create a simple table using ```<table>``` tag in html.

### STEP 4
Add header row using ```<th>``` tag.

### STEP 5
Add your timetable using ```<td>``` tag.

### STEP 6
Execute the program using runserver command.

## PROGRAM

```html
<html>  
<head>
    <title>Slot Time Table</title>
</head>
<body>  
    <img src="c:\Users\Trisha Priyadarshni\Downloads\SEC Logo.png" alt="Logo" width="500" height="100">
    <br><br>
    <caption><b>SLOT TIME TABLE - TRISHA PRIYADARSHNI PARIDA (24900017)</b></caption>
    <table border="1" bgcolor = "Cyan" cellpadding="5">  
        <tr bgcolor="Yellow" align = "center">  
            <th>Day/Time</th>  
            <th>Monday</th> 
            <th>Tuesday</th> 
            <th>Wednesday</th>
            <th>Thursday</th>
            <th>Friday</th>
        </tr>  
        <tr bgcolor="Cyan" align = "center">  
            <td bgcolor = "Yellow" align = "center"><b>8-10</b></td>  
            <td colspan = "3" style="text-align:center;">FREE SLOT</td>  
            <td>PHY</td>
            <td>CHE</td>
        </tr>  
        <tr bgcolor="Cyan" align = "center">  
            <td bgcolor = "Yellow" align = "center"><b>10-12</b></td>  
            <td>GER</td>
            <td>FREE SLOT</td>
            <td>FWAD</td>
            <td>FWAD</td>
            <td>PHY</td>
        </tr>  
        <tr bgcolor="Cyan" align = "center">  
            <td bgcolor = "Yellow" align = "center"><b>12-1</b></td>  
            <td colspan = "5" style="text-align:center;">LUNCH</td>  
        </tr>  
        <tr bgcolor="Cyan" align = "center">  
            <td bgcolor = "Yellow" align = "center"><b>1-3</b></td>  
            <td colspan="2"style="text-align:center;" >FREE SLOT</td>
            <td>MAT</td>
            <td>MAT</td>
            <td>SS</td>
        </tr>
        <tr bgcolor="Cyan" align = "center">  
            <td bgcolor = "Yellow" align = "center"><b>3-5</b></td>  
            <td colspan="2"style="text-align:center;">FREE SLOT</td>
            <td>GER</td>
            <td>CHE</td>
            <td>FWAD</td>
        </tr>
    </table>
    <br>
    <table border="1" cellpadding="5">
        <tr>
            <th><b>S.No.</b></th>
            <th><b>Subject Code</b></th>
            <th align="center"><b>Subject Name</b></th>
        </tr>
        <tr>
            <td align="center">1.</td>
            <td align="center">19AI414</td>
            <td>Fundamentals of Web Application Development (FWAD)</td>
        </tr>
        <tr>
            <td align="center">2.</td>
            <td align="center">19EN612</td>
            <td>German Basic (GER)</td>
        </tr>
                <tr>
            <td align="center">3.</td>
            <td align="center">19PH206</td>
            <td>Physics for Information Technology (PHY)</td>
        </tr>
                <tr>
            <td align="center">4.</td>
            <td align="center">19CY205</td>
            <td>Principles of Chemistry in Engineering (CHE)</td>
        </tr>
                <tr>
            <td align="center">5.</td>
            <td align="center">19MA201</td>
            <td>Calculus and Matrix Algebra (MAT)</td>
        </tr>
                <tr>
            <td align="center">6.</td>
            <td align="center">19EY701</td>
            <td>Soft Skills (SS)</td>
        </tr>
    </table>
</body>
</html>
```



## OUTPUT

<img width="1124" height="1027" alt="image" src="https://github.com/user-attachments/assets/206c6251-106d-44fc-93f1-7c1b10c5f48a" />

## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
