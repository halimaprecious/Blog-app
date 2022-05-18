#### Poets-blog

A Personal blog website where I can express and share my poems and other users can read and comment on them. It also has a feature that displays random quotes to inspire my users.

## Technology used
1. Python
2. Flask
3. HTML
4. PostgresSQL

## Requirements
An IDE such as VS code with Python version 3 installed,a terminal and a browser. 

## Setup and Instruction
1. Clone the repository at [here](https://github.com/halimaprecious/Blog-app.git).
2. Extract and open the folder on VS code or navigate to the folder on your terminal.
3. On the terminal, create a virtual environment `python3 -m venv virtual` and activate it `source virtual/bin/activate`. NB **virtual** is the name of the environment.
4. Pip install dependancies highlighted on the **requirements.txt** by running `pip install -r requirements.txt`
5. Create a **start.sh** file in the root directory of the folder and define the **secret key,email address and email password**.
6. Run `chmod +x start.sh` and `./start.sh` respectively on the terminal.
7. View the application on your browser through `http://127.0.0.1:5000`.


## Behaviour Driven Development

BDD focuses on how the user will interact with the application.

## User Story 
####  User view
* User can view the blog posts on the site
* User can see random quotes on the site
* User can view the most recent posts
* User can subscribe to blog mailing list and receives an email alert when a new post is made.
* User can comment on blog posts

####  Writer view
* sign in to the blog.
* create a blog from the application.
* delete comments that I find insulting or degrading
* update or delete blogs I have created

## Behavior Driven Development

| Input                    | Behaviour                       | Output                                       |
| -------------------------| ------------------------------  | -------------------------------------------- |
| Subscribe to mail list              | Input the email               | Redirect you to the index page               |
| Writer login                    | Take you to home page           | Redirect you to the Homepage                 |
| Create a blog post by filling blog form          | Write your blog and post it to blogs    | Your blog is displayed  in index page                     | 
| User comment on the Blog post plus a nickname | Write your feedback and post it | Your feedback is displayed under the blog post   |
| Writer delete a blog post       | Deleting the blog post from the database    | The blog post will be deleted and not appear on the page                  |
| Writer update a blog post       | Updating the blog post in database    | The blog post will be updated                |
| Writer delete a comment         | Deleting the blog post in database    | The comment will no longer appear under the post   

## Development
To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request

## Known Bugs
- Images do not display from db. 

If you find a bug or would like to request a new function, reach out to me via Email: halimaprecious3@gmail.com 

## Future Plans
- Display the owner of the blog.
- Ability to delete blog posts that have been voted or commented on.
- Save and display images from
- Ability to navigate to other users profiles.
- Enable user subscription to my blog.

## License

[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2022 **Precious Halima**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.