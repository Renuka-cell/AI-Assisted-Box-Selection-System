# AI Usage

## 1. Purpose

AI tools were used during the development of this project for requirement
understanding, project planning, Django development, debugging, testing,
and documentation.

AI-generated suggestions were reviewed and tested before being incorporated
into the final project.

---

## 2. AI Tool Used

### ChatGPT

AI tool used:
- ChatGPT

Primary uses:
- Understanding the assignment requirements
- Database and ER design
- Django project architecture
- REST API design
- Packing and box recommendation logic
- Debugging
- Automated test development
- Documentation assistance

---

## 3. AI-Assisted Development Log

### Interaction 1 — Requirement and System Design

**Prompt given:**

### 1. First prompt given - 
I am completing a Python/Django hiring assignment for an internship. I have attached the assignment document provided by the company.  I want to use you as a technical mentor and development assistant.
So before going towards development, i would like to go in the details of the project,like:

1. The requirements that are mentioned in the assigment.
2. A clear explanation that what exactly the project supposed to do.
3. Suggest me the workflow of the project.
4. The important technical and architecutal decisions I should think about before coding.
5. The main Django components I may need, such as models, views/API endpoints, serializers, services, etc.  
6. Should I need to design only the backend(i.e. Django part) or need to design frontend too.
7. The main business logic/algorithm that needs to be designed .
8. Suggested categories of test cases I should eventually write .
9. Tell me does we need to use any API(internal or external),if yes, than , how to test them(like using POSTMAN).
10. Also tell me what thinks I need to test before validation of the project.
11. Suggest me a proper plan from now till the sub,ission.
12. Anything in the assignment instructions that I need to be particularly careful about when preparing the final submission.   

### 2. Second prompt given -
"4. The difficult part: multiple products inside a box
Suppose an order contains:

```
```

```
Product A
10 × 10 × 10

Product B
20 × 10 × 10
```

We cannot simply say:

```
```

```
total length = 30
total width  = 20
total height = 20
```

because products can potentially be arranged differently.
This is essentially a **3D packing problem**.
For a small internship assignment, I would **not over-engineer this into a complex bin-packing solver** unless the assignment specifically requires it.
Instead, define a clear assumption.
For example:

> Products are packed using a simplified bounding-box approach, with rotation allowed, and the resulting required dimensions must fit inside the box.

But even this needs careful definition.
Another reasonable approach is to implement a simple deterministic packing strategy.
This is something I recommend we discuss **before writing models or views**, because it is the most important business-logic decision in the project."
In this i guess we should go for "Products are packed using a simplified bounding-box approach, with rotation allowed, and the resulting required dimensions must fit inside the box.  ", because just implementing a simple plan recommendation system is not enough, we need to make it more reboust for multiple products with different dimensions, so that they can fit into a single box.

In point-6, you have said about the components we need, i guess we need to have one more column or a tbale where we can see the stock avaiable of that product and the shipping boxes.

### 3. Third prompt given -
What exactly is "most suitable"?

There are potentially several interpretations:" Cheapest + minimize wasted space+ able to carry te weight of the product packed inside it."
 
### 4. Fourth prompt given -
Tell me next , what we need to work on now. And at the end give me all the Business rules from starting to end with workflow, so that I would validate it before moving forward.

### 5. Fifth prompt given -
1. So i guess the system is about the selection system,means it recommends the box, its work is to just recommend the box based on the order placed my the customer.Also tell me how it will be done, because if we have stock contraint than we can know that what type of boxes we have, if we bought new type of boxes than we can able to add the new boxs in the syatem with its diemsions, and based on the avalible type boxes the system will recommend the box for the order.
Clear me this thing, whether the system has all type of boxes which is manufactured in the world, or will be specific to the business.
2. So we will not work on the stock part, and i want to work on the weight part, you said that -"total_order_weight <= box.max_weight" if this condition satisfies than and than only the box is validate, i guess if the products fits properly inside the box than the box is automatically able to handle the weight of the product, if we need this condition in our system,then tell me the realistic logic behind it.Tell me about this, and then give me once again the complete final business rule that we have find till now in the above converstaion, and workflow/flowchart.

### 6. Sixth prompt given -
In point 10 you said that -"10. One correction to our previous business rule
We previously included **stock availability**.
After your clarification, I agree that we should remove stock from the **core business rules**.
The assignment doesn't require inventory management.
Instead:

### Box catalogue ≠ box inventory

The database tells us:

> What types/specifications of boxes this business supports.

It doesn't necessarily tell us:

> How many physical boxes are currently sitting in the warehouse.

That's an important distinction.
So:

```
```

