# adocao-mais
Sistema de Gestão de Centro de Adoção de Animais em Python

## Sobre o projeto

O **Adoção+** é um sistema de gestão para centros de adoção de animais, desenvolvido em Python, com interação pelo terminal.

O objetivo do projeto é ajudar a organizar informações sobre cães, gatos e outros pets, facilitando o controle de cadastros, cuidados, vacinas, atividades, adoções e sugestões personalizadas para possíveis adotantes.

## Funcionalidades

-Cadastro, visualização, edição e exclusão de animais;
-Registro de cuidados e atividades, como vacinas, banhos, consultas e treinos;
-Contagem regressiva para tarefas importantes;
-Armazenamento dos dados em arquivos .csv;
-Sugestões personalizadas com base no perfil do animal;
-Funcionalidade extra: Matching de Adoção, que recomenda animais compatíveis com o perfil informado pelo adotante.
-Funcionalidade Extra: Matching de Adoção

## Funcionalidade Extra:

O sistema contará com uma funcionalidade de matching entre adotante e animal.

O adotante poderá informar preferências como:

-Espécie desejada;
-Porte do animal;
-Nível de energia;
-Presença de crianças em casa;
-Presença de outros animais;
-Tipo de moradia.

Com base nessas informações, o sistema irá comparar os dados do adotante com os animais cadastrados e indicar os pets mais compatíveis.

## Tecnologias utilizadas
-Python
-Arquivos .csv
-Terminal / Linha de comando
-Como executar o projeto
-Baixe ou clone este repositório.
-Abra a pasta do projeto no terminal.
-Execute o arquivo principal:
-python main.py

## Estrutura inicial do projeto
adocao-mais/
│
├── main.py
├── README.md
└── dados/
    ├── animais.csv
    ├── tarefas.csv
    ├── adocoes.csv
    └── adotantes.csv

## Integrantes
-Isabelly Ribeiro
-Heitor Torres
-Yasmin Lopes
-Miguel Cabral
-Leandro Henrique
-Maria Carolina

## Status do projeto

Em desenvolvimento.

## Observações

Este projeto será desenvolvido sem o uso de bibliotecas externas, conforme os requisitos da atividade. As únicas bibliotecas permitidas inicialmente são os, datetime e random.
