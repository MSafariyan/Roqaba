from django import template
from main_app.models import Product
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def percentage(smallnumber, greaternumber):
    if smallnumber == 0 or greaternumber == 0:
        x = 0
    else:
        x = (smallnumber * 100) / greaternumber
        x = 100 - x
    return int(x)


@register.simple_tag
def avaOrNot(current_price, status):
    if current_price != 0 and status == True:

        return mark_safe(
            '<span class="badge rounded-pill bg-success">موجود</span>'
        )
    else:
        return mark_safe(
            '<span class="badge rounded-pill bg-danger">ناموجود</span>'
        )


@register.simple_tag
def publisherNameTranslator(publisherName):
    if publisherName == "jangal":
        return "جنگل"
    elif publisherName == "irlanguage":
        return "دنیای زبان"
    elif publisherName == "zabanmehr":
        return "زبان مهر"
    elif publisherName == "zabanshop":
        return "زبان شاپ"
    elif publisherName == "rahnama":
        return "رهنما"


@register.simple_tag
def color_hex():
    import random

    r = lambda: random.randint(0, 255)
    return "#%02X%02X%02X" % (r(), r(), r())


@register.simple_tag
def random_str():
    import random

    s = random.randint(0, 255)
    return str(s)


@register.simple_tag
def five_percent_above_of_average(children):
    if len(children) == 0:
        return 0
    else:

        child_prices = 0
        lengh_children = len(children)
        for child in children:
            child_prices+=child.special_price
        
        average_price = child_prices/lengh_children
        five_percent_above = (average_price*0.05)+average_price
        return mark_safe(f'</span>۵٪ بیشتر از قیمت متوسط<span class="badge rounded-pill bg-success"><p class="h5 text-white text-center">{five_percent_above}</p></span>')


@register.simple_tag
def penetration_pricing_calc(children):
    if len(children) == 0:
        return 0
    else:
        child_prices = []
        lengh_children = len(children)
        for child in children:
            child_prices.append(child.special_price)
        
        child_prices.sort()
        print(child_prices)
        penetration_pricing = child_prices[0]-(child_prices[0]*0.09)
        return mark_safe(f'قیمت نفوذی: ۹٪ زیر قیمت بازار<span class="badge rounded-pill bg-danger"><p class="h5 text-white text-center">{penetration_pricing}</p></span>')

@register.simple_tag
def average_price(children, status):
    flag = False
    if status == "True":
        flag = True
        
    if len(children) == 0:
        return 0
    else:
        child_prices = 0
        lengh_children = 0
        for child in children:
            if flag == True:
                if child.status == True:
                    child_prices+=child.special_price
                    lengh_children += 1
            else:
                if child.status == False and len(children)!=0:
                    child_prices+=child.special_price
                    lengh_children += 1
                else:
                    child_prices = 1
                    lengh_children = 1       
        average_price = round(child_prices/lengh_children, 1)
        return mark_safe(f'میانگین قیمت بازار<span class="badge rounded-pill bg-primary"><p class="h5 text-white text-center">{average_price}</p></span>')

@register.simple_tag
def price_distance_to_average(children, product, status):
    flag = True
    if status == "False":
        flag = False
    if len(children) == 0:
        return 0
    else:
        child_prices = 0
        lengh_children = len(children)
        if flag == True:
            for child in children:
                if child.status == True:
                    child_prices+=child.special_price
        elif flag == False:
            for child in children:
                if child.status == False:
                    child_prices+=child.special_price
                else:
                    child_prices=1
                    lengh_children=1
        
        average_price = child_prices/lengh_children
        our_price = product.special_price
        if average_price == 1:
            price_distance = 0
        else:
            price_distance = round(((our_price-average_price)*100)/our_price, 1)
        if price_distance >0:
            return mark_safe(f'<span dir="ltr" class="badge rounded-pill bg-success"><p class="h5 text-white text-center">{price_distance}% بالاتر از متوسط قیمت بازار</p></span>')
        elif price_distance == 0:
            return mark_safe(f'<span dir="ltr" class="badge rounded-pill bg-light"><p class="h5 text-dark text-center">میانگین قیمت 0 است</p></span>')
        else:
            return mark_safe(f'<span dir="ltr" class="badge rounded-pill bg-danger"><p class="h5 text-white text-center">{price_distance}% پایین‌تر از متوسط قیمت بازار</p></span>')