```
Box
--------------------------------
Name
Internal dimensions
Maximum weight
Cost
```

is enough for the core assignment.
If the company later wanted inventory management, we'd add stock separately."

1. So the admin will add the new boxes in the database, and apart from admin any other person who will use this will only use for suggestion of the boxes ,Right?

   Then clear my doubt that does we need to create admin logic for this      operations.

2. And also tell me do we need to remove the product stock.

3. And tell me how can we see the order(becasue yes we are implementing the suggestion system, but we don't have any part/system which will show the order, for this we need to create the order and then use the system to see the results)

### 7. Seventh prompt given -

okay firstly tell me how will be the output seen by me,when i will code and see the results.where i will see the result, how i should interact(does it will be like AI prompt and answers OR something else).And i think  we need the frontend to see the results and give inputs(if required). Tell me everything about this.

### 8. Eigth prompt given -

Okay so i got yur point, and i am statisfied with it, so tell me how to submit the test cases,does i need to include screenshot for this, if yes than should i give the POSTMAN's test cases(i aksed beacause this project does not explicitly mentions about any frontend, so can we just submit in the backend only with required evidences). If it is not possible than we will first build completely backend than we will move towards plain simple html,css and js part.


**AI output used:**

1. In this interaction, I can across all the requirements of the project like what actually the project does,what are the components involved here,what are the deliverables i have to prepare for this project.
2. Project is to recommend a suitable shipping box for the customers accrding to the number of products are oreded,types of products,the diemensions of the product and the box , so that the product should fit in it, does we use multiple boxes for mutiple diffrernt orders or can we go with a single box.
3. We came to know aboit the alogorithm, componenets like OrderItem,order,product,boxes which is need to add in the database.
4. Does we need to add the frontend or not just go for the backend.
Taked about the output, as we are not using any frontend, so we have used POSTMAN for testing.
5. We need to do the roataional space for the product.
6. We need to think about the six of the box so that we should spend resonable amount on boxes with less waste spaces.

**Output accepted/modified/rejected:**

- Accepted: 
    1. Almost Output were accpeted as it was my learning and understanding stage.
    2. Finalized business logic.
- Modified: 
    1. To use Admin configuration for addtion of new type of boxes if we buy.Similarly for products too.
    2. Packing the mutiple products are modified using the business logic.
    3. used the packing startery like "Cheapest + minimize wasted space + able to carry weight of the product"
- Rejected: 
    1. Just providing the recommendation without making it dynamic /robust for the new type of box addition. 
    2. Not to work on the stock part, as this is a system to recommend the shipping box for the order placed not any inventory management system.

**verification**
1. This was gone by continues evaluation of each output of every prompt and reading it thorughly.

---

### Interaction 2 — Database / ER Design

**Prompt given:**

### 1. first prompt
Yes we should move towards the ER disgram. Guide me according what we have validated till now in the above converstion.

### 2. second prompt
1. What does this "OrderItem " is, a table or something else, and how does it helps.
2. We discussed about Admin part, so does it will include in the ER-diagram,if yes than give me its guidence.Beacuse admin is able to perform CURD operations for order,products,etc.
3. How many entities ecavtly we would need to create in the ER-diagram.
4. I guess we do not need the recommended\_box data should be store, because we just need to recommend the box not to store it so that it would be useful in future, if in the future the requirements changes than we can again get the recommendations.
5. I did not understand this relation, once again tell me about this-

Product 1 ───── N OrderItem
Order   1 ───── N OrderItem
Order   N ───── 1 Box   (recommended box, optional)

### 3. third prompt
Okay so i got it, so now give me final well described ER diagram guidenace,with all type of keys,values,representation,etc.


## Purpose 
To design the databse and Er diagram for the project.

**AI output used:**

1. Here we ave discussed about the components of the project i.e. products,order,boxes,orderitem.
2. we have discussed about there attributs (which are given in the README.md file in detail with their corresponding relationship)
3. We have discussed that we can delete the order but we cannot delete the product , as the orderithem is depended on the product table only not on boxes or order.

**Output accepted/modified/rejected:**

- Accepted: The componenets where accpted with there attributes and relations.
- Modified: Got nothing to modify.
- Rejected: No rejections

**verification**

It is done by creating the ER diagram and reading the complete explanation of the db design and ER diagram.

---

### Interaction 3 — Set-up and developmenet

### Prompts given

### 1. first prompt
Okay so first lets start working on coding part, if we have done with other theorytical and research part. Can you tell me in detail from starting what i need to create, specially tell me about the dependencies that i need to install.

### 2. second prompt
How to delete all the installed dependencies.

### 3. third prompt
okay so set-up is done successfully, now lets move towards,next step, also i have to pull this project on my github repo, so i need to create .env file for secret key, tell me the variable name to create it properly, also we will move towards to the next step.

### 4. fourth prompt
(.venv) PS C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System> git status
warning: could not open directory 'Application Data/': Permission denied
warning: could not open directory 'Cookies/': Permission denied
warning: could not open directory 'Documents/My Music/': Permission denied
warning: could not open directory 'Documents/My Pictures/': Permission denied
warning: could not open directory 'Documents/My Videos/': Permission denied
warning: could not open directory 'Local Settings/': Permission denied
warning: could not open directory 'My Documents/':Permission denied
warning: could not open directory 'NetHood/': Permission denied
warning: could not open directory 'PrintHood/': Permission denied
warning: could not open directory 'Recent/': Permission denied
warning: could not open directory 'SendTo/': Permission denied
warning: could not open directory 'Start Menu/': Permission denied
warning: could not open directory 'Templates/': Permission denied
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../Ubantu/portfolio/.gitignore
        modified:   ../Ubantu/portfolio/portfolio/settings.py
        modified:   ../Ubantu/portfolio/portfolio_app/admin.py
        modified:   ../Ubantu/portfolio/portfolio_app/models.py
        modified:   ../Ubantu/portfolio/portfolio_app/views.py
        modified:   ../Ubantu/portfolio/static/css/style.css
        deleted:    
 
 .......(and so on)
no changes added to commit (use "git add" and/or "git commit -a")

This is what i got when i run the commands git status, i came to know that everything is pushing on the github repo instead of just my project, i guess it is beacuse my git is on another level or folder.
Help me to debug it and solve it.

### 5.fifth prompt

GIthub related issues

### 6. sixth prompt
okay so i got the correct dir and level of .git, now tell me what next we need to do.

# 1. Before writing `models.py`, let's decide field types

This is important enough that I don't want to blindly give you models.

Our physical values can contain decimals.

For example:

```
```

```
Product:
length = 30.5 cm
width  = 20.25 cm
height = 2.5 cm
weight = 1.75 kg

Box:
length = 40.5 cm
max_weight = 10.5 kg
cost = ₹49.99

So for this i guess we need to put the product quantity in whole positive number, whereas the others i.e. length,width,heigth,weight, Should be in non-zero and non-negative decimal points numbers.
```

### 7. seventh prompt
"Step 10 — Why `PROTECT` for Product?
Suppose Product #5 is:

```
```

```
Laptop
```

and it appears in existing orders.

If we allowed it to be deleted, historical order records could become meaningless.

So:

```
```

```
on_delete=models.PROTECT
```

means:

```
```

```
Product is referenced by OrderItem
        ↓
Don't allow Product deletion
```

This protects our order history."

There you said if one of the product will try to delete than it will not be happen beacuse fr the order history, but I think it is vaild when the order has multiple products.What if we have only single product in the order and try to delete it.

### 8. eighth prompt
Okay so now i am able to see the admin panel and all the models registered.
Now lets move towrads creation of urls.py i.e. endpoints and business logic.

**AI output used:**

1. Used to do set-up of the project.
2. created main file "AI-Assisted-Box-Selection-System" on desktop, then created .venv file using command - python -m venv .venv
3. Then installed dependec=nces like django djangoframework, then created requirements.txt file.
4. created project"config", then three apps "products","orders","boxes".
5. mapped urls in the whole project.
6. crested files serilizers.py in all the apps for validation of the requests and responses.
7. created orders/services.py to implement the main logic of the project like packing the product,box recommendation,dimension calculations, arrangements,etc.
9. created views.py file and created small logic for each app.
10. created urls for each eadpoint like CURD for both boxes and products.
11. recommenadtions and views orders, place orders.
12. Created '.env' and '.gitignore' files to prevent by pushing the SCECRET_KEY on the github repo.

**Output accepted/modified/rejected:**

- Accepted: Accpeted the business logic code, urls etc.
- Modified: Modified the set-up again, refined the code by rechecking and reading the explanation of the code.
when created the .env file Chatgpt not informed regarding the installtion of "dotenv" module, so it is done.
- Rejected: To create frontend for while creating the project, it could be done after completeion of task if found needed. 
Storing the recommended box against the Order,means storing the recommendations in the db, which is not required for now, it is temporary, if the order changes again then the shipping box size can also bechanged accordingly.

## Verification
 Verified is done only by one way, by again and again using the commnds

```bash
python manage.py check
python manage.py runserver
```
Also once used the commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
---

## interaction 4 - Testing
 
 
**prompt given**

### 1. first prompt-
Okay the services.py file is done, now tell me what next i need to do.Also tell me whay we have created services.py file only n "orders" app but not in other apps.

### 2. Second prompt
I guess we have not worked on HTML format of POST /api/orders/.I am not able to add it.

### 3. third prompt
okay so i got it, actually it is present in JSON format, so i have created the order, now tell me what next i need to do.

### 4. fourth prompt
"http://127.0.0.1:8000/api/orders/1/items/" there is no such type of end-point, also i am not getting any 
POST

Product:
[ Select a product ▼ ]

Quantity:
[          ]

[ POST ]

This king of interface, what is the exact problem.

[19/Sep/2026 00:18:12] "GET /static/rest_framework/img/grid.png HTTP/1.1" 304 0
[19/Sep/2026 00:18:37] "GET /api/orders/1/ HTTP/1.1" 200 5682
[19/Sep/2026 00:18:40] "GET /api/orders/ HTTP/1.1" 200 8935
[19/Sep/2026 00:19:28] "GET /api/orders/1/recommend-box HTTP/1.1" 301 0
Method Not Allowed: /api/orders/1/recommend-box/
[19/Sep/2026 00:19:28] "GET /api/orders/1/recommend-box/ HTTP/1.1" 405 5905
Not Found: /api/orders/1/items/
[19/Sep/2026 00:20:00] "GET /api/orders/1/items/ HTTP/1.1" 404 3458

### 5. fifth prompt
I guess you have done , something wrong, the actual code that you have given to me for-

1. orders/views.py is-from django.shortcuts import get_object_or_404

   from rest_framework import generics, status
   from rest_framework.response import Response
   from rest_framework.views import APIView

   from .models import Order
   from .serializers import OrderSerializer
   from .services import recommend_box


   class OrderListCreateView(generics.ListCreateAPIView):
       queryset = Order.objects.all()
       serializer_class = OrderSerializer


   class OrderDetailView(generics.RetrieveAPIView):
       queryset = Order.objects.all()
       serializer_class = OrderSerializer


   class RecommendBoxView(APIView):

       def post(self, request, pk):
           order = get_object_or_404(Order, pk=pk)

           try:
               result = recommend_box(order)

           except ValueError as error:
               return Response(
                   {
                       "error": str(error)
                   },
                   status=status.HTTP_400_BAD_REQUEST,
               )

           if result is None:
               return Response(
                   {
                       "order_id": order.id,
                       "recommended_box": None,
                       "message": (
                           "No suitable box is available "
                           "for this order."
                       ),
                   },
                   status=status.HTTP_200_OK,
               )

           box = result["box"]

           packed_dimensions = result["packed_dimensions"]

           return Response(
               {
                   "order_id": order.id,
                   "recommended_box": {
                       "id": box.id,
                       "name": box.name,
                       "length": str(box.length),
                       "width": str(box.width),
                       "height": str(box.height),
                       "max_weight": str(box.max_weight),
                       "cost": str(box.cost),
                   },
                   "total_weight": str(
                       result["total_weight"]
                   ),
                   "packed_dimensions": {
                       "length": str(packed_dimensions[0]),
                       "width": str(packed_dimensions[1]),
                       "height": str(packed_dimensions[2]),
                   },
                   "wasted_volume": str(
                       result["wasted_volume"]
                   ),
               },
               status=status.HTTP_200_OK,
           )
2. orders/serializers.py is -from rest_framework import serializers
   from .models import Order, OrderItem
   from products.models import Product


   class OrderItemSerializer(serializers.ModelSerializer):
       class Meta:
           model = OrderItem
           fields = [
               "id",
               "product",
               "quantity",
           ]


   class OrderSerializer(serializers.ModelSerializer):
       items = OrderItemSerializer(many=True)

       class Meta:
           model = Order
           fields = [
               "id",
               "created_at",
               "items",
           ]

       def create(self, validated_data):
           items_data = validated_data.pop("items")

           order = Order.objects.create(**validated_data)

           for item_data in items_data:
               OrderItem.objects.create(
                   order=order,
                   **item_data
               )

           return order

So you tell me which is correct and what actual changes i need to do.

### 6. sixth prompt
(.venv) PS C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\.venv\Lib\site-packages\django\utils\autoreload.py", line 354, in run
    get_resolver().urlconf_module
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\.venv\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ~~~~~~~~~^^^^^^^^^^
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\.venv\Lib\site-packages\django\urls\resolvers.py", line 722, in urlconf_module
    return import_module(self.urlconf_name)
  File "C:\Program Files\Python313\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\config\urls.py", line 24, in <module>
    path('api/orders/',include("orders.urls")),
                       ~~~~~~~^^^^^^^^^^^^^^^
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\.venv\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
  File "C:\Program Files\Python313\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\orders\urls.py", line 2, in <module>
    from .views import (
    ...<4 lines>...
    )
ImportError: cannot import name 'OrderItemCreateView' from 'orders.views' (C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\orders\views.py)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Program Files\Python313\Lib\threading.py", line 1043, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "C:\Program Files\Python313\Lib\threading.py", line 994, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\.venv\Lib\site-packages\django\utils\autoreload.py", line 81, in wrapper
    raise e from _url_module_exception
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\.venv\Lib\site-packages\django\utils\autoreload.py", line 66, in wrapper
    fn(*args, **kwargs)
    ~~^^^^^^^^^^^^^^^^^
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\.venv\Lib\site-packages\django\core\management\commands\runserver.py", line 134, in inner_run
    self.check(**check_kwargs)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\.venv\Lib\site-packages\django\core\management\base.py", line 498, in check
    all_issues = checks.run_checks(
        app_configs=app_configs,
    ...<2 lines>...
        databases=databases,
    )
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\.venv\Lib\site-packages\django\core\checks\registry.py", line 99, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\.venv\Lib\site-packages\django\core\checks\urls.py", line 138, in check_custom_error_handlers
    path = getattr(resolver.urlconf_module, "handler%s" % status_code)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\.venv\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ~~~~~~~~~^^^^^^^^^^
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\.venv\Lib\site-packages\django\urls\resolvers.py", line 722, in urlconf_module
    return import_module(self.urlconf_name)
  File "C:\Program Files\Python313\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\config\urls.py", line 24, in <module>
    path('api/orders/',include("orders.urls")),
                       ~~~~~~~^^^^^^^^^^^^^^^
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\.venv\Lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
  File "C:\Program Files\Python313\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\orders\urls.py", line 2, in <module>
    from .views import (
    ...<4 lines>...
    )
ImportError: cannot import name 'OrderItemCreateView' from 'orders.views' (C:\Users\renuk\OneDrive\Desktop\AI-Assisted-Box-Selection-System\orders\views.py)


### 7. seventh prompt
Still showing the same error, tell me what i need to do.I can clerly see that in the code we have POST, but in the bwroser we are getting GET method, which is showing methoda not found.

### 8. eigth prompt
okay so finally i am getting my output, so can you tell me what i need to do next, is there any coding part left or we can go with the documentation part.

### 9. ninth prompt
Let's build `orders/tests.py` properly and run the complete test suite.  
firstly tell me in short that whay we are using this file, and what actually this file works in the django based projects.


**AI output used:**

1. Okay so after creating all the files test the working on the broswer/POSTMAN to test whether your logic and APIs are working correctly.
2. Created orders/tests.py file for the automated testing after sucessful completeion of the manual testing.

**Output accepted/modified/rejected:**

- Accepted : The tests.py file code for automated testing.
- Modification : Modified the urls and method of one of the url as its output was not seen on the browser. In the automated testing we have modified in the code file "tests.py"

from - 
```bash
    self.assertEqual(
        packed_dimensions,
        (
            Decimal("10.00"),
            Decimal("5.00"),
            Decimal("5.00"),
        ),
    )

```

to this -

```bash

    self.assertEqual(
        sorted(packed_dimensions),
        sorted(
            (
                Decimal("10.00"),
                Decimal("5.00"),
                Decimal("5.00"),
            )
        ),
    )

```

- Rejected : it has given me the api which was not present/created in Urls.py "http://127.0.0.1:8000/api/orders/items/1/", so i debugged it manually by verifing the urls.py file and the code file like views.py and services.py.

**verification**
1. When I got the error of the page not found for the invalid url, i modified the required code file and again tested wheather it is working correctly or not.
2. run the automated test code file  using the commands - python manage.py test
3. This is given more briefly in the "TEST_CASES.md" and "TEST_OUTPUT.md" file.

---

### Interaction 5 - Documentation

**Prompt given:**
### 1. first prompt-
Okay so before making all this files, can you tell me should i need to push all this doc files on my github or should i seperately submit it.

### 2. second prompt-
Okay so tell me how to create the files one by one.

### 3. third prompt-
okay fisrt tell me what content should need to add in TEST_CASES.md file.

### 4. fourth prompt-
Okay so give me the content for TEST_OUTPUT.md file.


**Output accepted/modified/rejected:**

- Accpted : I have taken complete guidence from Chatgpt.
- Modify : Modified as Chatgpt suggested (if any).
- Rejection : No rejections.

**verification**
1. Verified by refering other github repo's README.md file.
