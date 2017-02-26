import requests
import json

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from imdb import IMDb
from models import Actor

# Provides the data source of movies and actors, via 'http' or a local DB
def initiate_imdb_api():
    #return IMDb('sql',uri='mysql://root:blueelephant@localhost/imdb_new')
    return IMDb('http')

# No longer in use, omdb api provides similar data with lesser latency
def actor_relations(movies_list, size, limit_movies):
    ia = initiate_imdb_api()
    relations_dict = {}
    for movie in movies_list[:limit_movies]:
        movie_detailed = ia.get_movie(movie.movieID)
        print "movie: " + str(movie_detailed)
        if movie_detailed.get('cast', None) is not None:
            for actor in movie_detailed['cast']:
                if relations_dict.get(actor['name'], None) is not None:
                    relations_dict[actor['name']] += 1
                else:
                    relations_dict[actor['name']] = 1
    #relation_dict =  {u'Kallirroi Tziafeta': 1, u'Arun Mathur': 1, u'Nadir': 1, u'Bindu Kamat': 1, u'Shivam Sharma': 1, u'Pandey': 1, u'Pitobash': 1, u'Firdausi Jussawalla': 1, u'Raj Prakash': 1, u'Ashok Laad': 1, u'Akash Khurana': 1, u'Manoj Kumar': 1, u'Kamlesh Oza': 1, u'Johnny Hayward': 1, u'Makrand Deshpande': 2, u'Harish Patel': 3, u'Vinod Raut': 1, u'Richard Lane Smith': 1, u'Sohrab Ardeshir': 2, u'Naseeruddin Shah': 3, u'Smita Jaykar': 1, u'Haniif Sheikh': 1, u'Abdul Hai': 1, u'Zack Brakke': 1, u'Charushila': 1, u'Rajul Gaur': 1, u'Prabir Kumar': 1, u'Jigmet Dorjey': 1, u'Chittaranjan Giri': 1, u'Bawani': 1, u'Sharman Joshi': 2, u'Anil Kapoor': 2, u'Deep Raj Rana': 1, u'Pooja Goswami': 1, u'Mahendra Gole': 1, u'Manoj Pahwa': 1, u'Dina Pathak': 1, u'Usha': 1, u'Meghna Malik': 1, u'Sunil Mehra': 1, u'Andrew Bicknell': 1, u'Gaurav Sethi': 1, u'Dolly Minhas': 1, u'Vivekanandan': 1, u'Rakesh Sharma': 1, u'Raja Duggal': 1, u'Kamaldeep': 1, u'Neelkamal': 1, u'Geoff Downer': 1, u'Naushaad Abbas': 1, u'Mahesh Balraj': 1, u'Anil Mange': 1, u'Deepak Bhatia': 1, u'Matty Robinson': 1, u'Reena Roy': 1, u'Sunil Dhawan': 2, u'Indumati Rajda': 1, u'Sitaram Devasi Kadam': 1, u'Murad': 1, u'Kalpana Divan': 1, u'Darsheel Safary': 1, u'Bapsi Sidhwa': 1, u'Taufiq': 1, u'Dharmendra Singh': 1, u'Paul D. Morgan': 1, u'Raja': 1, u'Amole Gupte': 2, u'Madhavendra': 1, u'Darren Elliot Fulsher': 1, u'Yashwant Singh': 1, u'Ranveer Singh': 1, u'Shazan St. James': 1, u'Varun Vardhan': 1, u'Parminder': 1, u'Manoj Mishra': 1, u'Lamba': 1, u'Shyam Kumar': 1, u'Vikrant Massey': 1, u'Fatima Sana Shaikh': 1, u'Yusuf Hussain': 1, u'Sarah Hashmi': 1, u'Raghunathan': 1, u'Rajinder Sharma Nanu': 1, u'Yarko': 1, u'Roberta Chung': 1, u'Ved Goswami': 1, u'Dilshad Edibam': 1, u'Sabina': 1, u'Sai Gundewar': 1, u'Jainendra': 1, u'Pradeep Singh Rawat': 3, u'Erin E. Clyne': 1, u'Amita Nangia': 1, u'Tj McGinty': 1, u'Meru Vernekar': 1, u'Mia Klein': 1, u'Monica Dogra': 1, u'Elizabeth Reiners': 1, u'Girija Shettar': 1, u'Mansee Deshmukh': 1, u'Himayat Ali': 1, u'Gatanjill Chopra': 1, u'Nidhi Tuli': 1, u'Joanne Slater': 1, u'Aloka Mukherjee': 1, u'Rajat Dholakia': 1, u'Trilok Sadhwani': 1, u'Kiran Rao': 1, u'Ananth Narayan Mahadevan': 3, u'Javed Rizvi Jarehavi': 1, u'Michael Joseph': 1, u'Mehmood Khan': 1, u'Suhasini Mulay': 2, u'Raveena Tandon': 3, u'Ahmed Ali': 1, u'Kaylee Vazquez': 1, u'Ben Nealon': 2, u'Ashok Varma': 1, u'Charlie': 1, u'Kamlesh Gill': 1, u'Jonathan Coffin': 1, u'Yasmin': 1, u'Avtar Sahani': 1, u'Mohd Afif Iszuddin B Ismail': 1, u'Dhruv Raj Singh': 1, u'Simran Makhija': 1, u'Arun': 1, u'Pankaj Titoria': 1, u'Jamila Shaikh': 1, u'Meher Vij': 1, u'Kumar Manav': 1, u'K.D. Chandran': 1, u'Sai Tamhankar': 1, u'Ranjeeta Kaur': 1, u'Sunil Pandey': 1, u'Aditya Narayan': 1, u'Gena Ellis': 1, u'Mohan Pandey': 1, u'Tabu': 1, u'Parveen Bano': 1, u'Kiron Kher': 3, u'Sagar Zakhmi': 1, u'Gurpreet Toti': 1, u'Yusuf': 1, u'Seema Vaz': 1, u'Angelina Angulo': 1, u'Raj Tilak': 1, u'Kamal Adib': 1, u'Manmauji': 4, u'Ivan Rodrigues': 1, u'Jamuna': 2, u'Kishore Anand Bhanushali': 1, u'K.K. Verma': 1, u'John Rowe': 1, u'Amin Hajee': 3, u'Vijay Raaz': 1, u'Simon Chandler': 1, u'Yunus Parvez': 4, u'Ashish Nayyar': 1, u'Shis Khan': 1, u'Paul Blackthorne': 1, u'Kunal Vijaykar': 1, u'Bharat Jha': 1, u'Zeena Bhatia': 1, u'Abhay Shukla': 1, u'Pankaj Jha': 1, u'Sanjeev Wilson': 1, u'Manjit Kumar': 1, u'Pallavi Batra': 1, u'Master Omkar Kapoor': 1, u'Shivraj': 1, u'Sahiba Chopra': 1, u'Ravi Khanvilkar': 2, u'Brian Dowden': 1, u'Vaidyanathan': 1, u'Dipti Bhatnagar': 1, u'Manjeet': 1, u'Mukesh': 1, u'Bobby Khanna': 1, u'Indrajeet Mukherjee': 1, u'Jalil Parkar': 1, u'Mukesh Tiwari': 1, u'Puneet Vashist': 1, u'Amitabh Bachchan': 2, u'Amarjeet Amle': 1, u'Amrish Puri': 1, u'Jehan Manekshaw': 1, u'Mayura Baweja': 1, u'Atul Kumar': 1, u'Christopher Adamson': 1, u'Sudhir Nema': 1, u'Nathyn Masters': 1, u'Vaibhav Mathur': 1, u'Avantika': 1, u'Avinash Nimeshswami': 1, u'Srishti': 1, u'Pradeep Kapoor': 1, u'Sanjay Chawla': 1, u'Bob Christo': 1, u'G.P. Singh': 4, u'Jaspal Bhatti': 1, u'Nilesh G. Naik': 1, u'Joginder Shelly': 1, u'Ranbir Kapoor': 1, u'Amrit Pal': 1, u'Satish Shah': 3, u'Claire': 1, u'Madhu Malhotra': 1, u'Mona Parekh': 2, u'Rajeev Ravindranathan': 1, u'Vikas Anand': 3, u'Bharat Kapoor': 2, u'Sanjay Sinha': 1, u'Nasrin': 1, u'Munireh Guhilot': 1, u'Mushtaq Khan': 5, u'Ankush Mohla': 1, u'Tanay Chheda': 1, u'Nilesh Ali Khan': 1, u'Rajesh Tailang': 1, u'Shahnaaz': 1, u'Sheeba Chaddha': 1, u'Gajanan Jadhav': 1, u'Daya Shankar Pandey': 2, u'Kabeer Handa': 1, u'Shiva Rindani': 3, u'Waheeda Rehman': 1, u'Mohan Nigam': 1, u'Zeenat Aman': 1, u'Pranil Darzi': 1, u'Ajay Devgn': 1, u'Jay': 1, u'Rahul Khanna': 1, u'Pramod Moutho': 1, u'Rohini Ramanathan': 1, u'Imtiaz Khan': 1, u'Mahendra Sandhu': 1, u'Amrit Patel': 2, u'Manoj Shah': 1, u'K.C. Shankar': 1, u'Naginder Malawade': 1, u'Gautami Kapoor': 1, u'Salim Shah': 2, u'Banerji': 1, u'Anangsha Limaye': 1, u'Udita Seksaria': 1, u'A.S. Duggal': 1, u'Afsari Sayeed': 1, u'Upasna Singh': 2, u'Mihir Thakkar': 1, u'Babloo': 1, u'Bharat Bhushan': 1, u'Roger Welp': 1, u'James Lamont': 1, u'Kamal': 2, u'Javed Khan': 4, u'Aditya Srivastava': 1, u'Dolly Mattoo': 1, u'Bihari': 1, u'Suhaas Ahuja': 1, u'Lauren Vilips': 1, u'Prakash Khetani': 1, u'Rahoul Daswani': 1, u'Rajit Kapoor': 1, u'Jyoti Pawar': 1, u'Sudarshan Khurana': 1, u'Umesh': 1, u'Vanessa Rewrie': 1, u'Angelica Salek': 1, u'Chandrashekhar': 4, u'Nayani Dixit': 1, u'Anna Baird Galloway': 1, u'Girish Kulkarni': 1, u'C.S. Dubey': 1, u'Gurkirtan Chauhan': 1, u'Shankar Sachdev': 2, u'Jackie Shroff': 2, u'Brian Christensen': 1, u'Kartik Dutt': 1, u'Sharad Vyas': 1, u'Mac Mohan': 1, u'Robin Bhatt': 3, u'Ram Mohan': 3, u'Reena Aggarwal': 1, u'Brihan Lamba': 1, u'Kiran Zaveri': 1, u'Anupam Maanav': 1, u'Marianna Adaire': 1, u'Farrokh Jaffer': 1, u'Noor Jehan': 1, u'Agnes Darenius': 1, u'Sanjay Dadich': 1, u'Anurag Arora': 1, u'Kavi Kumar Azad': 1, u'Girish Kumar Menon': 1, u'Kenya Alexia Sauder Scolamieri': 1, u'Tinnu Anand': 1, u'Rubina Shaikh': 1, u'Apul Jaisinghani': 1, u'Sana Khan': 1, u'Shraddha Musale': 1, u'Sushma Seth': 1, u'Rajendranath Zutshi': 4, u'Stevan Rimkus': 1, u'Rehan Khan': 1, u'Nandita Das': 1, u'Shamsuddin': 1, u'Michael Terry': 1, u'Beena Banerjee': 4, u'Vikraal Vij': 1, u'Jamie Whitby Coles': 1, u'Nasir': 1, u'Veena': 1, u'Babbanlal Yadav': 3, u'Grace Santos': 1, u'Shabana Azmi': 1, u'Mukund Bhatt': 1, u'Master Rizwan': 1, u'Gurdeepak Kaur': 1, u'Jaswinder Sachdev': 1, u'Jitendra Singh': 2, u'Sanjay Sood': 1, u'Freny Bhagat': 1, u'Tarun Ghosh': 1, u'Deepak Shroff': 1, u'Simon Holmes': 1, u'Boman Irani': 2, u'Siddharth Nigam': 1, u'Mona Ambegaonkar': 1, u'Pubali Sanyal': 1, u'Shehzad Khan': 2, u'Irfanouzzaman': 1, u'Ashish Lakhia': 1, u'Jessica Bentley': 1, u'Nikita Bhatt': 1, u'Preeti Jain': 1, u'Haidar Ali': 1, u'Martijn Kuiper': 1, u'Rubina': 1, u'Salman Khan': 1, u'Mindy Turano': 1, u'Vinod Khanna': 1, u'Priyanka Chopra': 1, u'Denise E. Schroeder': 1, u'David Gant': 1, u'Menka Patel': 1, u'Jon House': 1, u'Jorge Magana': 1, u'Zubaida': 1, u'Meenal Limaye': 1, u'Rakesh Roshan': 2, u'Helen': 1, u'Pratibha Sinha': 1, u'Babby Singh': 1, u'Rajab Jaffri': 1, u'Uday Bhan Mourya': 1, u'Ketki Dave': 2, u'Babloo Mukherjee': 2, u'Lalit Tiwari': 1, u'Tabrett Bethell': 1, u'Pradeep': 1, u'Jayne McKenna': 1, u'Mugdha Kalra': 1, u'Raghuvir Yadav': 2, u'Brijendra Kala': 1, u'Ghanshyam Rohera': 2, u'Dhananjay Singh': 1, u'Rajinikanth': 1, u'Shivani Tanksale': 1, u'Richa': 1, u'Neha Sawant': 1, u'Vandana Sajnani': 1, u'Annapurna Kaul': 1, u'Harjeet': 1, u'Nitant Shrivastava': 1, u'V.K. Chanana': 1, u'Aasha Pawar': 1, u'Naveen Bawa': 1, u'Kunika': 1, u'Bijaya Jena': 1, u'Jagdeep': 2, u'Jennifer Winget': 1, u'Pradeep Kabra': 1, u'Ashwini Bhave': 1, u'Randhawa': 1, u'Scott Clayborne': 1, u'Ayesha DeVitre': 1, u'Srinivas': 1, u'Vipin Sharma': 1, u'Neelima': 1, u'Bharat Patil': 1, u'Rohit Tiwari': 1, u'Omi Vaidya': 1, u'Ravi': 1, u'Neeraj Sood': 1, u'Himanshu Trivedi': 1, u'Beena': 1, u'Nafisa Sharma': 1, u'Navneet Nishan': 4, u'Rupali Tiwari': 1, u'Dibyendu Bhattacharya': 1, u'Mehmood Jr.': 2, u'Anupam Shyam': 2, u'Larry Nazimek': 1, u'Nawazuddin Siddiqui': 2, u'Aditya Lakhia': 2, u'Janardhan Darab': 1, u'Sheridan Clayborne': 1, u'Alice Patten': 1, u'Sumit Khanna': 1, u'Mino Mackic': 1, u'Devender Kumar': 1, u'Raaj Gopal Iyer': 1, u'Rohini Hattangadi': 1, u'Reema Debnath': 1, u'Maria Goretti': 1, u'Ayaan': 1, u'Aditya Pancholi': 1, u'Rajeev Verma': 1, u'Taniya': 1, u'Paresh Ganatra': 2, u'Katrina Kaif': 1, u'Asrani': 5, u'Tom Alter': 1, u'Rani Kochhar': 1, u'Shaji Chaudhary': 1, u'Rajendra Jadhav': 1, u'Santosh Sivan': 1, u'Justine M. Constantino': 1, u'Jeetu': 1, u'Shama Sikander': 1, u'Anand Mishra': 1, u'Cyrus Sahukar': 1, u'Ramdas Jadhav': 1, u'Hafiz Khan': 1, u'Riyaz Khan': 1, u'Sanam Oberoi': 1, u'Mohini Mathur': 1, u'Subhash': 1, u'Arun Bali': 2, u'Sophiya Haque': 1, u'Pratima Kulkarni': 1, u'Kerry Casey': 1, u'Kiran Kumar': 2, u'Sonali Kulkarni': 1, u'Neeta Puri': 2, u'Neil Patrick': 1, u'Rakesh Bedi': 3, u'Rajeev Gaursingh': 1, u'Lalitha Lajmi': 1, u'Ayesha Jhulka': 2, u'Jineet Rath': 1, u'Saurabh Shukla': 1, u'Rakesh Maudgal': 1, u'Babita Sehgal': 1, u'Om Shivpuri': 1, u'Chitra Kopikar': 1, u'Vijay Anand': 1, u'Mamik': 1, u'Manisha Koirala': 2, u'Laraia Ashley Gribble': 1, u'Vikas Shrivastav': 2, u'Krishna Bansal': 1, u'Pariva Pranati': 1, u'Vijay Gupta': 1, u'Jim Nieciecki': 1, u'Suhas Joshi': 2, u'Sunil Dutt': 1, u'Linden Clayborne': 1, u'Shri Vallabh Vyas': 2, u'Samantha Tremayne': 1, u'Shivrama Singh': 1, u'Sukanya Kulkarni': 1, u'Divya Bhatia': 1, u'Padma Rani': 1, u'Dushyant Wagh': 1, u'Izabelle Farias': 1, u'Parikshat Sahni': 3, u'Sharmila Tagore': 1, u'Vinusha Singh': 1, u'Kuldip Sareen': 1, u'Richa Sharma': 1, u'Mandala Tayde': 1, u'Narendra Sharma': 1, u'Jaya Mathur': 3, u'Rajesh Puri': 4, u'Rohini': 1, u'Manmeet Singh': 1, u'Avtar Gill': 3, u'Anushka Sharma': 2, u'Kitu Gidwani': 3, u'Shehnaz Kudia': 2, u'Asin': 1, u'Kenneth Cranham': 1, u'Krantikari Singh': 1, u'Ashish Vidyarthi': 1, u'Ashalata Kashmiri': 1, u'Aashique Hussain': 1, u'Anup Jalota': 1, u'Tariq': 1, u'Khodus Wadia': 1, u'Rukhsar': 1, u'Karim Hajee': 1, u'Sonali Sachdev': 1, u'Rajiv Gupta': 1, u'Benjamin Gilani': 1, u'Tirth': 1, u'Rahul Singh': 1, u'Varun Mehta': 1, u'Pinky Chinoy': 1, u'Ishan': 1, u'Soumi Roy': 1, u'Master Ravi': 1, u'Salim Khan Ding-Dong': 1, u'Chandni Ansari': 1, u'Sunny Charles': 1, u'Nuzhat Khan': 1, u'Vinod Nahardih': 1, u'Anmol Charan': 1, u'Meenakshi Verma': 1, u'Tiger Wilson': 1, u'Rauf': 1, u'Ajit Vachani': 5, u'Aamir': 2, u'Neeraj Vora': 4, u'Sandeep Singh': 1, u'Savita Bhatti': 1, u'Shrirang Godbole': 1, u'Jambura': 1, u'Dan Latham': 1, u'Ishrat Ali': 2, u'Ashwin Kaushal': 1, u'Keshav Rae': 1, u'Jatin Pandit': 1, u'Saubhagya Shukla': 1, u'Ahmed': 1, u'Ajit': 1, u'Salma Aman': 1, u'Aakash Dabhade': 1, u'Baby Deepali': 1, u'Sagar Jha': 1, u'Jadav': 1, u'Baby Guddu': 1, u'Parmeet Sethi': 2, u'Vibha Chhibber': 1, u'Amjad Ali Warsi': 1, u'M.B. Shetty': 1, u'Master Sailesh': 1, u'Surekha Sikri': 1, u'Shyama': 1, u'Kulbhushan Kharbanda': 6, u'Sarvanna': 1, u'Sarah Irwin': 2, u'Madhav Datt': 1, u'Dan Ali': 1, u'Rajendra Mehra': 1, u'Tiku Talsania': 7, u'Shashi Sharma': 1, u'Pavan Malhotra': 1, u'K.K. Raj': 2, u'Salma': 1, u'Rishi': 1, u'Krupa Jayesh': 1, u'Manoj Pandya': 1, u'Sonamoni Jayant': 1, u'Suresh Oberoi': 1, u'Ahmed Khan': 6, u'Surendra Shetty': 1, u'Manik Irani': 1, u'Shenaz Treasury': 1, u'Farhan Akhtar': 1, u'Bhagwan Singh': 1, u'Nasir Khan': 1, u'Suresh Menon': 1, u'Rupali Jambulkar': 1, u'Kumar Veer Singh': 1, u'Om Prakash': 1, u'Twinkle Khanna': 1, u'Anamika': 1, u'Saroj Khan': 1, u'Reema Lagoo': 2, u'Subhash Kapoor': 1, u'Anu Ansari': 1, u'Tarun Kumar': 1, u'Reyub Khan': 1, u'Lekh Tandon': 1, u'Asha Sharma': 3, u'Anupam Kher': 4, u'Rajshri Deshpande': 1, u'Abby Rose Merrill': 1, u'Sulabha Arya': 1, u'Pompi': 1, u'Sia Chopra': 1, u'Lillete Dubey': 1, u'Siraj Syed': 1, u'Jamuna Das': 1, u'Jalal Agha': 1, u'Supriya Pathak': 1, u'Vitthal': 1, u'Dinesh Lamba': 1, u'Shefali Shetty': 2, u'Miro Svercel': 1, u'Deven Verma': 4, u'Yash Raj Jadhav': 1, u'Ninad Deshpande': 1, u'Manoj Joshi': 1, u'Bani Sharad': 1, u'Howard Lee': 2, u'Sanjay Taneja': 1, u'Jamdade': 1, u'H. Prakash': 2, u'Swarnesh Mohan': 1, u'Kareena Kapoor': 2, u'Pappu Khan': 1, u'Kamlesh Surve': 1, u'Bally Gill': 1, u'Fayaz Shaiyad': 1, u'Sanjeev Siddharth': 1, u'Ishaq Abbas Variya': 1, u'Ramesh Goyal': 4, u'Simran': 1, u'Camila Bordonaba': 1, u'Chaitali Bose': 1, u'Donald Burman': 1, u'Sunil': 1, u'Shweta': 1, u'Kara S. Leigh': 1, u'Ikhlaque Khan': 1, u'Bugs Bhargava': 2, u'Raja Awasthi': 1, u'Jeremy Clyde': 1, u'Lara Dutta': 1, u'Dalip Tahil': 8, u'Poorna Jagannathan': 1, u'Kapila': 1, u'Tanveer Ahmed': 1, u'Mohammed Irshad': 1, u"M'laah Kaur Singh": 1, u'Christopher Kahler': 1, u'Shefali': 1, u'Anand Subaya': 1, u'Pravishi Das': 1, u'Deepak Tijori': 4, u'Habib Tanvir': 1, u'Vijay Arora': 1, u'Govinda': 1, u'Kabir Chowdhury': 1, u'Jacqueline Scislowski': 1, u'Rakesh Pandey': 1, u'Sofia': 1, u'Asif Ahmed': 1, u'Narendra': 1, u'Rajesh Vivek': 1, u'Govind Namdeo': 1, u'Dabloo Mishra': 1, u'Saloni Mehta': 1, u'Alex Shirtcliff': 1, u'Abhishek Khanna': 1, u'Narendra Gupta': 1, u'Daya Dongre': 1, u'Shivaji Satam': 1, u'Abhijit Lahiri': 1, u'Rishi Kapoor': 1, u'Shilpa Mehta': 1, u'Dileep Desai': 1, u'Chirag Vohra': 1, u'Simon Hewitt': 1, u'Rajesh D. Desai': 1, u'Anusha Dhandekar': 1, u'Kailash Kher': 1, u'Murli Sharma': 1, u'Dinesh Kumar': 1, u'Shafi Inamdar': 2, u'Raakesh Maudgal': 1, u'Tushar Joshi': 1, u'Master Mazhar': 1, u'M.K. Raina': 1, u'Neelam Kothari': 2, u'Neville Dadachanji': 2, u'Birbal': 5, u'Sudhir Pandey': 2, u'Shammi': 3, u'Farida Jalal': 1, u'Ram Gopal Bajaj': 1, u'Ayesha Raza Mishra': 1, u'Raj Arjun': 1, u'Imran Khan': 3, u'Smriti': 1, u'Rajesh Joshi': 2, u'Jagdish Raj': 1, u'Ashraf-Ul-Haque': 1, u'Ali Shah': 1, u'Vijay Gaikwad': 1, u'Sharat Saxena': 2, u'Tisca Chopra': 1, u'Michelle Roman': 1, u'Dinesh Kaushik': 1, u'Tariq Vasudeva': 1, u'Abhimanyyu Abhimanyu': 1, u'John Cardiel': 1, u'Lushin Dubey': 1, u'Lawrence Fernandes': 1, u'Nitin Chandrakant Desai': 1, u'Dhaval Barbhaya': 1, u'Dinesh Phadnis': 2, u'Ssanjay Swaraaj': 1, u'Udayan Seksaria': 1, u'Surya Pratap Singh': 1, u'Deven Bhojani': 1, u'Frank M. Ahearn': 1, u'Rajashri Deshpande': 1, u'McKenzie Franklin': 1, u'Ramakant Burman': 1, u'Anjula Bedi': 1, u'Master Rajesh': 1, u'Sushant Singh Rajput': 1, u'Libert Olivera': 1, u'Weston Ford': 1, u'Dharmendar Singh': 1, u'Sulabha Deshpande': 1, u'Disha Vakani': 1, u'Suhas Vaidya': 1, u'Eric Brakke': 1, u'Ursula Ellis': 1, u'Shruti Seth': 1, u'Abhishek Bachchan': 2, u'Madhavan': 2, u'Neha Daniel': 1, u'Celil Gezer': 1, u'Nishi Singh': 1, u'Caprice Cole': 1, u'Arnav Valcha': 1, u'Kannu Gill': 1, u'Nick Beyeler': 1, u'Mahendra Mewati': 1, u'Hiralal': 1, u'Prem Sagar': 4, u'Anirudh Agarwal': 2, u'Farhat': 1, u'Cinia Jain': 1, u'Tsanwal Namgyal': 1, u'Kapil Mehta': 1, u'Sumona Chakravarti': 1, u'Charles Rasmussen': 1, u'Archana Joglekar': 1, u'Rajendra Patwardhan': 1, u'Thomas Castro': 1, u'Sonali Bendre': 1, u'Indira Chowdhary': 1, u"Shayna Nicole E'Orio": 1, u'Kushboo': 1, u'Insia Lacewalla': 1, u'Adi Irani': 1, u'Pooja Bhatt': 1, u'R.S. Kodange': 1, u'Subroto Mahapatra': 1, u'Harbans Darshan M. Arora': 1, u'Rohit Raj': 2, u'Radhika Sarathkumar': 1, u'Mita Vasisht': 1, u'Jamie Mackenzie Williams': 1, u'Radha Seth': 1, u'Sahida Shaikh': 1, u'Sanskruti Kher': 1, u'Ajai Rohilla': 1, u'Gulshan Grover': 4, u'Rajendra': 2, u'Shashi Kiran': 3, u'Kahlia Greksa': 1, u'Sonal Sehgal': 1, u'Raj Jamdade': 1, u'Hakikulla Sheikh': 1, u'Renuka Bondre': 1, u'Shinjini Raval': 1, u'Gulfam Khan': 1, u'Sonu': 1, u'Suresh Rokde': 1, u'Ashok Lokhande': 1, u'Master Tito': 1, u'Matthew W. Allen': 1, u'Saurabh Agnihotri': 1, u'Rahul Ram': 1, u'Ridhima Sud': 1, u'Joel Guyton Lee': 1, u'Dheerendra Dwivedi': 1, u'Utpal Dutt': 1, u'Neetu Singh': 1, u'Rohit Bhotica': 1, u'Martin Lustenberger': 1, u'Joy Helfrich': 1, u'Dayal Sharma': 1, u'Rani Mukerji': 4, u'Rahil': 1, u'Rakesh': 1, u'Pankaj Kapur': 1, u'Ravindra Kapoor': 4, u'Meghna Bhalla': 1, u'Debashish Naha': 1, u'Miki Khan': 1, u'Zafar Karachiwala': 1, u"Claire 'Fluff' Llewellyn": 1, u'Master Hero': 1, u'Dev Anand': 1, u'Ram P. Sethi': 1, u'Anjan Srivastav': 4, u'Noora': 1, u'Sameer Chitre': 1, u'Vir Das': 1, u'Asad Dadarkar': 1, u'Tej Sapru': 1, u'Eric Peterson': 1, u'Malani Ramani': 1, u'Shailja Dhar': 1, u'Olivier Lafont': 1, u'Raj Rani': 1, u'Baby Shivani': 1, u'Krishn Gopinath': 1, u'Carlos Woods': 1, u'Nandu': 1, u'Saeed Jaffrey': 2, u'Avdesh Kumar': 1, u'Sanjay Goradia': 3, u'Gracy Singh': 1, u'J. Anthony Kopec': 1, u'Michael L. Howard': 1, u'Raksha Mehta': 1, u'Jaywant Wadkar': 1, u'Shweta Menon': 1, u'Jonathan Alonso Flete': 1, u'Nimisha Goswami': 1, u'Shaji Krishnan': 1, u'Jeremy Child': 1, u'Raj Kishore': 1, u'Karishma': 1, u'Elinor Krueger': 1, u'Datta Sonawne': 1, u'Ishwak Singh': 1, u'Ravi Jhankal': 1, u'Berkeley Clayborne': 1, u'Nissar Khan': 1, u'Shraddha Verma': 1, u'Clarence': 1, u'Sunil Rege': 1, u'Priti Khatri': 1, u'Sunita Padbidri': 1, u'Mohan Joshi': 1, u'Ray Eves': 1, u'Anil Rajput': 1, u'Albert Welling': 1, u'Leslie Shraifer': 1, u'Ram Avtar': 1, u'Bhushan Tiwari': 1, u'Pallavi Bhaskar': 1, u'Bobby Sainy': 1, u'Krutika Desai': 1, u'Prashant Prakash': 1, u'Yash': 1, u'Trani': 1, u'Johnny Walker': 1, u'Chris England': 1, u'K.K. Azad': 1, u'Bryan Royston': 1, u'Deepali Dadekar': 1, u'Aparajita': 1, u'Rubai': 1, u'Preeti Mamgain': 1, u'Alexander Klein': 1, u'Alok Nath': 1, u'Atul Kulkarni': 1, u'Gauri Karnik': 1, u'Steven Mackintosh': 1, u'Rajesh Kareer': 1, u'Suraj Thapar': 1, u'Varsha Usgaonkar': 1, u'Shreeram Lagoo': 1, u'Rajkummar Rao': 1, u'Narendra Nath': 1, u'Goga Kapoor': 2, u'Sanya Malhotra': 1, u'Malvika Singh': 1, u'Mustan Tambawalla': 1, u'Amardeep Jha': 2, u'Dimple Inamdar': 1, u'Mahavir Shah': 1, u'Firoz Irani': 1, u'Sameer Khakhar': 2, u'Danish Hussain': 1, u'Mohnish Bahl': 1, u'Jacob M Williams': 1, u'L. Frost': 1, u'Himanshu': 1, u'Shernaz Patel': 1, u'Aamir Khan': 50, u'Aatin': 1, u'Abhay Singh': 1, u'Sharmila': 1, u'Master Karan': 1, u'Shaina': 1, u'Meenu Prajapati': 1, u'Badrul Islam': 1, u'Ramdas': 1, u'Rajendra Sethi': 1, u'Mukhtar Ahmed': 1, u'Kim Bodnia': 1, u'Ajay Thakkar': 1, u'Mahesh Gahalot': 1, u'Kunal Kapoor': 1, u'Akshai Puri': 1, u'Brij Gopal': 2, u'Tarnnum Khan': 1, u'Rakesh Sarang': 1, u'Nandita Thakur': 1, u'Sanjivani Oagle': 1, u'Ali Sichilongo': 1, u'Hrishikesh Pandey': 1, u'Elihud George': 1, u'Shahbaaz Khan': 1, u'Veeru Krishnan': 5, u'Kiran Randhawa': 1, u'Arif Zakaria': 1, u'Tahir Hussain': 1, u'Don Kress': 1, u'Fayaz Ahmed Shah': 1, u'Razak Khan': 5, u'Archana Puran Singh': 2, u'Ronnie Toms': 1, u'Shakti Kapoor': 2, u'Rita Bhaduri': 1, u'Mohan Gokhale': 1, u'Viral Thakkar': 1, u'Sumona': 1, u'Akshay Anand': 1, u'Prashant': 1, u'Dewayne Perkins': 1, u'Prithvi Zutshi': 1, u'Coral Beed': 1, u'Lucky Singh': 1, u'Achyut Potdar': 3, u'Suhani Bhatnagar': 1, u'Faisal Khan': 3, u'Maanvi Gagroo': 1, u'Hale Cigek': 1, u'Nagesh Salwan': 1, u'Gary W Golden': 1, u'Master Kunal': 1, u'Jayshree T.': 1, u'Farida Dadi': 1, u'Moolchand': 1, u'Andrew Popovich': 1, u'M.N. Alam': 1, u'Madhur Bhandarkar': 1, u'Madhuri Dixit': 2, u'Sashi Gupta': 1, u'Gabriel John': 1, u'Eddie J. Fernandez Jr.': 1, u'Adil Sheikh': 1, u'Shaikh Sami': 1, u'Madison Moran': 1, u'Aditi Vasudev': 1, u'Gafoor': 1, u'Gulshan': 2, u'Subbiraj': 2, u'Kishore Sawant': 1, u'Ravi Kumar': 1, u'Manoj Sharma': 1, u'Shubha Khote': 2, u'Aman Sagar': 1, u'Dinesh Hingoo': 3, u'Amin Gazi': 1, u'Ashutosh Rana': 1, u'Dimple Kapadia': 1, u'Navtej Singh Johar': 1, u'Naaz Sayyed': 1, u'Karinna Greksa': 1, u'Sanjay Ingle': 1, u'Farookh Shaikh': 1, u'Jagbir': 1, u'Nafisa Amin Khan': 1, u'Jitendra Shinde': 1, u'Soha Ali Khan': 1, u'Iqbal Dosani': 1, u'Jehangi Ratansha Karkaria': 1, u'Prubidal Singh Pannu': 1, u'Shoaib Ahmed': 1, u'Uma Dutt': 1, u'Ved Thappar': 1, u'Pooja Bedi': 2, u'Rahul Pendkalkar': 2, u'Manish': 1, u'Raza Murad': 3, u'Anix Vyas': 1, u'January Stern': 1, u'Naseem': 1, u'Robert Finlayson': 1, u'Zaira Wasim': 2, u'Komal Jha': 1, u'Joya': 1, u'Supriya Shukla': 1, u'Prince Paul': 1, u'Yashpal Sharma': 1, u'Viju Khote': 8, u'Akshaye Khanna': 1, u'Sopariwala': 1, u'Satindir Anand': 1, u'Merlin Lucian': 1, u'Anila Chandan': 1, u'Ajit Soni': 1, u'Debanshi Shah': 1, u'Anil Saxena': 1, u'Neena Cheema': 1, u'Sopreet Redot': 1, u'Sakshi Tanwar': 1, u'Akhilendra Mishra': 2, u'Sadashiv Amrapurkar': 1, u'Robert': 1, u'Alyssa Fountoutalis': 1, u'Vivek Madaan': 1, u'Tarikh': 1, u'Toby Stephens': 1, u'Ali Khan': 1, u'Digesh': 1, u'Gajendra Ojha': 1, u'Jayant Kripalani': 1, u'Sanjay Batra': 2, u'Prithvi': 1, u'Girija Oak': 1, u'Merlyn': 1, u'Aslam': 1, u'Mona Saxena': 1, u'Ghanshyam Nayak': 1, u'Megha Bengali': 1, u'Yousaf Bokhari Bustamante': 1, u'Pramatesh Mehta': 1, u'Nilofar': 1, u'Shilpa': 1, u'Jagesh Mukati': 1, u'Jordyn Paige Bolber': 1, u'Anita Neha': 1, u'Chitresh Ranjan': 1, u'Ramesh Khanna': 1, u'Mick Ward': 2, u'Sanjeev Gandhi': 1, u'Micheal Ward': 1, u'Homi Mulla': 1, u'Kiran Deep Jagi': 1, u'Ulhas Barve': 1, u'Deepti Naval': 1, u'Kevin Lingle': 1, u'Rajesh S. Khatri': 1, u'Sukrit Dhandhania': 1, u'Jankidas': 1, u'Sarla Yeolekar': 1, u'Kim DeJesus': 1, u'Balwant Jadhav': 1, u'Cyrus Khatau': 1, u'Annabelle': 1, u'Ayub Khan': 2, u'Vishesh Kaul': 1, u'Abhijit Kulkarni': 1, u'Zarina Wahab': 1, u'Rio Kapadia': 1, u'Aftab Shivdasani': 1, u'Kajol': 2, u'Saif Ali Khan': 2, u'Jagdish': 1, u'Vivan Bhatena': 2, u'Indu Verma': 1, u'Sayed Allahabadi': 1, u'Tayyab Qureshi': 1, u'Rachel Shelley': 1, u'Akbar': 1, u'Siddharth': 1, u'Ali Haji': 1, u'Madhukar Toradmal': 1, u'Yatin Karyekar': 2, u'Lala Nazir': 1, u'Sanjana': 1, u'Veer Prakash Nayar': 1, u'Pran': 1, u'Ritwik Sahore': 1, u'Kishor Patil': 1, u'Mukesh Ahuja': 1, u'Tarun': 1, u'Khushi': 1, u'Nitin Shingal': 1, u'Shiney Ahuja': 1, u'Suman': 1, u'Aakarsh Chandan': 1, u'Sanjay Dutt': 1, u'Pappu Polyester': 1, u'Mangesh K. Kshirsagar': 1, u'Bhim Vakani': 1, u'Dave': 1, u'Shubhangi Latkar': 1, u'Rita': 1, u'Praful Kulkarni': 1, u'Ramit Gupta': 1, u'Kriz Chris Henri Harriz': 1, u'Anil Upadhyay': 2, u'Vivek Mishra': 1, u'Raju Barot': 1, u'Amar Banerjee': 1, u'Larry Hauge': 1, u'Bipin Nadkarni': 1, u'Delphine Pontvieux': 1, u'Suresh Bhagwat': 3, u'Ali Fazal': 1, u'Kabir Shaikh': 1, u'Sarah Neilson': 1, u'Sandeep Lokre': 1, u'Mukesh Rishi': 3, u'Sachin Parikh': 1, u'Madhav Vaze': 1, u'Raman': 2, u'Sunil Grover': 1, u'Sharokh Bharucha': 2, u'Akash': 1, u'Uday Chopra': 1, u'Dharmendra': 1, u'Ashutosh Gowariker': 1, u'Ashoo': 2, u'Puneet Issar': 1, u'Shireesh Sharma': 1, u'Atul Tiwari': 1, u'Master Adil': 1, u'Mukesh Chhabra': 1, u'Suruchi Aulakh': 1, u'Jeet Upendra': 1, u'Satyendra Kapoor': 5, u'Raj Khandelwal': 1, u'Blaine Mallory': 1, u'Subrat Dutta': 2, u'Prakash': 2, u'Alorika Chatterjee': 1, u'Ravinder Kumar': 1, u'C.K. Taneja': 1, u'Norma Lobo': 1, u'Ajit Mehra': 1, u'Akhil Mishra': 1, u'Jiah Khan': 1, u'Bryan Conner': 1, u'Ayush Morarka': 1, u'A.K. Hangal': 1, u'Ekta Sohini': 1, u'Laurence Spellman': 1, u'Anil Chandra Prakash': 1, u'Arif': 1, u'Farha Naaz': 2, u'Ruhi Khan': 1, u'Beatrice Gibson': 1, u'Rakesh Kumar': 1, u'Hitesh Tak': 1, u'Ahsan Baksh': 1, u'Sheela Sharma': 1, u'Vrajesh Hirjee': 1, u'Girja Shankar': 1, u'Khushi Dubey': 1, u'Kalpana Iyer': 2, u'Sitaram Sharma': 1, u'Anjana Mumtaz': 1, u'Raxit Patel': 1, u'Keshav Rana': 1, u'Maia Sethna': 1, u'Navin Kumar': 3, u'Lata Kurdikar': 1, u'Arthur-Angelo Sarinas': 1, u'Prakash Agarwal': 1, u'Urmila Matondkar': 1, u'Dimple Shah': 1, u'Somesh Agarwal': 1, u'Tanvi Azmi': 2, u'Nausha Khan': 1, u'Radhika Singh': 1, u'Ameesha Patel': 1, u'Dipti Avlani': 1, u'Naina Balsaver': 1, u'Reshma': 1, u'Anand Balraj': 1, u'Afzal': 1, u'Rajendra Gupta': 1, u'Dilip Pavle': 1, u'Dhanna': 1, u'Om Puri': 4, u'Almas Khan': 1, u'Yaprak Piren Karpuzoglu': 1, u'Rajeev Mehta': 1, u'Deb Mukherjee': 1, u'Aishwarya Rai Bachchan': 1, u'Shishir Sharma': 2, u'Ashok Jain': 1, u'Sachet Engineer': 1, u'Aparshakti Khurana': 1, u'Vikram Gokhale': 1, u'Manoj Bakshi': 1, u'Deepak Kejriwal': 1, u'Javed Jaffrey': 3, u'Gurbachchan Singh': 1, u'Karisma Kapoor': 2, u'Pawan Chopra': 1, u'Hussain': 1, u'Sandeep Sidhwani': 1, u'Robert Bobinsky': 1, u'Salome Narayana Polaki': 1, u'Swagata Sharma': 1, u'Louis Scherschel': 1, u'Anjum Rajabali': 1, u'Juhi Chawla': 8, u'Baby Ashrafa': 1, u'Paresh Rawal': 5, u'Harvinder Singh': 1, u'Arif Tahir': 1, u'Tommy Martin': 1, u'Jaffar Hussain': 1, u'Olia Klein': 1, u'Arjun': 1, u'Ozge Cagaloglu': 1, u'Graham Cull': 1, u'Roshan Banu': 1, u'Archana': 1, u'Lisa Millett': 1, u'Hudson Ford': 1, u'Shekhar Shukla': 1, u'Prateik': 1, u'Janet Hookway': 1, u'Mehmood': 1, u'Rakesh Shrivastava': 1, u'Sanaya Irani': 1, u'Kunal Khemu': 2, u'Dharmendra Bhurji': 1, u'Shail Mehta': 1, u'Dayanand Shetty': 1, u'Ricky': 1, u'Preity Zinta': 1, u'Bomi Doctor': 1, u'Master Wajid': 2, u'Ashraf Ul Haq': 3, u'Mevlana St. James': 1, u'Emrah Kolukisaoglu': 1, u'Akash Ajmera': 1, u'Saagar Kale': 1, u'Mohan Agashe': 1, u'Sachin Patil': 1, u'Rocky Rector': 1, u'Roma Manik': 1, u'Barry Hart': 1, u'Raju Shrestha': 1, u'Harjeet Walia': 1, u'Preet Oberoi': 1, u'Mamta Kulkarni': 1, u'Rashid': 1, u'Mona Singh': 1, u'Kunaal Roy Kapur': 1, u'Veerendra Saxena': 1, u'Deepak Shirke': 1, u'Veer Mohan': 1, u'Rajat Kapoor': 1, u'Raju Kher': 2, u'Neeraj Vikram': 1, u'Kabir Bedi': 1, u'Habib Khan': 1, u'Lauren Walker': 1, u'Ramya Krishnan': 1, u'Keira McCarthy': 1, u'Rahul Ranade': 1, u'Avneet Singh': 1, u'Rishabh Chaddha': 1, u'Mandar Gokhale': 1, u'Suchitra Pillai': 1, u'Jayme Wojciechowski': 1, u'Chandan Roy Sanyal': 1, u'Rahul Bose': 1, u'Johnny Lever': 4, u'Nawab': 2, u'Pundit Prayag Raj': 1, u'Chitra Deshmukh': 1, u'Vivienne Pocha': 1, u'Kader Khan': 2, u'Mahesh Raj': 2, u'Tinnu Verma': 2, u'Kriti Malhotra': 1, u'Chandu': 1, u'K.B. Jatin': 1, u'Darshana': 1, u'Riya Ray': 1, u'Sunil Shende': 1, u'Khalid Siddiqui': 1, u'Harish Iyer': 1, u'Deepak Malhotra': 1, u'Bianca Mare': 1, u'Vedant Nerurkar': 1, u'Rahul Kumar': 1, u'Aniket Engineer': 1}
    data =  actor_relations_translator(relations_dict, size)
    return data

