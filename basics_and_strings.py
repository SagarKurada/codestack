List:
i) Removing duplicates:
    mylist = list(dict.fromkeys(mylist))
ii) 




# test python file
#sagar-updated
1.List Comprehensions:
  p= [ ([ i, j,k])for i in range( x + 1) for j in range( y + 1) for k in range(z+1) if ( ( i + j+ k ) != n )]
    print(p)

2.1Split Function:
  returns a list of strings after breaking the given string by the specified separator
  word = 'geeks, for, geeks'
  print(word.split(', '))# splits on commas
  ['geeks', 'for', 'geeks']
  
 2.2 word.partition('#) :acts like a delimiter
  
   y,m,d=map(int,date.split('-'))

3.Map Function:
  Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
  def addition(n): 
    return n + n
  numbers = (1, 2, 3, 4) 
  result = map(addition, numbers) 
  print(list(result))
  {2, 4, 6, 8}
  
4.Join Function:
  myTuple = ("John", "Peter", "Vicky")
  x = "#".join(myTuple)
  John#Peter#Vicky

5.Checking and converting to upper/lower
  list=[x for x in s]
  h=[x.upper() if x.islower() else x.lower() for x in list ]
  g=''.join(h)

6.Print Function
  print("Hello {} {}! You just delved into python.".format(a,b))
 
7.String to a list : list(string)
  
8.List to a string :''.join(list)
  
9.Find the position of a  substring within the string
  testString1.find('xxy')
  testString1.rfind('l')

10.Text Allignment
    width = 20
    print 'HackerRank'.ljust(width,'-')
    print 'HackerRank'.center(width,'-')
    print 'HackerRank'.rjust(width,'-')
    HackerRank---------- 
    -----HackerRank-----
    ----------HackerRank
 
11.Text Wrapping 
   print textwrap.fill(string,max_width) : breaking a paragraph or long string in line by line 
   print textwrap.wrap(string,max_width) : lists

12. Supressing next line print
    for i in range(1, n+1):
        print(i, end = '') # end forces the print to come on the same line

13. Reverse a list
    list.reverse()
    print(list)
    list[::-1]
    
14.1  Finding number of occurences/index numbers of a substring in a string
    def count_substring(string, sub_string):
      count = [i for i in range(len(string)) if string.startswith(sub_string, i)]
      return len(count) # for number of occurences
      return count # for list containiing index numbers of occurences
    Count=keyboard.index(j)
            
14.2 To find whether an element is there in a list or not
        m=[x for x in l if x in arr3]
                   
 
15. String validators: syntax - string.func()
    isdigit()
    isalpha()
    isalnum()
    islower()
    isupper()

16. Capitalize first letter of each word in a string
    import string
    answer = string.capwords(sentence, sep = None)

17. Finding all possible substrings in a string
    length = len(input_string)
    print [input_string[i:j+1] for i in range(0, length) for j in xrange(i,length)]
   
18. Sort: i) sorted(list) : gives the list
         ii) sort.list()
             print(list)

19. EOF - End of file error. If the input is initiated once, we can call the function only once. Other wise, we get EOF error. 

20. The major difference is that sets, unlike lists or tuples, cannot have multiple occurrences of the same element and store unordered values.

21. List to dictionary: 
    Collections:i) A counter is a container that stores elements as dictionary keys, 
                 and their counts are stored as dictionary values.
                ii) A Counter is a dict subclass for counting hashable objects. 
                    It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
                    Counts are allowed to be any integer value including zero or negative counts.
                    The Counter class is similar to bags or multisets in other languages.
    from collections import Counter
    print(Counter(myList).items()) : returns the dictionary ( Also can use .keys, .values)
      
21.1 List index to dictionary values - Key will take only one value
      d = {b:i for i,b in enumerate(B)} 
      
     
    
21.2 List index to dictionary values - 
     a) Key taking multiple values

     ll=[[b,i] for i,b in enumerate(B)]
     import collections
     d = collections.defaultdict(list)
     for k,v in ll:
      d[k].append(v)
   
     b) #indices as count
        d={}
        for i in l:
            d[i]=d.get(i,0)+1

        # indices as values
        d_1={}
        for i,num in enumerate(l):
            if num not in d_1:
                d_1[num]=[i]
            else:
                d_1[num].append(i)

