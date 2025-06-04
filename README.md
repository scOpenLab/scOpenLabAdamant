# ScOpenLab Adamant

This is a fork of Adamant for use at the ScOpenLab. It was forked from the original repository at: https://github.com/csihda/adamant
The main changes are:
- Revomal of ElabFTW
- Setup a submit function in the server API for uploading the form data to and S3 bucket.
- Remove default forms and add a form for Xenium Slide Metadata.

# Workflow:

1) Open our Adamant webpage at: http://10.128.131.169:3000/ (TEMPORARY DEV INSTANCE).

2) Select the "xenium_slide.json" form
    <img width="954" alt="{DBDAB585-0D1F-4A10-B58C-7904CD0D9581}" src="https://github.com/user-attachments/assets/f5e48ec8-7ff6-4ee2-95c0-8acb26d5941a" />

3) Click the "RENDER" button
     <img width="827" alt="{9FD0EC79-37D1-4975-AAC0-0B52A08EDB79}" src="https://github.com/user-attachments/assets/71daa92a-bdae-4d5f-9d3c-79053e9fb2f0" />

4) Fill in the form
   
    - Fill in the slide metadata
       <img width="831" alt="{757512AC-6480-4903-B305-D4E8FDFA86EB}" src="https://github.com/user-attachments/assets/f2d89df9-4d2b-4fee-9ba2-c5602c9f58af" />
 
    - For each region: Add and fill a "Xenium Slide Region" section
       <img width="770" alt="{D595C269-F817-409A-B279-66EA45F2717F}" src="https://github.com/user-attachments/assets/e3d82365-077c-400f-83a9-9daa980403f3" />
       <img width="837" alt="{338D37B2-1E49-40FE-B2BA-EFC3FE149DD2}" src="https://github.com/user-attachments/assets/c6bbe2bb-7c7f-4c30-9cd4-e14e0257ed1f" />

5) Click the "COMPILE" button
       <img width="782" alt="{F6A0F686-1F43-469B-88B0-07E98DE9F436}" src="https://github.com/user-attachments/assets/e834992c-a0ed-4577-a48e-4efeb79bb73b" />

6) Click the "PROCEED" button
 <img width="774" alt="{0B61723A-4944-4248-995A-A036B4A3FE1E}" src="https://github.com/user-attachments/assets/c1ca196d-11d9-49ba-926b-5ebc1d8544d1" />


7) Click the "Submit Slide Metadata" button
       <img width="761" alt="{3612ED58-E365-4915-B814-628DFB2B981D}" src="https://github.com/user-attachments/assets/7d900cd4-95c6-41e3-a028-13f2ac0cfb1e" />

The slide metadata in json format are submitted to the ScOpenLab S3 bucket. Resubmitting a form with the same slide id will overwrite the previous submission! 


# Deployment
We recommend deploying Adamant with docker-compose, which can be done with ease:
- `$ git clone https://github.com/csihda/adamant.git`—clone the repository
- `$ cd adamant`—go to adamant project directory
- `adamant$ docker−compose build`—build the docker images for both back-end and front-end
- `adamant$ docker−compose up -d`—start both client and server containers, i.e., the whole system

By default, the deployed system can be accessed at `http://localhost:3000`.

# Development details

## Supported JSON schema keywords
Currently, Adamant supports the rendering and editing of JSON schemas with a specification version draft 4 and 7. The following table lists all the implemented JSON schema keywords in the current version of Adamant. Note that the `id` keyword only works with the JSON schema specification version draft 4, whereas `$id` is used for the newer specification drafts. Lastly, the `contentEncoding` keyword is intended to be used with the specification version draft 7 or newer.

| Field Type | Implemented Keywords | Note |
|-----------|----------------------|----|
|String|`title`, `id`, `$id`, `description`, `type`, `enum`, `contentEncoding`, `default`, `minLength`, `maxLength`|`contentEncoding` can only receive a string value of `"base64"`|
|Number| `title`, `id`, `$id`, `description`, `type`, `enum`, `default`, `minimum`, `maximum` | |
|Integer| `title`, `id`, `$id`, `description`, `type`, `enum`, `default`, `minimum`, `maximum` | |
|Boolean| `title`, `id`, `$id`, `description`, `type`, `default` | |
|Array| `title` , `id`, `$id`, `description`, `type`, `default`, `items`, `minItems`, `maxItems`, `uniqueItems` | |
|Object| `title`, `id`, `$id`, `description`, `type`, `properties`, `required` | |

## Development Setup
Setting up Adamant on a local machine for development:
- `$ git clone https://github.com/csihda/adamant.git`—clone the repository
- `$ cd adamant`—go to adamant project directory
- `adamant$ npm install`—install the dependencies for the client-side
- `adamant$ cd backend`—go to backend directory
- `adamant/backend$ python -m venv venv`—create a python virtual environment
- `adamant/backend$ ./venv/Scripts/activate`—activate the virtual environment
- `adamant/backend$ pip install -r requirements.txt`—install the dependencies for the back-end
- `adamant/backend$ cd ..`—go back to adamant project directory
- `adamant$ yarn start-api`—start the back-end
- `adamant$ yarn start`—on a new terminal, in the adamant project directory, start the front-end

By default, Adamant is accessible at `http://localhost:3000`.

# Citation

Please cite this paper if you use this code/tool in your publication. 
```
@article{ 10.12688/f1000research.110875.2,
author = {Chaerony Siffa, I and Schäfer, J and Becker, MM},
title = {Adamant: a JSON schema-based metadata editor for research data management workflows 
[version 2; peer review: 3 approved]},
journal = {F1000Research},
volume = {11},
year = {2022},
number = {475},
doi = {10.12688/f1000research.110875.2}
}
```

[![DOI:10.12688/f1000research.110875.2](http://img.shields.io/badge/DOI-10.12688/f1000research.110875.2-B31B1B.svg)](https://doi.org/10.12688/f1000research.110875.2)
