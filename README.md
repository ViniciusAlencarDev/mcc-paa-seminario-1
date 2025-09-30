# Seminário I - PAA: Árvore de Busca Binária Ótima (OBST)

**Autores:** Augusto César e Vinícius Alencar

## Descrição

Este repositório contém os materiais para o Seminário I da disciplina de Projeto e Análise de Algoritmos. O tema abordado é a **Árvore de Busca Binária Ótima (OBST)**, uma técnica de programação dinâmica para construir uma árvore de busca com o menor custo esperado de pesquisa.

O algoritmo implementado utiliza um modelo simplificado, baseado nas **frequências de acesso** conhecidas para cada chave de busca.

## Apresentação em Vídeo

A apresentação de 15 minutos está disponível no YouTube:

https://youtu.be/RSHOJGZaN0g

## Conteúdo do Repositório

* `/slides.pdf`: Slides utilizados na apresentação.
* `/codigo_e_dados`: Pasta contendo a implementação em Python do algoritmo e o arquivo de dados.

## Sobre a Implementação

O código-fonte (`/codigo_e_dados/obst.py`) foi estruturado para ser didático e de fácil compreensão. Ele foca no conceito central da OBST, considerando apenas as frequências de buscas bem-sucedidas (ou seja, buscas por chaves que existem na árvore). A lógica utiliza indexação base 0, seguindo as convenções da linguagem Python.