# Veritas Vinos

Veritas Vinos is an online shop, which offers a huge wine variety. The website also publishes blog posts about wine and it's cultivation where the site visitors can leave a comment.
This project was built as the 4th Milestone Project for the Code Institute - Full Stack Developer Course.
**IMPORTANT (disclaimer): This project contains real products from existing brands.
If you wish to purchase them you can visit: [Vinexus](https://www.vinexus.de/en/wine/)
If you want to make a test purchase on my site you can use the deteails below.

Test transaction details:
* **credit card:** 4242 4242 4242 4242
* **expiration date:** 04 / 24
* **CVC:** 424
* **ZIP:** 42424
<div align="center"><img src = "https://github.com/lemon-squeezy/veritas_vinos/blob/master/readme_materials/demo.jpg" width=900></div>  
<a href="https://de.freepik.com/psd/mockup">Mockup PSD created by aleksandr_samochernyi - de.freepik.com</a><br>
You can view the live website here. [Veritas Vinos](https://veritas-vinos.herokuapp.com/)

# UX
## Project Goals
### Target Audience
- People who want to buy wine 
- People who prefer more exclusive products that they can't get in a supermarket.
- People who seek for presents for special occasions such as birthdays, weddings, anniversaries, etc.
- People who want to read interesting blog articles about wine, it's cultivation and production

### Visitor / User Goals
- Purchase products in a smooth and secure way
- Get informed with the products before buying by product reviews / product information or rating
- Gain interesting knowledge about wine from blog articles and leave a comment on blog articles

### Business Goals (Site Owner's Goals)
- Provide customers with a secure and safe ecommerce shop
- Establish the shop's brand image
- Expand their business effectively
- Make profit from selling products / services

### User stories
You can view the user stories [here](readme_materials/user_stories.pdf)

## Design
### Wireframes
You can find the wireframes [here](https://github.com/lemon-squeezy/veritas_vinos/blob/master/readme_materials/wireframes).

### Brand Identity
- Vision: Satisfy individual taste requirements.
- Mission: Provide a wide range of wines which can be purchased with one click online without the hassle of going to a physical shops.
- Values: 1. Enjoyment - Enjoy the variety and the unique taste of the wine. 2. Quality - We stand out with a particularly high quality. 3. Lifestyle - Our products raise your lifestyle.

### Color Scheme
I used 3 different colors for this page. The background is white, so you can focus more on the products. Body texts are laid out in black. The logo and the headings are represented by a wine red.

<p align="center"><img src = "https://raw.githubusercontent.com/lemon-squeezy/veritas_vinos/master/readme_materials/colors.png" width=900></p>

# Features

## Existing Features
This website is composed of 6 applications: `home`, `blog`, `bag`, `checkout`, `products`, `profiles`.
**Landing Page**
Landing Page is designed as a single page website to provide site visitors with enough information so they can understand what the business is about of this site.
This page has minimal amount of information to let the site visitors take next actions. The page compose of `Navbar`, `Carousel`, `About`, `Why Choose Us?` and `Contact Form` section.
As scrolling down on thie page, the elements are smoothly being placed by [Animate.css](https://animate.style/) and [wow.js](https://wowjs.uk/docs) animation effects to give a dynamic and sophisticated experience to the site visitors.

**Navigation Bar:** The navbar is split into 3 sections with 2 navigation sections to make navigating the site easy. The first is the main navigation items contain 'All Products', 'Blog' and a 'Contact" Section. The second is the details for MyAccount, with its sub-menu dependant on whether the users are already logged in or not, or is a superuser, and the bag which displays an up to date total of items in it.

**Sign up/Register & Sign In** This is found under the My Account menu item where users can log in to their account or register for the site.

**Delete product (superuser only):** Superusers can delete products easily either by clicking the delete button found under the items on the Shop page or the individual product page.

**Update product (superuser only):** Superusers can update the details of a product easily either by clicking the delete button found under the items on the Shop page, or on the individual product page, and then amending the form.

**Contact form:** The Contact page includes a form which submits messages from users directly to the site owner.

**Add item(s) to bag:** This button allows users to add items to the bag without navigating away from the page they are on. 

**Select item quantity:** On the product details page, users can select the number of items of that product they want to add to their basked using the + and – buttons, then ‘Add to Bag’

**Update item(s) Quantity:** On the bag page, users can update the number of items they wish to order of a product by changing the quantity number using the + and – buttons, then click the ‘update’ button

**Delete item(s) from the bag:** Users can remove an item from the bag completely by clicking the ‘remove’ button beneath the item in their bag.

**Back to the top on selected mobile pages:** Some pages of the website can become a little long on mobile. To help users with this I have added a ‘back to top’ button on these longer pages.

**Blog:** A blog is a perfect way for the website owner to provide useful information to users. This could include new product news, makeup tips and reviews from bloggers etc. The blog has been paginated so that it does not become too long, and users can also leave comments below a blog post.

**Sign in with Google:** These days, a user expects to be able to log into websites using other accounts such as social media. Therefore, I decided to add a ‘Sign in with Google’ option. If a user signs in this way, their email address gets added to the Admin of the site.


### Features Left to Implement
* Defensive delete button: Currently, the Delete button to delete a product has no defence to stop it being automatically pressed. A confirmation of delete should be added.
* The possibilty for user to rate the products. Curently the admin provides the rating for each product.
* Leave reviews beneath products: Reading reviews are a great way to help users decide to purchase a product. This feature would be great to include in the future but was not seen as imperative for launch.
* Subscription purchase model: To entice users to regularly receive lashes, a subscription service would provide them with regular deliveries and a reduced cost. This would also benefit the website owner so that they have pre-orders already in place each month.

## Schema Design
After careful consideration and taking into account all the different parts of the website and needs of the database, I designed the schema in 5 main sections/models:

**user_profile:** These are the details that the user saves to their profile for quick checkouts in the future. The username, email address and password details are set when the user registers for the site, and the delivery details are added when the user makes a purchase and selects to save those details to their profile.

**order:** This includes the overall order in full, including the delivery details from (from or added to the user profile) and the order_line_items.

**order_line_items:** This includes details of each product the user orders, the details of each product are linked to the products section.

**products:** This includes all the information related to each product, including the category, sku, name, taste, winery, country, grape_variety, alcohol, acid, residual_sugar, description, price, rating, image.

**category:** Linking to the category field in the products section, the Category model simply holds the categories which are chosen in the product model. These categories are pre-set and can only be modified or added to by a Superuser/Authenticated user.

**blog:** This section is non-relational to the rest of the database, and it holds details of the blog posts including the blog title, author, status, image, image_url and the post itself. The blog can only be added by a Superuser/Authenticated user.

**blog Comment:** If a user is signed into their account and they wish to leave a comment on the blog, the email field required in the form will be linked to their account and pre-filled with the user’s email. The blog comment models also require a name, comment body, date it was created on and the active status (published or draft).

![Schema](static/readme_docs/schema.jpg)

# Technologies
## Tools and Services Used
- [Balsamiq](https://balsamiq.com/) for the wireframes design.
- [GitHub](https://github.com/) to share and store code remotely.
- [GitPod](https://www.gitpod.io/) Development environment
- [Heroku](https://www.heroku.com/) for hosting the application and deploy.
- [Stripe](https://stripe.com) to receive paymnets
- [Amazon Web Services]( https://aws.amazon.com/) was used as a cloud service to host static files.

## Libraries and frameworks

- [Django](https://www.djangoproject.com/) a high level python web-framework used to design this project.
- [Bootstrap 4](https://getbootstrap.com/) a CSS library grid used for the development of this site.
- [FontAwesome](https://fontawesome.com/) for the creation and implementation of icons.
- [Google fonts](https://fonts.google.com/) to bring custom font styling.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) a template language for python used to bring logic into templates.
- [Psycopg2-binary](https://pypi.org/project/psycopg2-binary/#description) used as the Python PostgreSQL adapter.
- [Jquery](https://jquery.com/) a Javascript library to simplify the code.
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) a library that enables python code to modify AWS service.
- [AOS](https://michalsnik.github.io/aos/) used to bring animation on scroll.

## Languages

  - This project uses HTML, CSS, Javascript and Python programming languages.

## Manual Testing
For this project, I put the website through some vigorous testing. This included testing manually myself, by a friend, by my Mentor and also by the slack community in the peer-code review page.

#### Home page
  1. Check navbar links to see whether they are sending to the real url.
  2. Add keyword on the `search` bar and check if it brings the result asked or a feedback message.
  3. On the contact form add the name, email, subject and message checking if it will be submitted.
  4. Check if all the links on footer are working proper.

### Accounts app

#### Register page
  1. At the home page click on register.
  2. On the register page add your name, email address and password twice.
  3. If the register page be successful the register page will redirect to the home page with a message the user is registered or logged in.

#### Login page
  1. Add your user name or email and password.
  2. If the username or email and password works well the user will be redirected to the home page already logged in.

#### Reset password pages
  1. At the login page click on the `forgot password` link.
  2. Add your email address linked to the account.
  3. Receiving the email address click on the link to reset the email.
  4. Add new password twice.
  5. Click on the login page to be authorised.

### Cart app
  1. On the product detail page click on add to cart.
  2. Click on the remove or update link to remove an item or increase / decrease the quantity.
  3. Click on the button checkout to be redirected to login if you are not logged in or checkout if you already is logged.

### Checkout
 following the step 3 of the cart app, add the following details:

  1. Full name, phone number, country, postcode, town or city, street address 1 and 2 and county.
  2. For the credit card number you should add `4242424242424242`, any cvv and a correspondent data in the future.
  3. Click on the submit payment button.
  4. If the payment went through you will be redirected to the checkout_success page and receive a message with your bill.
  5. If the payment doesn't go through you will receive a message the card was not accepted.

## Web testing

The devices the application was tested were:

### Mobile
  - Galaxy S5
  - Pixel 2
  - iPhone 6, 7 and 8
  - iPhone X (real device)

### Tablet
  - iPad
  - iPad Pro

### Laptop
  - Macbook (real device)

For the web testing I used Chrome dev tools to find bugs, errors and test new styles for HTML, CSS and JavaScript.

# Deployment
## Heroku Deployment with AWS
This website is deployed on [Heroku](https://www.heroku.com/), following these steps:
1. Install these packages to your local environment, since these packages are required to deploy a Django project on Heroku.
- [gnicorn](https://gunicorn.org/): `gnicorn` is Python WSGI(web server gataway interface) server for UNIX.
- [gninx](https://www.nginx.com/): `gninx` is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/): `psycopg2-binary` is PostgreSQL database adapter for the Python programming language.
- [dj-database-url](https://pypi.org/project/dj-database-url/): `dj-database-url` allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
2. Create a `requirements.txt` file and freeze all the modules with the command `pip3 freeze > requirements.txt` in the terminal.
3. Create a `Procfile` write `web: gunicorn boutique_ado.wsgi:application` in the file.
4. `git add` and `git commit` and `git push` all the changes to the Github repositoty of this project.
5. Go to Heroku and create a **new app**. Set a name for this app and select the closest region (Europe) and click **Create app**.
6. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heorku Postgres**(you can type postgres), select **Hobby Dev — Free** and click **Submit Order Form** button to add it to your project.
7. In the heroku dashboard for the application, click on **Setting** > **Reveal Config Vars** and set the values as follows:

| Key | Value |
| ----------- | ----------- |
| AWS_ACCESS_KEY_ID | `Your AWS Access Key` |
| AWS_SECRET_ACCESS_KEY | `Your AWS Secret Access Key` |
| DATABASE_URL | `Your Postgres Database URL` |
| EMAIL_HOST_PASS | `Your Email Password (generated by Gmail)` |
| EMAIL_HOST_USER | `Your Email Address` |
| SECRET_KEY | `Your Secret Key` |
| STRIPE_PUBLIC_KEY | `Your Stripe Public Key` |
| STRIPE_SECRET_KEY | `Your Stripe Secret Key` | 
| STRIPE_WH_SECRET | `Your Stripe WH Key` |
| USE_AWS | `True` |

* I used [miniwebtool](https://miniwebtool.com/de/django-secret-key-generator/) to generate Django Secret Key.

8. Comment out the current database setting in settings.py, and add the code below instead. This is done temporarily to migrate the datbase on Heroku.
```
  DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }
```
9. Migrate the database models to the Postgres database using the following commands in the terminal:
`python3 manage.py migrate`
10. Load the data fixtures(color_table, flower_table, image_table, product_table) into the Postgres database using the following command:
`python3 manage.py loaddata <fixture_name>`
11. Create a superuser for the Postgres database by running the following command:
`python3 manage.py createsuperuser`
12. Replace the database setting with the code below, so that the right database is used depending on development/deployed environment.
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
13. Disable collect static, so that Heroku won't try to collect static file with: `heroku config:set DISABLE_COLLECTSTATIC=1`
14. Add `'veritas-vinos.herokuapp.com', 'localhost', '127.0.0.1'` to `ALLOWED_HOSTS` in settings.py.
```
ALLOWED_HOSTS = ['flowerydays.herokuapp.com', 'localhost', '127.0.0.1']
```
15. In Stripe, add Heroku app URL a new webhook endpoint.
16. Update the settings.py with the new Stripe environment variables and email settings.
17. Commit all the changes to Heroku. Medial files are not connected to the app yet but the app should be working on Heroku.
### Amazon Web Service S3
The static files and media files for this deployed site (e.g. image files for product/blog) are hosted in the [AWS](https://aws.amazon.com/) S3 Bucket. You will need to create S3 bucket, complete the setting up and upload static files and media files to the S3 bucket. You can find [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) for more information on the setting.
I used CORS configuration below:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

- Setting for static/media files in settings.py
1. Install `boto3` and `django-storages` with a command `pip3 install boto3` and `pip3 install django-storages` in your terminal, to connect AWS S3 bucket to Django.
2. Add 'storages' to `INSTALLED_APPS` in settings.py.
3. Add the following in settings.py.
```
if 'USE_AWS' in os.environ:
    # Cache Control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'flowerydays'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3-eu-west-1.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
5. Add [custom_storages.py](https://github.com/AsunaMasuda/FloweryDays/blob/master/custom_storages.py).
6. Delete DISABLE_COLLECTSTATIC from Heroku Config Var.
7. Push all the changes to Github/Heroku and all the static files will be uploaded to S3 bucket.
By setting up above, Heroku will run python3 manage.py collectstatic during the build process and look for static and media files.

### Automatic Deploy on Heroku
You can enable automatic deploy in the following steps that pushes update to Heroku everytime you push to github.
1. Go to Deploy in Heroku dashboard.
2. At `Automatic deploys`, choose a github repository you want to deploy.
3. Click `Enable Automatic Deploys`.


## Local Deployment
For local deployment, you need to have an IDE (I used Gitpod for this project) and you need to install the following:
- Git, Python3, PIP3
Also, you need to create account in the following services if you don't own yet:
- Stripe, AWS (S3 bucket), Gmail

1. In the IDE you are using, copy and paste the following command into the terminal to clone this repository.
 `git clone https://github.com/lemon-squeezy/veritas_vinos.git`
(the other ways to clone a repository are written in this [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository))
2. Set up environment variable in your selected IDE, or you can create `.env` file in your root directory and add `.env` to `.gitignore` file, and add the followings to the `.env` file.
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"    
```
3. Install all the required packages with `pip3 install -r requirements.txt`
4. Migrate the models to crete a database using in your IDE with `python3 manage.py makemigrations` and `python3 manage.py migrate`
5. Load the data fixtures(color_table, flower_table, image_table, product_table) into the database using the following command:
`python3 manage.py loaddata <fixture_name>`
6. Create a superuser for the Postgres database by running with `python3 manage.py createsuperuser`
7. Now you can access the app using the command `python3 manage.py runserver`

# Credits

## Content & Code
- I constantly read [Django](https://docs.djangoproject.com/en/3.1/), [Stripe](https://stripe.com/docs) and [Python](https://docs.python.org/3/) documenation and tutorial throughout the development.
- For `Blog` app, I refer to [this tutorial](https://djangocentral.com/building-a-blog-application-with-django/).
- For the text of my products I refer to [Vinexus](https://www.vinexus.de/en/wine/)
- This project was developed refering to the Boutique Ado Django mini-project from Code Institute course materials. The codes are customized and modified to fit the purpose of this milestone project.

## Images & Media
- All the icons in this website were provided by [Font Awesome](https://fontawesome.com/).
- Favicon was created with Adobe Photoshop
- The credits for the images used in this site can be found in this [separated file](https://github.com/lemon-squeezy/veritas_vinos/blob/master/readme_materials/image_credit.md).

## Acknowledgements
- Thanks to: my Code Institute Mentor Akshat_Garg for his advice throughout the development process.
- Code Institute Slack Community that gave me a light when I was stuck in my coding.
- And especially the CI Tutor Support.

## Disclaimer
This website is created for educational purpose only.