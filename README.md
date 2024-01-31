# Groceries

![image](https://github.com/JuanjoSalvador/groceries-app/assets/5058655/8a703542-10d4-4019-a974-373b63cbd0e7)

Groceries is an app designed to helping you finding best prices for your daily/weekly/monthly shopping list at different stores and supermarkets. Made with Django and Bulma.

Current version is v0.0.1

## Roadmap
Something not planned, doesn't mean it won't or couldn't be implemented in the future.

### User features

| Status | Features |
|:-------|:---------|
✔ Ready | Basic database search functions  
✔ Ready | Allow self-hosting for personal usage
❔ Planned | Multi-language support (English/Spanish)
❔ Planned | Full-text search engine
❔ Planned | Allow user registration
❔ Planned | Allow user submitions
❔ Planned | Suggestion based on the product user is watching now


### Development features

|Status | Features |
|:------|:---------|
✔ Ready  | Contributing guidelines
👷‍♂️ Work in Progress | Linter, style and quality checkings on push
❔ Planned | Container support (Docker/Podman)


## Development

First of all, you need to grab the project and install dependecies using one of the following methods. You will also need `yarn` for JavaScript packages.

Groceries is using SQLite3 as default database but I'm planning to move to PostgreSQL in order to allow full-text search during next releases.

### Installation (local)

#### Dependencies

* Python 3.10+
* Node.js and Yarn
* Poetry (optional)
* Virtualenv (optional)

To install Poetry and Virtualenv, you will need also `pip`.

```shell
python -m pip install poetry
```

or

```shell
python -m pip install virtualenv
```

and

```shell
npm install -g yarn
```

#### Poetry
By default, this project uses Poetry to manage dependencies.

```shell
git clone git@github.com:JuanjoSalvador/groceries-app.git && cd groceries-app
poetry install
yarn install --modules-folder ./groceries/staticfiles/node_modules
```
#### Virtualenv
This project uses Poetry by default, but you can run it using a classic virtual environment management tool and pip.

```shell
git clone git@github.com:JuanjoSalvador/groceries-app.git && cd groceries-app
python -m virtualenv env
source env/bin/activate
pip install --user -r requirements.txt
yarn install --modules-folder ./groceries/staticfiles/node_modules
```

### Running Groceries
First of all, you need to collect all static files.

```shell
python manage.py collectstatic
```
After this step, you can just run migrations and initialize database. You will need an email at the moment of initialize database since it will also create a superuser for you. You can enter whatever email you want, since is made for local development it doesn't need to exists, but make sure you remember it! It also will prompt you for a password.

Database initialization will add some sample data. Sample data can be found at `/data/sample-data.ods`, feel free to modify it as you want.

```shell
python manage.py migrate
python manage.py initdb [email] 
```

Once database is ready, you can run the app and make sure everything is OK.

```python
python manage.py runserver
```

### Container support
Since it still not ready, I'm planning to add Docker/Podman support for this project in the future.

## License

Groceries is under GNU GPL 3.0 License
