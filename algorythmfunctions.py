from functools import reduce
import json
import os
import collections


def get_mvdm_genre(genre):
    with open("json/genre" + '/' + genre + '.json', 'r') as file:
        dic = json.load(file)
        column1 = dic[genre]["YES"]["popularity+"] + dic[genre]["YES"]["popularity-"]
        column2 = dic[genre]["NO"]["popularity+"] + dic[genre]["NO"]["popularity-"]
        return round(abs((dic[genre]["YES"]["popularity+"]/column1) - (
            dic[genre]["NO"]["popularity+"]/column2)) + abs(
            (dic[genre]["YES"]["popularity-"]/column1) - (
                dic[genre]["NO"]["popularity-"]/column2)), 2)

def get_mvdm_budget_alto_medio():
    with open("json/budget" + '/' + 'budget' + '.json', 'r') as file:
        dic = json.load(file)
        column1 = dic['budget']["ALTO"]["popularity+"] + dic['budget']["ALTO"]["popularity-"]
        column2 = dic['budget']["MEDIO"]["popularity+"] + dic['budget']["MEDIO"]["popularity-"]
        return round(abs((dic['budget']["ALTO"]["popularity+"]/column1) - (
            dic['budget']["MEDIO"]["popularity+"]/column2)) + abs(
            (dic['budget']["ALTO"]["popularity-"]/column1) - (
                dic['budget']["MEDIO"]["popularity-"]/column2)), 2)


def get_mvdm_budget_bajo_medio():
    with open("json/budget" + '/' + 'budget' + '.json', 'r') as file:
        dic = json.load(file)
        column1 = dic["budget"]["BAJO"]["popularity+"] + dic["budget"]["BAJO"]["popularity-"]
        column2 = dic["budget"]["MEDIO"]["popularity+"] + dic["budget"]["MEDIO"]["popularity-"]
        return round(abs((dic["budget"]["BAJO"]["popularity+"]/column1) - (
            dic["budget"]["MEDIO"]["popularity+"]/column2)) + abs(
            (dic["budget"]["BAJO"]["popularity-"]/column1) - (
                dic["budget"]["MEDIO"]["popularity-"]/column2)), 2)

def get_mvdm_budget_alto_bajo():
    with open("json/budget" + '/' + 'budget' + '.json', 'r') as file:
        dic = json.load(file)
        column1 = dic["budget"]["BAJO"]["popularity+"] + dic["budget"]["BAJO"]["popularity-"]
        column2 = dic["budget"]["ALTO"]["popularity+"] + dic["budget"]["ALTO"]["popularity-"]
        return round(abs((dic["budget"]["BAJO"]["popularity+"]/column1) - (
            dic["budget"]["ALTO"]["popularity+"]/column2)) + abs(
            (dic["budget"]["BAJO"]["popularity-"]/column1) - (
                dic["budget"]["ALTO"]["popularity-"]/column2)), 2)


def get_mvdm_revenue_alto_medio():
    with open("json/revenue" + '/' + 'revenue' + '.json', 'r') as file:
        dic = json.load(file)
        column1 = dic["revenue"]["ALTO"]["popularity+"] + dic["revenue"]["ALTO"][
            "popularity-"]
        column2 = dic["revenue"]["MEDIO"]["popularity+"] + \
                  dic["revenue"]["MEDIO"]["popularity-"]
        return round(abs((dic["revenue"]["ALTO"]["popularity+"] / column1) - (
            dic["revenue"]["MEDIO"]["popularity+"] / column2)) + abs(
            (dic["revenue"]["ALTO"]["popularity-"] / column1) - (
                dic["revenue"]["MEDIO"]["popularity-"] / column2)), 2)


def get_mvdm_revenue_bajo_medio():
    with open("json/revenue" + '/' + 'revenue' + '.json', 'r') as file:
        dic = json.load(file)
        column1 = dic["revenue"]["BAJO"]["popularity+"] + dic["revenue"]["BAJO"][
            "popularity-"]
        column2 = dic["revenue"]["MEDIO"]["popularity+"] + \
                  dic["revenue"]["MEDIO"]["popularity-"]
        return round(abs((dic["revenue"]["BAJO"]["popularity+"] / column1) - (
            dic["revenue"]["MEDIO"]["popularity+"] / column2)) + abs(
            (dic["revenue"]["BAJO"]["popularity-"] / column1) - (
                dic["revenue"]["MEDIO"]["popularity-"] / column2)), 2)


def get_mvdm_revenue_alto_bajo():
    with open("json/revenue" + '/' + 'revenue' + '.json', 'r') as file:
        dic = json.load(file)
        column1 = dic["revenue"]["BAJO"]["popularity+"] + dic["revenue"]["BAJO"][
            "popularity-"]
        column2 = dic["revenue"]["ALTO"]["popularity+"] + dic["revenue"]["ALTO"][
            "popularity-"]
        return round(abs((dic["revenue"]["BAJO"]["popularity+"] / column1) - (
            dic["revenue"]["ALTO"]["popularity+"] / column2)) + abs(
            (dic["revenue"]["BAJO"]["popularity-"] / column1) - (
                dic["revenue"]["ALTO"]["popularity-"] / column2)), 2)