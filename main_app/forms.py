#!/usr/bin/env python3

from django import forms


class editProductForm(forms.Form):
    product_name = forms.CharField(label="Product name", max_length=255)
    slug = forms.SlugField(label="Slug")
    current_price = forms.IntegerField(label="Old price")
    special_price = forms.IntegerField(label="Special price")