# Performs computation essential for plotting of network graph
def actor_relations_omdb(movies_list, size, limit_movies):
    API_ENDPOINT = 'http://www.omdbapi.com/?t='
    relations_dict = {}
    for movie in movies_list[:limit_movies]:
        print movie['title']
        movie_detailed = requests.get(API_ENDPOINT + movie['title'])
        try:
            for actor in movie_detailed.json()['Actors'].split(','):
                if relations_dict.get(actor, None) is not None:
                    relations_dict[actor] += 1
                else:
                    relations_dict[actor] = 1
        except KeyError:
            print "can't find actors in movie: " + movie['title']
    print relations_dict
    data =  actor_relations_translator(relations_dict, size)
    return data

# Translates the results returned by the actor_relations into a
# format understood by the nvd3 library used in frontend.
def actor_relations_translator(relation_dict, size):
    sorted_relationships = sorted(relation_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True)
    if len(sorted_relationships) > size:
        sorted_relationships = sorted_relationships[:size]
    nodes = [{"name": key, "group": value/2, "relation_score": value} for (key, value) in sorted_relationships]
    links = [{"source": 0, "target": i ,"value": d['relation_score']} for i, d in enumerate(nodes)]
    translated_relations = {"nodes": nodes, "links": links}
    return translated_relations

