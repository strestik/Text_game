# přidat text, tytuli jména a názvy
import random
import time
import sys
from chractering import *
from potion import *
from items import *
from effect import *
from h_characters import *
from e_chracters import *
from base_character import *
from attack import *

titles = [
    "Neporazitelný",
    "Khemrikara",
    "Velký král Nehekhary",
    "Král králů",
    "Velekrál Khemri",
    "Potomek bohů",
    "Velký jestřáb nebes",
    "Vyvolený Ptry",
    "Posvátný potomek Usiriana",
    "Šampion Velké pouště",
    "Pán Země",
    "Vládce oblohy",
    "Přinášející světlo",
    "Vyvolený bohů",
    "Překonavší kodex mrtvých",
    "Věčný vládce dvou zemí",
    "První kněžský král",
    "Světlo Nehekhary",
    "Nepokojný",
    "Zlatý faraon",
    "Metla bezvěrců",
    "Věčný král",
    "Nesporný vládce Khemri a celé Nehekhary",
    "Jediný pravý král",
    "Král Divokého honu",
    "Řezník světů",
    "Chladný plamen prázdnoty",
    "Elfská záhada",
    "Bílý plamen tančící na mohylách svých nepřátel",
    "Zrádce z Thaneddu",
    "Bestie v lidské kůži",
    "Ohař Vilgefortze",
    "Bestie z Beauclairu",
    "Pán zrcadel",
    "Oheň Salamandry",
    "Vrah králů",
    "Falešný prorok",
    "Šílený král",
    "Černý jezdec",
    "Šeptač ze stínů",
    "Čarodějka stínů",
    "Pavoučí tkadlec války",
    "Čepel v zahradě",
    "Paní kontroly"
]

enemy_names = [
    "Eredin",
    "Imlerith",
    "Caranthir",
    "Avallac'h",
    "Emhyr",
    "Vilgefortz",
    "Bonhart",
    "Rience",
    "Dettlaff",
    "Gaunter",
    "Azar",
    "Letho",
    "Jacques",
    "Radovid",
    "Cahir",
    "Stefan",
    "Fringilla",
    "Sigismund",
    "Reynard",
    "Tissaia",
    "Settra"
]

characters = [
    "Witcher",
    "Sorcerer",
    "Archer",
    "Jarl",
    "Bard",
    "Monster"
]