21.3 The defaultdict tool is a container in the collections class of Python. 
    It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will
    have a default value if that key has not been set yet.
 
22. Hashable objects: which has fixed function and unchangeable. Ex: tuple, int, string

23. To check whether the dictionary has the key :
    if dic[key]:
      True
      
24. Storing index as value:
    for i in range(0,n):
    d[raw_input()].append(i+1)
 
25. Named Tuple:    Link
  
     i)from collections import namedtuple
      Marks = namedtuple('Marks', 'physics, chemistry, biology')
      m1 = Marks('87', '54', '69')
      print(m1.chemistry)
      
    ii) m2 = Marks._make(['63','72','94'])
        print(m2)
      
    Example:
      from collections import namedtuple

      (n, categories) = (int(input()), input().split())
      Grade = namedtuple('Grade', categories)
      marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
      print((sum(marks) / len(marks)))
 
26. Collections- Python 
    https://towardsdatascience.com/a-hands-on-guide-to-python-collections-aa350cb399e3
    
    
27. To count the unique elements in the list:
    Either use set or counter
    shoes = collections.Counter(map(int, raw_input().split()))
    
    from operator import itemgetter

    chars = list(input())
    d = [[c,chars.count(c)] for c in set(chars)]
    d.sort(key=itemgetter(0))
    d.sort(key=itemgetter(1), reverse=True)
    for i in d[:3]:
        print("{0} {1}".format(i[0], i[1]))

28. Deque:
    The deque is a list optimized for inserting and removing items.
    Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same  
    O(1) performance in either direction
    d=deque()
    list = [1, 2, 3, 4, 5]
    deq = deque(list)
    d.rotate(3)
    d.popleft() : gives the the left most object
    d.pop(index number)
    https://www.geeksforgeeks.org/deque-in-python/
    
29. Itertools:
    product(A, B) returns the same as ((x,y) for x in A for y in B).
    
30. Append and Extend:
    append adds an element to a list, and extend concatenates the first list 
    with another list (or another iterable, not necessarily a list.)
    x = [1, 2, 3]
    x.append([4, 5]) : [1, 2, 3, [4, 5]]
    x.extend([4, 5]) : [1, 2, 3, 4, 5]

31. Args & Kwargs: [def(*agrs), def(*kwargs)]
    https://www.geeksforgeeks.org/args-kwargs-python/


32. import math
    math.degrees() # to convert angle calculation to degrees
    math.atan() # to calculate tan of an angle
    pow(x, 2) # raise x to the power of 2. Both pow() and math.pow() are slower than ** 
    divmod(177, 10) # gives both - quotient and remainder of the division in a tuple ---> answer = (17, 7)