# Called by the api for actors
def get_actor(request):
    ALL_MOVIES = 500
    search_text = request.GET.get('search', 'None')
    limit_movies = int(request.GET.get('limit_movies', ALL_MOVIES))
    ia = initiate_imdb_api()
    actor_query_set = ia.search_person(search_text)
    if len(actor_query_set) == 0:
        return HttpResponse('no such actor found')
    actor_id = actor_query_set[0].personID
    try:
        print 'in try: {}'.format(actor_id)
        actor_db_obj = Actor.objects.get(pk=actor_id)
        jsonDec = json.decoder.JSONDecoder()
        data = jsonDec.decode(actor_db_obj.response_data)
    except:
        actor_details = ia.get_person(actor_id)
        data = actor_details_translator(actor_details, limit_movies)
        create_actor_entry(actor_id, actor_details, data)
    jd = JSONRenderer().render(data)
    return HttpResponse(jd)

def create_actor_entry(actor_id, actor_details, data):
    gender = 'actor' if actor_details.has_key('actor') else 'actress'
    actor_data = {
        'id' : actor_id,
        'name' : actor_details['name'],
        'gender' : 'male' if actor_details.has_key('actor') else 'female',
        'image' : actor_details['full-size headshot'],
        'biography' : actor_details['biography'],
        'response_data' : json.dumps(data)
    }
    actor_db_obj = Actor(**actor_data)
    actor_db_obj.save()
    print 'actor saved'

