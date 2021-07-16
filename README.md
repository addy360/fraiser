

![Fundraiser image](https://www.henryford.com/-/media/henry-ford-blog/images/interior-banner-images/2017/04/healthy-fundraiser.jpg?h=785&la=en&w=1920&hash=F9C844978BB5721C6199806F2335E978)
# Fraiser (Fundraiser) 


> Is a solution made to simplify the process of seeking and gathering voluntary       financial contributions by engaging individuals, businesses, charitable foundations, or governmental
 


>It is designed in a way to help organizations to collect funds from not only people around them, but covers even more people through the help of technology


## Installation
*Assuming python and git are installed*

### Navigate to project folder / working folder

``` bash
    git clone https://github.com/addy360/fraiser.git
    cd fraiser
```
*Optionally virtual environment can be activated*

```bash
pip install -r requirements.txt
cp keys.py.example keys.py
```
> necessary variables should be filled in the `keys.py`

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

> Hopefully it should work.