# Veritas Vinos

Veritas Vinos is an online shop, which offers a huge wine variety. The website also publishes blog posts about wine and it's cultivation where the site visitors can leave a comment.
 
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

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X