# helper function to append the personID to the returned JSON
# not used currently by the frontend, would help in future.
def append_actor_id(actors_list):
    for actor in actors_list:
        actor['id'] = actor.personID
    return actors_list

# translates the result returned by the api in something
# underestood by the frontend
def actor_details_translator(actor_details, limit_movies):
    response_data = {}
    relation_dict = {}
    work_count = 0
    gender = 'actor' if actor_details.has_key('actor') else 'actress'
    if actor_details.get(gender, None):
        relation_dict = actor_relations_omdb(actor_details[gender], 40, limit_movies)
        response_data['recent_movies'] = make_movies_serializable(actor_details[gender][:limit_movies])
        work_count = len(actor_details[gender])
    try:
        response_data['headshot'] = actor_details['full-size headshot']
        response_data['biography'] = actor_details['mini biography'][0]
    except KeyError:
        print 'some data was not found'
        pass
    response_data['relations'] = relation_dict
    response_data['work_count'] = work_count
    response_data['name'] = actor_details['name']
    return response_data

# Called by the api for movies
def get_movie(request):
    search_text = request.GET.get('search', 'None')
    ia = initiate_imdb_api()
    movie_query_set = ia.search_movie(search_text)
    if len(movie_query_set) == 0:
        return HttpResponse('no such movie found')
    movie_id = movie_query_set[0].movieID
    movie_details = ia.get_movie(movie_id)
    #data = movie_details
    data = movie_details_translator(movie_details)
    jd = JSONRenderer().render(data)
    return HttpResponse(jd)

# helper function to append the movie id to the returned JSON
# not used currently by the frontend, would help in future.
def make_movies_serializable(movies_list):
    ret_list = []
    for movie in movies_list:
        movie_dict = {}
        movie_dict['id'] = movie.movieID
        movie_dict['title'] = movie['title']
        movie_dict['year'] = movie['year']
        ret_list.append(movie_dict)
    return ret_list

# translates the result returned by the api in something
# underestood by the frontend
def movie_details_translator(movie_details):
    response_data = {}
    try:
        response_data['rating'] = movie_details['rating']
        response_data['runtime'] = movie_details['runtimes'][0]
        response_data['plot'] = movie_details['plot outline']
        response_data['cover_url'] = movie_details['full-size cover url']
    except KeyError:
        print 'some data was not found'
        pass
    response_data['year'] = movie_details['year']
    response_data['title'] = movie_details['title']
    response_data['languages'] = movie_details['languages'] # List
    response_data['genres'] = movie_details['genres'] # List
    response_data['director'] = movie_details['director'][0]['name']
    # taking top 10 actors of a movie
    response_data['cast'] = append_actor_id(movie_details['cast'][:10])
    return response_data