33. itertools:
    from itertools import permutations/combinations/combinations_with_replacement
    print list(permutations('abc',3))
    answer = [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
    
    from itertools import groupby
    for (key,group) in groupby(numbers): 
    print (key,list(group))
    answer = (1, [1, 1, 1])
              (3, [3, 3])
              (2, [2, 2])
              (1, [1, 1])
          
34. Getattr: The getattr() function returns the value of the specified attribute from the specified object.
     getattr(object, attribute, default)
    for _ in range(int(input())):
      inp = input().split()
      getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
    print(*[item for item in d])

35. from collections import defaultdict
    d = defaultdict(lambda: -1)
    defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default value, in this case -1.

36. from collections import OrderedDict
    It is a dictionary where keys maintain the order in which they are inserted.
    
    ordered_dictionary = OrderedDict()
    for _ in range(int(input())):
        item, price = input().rsplit(' ', 1) # 1 specifies the number of times split can happen
        ordered_dictionary[item] = ordered_dictionary.get(item, 0) + int(price) # get retrieves the value from the container. O specifies the default value to be returned
    [print(item, ordered_dictionary[item]) for item in ordered_dictionary]
    
 37. To know the the type of error:
     for i in range(int(input())):
     try:
        a,b=map(int,input().split())
        print(a//b)
     except Exception as e:
        print("Error Code:",e)
        
 38. Regex : Reg. exp. is a sequence of characters that define a search pattern. 
     Patterns are used by string searching algorithms for "find" or "find and replace" operations on strings, 
     or for input validation. 
      
     Find, Search, Split, Subject:
     str = "The rain in Spain"
     x = re.findall("ai", str): ['ai', 'ai']
     x = re.search("\s", str): If there is more than one match, only the first occurrence of the match will be returned : 3
     x = re.split("\s", str, 1): ['The','rain in Spain']
     x = re.sub("\s", "9", str) :The9rain9in9Spain
     x = re.sub("\s", "9", str, 2):The9rain9in Spain
      
     
     https://www.w3schools.com/python/python_regex.asp
      
     import re
     re.split(r"[.,]", "any sample string containing , and .") - square parenthesis ensure that the string is split on both- . and ,
      
     >>> import re
      >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com') - w is for words, + is for all occurences
      >>> m.group(0)       # The entire match 
      'username@hackerrank.com'
      >>> m.group(1)       # The first parenthesized subgroup.
      'username'
      >>> m.group(2)       # The second parenthesized subgroup.
      'hackerrank'
      >>> m.group(3)       # The third parenthesized subgroup.
      'com'
      >>> m.group(1,2,3)   # Multiple arguments give us a tuple.
      ('username', 'hackerrank', 'com')
      >>> m.groups()
      ('username', 'hackerrank', 'com')
      >>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
      >>> m.groupdict()
      {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
      
      
      m = re.search(r"([a-z0-9])\1+", input()) - more than 1 occurences for group 1
      print(m.group(1) if m else -1)

 39. Zip Fucntions: 
     This function returns a list of tuples. 
     The th tuple contains the th element from each of the argument sequences or iterables.
     If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.
     i) zip([1,2,3,4,5,6],'Hacker')
     [(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
     ii) A = [1,2,3], B = [6,5,4], C = [7,8,9]
         X = [[A],][B],[C]] = [[1,2,3],[6,5,4],[7,8,9]]
         print zip(*X)
         [(1, 6, 7), (2, 5, 8), (3, 4, 9)]
         for i in zip(*X):
            sum(i)/len(i)
 40. Strip: Removes all the leading and trailing spaces from a string
     string = '   Geeks for Geeks   '
     print(string.strip()) : Geeks for Geeks
     print(string.strip('   Geeks')) : for
     string = 'www.Geeksforgeeks.org'
     print(string.strip('.grow')) : Geeksforgeeks
 
41. Sorting of lists of lists based on particular index : 
         sorted(arr,key = lambda x: x[k])
         

42. any([1>0,1==0,1<0]) : True
    all(['a'<'b','b'<'c']) : True
      
43. List Comprehensions: 
    [i for i in range(8) if i%2!=0]
    [i for i in range(8) if i%2==0 if i%3==0] : Nested Loop
    ["Even" if i%2==0 else "Odd" for i in range(8)] : If-Else 
    all(i>0 for i in ls) - postivity check using for loop format
    any(str(i)==str(i)[::-1] for i in ls) - palindrome check unding for loop format
  
44. Palindrome/Reverse 
    i[::]=i[::-1]
45. Filter: l = list(filter(lambda x: x > 10 and x < 80, l))
46. Reminder : y%x
47. Replace :
    return address.replace('.', '[.]')
    return address.replace('.', '[.]',n) : 'n' replacememts
48. Create list of single item repeated N times
     [5]*n
49. Comparing the lists and checking the count
       sum(map(S.count, J)) 
50. If else:
      count += 1 if ch == "L" else -1
51. Enumerate:
    for count,ele in enumerate(l1,100): 
    print count,ele 
    
52. Linked List: 
     answer = 0
        while head: 
            answer = 2*answer + head.val 
            head = head.next 
        return answer 
53. //: divide with integral result (discard remainder)
54. Ord function:
    Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, 
    or the value of the byte when the argument is an 8-bit string.
55. Get Function :
     The get() method is used to avoid such situations. This method returns the value for the given key, if present in the dictionary. 
      If not, then it will return None (if get() is used with only one argument).
  
56. List to dictionaries:
     d={}
        for i in A:
            d[i]=d.get(i,0)+1
        print(d)
        a=max(d.values())
        for k,v in d.items():
            if v== a:
                return k
              
 57. Reversing an integer:
    def reverse(self, x: int) -> int:
        if x>0:
            s=1
        else:
            s=-1
            x=-x
        result =0
        while(x>0):
            result=(10*result)+(x%10)
            x=x//10
        return 0 if result > pow(2, 31) else result*s
        
 58. Printing the alphabets:
    capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    
 59. BFS:
    row, col = len(grid), len(grid[0])
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        timer = 0
        while fresh:
            if not rotting: return -1
            rotting = {(i+di, j+dj) for i, j in rotting for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh}
            fresh -= rotting
            timer += 1
        return timer
    
  60. Sorting of group of sentences
      letters.sort(key = lambda x: x.split()[1]) # based on first word of every sentence
      letters.sort(key = lambda x: x.split()[1:]) #based on all sentences from first word
    
  61. Palindrome-Alphanumeric:
      s = [c.lower() for c in s if c.isalnum()]
       return s == s[::-1]
  62. DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    count  += 1
        print(grid)
        return count
    # use a helper function to flip connected '1's to 0
    def dfs(self,grid,i,j):
        grid[i][j] = '0'
        for c,r in [i-1,j],[i+1,j],[i,j-1],[i,j+1]:
            if 0 <= c < len(grid) and 0 <= r < len(grid[0]) and grid[c][r] == '1':
                self.dfs(grid,c,r)
                
   63. Insert :
       for i, v in zip(index, nums):
            res.insert(i, v)
   64. Creating a list = [0]*n
       Creating a matrix = rows=[0]*n ; cols =[0]*n
    
   65. XOR function:
       0^0 - 0
       1^0 - 1
       1^1 - 0
       0^1 - 1
    
   66. Prime - Time Complexity:
        def countPrimes(self, n: int) -> int:
        l=[]
        if n<3:
            return 0
        l=[1]*n
        #print(l)
        l[0]=0
        #print(l)
        l[1]=0
        #print(l)
        m=2
        while m*m<n:
            if l[m]==1:
                l[m*m:n:m]=[0]*(1+(n - m * m - 1) // m)
            m+=1 if m==2 else 2
        return sum(l)
    67. def find_sub_sets(nums):
            z_list = []
            sub_sets = []
            for i in range(len(nums)):
                if nums[i] == 0:
                    z_list.append(i)
            #print(z_list)
            i = 0
            j=0
            for k in range(len(z_list)):
                j = z_list[k]
                sub_sets.append(nums[i:j])
                i = j + 1
                if j==z_list[-1]:
                    sub_sets.append(nums[i:])     

            return sub_sets
     68. Selecting elements for the given target sum
          Sorted Converging solutions:
             def sa(s,net):
                i=0
                j=len(s)-1
                while(i<j):
                    if s[i]+s[j] == net:
                        return [i,j]
                    elif s[i]+s[j] >= net:
                        j=j-1
                    else:
                        i=i+1
         Unsorted solns
         def sa(s,net):
            import collections
            d=collections.Counter(s)
            #print(d)
            for k,v in d.items():
                diff=net-k
                if diff==k and k in d.keys() and d[k]>1:
                    return [k,k]
                elif diff in d.keys() and diff!=k :
                    return [k,diff]
            return False
      
    69. Maximum 2 numbers in the list:
             max_1=float("-inf")
            max_2=float("-inf")
            for i in range(len(l)):
                if l[i]>= max_1:
                    max_2=max_1
                    max_1=l[i]
                if l[i] > max_2 and l[i] < max_1:
                    max_2=l[i]
            print(max_1,max_2)
            
    70. Minimum 2 numbers in the list:
            min_1=float("inf")
            min_2=float("inf")

            for i in range(len(l)):
                if l[i] <= min_1:
                    min_2=min_1
                    min_1=l[i]
                if l[i] < min_2 and l[i] > min_1:
                    min_2=l[i]
            print(min_1,min_2)
    71. Peak Finding
         def p_f(l,start,end):
            mid=start+(end-start)//2
            print(mid)
            s_=0
            e_=len(l)-1
            if mid == e_ or mid == s_:
                print("a",mid,l[mid])
                return l[mid]
            if l[mid] > l[mid-1] and l[mid] > l[mid+1]:
                print("b",mid,l[mid])
                return l[mid]
            elif l[mid-1] > l[mid]:
                print("c")
                end = mid-1
                return p_f(l,start,end)
            elif l[mid] < l[mid+1]:
                print("d")
                start = mid+1
                return p_f(l,start,end)
     72. Performing multiple fucntions in dictionary:
        def f_a(a,q):
        input_dict={}
        output_list=[]
        for i, num in enumerate(a):
            if num not in input_dict:
                input_dict[num]=([i],float("+inf"))
            else:
                tuple_from_input_key = input_dict.get(num)
                tuple_from_input_key[0].append(i)
                index_list = tuple_from_input_key[0]
                prev_val=index_list[-1]-index_list[-2]
                current_min=min(prev_val,tuple_from_input_key[1])
                tuple_from_input_key = (tuple_from_input_key[0], current_min)
                input_dict[num]=tuple_from_input_key 

        for j in q:
            if j not in input_dict:
                output_list.append(-1)
            else:
                output_list.append(input_dict[j][1])
        return output_list  
    
    
    Data Frames:
    1. columns data type: data.dtypes
    2. String to datetime : tx_data['InvoiceDate'] = pd.to_datetime(tx_data['InvoiceDate'])
    3. creating YearMonth field for the ease of reporting and visualization:
      tx_data['InvoiceYearMonth'] = tx_data['InvoiceDate'].map(lambda date: 100*date.year + date.month)
    4. Group by :
      tx_revenue = tx_data.groupby(['InvoiceYearMonth'])['Revenue'].sum().reset_index()
    5. Percentage growth: tx_revenue['MonthlyGrowth'] = tx_revenue['Revenue'].pct_change()
    6. Rows and Columns filtering : 
      https://towardsdatascience.com/data-science-with-python-intro-to-loading-and-subsetting-data-with-pandas-9f26895ddd7f
    7. Loc and iloc - labels and indexes
    8. Convert categorical columns to numerical
        tx_class = pd.get_dummies(tx_cluster)
    9. classification_report(y_test, y_pred) :  gets all precision, recall, f1-score, support
    10. #drop duplicates
        data_day_order = data_day_order.drop_duplicates(subset=['CustomerID','InvoiceDay'],keep='first')
    11. by using shift, we create new columns with the dates of last 3 purchases
        #shifting last 3 purchase dates
        tx_day_order['PrevInvoiceDate'] = tx_day_order.groupby('CustomerID')['InvoiceDay'].shift(1)
        tx_day_order['T2InvoiceDate'] = tx_day_order.groupby('CustomerID')['InvoiceDay'].shift(2)
        tx_day_order['T3InvoiceDate'] = tx_day_order.groupby('CustomerID')['InvoiceDay'].shift(3)
    12. Drop Columns
        tx_class = tx_class.drop('NextPurchaseDay',axis=1)
    13. Cross-validation :
            models.append(("KNN",KNeighborsClassifier()))
            #measure the accuracy 
            for name,model in models:
                kfold = KFold(n_splits=2, random_state=22)
                cv_result = cross_val_score(model,X_train,y_train, cv = kfold,scoring = "accuracy")
                print(name, cv_result)
     14. How can we be sure of the stability of our machine learning model across different datasets? 
         Also, what if there is a noise in the test set we selected.
         Cross Validation is a way of measuring this. 
         It provides the score of the model by selecting different test sets.
         If the deviation is low, it means the model is stable. 
         In our case, the deviations between scores are acceptable (except Decision Tree Classifier).
          
     15. #represent month in date field as its first day
        df_sales['date'] = df_sales['date'].dt.year.astype('str') + '-' + df_sales['date'].dt.month.astype('str') + '-01'
        df_sales['date'] = pd.to_datetime(df_sales['date'])
