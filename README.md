# react-drf-sample

## 出来ること

- drf公式チュートリアル(https://www.django-rest-framework.org/topics/documenting-your-api/)のスニペット投稿 
- swaggerを見てスニペット作成のコードを模倣すればスニペット削除機能などが生える

- 参考資料
- https://www.kthksgy.com/web/make-react-django-blog1/
- https://www.python-program.tech/?p=7

/componets以下は見なくていい

## わかるようになること

- cors
- cookie
- docker
- http(axios)
- Promise
- REST API

## メモ (意見募集)

- ログインしているかどうかの判定をアクセストークンの所持の有無だけでいいのか
- jwtを保持するcookieをhttponlyにするとxss対策になるがAPIを叩くときにjwtを保持してAPIをたたけない(サーバー側で管理するしかない🤔


### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Django][Django]][Django-url]


## Prerequirement

- yarn
- docker-compose

## Usage

### first time only

```sh
cd front

yarn
``````
### Run

```sh
docker-compose up -d

```

### Initilize databese

<!-- docker-compose exec back /bin/sh -->
```
docker-compose exec back python /back/manage.py makemigrations
docker-compose exec back python /back/manage.py migrate
docker-compose exec back python /back/manage.py createsuperuser
```
### Adopt model change

<!-- docker-compose exec back /bin/sh -->
```
docker-compose exec back python /back/manage.py makemigrations
docker-compose exec back python /back/manage.py migrate
```

if you add or remove packages from Pipfile,please run 'docker-compose build'

<!-- if you add or remove packages from packages.json or Pipfile, -->
<!-- please run 'docker-compose build' -->

### Relationship with front and back

```mermaid
sequenceDiagram
    react->>djoser: Create new account (/auth/users/)
    djoser->>react: auth_token

    react->>djoser: login (auth/token/login/)
    djoser->>react: auth_token

    react->>djoser: Create access token (/auth/jwt/create/)
    djoser->>react: access token, refresh token

    react-->>djoser: Refresh access token(/auth/jwt/refresh/)
    djoser->>react: New access token, New refresh token

    react->>drf: API request (Beare:JWT)
    drf->>react: API Response

    react->>djoser: logout (auth/token/logout/)(Beare:JWT)
    djoser->>react: success or error

```

## URL for development

- front  
http://localhost:3000/
- back  
http://localhost:8000/
- swagger 
http://localhost:8000/api/schema/swagger-ui/

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Django]: https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=flat-square
[Django-url]:"https://docs.djangoproject.com/en/4.1/"