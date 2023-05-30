<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Bangla Assignment Plagiarism Checker (api's)</h3>

  <p align="center">
    Only for bengali language Plagiarism checker tools for pdf and text
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br /> -->
    <br />
    <a href="#">View Demo</a>
    <!-- ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Dependencies</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Plagiarism means duplicate other work and not giving any credit to them. So this is one of the most serious problems in academia and among researchers. All over the world have many application for plagiarism detector, But most this used in English language, doesn’t have any single language like Bengali. Bengali is the fourth language in our world where speak in Bangladeshi people,  also India’s second-language. Plagiarism detection requires a large corpus for comparison. Our experimental results find out average accuracy between 70 % - 80% in text extraction using OCR. Levenshtein Distance algorithm is used for determining Plagiarism. We have built a web application for end-user and successfully tested it for Plagiarism detection in Bengali texts by drop PDF file or only text. In future, we aim to construct a corpus with more books for more accurate detection.

Here's why:
* People can easily check Plagiarism in Bengali language.
* Easy to use multiple file.
* From pdf in Bengali text read accurately.

In English language so many Plagiarism tool’s are available in all over the world but in Bengali language didn’t have any tool’s for checking plagiarism. So that’s why I decide to create a tool for detecting plagiarism.

Use the `Bengali Assignment Plagiarism checker` to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![Bootstrap][Django.com]][Django-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

Use some package and trained data for this application. 

* [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition)
* [pytesseract](https://pypi.org/project/pytesseract/)
* [NLTK](https://www.nltk.org/)
* [PIL](https://pypi.org/project/Pillow/)
* [tempfile](https://docs.python.org/3/library/tempfile.html)

<!-- installation proccess -->
## Installation

Clone the repository

    git clone https://github.com/safiul-dev/plagiarism-checker.git

Switch to the repo folder

    cd bangla-assignment-plagiarism-checker

go to env folder activate it, use below command

    source plug_env/bin/activate

now write dependencis file using below command

    pip freeze > requirements.txt

This command can be used to update the file too.

And then, whenever someone wants to run our project on their computer, all they need to do is:

    python3 -m pip install -r requirements.txt

now need trained data for Image to bangla text extraction. 

https://pyimagesearch.com/2020/08/03/tesseract-ocr-for-non-english-languages/#:~:text=The%20first%20version%20of%20Tesseract,added%20in%20the%20second%20version.

this location will give you how to clone and where to clone this trained data

Start the local development server

    python manage.py runserver --8000

You can now access the server at http://localhost:8000


<!-- CONTACT -->
## Contact

Linkedin Profile - [@Safiullah](https://www.linkedin.com/in/md-safiullah-2b1408162/) - safiul7303@gmail.com


<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Django.com]: https://img.shields.io/badge/Django-563D7C?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
